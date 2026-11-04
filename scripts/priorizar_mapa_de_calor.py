"""Prioriza un mapa de calor de la herramienta del MinTIC sin abrir Excel.

Uso:
    python scripts/priorizar_mapa_de_calor.py <herramienta .xlsm> <fuente .md> <bloque de cruces> [procesos.md]

Lee de la fuente el bloque <!-- <bloque> --> con filas Área | Proceso | F | P | U | Valor | …, toma los
procesos y las áreas de los bloques <!-- procesos --> y <!-- areas --> (de la misma fuente o de la
indicada al final), comprueba cada valor contra la tabla de priorización y ejecuta la macro `vecinos`
original con scripts/vba_vecinos.py. Imprime la matriz y los tres puntos calientes en Markdown.
"""
import sys

from generar_madurez_digital import PRIORIDAD, bloque
from vba_vecinos import priorizar


def main():
    if len(sys.argv) not in (4, 5):
        sys.exit(__doc__)
    xlsm, fuente, nombre = sys.argv[1:4]
    md = open(fuente, encoding="utf-8").read()
    ejes = open(sys.argv[4], encoding="utf-8").read() if len(sys.argv) == 5 else md
    procesos = [(f[0], f[1]) for f in bloque(ejes, "procesos")]
    areas = [(f[0], f[1]) for f in bloque(ejes, "areas")]
    ids_p, ids_a = [p for p, _ in procesos], [a for a, _ in areas]
    matriz = [[0] * len(procesos) for _ in areas]
    for area, proceso, f, p, u, valor, *_ in bloque(md, nombre):
        esperado = PRIORIDAD[int(f)][int(p)][int(u) - 1]
        if int(valor) != esperado:
            sys.exit(f"{area} × {proceso}: F{f} P{p} U{u} da {esperado} en la tabla, no {valor}")
        matriz[ids_a.index(area)][ids_p.index(proceso)] = esperado

    print("| Área | " + " | ".join(ids_p) + " |")
    print("|---|" + "---|" * len(ids_p))
    for (a, n), fila in zip(areas, matriz):
        print(f"| {a} {n} | " + " | ".join(str(v) for v in fila) + " |")
    print()
    print("| Puesto | Proceso | Área | Valor | Índice de priorización |")
    print("|---|---|---|---|---|")
    resultados = priorizar(xlsm, [f"{i} {n}" for i, n in procesos], [f"{i} {n}" for i, n in areas], matriz, 3)
    for k, (proc, area, valor, indice) in enumerate(resultados, 1):
        print(f"| {k} | {proc} | {area} | {valor:g} | {indice:.2f} |".replace(".", ","))


if __name__ == "__main__":
    main()
