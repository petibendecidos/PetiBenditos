"""Llena la autoevaluación de madurez del gobierno de TI (EIS, IT Governance Self-Assessment) con Excel.

Uso:
    python scripts/generar_autoevaluacion_gobierno_ti.py <plantilla.xlsx> <fuente.md> <salida.xlsx>

Toma de la fuente la tabla entre <!-- respuestas --> y <!-- fin-respuestas --> (31 filas: N.º, pregunta,
respuesta Yes/Partial/No y sustento), escribe la respuesta en la columna D y el sustento en la columna E
("Comments") de la hoja Assessment, deja que Excel recalcule la hoja oculta Validation y comprueba que
los puntos por sección y el total coinciden con la tabla "Resultado" de la fuente. Exporta además la
hoja Results como resultados.png junto a la fuente, para el Word del análisis.

Se usa Excel por COM y no openpyxl porque openpyxl borra las extensiones de formato condicional y puede
perder las imágenes y los comentarios de la plantilla.
"""
import datetime
import os
import re
import shutil
import sys

import win32com.client

AGENCIA = "Perficient Inc. - Operación en Colombia"  # más largo no cabe en la celda de Results
FECHA = datetime.date(2026, 11, 16)
# Fila de la primera pregunta y número de preguntas de cada sección en la hoja Assessment.
SECCIONES = [(9, 6), (19, 5), (28, 8), (40, 5), (49, 7)]
PUNTOS = {"Yes": 2, "Partial": 1, "No": 0}


def leer_respuestas(texto):
    bloque = re.search(r"<!-- respuestas -->(.*?)<!-- fin-respuestas -->", texto, re.S).group(1)
    filas = []
    for linea in bloque.splitlines():
        celdas = [c.strip() for c in linea.strip().strip("|").split("|")]
        if len(celdas) == 4 and re.fullmatch(r"\d\.\d", celdas[0]):
            filas.append(celdas)
    esperadas = [f"{s + 1}.{i + 1}" for s, (_, n) in enumerate(SECCIONES) for i in range(n)]
    if [f[0] for f in filas] != esperadas:
        sys.exit(f"La tabla de respuestas debe tener las preguntas {esperadas[0]} a {esperadas[-1]} en orden")
    for f in filas:
        if f[2] not in PUNTOS:
            sys.exit(f"Pregunta {f[0]}: la respuesta debe ser Yes, Partial o No, no '{f[2]}'")
    return filas


def leer_resultado(texto):
    """Puntos por sección y total de la tabla 'Resultado' de la fuente."""
    bloque = texto.split("## Resultado", 1)[1].split("\n## ", 1)[0]
    puntos = {}
    for linea in bloque.splitlines():
        celdas = [c.strip() for c in linea.strip().strip("|").split("|")]
        if len(celdas) == 7 and (re.match(r"\d\.", celdas[0]) or celdas[0] == "Total"):
            puntos[celdas[0][0] if celdas[0] != "Total" else "Total"] = int(celdas[4])
    return puntos


def main(plantilla, fuente, salida):
    texto = open(fuente, encoding="utf8").read()
    filas = leer_respuestas(texto)
    esperado = leer_resultado(texto)

    calculado, k = {}, 0
    for s, (_, n) in enumerate(SECCIONES):
        calculado[str(s + 1)] = sum(PUNTOS[f[2]] for f in filas[k:k + n])
        k += n
    calculado["Total"] = sum(calculado.values())
    if calculado != esperado:
        sys.exit(f"La tabla 'Resultado' de la fuente no cuadra con las respuestas: {esperado} frente a {calculado}")

    salida = os.path.abspath(salida)
    shutil.copyfile(plantilla, salida)
    xl = win32com.client.DispatchEx("Excel.Application")
    xl.Visible = False
    xl.DisplayAlerts = False
    try:
        wb = xl.Workbooks.Open(salida)
        ws = wb.Worksheets("Assessment")
        ws.Range("C4").Value = AGENCIA
        # La hoja está protegida con contraseña: deja escribir en las celdas de respuesta y cambiar el alto
        # de las filas, pero no el formato de celda. E4 ya trae formato de fecha ("November 16, 2026") y la
        # columna E ya ajusta el texto.
        ws.Range("E4").Value = datetime.datetime(FECHA.year, FECHA.month, FECHA.day)
        k = 0
        for fila0, n in SECCIONES:
            for i in range(n):
                _, _, resp, sustento = filas[k]
                r = fila0 + i
                alto = ws.Rows(r).RowHeight
                ws.Cells(r, 4).Value = resp
                ws.Cells(r, 5).Value = sustento
                ws.Rows(r).AutoFit()
                # AutoFit ignora las celdas combinadas de la pregunta; se suma un margen para que el
                # comentario no quede pegado al borde.
                ws.Rows(r).RowHeight = min(409, max(alto, ws.Rows(r).RowHeight + 6))
                k += 1
        xl.CalculateFull()

        val = wb.Worksheets("Validation")
        libro = {str(s + 1): int(val.Cells(10, 4 + s).Value) for s in range(5)}
        libro["Total"] = int(val.Range("I10").Value)
        if libro != calculado:
            sys.exit(f"El libro calculó {libro} y la fuente dice {calculado}")
        porcentaje = val.Range("I12").Value
        nivel = wb.Worksheets("Results").Range("J4").Value
        print(f"Puntos {libro['Total']} de {int(val.Range('I11').Value)} ({porcentaje:.1%}); nivel {nivel}")

        # Results también está protegida: la imagen se arma en un libro temporal.
        res = wb.Worksheets("Results")
        res.Activate()
        rango = res.Range("B2:L22")
        rango.CopyPicture(1, 2)  # xlScreen, xlBitmap
        tmp = xl.Workbooks.Add()
        co = tmp.Worksheets(1).ChartObjects().Add(0, 0, rango.Width, rango.Height)
        co.Chart.ChartArea.Format.Line.Visible = False
        co.Activate()
        co.Chart.Paste()
        png = os.path.join(os.path.dirname(os.path.abspath(fuente)), "resultados.png")
        co.Chart.Export(png)
        tmp.Close(False)
        wb.Activate()
        wb.Worksheets("Assessment").Activate()
        wb.Worksheets("Assessment").Range("D9").Select()
        wb.Save()
        wb.Close(False)
        print("ok", salida)
        print("ok", png)
    finally:
        xl.Quit()


if __name__ == "__main__":
    main(*sys.argv[1:4])
