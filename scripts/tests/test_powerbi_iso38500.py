"""Pruebas TDD del generador del modelo de datos en estrella para Power BI (ISO/IEC 38500:2024).

Ejecutar: python -m pytest scripts/tests/test_powerbi_iso38500.py -q
"""
import csv
import datetime as dt
import json
import re
import sys
from pathlib import Path

import openpyxl
import pytest

RAIZ = Path(__file__).resolve().parents[2]
SCRIPTS = RAIZ / "scripts"
DATOS_SINTETICOS = RAIZ / "docs" / "entregas-2026-11-04" / "dashboard" / "datos"

if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import powerbi_iso38500_datos as gen  # noqa: E402


TABLAS_ESPERADAS = [
    "dim_fecha",
    "dim_corte",
    "dim_principio",
    "dim_tarea",
    "dim_indicador",
    "dim_celula",
    "dim_proyecto",
    "dim_riesgo",
    "fact_medicion",
    "fact_proyecto_mes",
    "fact_vulnerabilidad",
    "fact_sistema_ia",
    "fact_solicitud_titular",
    "fact_decision",
]


@pytest.fixture(scope="module")
def modelo():
    return gen.construir_modelo(DATOS_SINTETICOS, semilla=38500)


def _serie_indicador(mod, id_ind):
    escala = next(r["escala"] for r in mod["dim_indicador"] if r["id_indicador"] == id_ind)
    por_mes = {}
    for f in mod["fact_medicion"]:
        if f["id_indicador"] == id_ind and f["estado_reporte"] == "Reportado" and f["denominador"]:
            num, den = por_mes.get(f["mes"], (0.0, 0.0))
            por_mes[f["mes"]] = (num + f["numerador"], den + f["denominador"])
    return {m: num / den * escala for m, (num, den) in sorted(por_mes.items())}


@pytest.mark.parametrize(
    "valor,meta,sentido,esperado",
    [
        (181, 72, "menor", 39.8),
        (60, 72, "menor", 100.0),
        (0, 0, "menor", 100.0),
        (1, 0, "menor", 0.0),
        (-4.4, -5, "mayor", 88.0),
        (2, -5, "mayor", 0.0),
        (None, 72, "menor", None),
        (5, None, "mayor", None),
    ],
)
def test_cumplimiento(valor, meta, sentido, esperado):
    res = gen.cumplimiento(valor, meta, sentido)
    if esperado is None:
        assert res is None
    else:
        assert res == pytest.approx(esperado, abs=0.05)


@pytest.mark.parametrize(
    "cumpl,esperado",
    [
        (95, "Bueno"),
        (94.9, "Intermedio"),
        (70.1, "Intermedio"),
        (70, "Bajo"),
        (None, "No evaluado"),
    ],
)
def test_estado(cumpl, esperado):
    assert gen.estado(cumpl) == esperado


def test_estados_mes12(modelo):
    corte = {r["id_indicador"]: r["estado"] for r in gen.control_corte(modelo, 12)}
    esperados = {
        "KPI-07": "Bueno",
        "KPI-08": "Bueno",
        "KPI-09": "Bueno",
        "KPI-14": "Bueno",
        "DAT-03": "Bueno",
        "IA-02": "Bueno",
        "KPI-01": "Intermedio",
        "KPI-02": "Intermedio",
        "KPI-04": "Intermedio",
        "KPI-06": "Intermedio",
        "DAT-01": "Intermedio",
        "IA-01": "Intermedio",
        "KPI-03": "Bajo",
        "KPI-05": "Bajo",
        "KPI-10": "Bajo",
        "KPI-11": "Bajo",
        "DAT-02": "Bajo",
        "KPI-13": "No evaluado",
    }
    assert corte == esperados


def test_valores_de_referencia(modelo):
    corte = {r["id_indicador"]: r["valor"] for r in gen.control_corte(modelo, 12)}
    assert corte["KPI-01"] == pytest.approx(52.0, abs=0.05)
    assert corte["KPI-05"] == pytest.approx(217.9, abs=0.05)
    assert corte["KPI-09"] == pytest.approx(66.7, abs=0.05)
    assert corte["KPI-10"] == pytest.approx(33.2, abs=0.05)


def test_kpi05_por_celula(modelo):
    with (DATOS_SINTETICOS / "sintetico_vulnerabilidades.csv").open(encoding="utf-8") as f:
        crit_c05 = [
            float(r["horas_remediacion"])
            for r in csv.DictReader(f)
            if r["celula"] == "C05"
            and r["severidad"] == "Critica"
            and r["fecha_deteccion"].startswith("2027-09")
        ]
    assert crit_c05
    esperado = sum(crit_c05) / len(crit_c05)
    filas = [
        r
        for r in modelo["fact_medicion"]
        if r["mes"] == 12 and r["id_indicador"] == "KPI-05" and r["id_celula"] == "C05"
    ]
    assert len(filas) == 1
    assert filas[0]["numerador"] / filas[0]["denominador"] == pytest.approx(esperado, abs=0.05)


def test_valor_al_corte_usa_ultimo_reporte(modelo):
    corte11 = {r["id_indicador"]: r for r in gen.control_corte(modelo, 11)}
    assert corte11["KPI-02"]["mes_ultimo_reporte"] == 9
    assert corte11["KPI-02"]["valor"] is not None

    corte12 = {r["id_indicador"]: r for r in gen.control_corte(modelo, 12)}
    assert corte12["KPI-07"]["mes_ultimo_reporte"] == 5
    assert corte12["KPI-07"]["estado"] == "Bueno"


def test_antes_de_linea_base(modelo):
    corte4 = {r["id_indicador"]: r for r in gen.control_corte(modelo, 4)}
    assert corte4["KPI-06"]["estado"] == "No evaluado"
    assert corte4["KPI-06"]["valor"] is None


def test_mes_sin_reporte(modelo):
    filas_kpi04_m8 = [
        r for r in modelo["fact_medicion"] if r["mes"] == 8 and r["id_indicador"] == "KPI-04"
    ]
    c11 = next(r for r in filas_kpi04_m8 if r["id_celula"] == "C11")
    assert c11["estado_reporte"] == "Sin reporte"
    assert c11["numerador"] is None
    assert c11["denominador"] is None
    assert sum(r["denominador"] for r in filas_kpi04_m8 if r["denominador"] is not None) == 11


def test_series_no_rectas(modelo):
    for id_ind in ("KPI-04", "KPI-06"):
        serie = _serie_indicador(modelo, id_ind)
        vals = [v for _, v in sorted(serie.items())]
        diffs = [round(vals[i] - vals[i - 1], 4) for i in range(1, len(vals))]
        assert any(d < 0 for d in diffs), f"{id_ind} debe tener al menos un retroceso"
        assert len(set(diffs)) > 1, f"{id_ind} no puede tener pendiente constante"


def test_integridad(modelo, tmp_path):
    assert list(modelo.keys()) == TABLAS_ESPERADAS
    assert len(modelo["dim_principio"]) == 11

    secciones = {r["seccion"] for r in modelo["dim_principio"]}
    tareas = {r["id_tarea"] for r in modelo["dim_tarea"]}
    indicadores = {r["id_indicador"] for r in modelo["dim_indicador"]}
    celulas = {r["id_celula"] for r in modelo["dim_celula"]}
    meses = {r["mes"] for r in modelo["dim_fecha"]}
    proyectos = {r["id_proyecto"] for r in modelo["dim_proyecto"]}

    ind_secciones = {r["seccion_principio"] for r in modelo["dim_indicador"]}
    assert "5.2" not in ind_secciones and "5.8" not in ind_secciones
    for r in modelo["dim_indicador"]:
        assert r["seccion_principio"] in secciones
        assert r["id_tarea"] in tareas

    for r in modelo["fact_medicion"]:
        assert r["mes"] in meses
        assert r["id_indicador"] in indicadores
        assert r["id_celula"] in celulas
    for r in modelo["fact_proyecto_mes"]:
        assert r["mes"] in meses
        assert r["id_proyecto"] in proyectos
    for r in modelo["fact_vulnerabilidad"]:
        assert r["mes"] in meses
        assert r["id_celula"] in celulas
    for r in modelo["fact_sistema_ia"]:
        assert r["id_celula"] in celulas
    for r in modelo["fact_solicitud_titular"]:
        assert r["mes"] in meses
    for r in modelo["fact_decision"]:
        assert r["mes"] in meses
        assert r["celula"] in celulas
        if r["id_indicador"]:
            assert r["id_indicador"] in indicadores
        if r["id_proyecto"]:
            assert r["id_proyecto"] in proyectos

    xlsx = tmp_path / "modelo.xlsx"
    gen.escribir_xlsx(modelo, xlsx)
    wb = openpyxl.load_workbook(xlsx)
    assert wb.sheetnames == TABLAS_ESPERADAS
    ws_med = wb["fact_medicion"]
    assert isinstance(ws_med.cell(2, 1).value, int)
    ws_fecha = wb["dim_fecha"]
    assert isinstance(ws_fecha.cell(2, 2).value, (dt.date, dt.datetime))


def test_proyectos_mes12(modelo):
    m12 = [r for r in modelo["fact_proyecto_mes"] if r["mes"] == 12]
    conteo = {}
    for r in m12:
        conteo[r["estado"]] = conteo.get(r["estado"], 0) + 1
    assert conteo == {"Terminado": 13, "Atrasado": 4, "Por iniciar": 8}


def test_decisiones(modelo):
    decs = modelo["fact_decision"]
    assert 12 <= len(decs) <= 16
    assert list(decs[0].keys())[:7] == [
        "fecha", "ciclo", "celula", "foco", "justificacion", "decision", "responsable"
    ]
    focos_validos = {"Priorización", "Riesgo", "Desempeño", "Estrategia"}
    for d in decs:
        assert d["foco"] in focos_validos
        assert len(d["justificacion"]) <= 160
        assert len(d["decision"]) <= 160
    cels_m12 = {d["celula"] for d in decs if d["mes"] == 12}
    assert cels_m12 == {"C01", "C03", "C04", "C05", "C06", "C08", "C09", "C10", "C11", "C12"}

    for tabla, filas in modelo.items():
        for fila in filas:
            for k, v in fila.items():
                if isinstance(v, str):
                    assert "@" not in v, f"Caracter '@' en {tabla}.{k}: {v}"


def test_determinista():
    m1 = gen.construir_modelo(DATOS_SINTETICOS, semilla=38500)
    m2 = gen.construir_modelo(DATOS_SINTETICOS, semilla=38500)
    assert m1 == m2


POWERBI_DIR = RAIZ / "docs" / "entregas-2026-11-16" / "dashboard-iso38500" / "powerbi"

MEDIDAS_ESPERADAS = [
    "Corte",
    "Es de operación",
    "Valor",
    "Mes último reporte",
    "Valor al corte",
    "Meta al corte",
    "Cumplimiento",
    "Estado",
    "Estado orden",
    "Color estado",
    "Valor texto",
    "Último reporte texto",
    "Valor (serie)",
    "Meta (serie)",
    "Indicadores Bueno",
    "Indicadores Intermedio",
    "Indicadores Bajo",
    "Proyectos al corte",
    "Terminados plan (acum)",
    "Terminados real (acum)",
    "Color proyecto",
    "Vulnerabilidades",
    "Sistemas identificados",
    "Sistemas registrados",
    "Con evaluación de riesgo",
    "Con supervisión humana",
    "Solicitudes",
    "Solicitudes fuera de plazo",
    "Decisiones hasta el corte",
]


def test_tema():
    tema = json.loads((POWERBI_DIR / "tema-gobierno-ti.json").read_text(encoding="utf-8"))
    assert tema["name"] == "Gobierno TI PETI"
    assert tema["dataColors"][:3] == ["#2a78d6", "#eb6834", "#1baf7a"]
    assert tema["good"] == "#0ca30c"
    assert tema["neutral"] == "#fab219"
    assert tema["bad"] == "#d03b3b"


def test_medidas_declaradas():
    texto = (POWERBI_DIR / "medidas.dax").read_text(encoding="utf-8")
    for nombre in MEDIDAS_ESPERADAS:
        patron = rf"(?m)^{re.escape(nombre)}\s*="
        assert re.search(patron, texto), f"Falta la medida '{nombre}' en medidas.dax"

