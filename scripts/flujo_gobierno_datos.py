"""Arma el libro de la hoja de Google del flujo "Gobierno de TI por célula" (n8n, ISO/IEC 38500:2024).

Uso:
    python scripts/flujo_gobierno_datos.py <carpeta_datos> <salida.xlsx>
        [--correo-comite X --correo-lider Y --correo-copia Z]

Toma los datos sintéticos del dashboard del 4 de noviembre (sintetico_vulnerabilidades, sintetico_tickets,
sintetico_personas) y calcula cuatro indicadores por célula y por mes (mes 1 = octubre de 2026):
  KPI-05  promedio de horas de remediación de las vulnerabilidades críticas detectadas en el mes (meta 72 h)
  ANS     % de tickets dentro del ANS en el mes (meta 90 %, supuesto del equipo, INT-001)
  KPI-09  % de personas con más de 6 meses y al menos una certificación (foto: igual todos los meses; meta 70 %)
  KPI-10  % de personas rotadas en el último año (foto; meta 50 %, interpolada como en el dashboard)
Sin correos por argumento escribe los de ejemplo (@ejemplo.com): esa es la versión que va al repositorio.
La versión con correos reales se escribe fuera del repositorio (D:\\dev\\n8n\\peti\\).
"""
import argparse
import csv
from datetime import date
from pathlib import Path

import openpyxl
from openpyxl.styles import Font

MESES = 12
UMBRALES = [
    ("KPI-05", "Remediación de vulnerabilidades críticas", 72, "Si", "h", "P2.2, P2.3"),
    ("ANS", "Tickets de soporte dentro del ANS", 90, "No", "%", "P2.5"),
    ("KPI-09", "Personal técnico certificado", 70, "No", "%", "P1.7"),
    ("KPI-10", "Rotación entre células", 50, "No", "%", "P2.1 (R06)"),
]
HISTORIAL = ["clave", "ciclo", "celula", "estado", "KPI-05", "ANS", "KPI-09", "KPI-10", "fecha_ejecucion"]
DECISIONES = ["fecha", "ciclo", "celula", "foco", "justificacion", "decision", "responsable"]
ETIQUETAS = ["oct 26", "nov 26", "dic 26", "ene 27", "feb 27", "mar 27", "abr 27", "may 27", "jun 27", "jul 27", "ago 27", "sep 27"]


def mes_de(texto: str) -> int:
    d = date.fromisoformat(texto[:10])
    return (d.year - 2026) * 12 + d.month - 10 + 1


def leer(carpeta: Path, nombre: str):
    with open(carpeta / nombre, encoding="utf8") as f:
        return list(csv.DictReader(f))


def pct(si: int, total: int):
    return round(100 * si / total, 1) if total else None


def mediciones(carpeta: Path):
    vul = leer(carpeta, "sintetico_vulnerabilidades.csv")
    tic = leer(carpeta, "sintetico_tickets.csv")
    per = leer(carpeta, "sintetico_personas.csv")
    celulas = sorted({p["celula"] for p in per} | {v["celula"] for v in vul} | {t["celula"] for t in tic})
    filas = []
    for mes in range(1, MESES + 1):
        for c in celulas:
            crit = [float(v["horas_remediacion"]) for v in vul
                    if v["celula"] == c and v["severidad"] == "Critica" and mes_de(v["fecha_deteccion"]) == mes]
            ts = [t for t in tic if t["celula"] == c and mes_de(t["fecha"]) == mes]
            ps = [p for p in per if p["celula"] == c]
            mas6 = [p for p in ps if float(p["antiguedad_meses"]) > 6]
            valores = {
                "KPI-05": (round(sum(crit) / len(crit), 1) if crit else None, len(crit)),
                "ANS": (pct(sum(t["dentro_ans"] == "Si" for t in ts), len(ts)), len(ts)),
                "KPI-09": (pct(sum(int(float(p["certificaciones"])) >= 1 for p in mas6), len(mas6)), len(mas6)),
                "KPI-10": (pct(sum(p["rotado_ultimo_anio"] == "Si" for p in ps), len(ps)), len(ps)),
            }
            for kpi, (valor, n) in valores.items():
                filas.append([mes, ETIQUETAS[mes - 1], c, kpi, valor, n])
    return celulas, filas


def hoja(wb, titulo, encabezado, filas):
    ws = wb.create_sheet(titulo)
    ws.append(encabezado)
    for c in ws[1]:
        c.font = Font(bold=True)
    for f in filas:
        ws.append(f)
    for i, col in enumerate(encabezado, start=1):
        ws.column_dimensions[openpyxl.utils.get_column_letter(i)].width = max(12, len(col) + 4)
    return ws


def generar(carpeta, salida, correo_comite="comite@ejemplo.com", correo_lider="lider@ejemplo.com",
            correo_copia="copia@ejemplo.com"):
    carpeta, salida = Path(carpeta), Path(salida)
    celulas, filas = mediciones(carpeta)
    wb = openpyxl.Workbook()
    wb.remove(wb.active)
    hoja(wb, "Config", ["mes_corte", "correo_comite", "correo_copia"], [[MESES, correo_comite, correo_copia]])
    hoja(wb, "Celulas", ["celula", "nombre", "correo_lider"],
         [[c, f"Célula {c[1:]}", correo_lider] for c in celulas])
    hoja(wb, "Umbrales", ["kpi", "nombre", "meta", "menor_es_mejor", "unidad", "proyecto"], [list(u) for u in UMBRALES])
    hoja(wb, "Mediciones", ["mes", "etiqueta", "celula", "kpi", "valor", "n"], filas)
    hoja(wb, "Historial", HISTORIAL, [])
    hoja(wb, "Decisiones", DECISIONES, [])
    salida.parent.mkdir(parents=True, exist_ok=True)
    wb.save(salida)
    return salida


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("carpeta_datos")
    ap.add_argument("salida")
    ap.add_argument("--correo-comite", default="comite@ejemplo.com")
    ap.add_argument("--correo-lider", default="lider@ejemplo.com")
    ap.add_argument("--correo-copia", default="copia@ejemplo.com")
    a = ap.parse_args()
    print("ok", generar(a.carpeta_datos, a.salida, a.correo_comite, a.correo_lider, a.correo_copia))


if __name__ == "__main__":
    main()
