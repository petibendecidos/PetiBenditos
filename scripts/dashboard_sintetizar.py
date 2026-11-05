"""Entrena un generador de mostly.ai (modo local, sin cuenta) por cada tabla semilla y genera su versión sintética.

Uso (en un entorno con Python 3.12 y `mostlyai[local]`; no correr con el Python 3.14 del equipo,
donde numpy falla):
    python scripts/dashboard_sintetizar.py <carpeta_datos> [minutos_por_tabla] [tabla ...]

Lee semilla_*.csv y escribe sintetico_*.csv con el mismo número de filas.
"""
import sys
import tempfile
import time
from pathlib import Path

import pandas as pd
from mostlyai.sdk import MostlyAI

TABLAS = {
    "tickets": ["fecha"],
    "vulnerabilidades": ["fecha_deteccion"],
    "personas": [],
}


def main():
    carpeta = Path(sys.argv[1]).resolve()
    minutos = float(sys.argv[2]) if len(sys.argv) > 2 else 2
    solo = sys.argv[3:]  # opcional: nombres de tablas a regenerar
    mostly = MostlyAI(local=True, local_dir=str(Path(tempfile.gettempdir()) / "mostlyai-peti"))
    for nombre, fechas in TABLAS.items():
        if solo and nombre not in solo:
            continue
        df = pd.read_csv(carpeta / f"semilla_{nombre}.csv", parse_dates=fechas or False)
        inicio = time.time()
        g = mostly.train(config={
            "name": f"PETI Colombia - {nombre}",
            "tables": [{
                "name": nombre,
                "data": df,
                "tabular_model_configuration": {"max_training_time": minutos},
            }],
        }, start=True, wait=True)
        sd = mostly.generate(g, size=len(df), start=True, wait=True)
        sint = sd.data()
        if isinstance(sint, dict):
            sint = sint[nombre]
        for col in fechas:
            sint[col] = pd.to_datetime(sint[col]).dt.date
        sint.to_csv(carpeta / f"sintetico_{nombre}.csv", index=False, encoding="utf-8")
        print(f"{nombre}: {len(df)} filas semilla -> {len(sint)} sintéticas en {time.time() - inicio:.0f} s")


if __name__ == "__main__":
    main()
