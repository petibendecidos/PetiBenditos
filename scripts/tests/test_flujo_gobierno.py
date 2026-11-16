"""Pruebas del flujo de gobierno de TI por célula: datos de la hoja y constructor del JSON de n8n.

Ejecutar: python -m pytest scripts/tests/test_flujo_gobierno.py -q
"""
import csv
import importlib.util
import json
import re
from datetime import date
from pathlib import Path

import openpyxl
import pytest

RAIZ = Path(__file__).resolve().parents[2]
DATOS = RAIZ / "docs" / "entregas-2026-11-04" / "dashboard" / "datos"


def cargar(nombre):
    spec = importlib.util.spec_from_file_location(nombre, RAIZ / "scripts" / f"{nombre}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture(scope="module")
def libro(tmp_path_factory):
    salida = tmp_path_factory.mktemp("hoja") / "hoja.xlsx"
    cargar("flujo_gobierno_datos").generar(DATOS, salida)
    return openpyxl.load_workbook(salida)


def filas(ws):
    encabezado = [c.value for c in ws[1]]
    return [dict(zip(encabezado, [c.value for c in fila])) for fila in ws.iter_rows(min_row=2)]


def test_pestanas(libro):
    assert libro.sheetnames == ["Config", "Celulas", "Umbrales", "Mediciones", "Historial", "Decisiones"]
    assert [c.value for c in libro["Historial"][1]] == [
        "clave", "ciclo", "celula", "estado", "KPI-05", "ANS", "KPI-09", "KPI-10", "fecha_ejecucion"]
    assert [c.value for c in libro["Decisiones"][1]] == [
        "fecha", "ciclo", "celula", "foco", "justificacion", "decision", "responsable"]


def test_mediciones(libro):
    med = filas(libro["Mediciones"])
    assert len(med) == 12 * 12 * 4
    vul = [r for r in csv.DictReader(open(DATOS / "sintetico_vulnerabilidades.csv", encoding="utf8"))
           if r["celula"] == "C05" and r["severidad"] == "Critica"
           and date.fromisoformat(r["fecha_deteccion"]).strftime("%Y-%m") == "2027-09"]
    esperado = round(sum(float(r["horas_remediacion"]) for r in vul) / len(vul), 1)
    fila = next(r for r in med if r["mes"] == 12 and r["celula"] == "C05" and r["kpi"] == "KPI-05")
    assert fila["valor"] == esperado
    assert fila["n"] == len(vul)


def test_config_y_umbrales(libro):
    config = filas(libro["Config"])[0]
    assert config["mes_corte"] == 12
    umbrales = {u["kpi"]: u for u in filas(libro["Umbrales"])}
    assert umbrales["KPI-05"]["meta"] == 72 and umbrales["KPI-05"]["menor_es_mejor"] == "Si"
    assert umbrales["ANS"]["meta"] == 90
    assert umbrales["KPI-09"]["meta"] == 70
    assert umbrales["KPI-10"]["meta"] == 50
    assert len(filas(libro["Celulas"])) == 12


def test_correos_de_ejemplo(libro):
    correos = [c.value for ws in libro for fila in ws.iter_rows() for c in fila
               if isinstance(c.value, str) and "@" in c.value]
    assert correos and all(c.endswith("@ejemplo.com") for c in correos)


NODOS = [
    "Disparo mensual", "Disparo manual", "Leer Config", "Leer Células", "Leer Umbrales", "Leer Mediciones",
    "Evaluar células", "Preparar historial", "Registrar historial", "Según estado", "Avisar a líderes",
    "Agrupar rojos", "Aprobación del Comité", "Preparar decisión", "Registrar decisión", "Armar informe",
    "Enviar informe",
]
CORREO = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-z]{2,}")


def construir(tmp_path, **ids):
    salida = tmp_path / "flujo.json"
    cargar("flujo_gobierno_construir").construir(salida, **ids)
    texto = salida.read_text(encoding="utf8")
    return json.loads(texto), texto


def nodo(flujo, nombre):
    return next(n for n in flujo["nodes"] if n["name"] == nombre)


def test_flujo_estructura(tmp_path):
    flujo, texto = construir(tmp_path)
    assert sorted(n["name"] for n in flujo["nodes"]) == sorted(NODOS)
    nombres = set(NODOS)
    for origen, salidas in flujo["connections"].items():
        assert origen in nombres
        for rama in salidas["main"]:
            for destino in rama:
                assert destino["node"] in nombres
    assert not CORREO.search(texto)
    for marcador in ("__SPREADSHEET_ID__", "__CREDENCIAL_SHEETS__", "__CREDENCIAL_GMAIL__"):
        assert marcador in texto
    espera = nodo(flujo, "Aprobación del Comité")["parameters"]["options"]["limitWaitTime"]["values"]
    assert (espera["resumeAmount"], espera["resumeUnit"]) == (3, "days")
    assert "module.exports" not in texto
    assert "function evaluarCelulas" in nodo(flujo, "Evaluar células")["parameters"]["jsCode"]
    for lectura in ("Leer Células", "Leer Umbrales", "Leer Mediciones"):
        assert nodo(flujo, lectura).get("executeOnce") is True
    historial = nodo(flujo, "Registrar historial")["parameters"]
    assert historial["operation"] == "appendOrUpdate"
    assert historial["columns"]["matchingColumns"] == ["clave"]
    for escritura in ("Registrar historial", "Registrar decisión"):
        assert nodo(flujo, escritura)["parameters"]["options"]["cellFormat"] == "RAW"
    aprobacion = nodo(flujo, "Aprobación del Comité")["parameters"]
    assert aprobacion["message"] == "={{ $json.cuerpoTexto }}"
    assert aprobacion["options"]["appendAttribution"] is False


def test_flujo_con_ids(tmp_path):
    _, texto = construir(tmp_path, spreadsheet_id="hoja123", credencial_sheets="cs1", credencial_gmail="cg1")
    assert "__" not in texto.replace("__rl", "")
    assert "hoja123" in texto and "cg1" in texto


def test_codigo_de_evaluar_corre_con_datos_de_la_hoja(tmp_path, libro):
    """El código incrustado en "Evaluar células" corre con las filas de la hoja como las entrega n8n."""
    flujo, _ = construir(tmp_path)
    datos = {t: filas(libro[t]) for t in ("Config", "Celulas", "Umbrales", "Mediciones")}
    datos["Config"][0].update(correo_comite="a@x.co", correo_copia="c@x.co")
    for c in datos["Celulas"]:
        c["correo_lider"] = "b@x.co"
    nodos_hoja = {"Leer Config": "Config", "Leer Células": "Celulas", "Leer Umbrales": "Umbrales", "Leer Mediciones": "Mediciones"}
    stub = ("const DATOS = " + json.dumps({n: datos[t] for n, t in nodos_hoja.items()}, default=str) + ";\n"
            "const $ = (n) => ({ first: () => ({ json: DATOS[n][0] }), all: () => DATOS[n].map((json) => ({ json })) });\n"
            "const salida = (function () {\n" + nodo(flujo, "Evaluar células")["parameters"]["jsCode"] + "\n})();\n"
            "console.log(JSON.stringify(salida.map((i) => [i.json.celula, i.json.estado])));")
    script = tmp_path / "correr.js"
    script.write_text(stub, encoding="utf8")
    import subprocess
    r = subprocess.run(["node", str(script)], capture_output=True, text=True, encoding="utf8")
    assert r.returncode == 0, r.stderr
    resultado = json.loads(r.stdout)
    assert len(resultado) == 12
    assert all(estado in {"Bueno", "Intermedio", "Bajo", "Sin datos"} for _, estado in resultado)


def test_correos_reales_por_argumento(tmp_path):
    salida = tmp_path / "hoja.xlsx"
    cargar("flujo_gobierno_datos").generar(DATOS, salida, correo_comite="a@x.co", correo_lider="b@x.co", correo_copia="c@x.co")
    wb = openpyxl.load_workbook(salida)
    assert filas(wb["Config"])[0]["correo_comite"] == "a@x.co"
    assert {c["correo_lider"] for c in filas(wb["Celulas"])} == {"b@x.co"}
