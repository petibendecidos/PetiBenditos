"""Compara las tablas semilla con las sintéticas de mostly.ai y escribe las tablas Markdown del informe.

Uso: python scripts/dashboard_comparar.py <carpeta_datos>
Solo usa la biblioteca estándar.
"""
import csv
import sys
from pathlib import Path
from statistics import mean


def leer(ruta):
    with ruta.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def pct(filas, cond):
    return 100 * sum(1 for f in filas if cond(f)) / len(filas)


METRICAS = {
    "tickets": [
        ("Horas promedio de resolución", lambda r: mean(float(f["horas_resolucion"]) for f in r), "{:.1f}"),
        ("Tickets dentro del ANS", lambda r: pct(r, lambda f: f["dentro_ans"] == "Si"), "{:.1f} %"),
        ("Resueltos al primer contacto", lambda r: pct(r, lambda f: f["primer_contacto"] == "Si"), "{:.1f} %"),
        ("Satisfacción promedio (1 a 5)", lambda r: mean(float(f["csat"]) for f in r), "{:.2f}"),
        ("Tickets de prioridad P1", lambda r: pct(r, lambda f: f["prioridad"] == "P1"), "{:.1f} %"),
    ],
    "vulnerabilidades": [
        ("Vulnerabilidades críticas", lambda r: pct(r, lambda f: f["severidad"] == "Critica"), "{:.1f} %"),
        ("Horas promedio para remediar una crítica",
         lambda r: mean(float(f["horas_remediacion"]) for f in r if f["severidad"] == "Critica"), "{:.0f}"),
        ("Horas promedio de detección", lambda r: mean(float(f["horas_deteccion"]) for f in r), "{:.1f}"),
    ],
    "personas": [
        ("Personas con al menos una certificación", lambda r: pct(r, lambda f: float(f["certificaciones"]) >= 1), "{:.1f} %"),
        ("Antigüedad promedio (meses)", lambda r: mean(float(f["antiguedad_meses"]) for f in r), "{:.1f}"),
        ("Rotadas en el último año", lambda r: pct(r, lambda f: f["rotado_ultimo_anio"] == "Si"), "{:.1f} %"),
    ],
}

DESCRIPCION = {
    "tickets": "Tickets de la mesa de servicio de TI interna: fecha, célula, categoría, prioridad, horas de resolución, ANS, primer contacto y satisfacción",
    "vulnerabilidades": "Hallazgos de seguridad: fecha, célula, severidad, origen (SAST, SCA, DAST, pentest), horas de detección y de remediación",
    "personas": "Personal técnico: rol, célula, antigüedad, certificaciones y rotación entre células",
}


def main():
    carpeta = Path(sys.argv[1])
    print("| Tabla | Contenido | Filas semilla | Filas sintéticas |\n|---|---|---|---|")
    datos = {}
    for t in METRICAS:
        s, y = leer(carpeta / f"semilla_{t}.csv"), leer(carpeta / f"sintetico_{t}.csv")
        datos[t] = (s, y)
        print(f"| {t} | {DESCRIPCION[t]} | {len(s)} | {len(y)} |")
    print("\n| Tabla | Métrica | Semilla | Sintética (MOSTLY AI) |\n|---|---|---|---|")
    for t, metricas in METRICAS.items():
        s, y = datos[t]
        for nombre, fn, fmt in metricas:
            print(f"| {t} | {nombre} | {fmt.format(fn(s))} | {fmt.format(fn(y))} |".replace(".", ","))


if __name__ == "__main__":
    main()
