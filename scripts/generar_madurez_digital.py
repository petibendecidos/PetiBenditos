"""Diligencia la Herramienta de Medición de Madurez Digital del MinTIC (.xlsm) desde una fuente Markdown.

Uso:
    python scripts/generar_madurez_digital.py <herramienta original .xlsm> <fuente .md> <salida .xlsm>

Toma de la fuente (docs/entregas-2026-11-04/madurez-digital.md) cuatro bloques marcados con comentarios
HTML: <!-- respuestas --> (17 filas N.º | Dimensión | Pregunta | Puntaje | Sustento), <!-- procesos -->,
<!-- areas --> y <!-- cruces --> (Área | Proceso | F | P | U | Valor | Iniciativa). Comprueba que cada
valor del mapa de calor coincida con la tabla de priorización del MinTIC, calcula los puntos
calientes con el código original de la macro `vecinos` (scripts/vba_vecinos.py) y pasa todo a
scripts/excel_com_madurez.ps1, que llena el libro con Excel. Imprime el resultado leído del libro
(niveles por dimensión y puntos calientes).
"""
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

from vba_vecinos import priorizar

PS1 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "excel_com_madurez.ps1")
INICIATIVAS = 3   # opción "Priorización de Iniciativas" del mapa de calor (1, 2 o 3)

# Tabla de priorización del Marco de Transformación Digital (MinTIC, 2020, figura 41):
# PRIORIDAD[factibilidad][potencial][urgencia], cada factor de 1 a 3.
PRIORIDAD = {
    1: {1: (1, 1, 2), 2: (1, 3, 5), 3: (3, 4, 6)},
    2: {1: (1, 2, 3), 2: (4, 6, 7), 3: (7, 8, 9)},
    3: {1: (3, 4, 7), 2: (6, 7, 8), 3: (9, 9, 9)},
}


def bloque(md, nombre):
    m = re.search(rf"<!-- {nombre} -->(.*?)<!-- fin-{nombre} -->", md, re.S)
    if not m:
        sys.exit(f"Falta el bloque <!-- {nombre} --> en la fuente")
    filas = []
    for linea in m.group(1).strip().splitlines():
        celdas = [c.strip() for c in linea.strip().strip("|").split("|")]
        if not linea.strip().startswith("|") or set(celdas[0]) <= {"-"}:
            continue
        filas.append(celdas)
    return filas[1:]  # sin encabezado


def main():
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    plantilla, fuente, salida = (os.path.abspath(a) for a in sys.argv[1:])
    md = open(fuente, encoding="utf-8").read()

    respuestas = {int(f[0]): int(f[3]) for f in bloque(md, "respuestas")}
    if sorted(respuestas) != list(range(1, 18)) or not all(0 <= v <= 4 for v in respuestas.values()):
        sys.exit("El cuestionario necesita las preguntas 1 a 17, con puntajes de 0 a 4")

    procesos = [(f[0], f[1]) for f in bloque(md, "procesos")]
    areas = [(f[0], f[1]) for f in bloque(md, "areas")]
    ids_p = [p for p, _ in procesos]
    ids_a = [a for a, _ in areas]
    matriz = [[0] * len(procesos) for _ in areas]
    for area, proceso, f, p, u, valor, *_ in bloque(md, "cruces"):
        esperado = PRIORIDAD[int(f)][int(p)][int(u) - 1]
        if int(valor) != esperado:
            sys.exit(f"{area} × {proceso}: F{f} P{p} U{u} da {esperado} en la tabla, no {valor}")
        matriz[ids_a.index(area)][ids_p.index(proceso)] = esperado

    datos = {
        "respuestas": [respuestas[i] for i in range(1, 18)],
        "procesos": [f"{i} {n}" for i, n in procesos],
        "areas": [f"{i} {n}" for i, n in areas],
        "matriz": matriz,
        "iniciativas": INICIATIVAS,
    }
    datos["resultados"] = priorizar(plantilla, datos["procesos"], datos["areas"], matriz, INICIATIVAS)
    shutil.copyfile(plantilla, salida)
    with tempfile.TemporaryDirectory() as tmp:
        ruta_json = os.path.join(tmp, "datos.json")
        with open(ruta_json, "w", encoding="utf-8") as fh:
            json.dump(datos, fh, ensure_ascii=False)
        subprocess.run(["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", PS1,
                        "-Libro", salida, "-Datos", ruta_json], check=True, timeout=600)


if __name__ == "__main__":
    main()
