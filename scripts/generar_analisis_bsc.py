"""Arma en Excel el análisis del diagnóstico BSC de gestión y gobierno de TI (tablas dinámicas, segmentaciones y tablero).

Uso:
    python scripts/generar_analisis_bsc.py <formato_diligenciado.docx> <diagnostico-bsc.md> <clasificacion-bsc.md> <salida.xlsx>

Junta tres fuentes:
- el texto de los 40 enunciados, de las tablas del formato diligenciado (Word);
- el puntaje y el sustento de cada enunciado, del bloque <!-- calificaciones --> de diagnostico-bsc.md;
- la clasificación (tema, perspectiva, objetivo de COBIT, respuesta y cobertura del PETI, puntaje al mes 24),
  del bloque <!-- clasificacion --> de clasificacion-bsc.md.

El libro se construye con Excel por COM porque openpyxl no crea tablas dinámicas ni segmentaciones. Las columnas
derivadas (banda, crítico, ámbito, brechas) son fórmulas de la tabla, así que cambiar un puntaje o el umbral de la
hoja Parámetros recalcula todo. Al final compara los totales del libro con los de la fuente y exporta tres imágenes
(tablero.png, resumen.png y prioridades.png) junto a clasificacion-bsc.md para el Word del análisis.
"""
import os
import re
import sys
from collections import Counter, defaultdict

import docx
import win32com.client

ELEMENTOS = ["1. Enfoque estratégico", "2. Traslado hacia el BSC",
             "3. Sincronización y despliegue", "4. Cultura de ejecución"]
PERSPECTIVAS = ["Financiera", "Cliente", "Procesos internos", "Aprendizaje y crecimiento", "Sistema de gestión"]
COBERTURAS = ["Cubierto", "Cubierto en parte", "Sin respuesta", "Fuera del alcance de TI"]
RESPALDOS = ["Pública", "Pública y cuenta analizada", "Cuenta analizada", "Documentos del equipo"]
BANDAS = [(0, "0", "No existe y no hay ningún indicio"),
          (1, "1 a 2", "Indicios aislados, sin documento"),
          (3, "3 a 4", "Existe en parte o de manera informal, o solo se observó en la cuenta analizada"),
          (5, "5 a 6", "Está definido o documentado, pero no aprobado, no medido o en uso parcial"),
          (7, "7 a 8", "Documentado y en uso, con brechas menores"),
          (9, "9 a 10", "Documentado, medido y mejorado de forma sistemática")]
NIVELES = [(0, "Bloqueador", "El elemento impide ejecutar la estrategia"),
           (40, "En construcción", "Existe por partes, sin conexión"),
           (60, "Funcional", "Opera con brechas puntuales"),
           (80, "Impulsor", "Sostiene la ejecución")]
UMBRAL = 3
# Formatos de número con un decimal. pywin32 llama a Excel con la configuración regional del usuario, así que
# NumberFormat se lee en el idioma de Excel (en español, "." es separador de miles). main() los ajusta.
F1, FP = "0.0", "0.0%"

# Colores (Excel usa BGR en los enteros RGB).
def rgb(h):
    h = h.lstrip("#")
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return r + g * 256 + b * 65536

AZUL, NARANJA, ROJO, GRIS, GRIS_CLARO, BLANCO = (rgb("1F3A5F"), rgb("D9822B"), rgb("B03A2E"),
                                                 rgb("6B7280"), rgb("EEF1F5"), rgb("FFFFFF"))

# Constantes de Excel.
XL_DATABASE, XL_ROW, XL_COL, XL_DATA = 1, 1, 2, 4
XL_SUM, XL_COUNT, XL_AVG = -4157, -4112, -4106
XL_COLUMN, XL_COLUMN_STACKED, XL_RADAR_MARKERS, XL_BAR = 51, 52, 81, 57
XL_TABULAR, XL_ASC, XL_DESC = 1, 1, 2
XL_CENTER, XL_LEFT, XL_TOP = -4108, -4131, -4160


def tabla_md(texto, marca, columnas):
    bloque = re.search(rf"<!-- {marca} -->(.*?)<!-- fin-{marca} -->", texto, re.S).group(1)
    filas = []
    for linea in bloque.splitlines():
        celdas = [c.strip() for c in linea.strip().strip("|").split("|")]
        if len(celdas) == columnas and celdas[0].isdigit():
            filas.append(celdas)
    if [int(f[0]) for f in filas] != list(range(1, 41)):
        sys.exit(f"El bloque {marca} debe tener los enunciados 1 a 40 en orden")
    return filas


def leer_enunciados(ruta_docx):
    d = docx.Document(ruta_docx)
    textos = []
    for t in d.tables:
        cab = t.rows[0].cells[1].text if len(t.columns) >= 3 else ""
        if "Impulsores/bloqueadores" in cab:
            textos += [r.cells[1].text.strip() for r in t.rows[1:]]
    if len(textos) != 40:
        sys.exit(f"Se esperaban 40 enunciados en el formato y se encontraron {len(textos)}")
    return textos


def respaldo(sustento):
    pub, prv = "PUB-" in sustento, "PRV-" in sustento
    if pub and prv:
        return "Pública y cuenta analizada"
    if pub:
        return "Pública"
    if prv:
        return "Cuenta analizada"
    return "Documentos del equipo"


def ids(sustento):
    vistos = []
    for i in re.findall(r"(?:PUB|PRV|INT)-\d{3}", sustento):
        if i not in vistos:
            vistos.append(i)
    return ", ".join(vistos) if vistos else "—"


def construir_filas(enunciados, calif, clasif):
    filas = []
    for i in range(40):
        n = i + 1
        _, puntaje, sustento = calif[i]
        _, tema, persp, cobit, resp, cob, mes24, por_que = clasif[i]
        if persp not in PERSPECTIVAS or cob not in COBERTURAS:
            sys.exit(f"Enunciado {n}: perspectiva '{persp}' o cobertura '{cob}' no válida")
        if not re.fullmatch(r"(EDM|APO|BAI|DSS|MEA)\d\d", cobit):
            sys.exit(f"Enunciado {n}: objetivo de COBIT '{cobit}' no válido")
        filas.append({
            "n": n, "elemento": ELEMENTOS[i // 10], "n_formato": i % 10 + 1, "enunciado": enunciados[i],
            "tema": tema, "puntaje": int(puntaje), "mes24": int(mes24), "persp": persp, "cobit": cobit,
            "resp": resp, "cob": cob, "respaldo": respaldo(sustento), "ids": ids(sustento),
            "sustento": sustento, "por_que": por_que,
        })
    return filas


def resumen_python(filas):
    """Cifras que el libro debe reproducir y que usa el análisis escrito."""
    r = {"elemento": {}, "persp": {}, "ambito": {}, "cob": Counter(), "respaldo": Counter()}
    for e in ELEMENTOS:
        fs = [f for f in filas if f["elemento"] == e]
        r["elemento"][e] = (sum(f["puntaje"] for f in fs), sum(f["mes24"] for f in fs))
    for p in PERSPECTIVAS:
        fs = [f for f in filas if f["persp"] == p]
        r["persp"][p] = (len(fs), sum(f["puntaje"] for f in fs) / len(fs), sum(f["mes24"] for f in fs) / len(fs),
                         sum(f["puntaje"] <= UMBRAL for f in fs))
    for a in ("Gobierno", "Gestión"):
        fs = [f for f in filas if (f["cobit"].startswith("EDM")) == (a == "Gobierno")]
        r["ambito"][a] = (len(fs), sum(f["puntaje"] for f in fs) / len(fs), sum(f["mes24"] for f in fs) / len(fs),
                          sum(f["puntaje"] <= UMBRAL for f in fs))
    for f in filas:
        r["cob"][f["cob"]] += 1
        r["respaldo"][f["respaldo"]] += 1
    r["total"] = (sum(f["puntaje"] for f in filas), sum(f["mes24"] for f in filas))
    r["criticos"] = [f["n"] for f in filas if f["puntaje"] <= UMBRAL]
    return r


# ----------------------------------------------------------------------------------------------- Excel

def titulo(ws, celda, texto, tam=16, color=AZUL):
    c = ws.Range(celda)
    c.Value = texto
    c.Font.Size = tam
    c.Font.Bold = True
    c.Font.Color = color


def encabezado(rango):
    rango.Font.Bold = True
    rango.Font.Color = BLANCO
    rango.Interior.Color = AZUL
    rango.WrapText = True
    rango.VerticalAlignment = XL_CENTER


def bordes(rango):
    for b in (7, 8, 9, 10, 11, 12):  # izquierda, arriba, abajo, derecha, internos
        rango.Borders(b).LineStyle = 1
        rango.Borders(b).Color = rgb("C9D1DB")


def hoja_parametros(wb, ws):
    ws.Name = "Parámetros"
    titulo(ws, "B2", "Parámetros del análisis")
    ws.Range("B3").Value = "Cambie el umbral y todo el libro se recalcula: columna Crítico, tarjetas, resumen y prioridades."
    ws.Range("B5").Value = "Umbral de causa crítica (puntaje igual o menor)"
    ws.Range("C5").Value = UMBRAL
    ws.Range("C5").Interior.Color = rgb("FFF4CC")
    ws.Range("C5").Font.Bold = True
    wb.Names.Add("UmbralCritico", "='Parámetros'!$C$5")

    ws.Range("B7").Value = "Rúbrica de calificación de cada enunciado (0 a 10)"
    ws.Range("B7").Font.Bold = True
    ws.Range("B8:D8").Value = ("Desde", "Banda", "Criterio")
    encabezado(ws.Range("B8:D8"))
    ws.Range(f"B9:D{8 + len(BANDAS)}").Value = BANDAS
    bordes(ws.Range(f"B8:D{8 + len(BANDAS)}"))
    wb.Names.Add("BandaDesde", f"='Parámetros'!$B$9:$B${8 + len(BANDAS)}")
    wb.Names.Add("BandaNombre", f"='Parámetros'!$C$9:$C${8 + len(BANDAS)}")

    f0 = 10 + len(BANDAS)
    ws.Range(f"B{f0}").Value = "Niveles de cada elemento (puntos sobre 100) y del total (porcentaje)"
    ws.Range(f"B{f0}").Font.Bold = True
    ws.Range(f"B{f0 + 1}:D{f0 + 1}").Value = ("Desde", "Nivel", "Lectura")
    encabezado(ws.Range(f"B{f0 + 1}:D{f0 + 1}"))
    ws.Range(f"B{f0 + 2}:D{f0 + 1 + len(NIVELES)}").Value = NIVELES
    bordes(ws.Range(f"B{f0 + 1}:D{f0 + 1 + len(NIVELES)}"))
    wb.Names.Add("NivelDesde", f"='Parámetros'!$B${f0 + 2}:$B${f0 + 1 + len(NIVELES)}")
    wb.Names.Add("NivelNombre", f"='Parámetros'!$C${f0 + 2}:$C${f0 + 1 + len(NIVELES)}")
    f1 = f0 + 3 + len(NIVELES)
    ws.Range(f"B{f1}").Value = ("La rúbrica y los niveles son criterio del equipo; el formato del docente no trae "
                                "ninguno. Los niveles se leen igual para los puntos de un elemento (sobre 100) y para "
                                "el porcentaje del total.")
    ws.Columns("A").ColumnWidth = 2
    ws.Columns("B").ColumnWidth = 44
    ws.Columns("C").ColumnWidth = 18
    ws.Columns("D").ColumnWidth = 80
    ws.Range("B5").WrapText = True


COLS = ["N.º", "Elemento", "N.º en el formato", "Enunciado", "Tema", "Puntaje", "Puntaje mes 24", "Mejora",
        "Brecha actual", "Brecha mes 24", "Banda", "Crítico", "Es crítico", "Perspectiva BSC", "Objetivo COBIT 2019",
        "Ámbito", "Respuesta del PETI", "Cobertura del PETI", "Respaldo", "Evidencia", "Sustento",
        "Razón de la proyección"]
FORMULAS = {
    "Mejora": "=[@[Puntaje mes 24]]-[@Puntaje]",
    "Brecha actual": "=10-[@Puntaje]",
    "Brecha mes 24": "=10-[@[Puntaje mes 24]]",
    "Banda": "=XLOOKUP([@Puntaje],BandaDesde,BandaNombre,\"\",-1)",
    "Crítico": "=IF([@Puntaje]<=UmbralCritico,\"Sí\",\"No\")",
    "Es crítico": "=IF([@Puntaje]<=UmbralCritico,1,0)",
    "Ámbito": "=IF(LEFT([@[Objetivo COBIT 2019]],3)=\"EDM\",\"Gobierno\",\"Gestión\")",
}


def hoja_datos(ws, filas):
    ws.Name = "Datos"
    titulo(ws, "A1", "Datos del diagnóstico: un registro por enunciado")
    ws.Range("A2").Value = ("Fuente única del análisis. Las columnas en gris son fórmulas; las demás se capturan. "
                            "Puntaje y sustento: diagnóstico BSC del equipo (INT-001). Proyección al mes 24: "
                            "puntaje si los 25 proyectos del PETI Colombia v1.0 se ejecutan como están escritos.")
    ws.Range("A2").WrapText = False
    valores = []
    for f in filas:
        fila = {"N.º": f["n"], "Elemento": f["elemento"], "N.º en el formato": f["n_formato"],
                "Enunciado": f["enunciado"], "Tema": f["tema"], "Puntaje": f["puntaje"],
                "Puntaje mes 24": f["mes24"], "Perspectiva BSC": f["persp"], "Objetivo COBIT 2019": f["cobit"],
                "Respuesta del PETI": f["resp"], "Cobertura del PETI": f["cob"], "Respaldo": f["respaldo"],
                "Evidencia": f["ids"], "Sustento": f["sustento"], "Razón de la proyección": f["por_que"]}
        valores.append(tuple(fila.get(c, "") for c in COLS))
    ncol = len(COLS)
    ult = ws.Cells(4 + 40, ncol).Address
    ws.Range(ws.Cells(4, 1), ws.Cells(4, ncol)).Value = tuple(COLS)
    ws.Range(ws.Cells(5, 1), ws.Cells(44, ncol)).Value = valores
    lo = ws.ListObjects.Add(1, ws.Range(f"A4:{ult}"), None, 1)
    lo.Name = "tblDiagnostico"
    lo.TableStyle = "TableStyleMedium2"
    for col, formula in FORMULAS.items():
        rango = lo.ListColumns(col).DataBodyRange
        rango.Formula2 = formula
        rango.Interior.Color = rgb("E7EAEE")
    anchos = {"N.º": 5, "Elemento": 24, "N.º en el formato": 9, "Enunciado": 60, "Tema": 32, "Puntaje": 9,
              "Puntaje mes 24": 9, "Mejora": 8, "Brecha actual": 8, "Brecha mes 24": 8, "Banda": 7, "Crítico": 8,
              "Es crítico": 7, "Perspectiva BSC": 20, "Objetivo COBIT 2019": 10, "Ámbito": 10,
              "Respuesta del PETI": 34, "Cobertura del PETI": 18, "Respaldo": 20, "Evidencia": 18,
              "Sustento": 80, "Razón de la proyección": 50}
    for i, c in enumerate(COLS, start=1):
        ws.Columns(i).ColumnWidth = anchos[c]
    ws.Range(ws.Cells(4, 1), ws.Cells(4, ncol)).WrapText = True
    ws.Rows(4).RowHeight = 32
    cuerpo = ws.Range(ws.Cells(5, 1), ws.Cells(44, ncol))
    cuerpo.WrapText = True
    cuerpo.VerticalAlignment = XL_TOP
    # Barras de datos sobre el puntaje y el puntaje proyectado.
    for c in ("Puntaje", "Puntaje mes 24"):
        r = lo.ListColumns(c).DataBodyRange
        db = r.FormatConditions.AddDatabar()
        db.BarColor.Color = AZUL if c == "Puntaje" else NARANJA
        db.MinPoint.Modify(0, 0)   # xlConditionValueNumber = 0
        db.MaxPoint.Modify(0, 10)
    crit = lo.ListColumns("Crítico").DataBodyRange
    fc = crit.FormatConditions.Add(1, 3, '="Sí"')  # xlCellValue, xlEqual
    fc.Font.Color = ROJO
    fc.Font.Bold = True
    return lo


def inmovilizar_datos(ws):
    """Encabezado y tema fijos en Datos. Va al final: con Excel oculto, inmovilizar paneles antes de escribir
    fórmulas que se desbordan (FILTER, SORTBY) hace que Excel se cierre."""
    ws.Activate()
    ws.Range("F5").Select()
    ws.Application.ActiveWindow.FreezePanes = True


def hoja_resumen(wb, ws):
    ws.Name = "Resumen"
    titulo(ws, "B2", "Resumen calculado con fórmulas sobre la hoja Datos")
    ws.Range("B3").Value = ("No depende de las segmentaciones del tablero: muestra siempre los 40 enunciados. "
                            "Mes 24: proyección si se ejecuta el PETI Colombia v1.0 como está escrito.")
    t = "tblDiagnostico"
    # 1. Elementos.
    ws.Range("B5").Value = "1. Resultado por elemento del método (puntos sobre 100)"
    ws.Range("B5").Font.Bold = True
    cab = ("Elemento", "Puntaje", "Máximo", "Porcentaje", "Nivel", "Mes 24", "Nivel mes 24", "Mejora",
           "Causas críticas")
    ws.Range("B6:J6").Value = cab
    encabezado(ws.Range("B6:J6"))
    for i, e in enumerate(ELEMENTOS):
        r = 7 + i
        ws.Range(f"B{r}").Value = e
        ws.Range(f"C{r}").Formula2 = f"=SUMIFS({t}[Puntaje],{t}[Elemento],$B{r})"
        ws.Range(f"D{r}").Formula2 = f"=COUNTIFS({t}[Elemento],$B{r})*10"
        ws.Range(f"E{r}").Formula2 = f"=C{r}/D{r}"
        ws.Range(f"F{r}").Formula2 = f"=XLOOKUP(E{r}*100,NivelDesde,NivelNombre,\"\",-1)"
        ws.Range(f"G{r}").Formula2 = f"=SUMIFS({t}[Puntaje mes 24],{t}[Elemento],$B{r})"
        ws.Range(f"H{r}").Formula2 = f"=XLOOKUP(G{r}/D{r}*100,NivelDesde,NivelNombre,\"\",-1)"
        ws.Range(f"I{r}").Formula2 = f"=G{r}-C{r}"
        ws.Range(f"J{r}").Formula2 = f"=COUNTIFS({t}[Elemento],$B{r},{t}[Es crítico],1)"
    ws.Range("B11").Value = "Total"
    for col in "CDGIJ":
        ws.Range(f"{col}11").Formula2 = f"=SUM({col}7:{col}10)"
    ws.Range("E11").Formula2 = "=C11/D11"
    ws.Range("F11").Formula2 = "=XLOOKUP(E11*100,NivelDesde,NivelNombre,\"\",-1)"
    ws.Range("H11").Formula2 = "=XLOOKUP(G11/D11*100,NivelDesde,NivelNombre,\"\",-1)"
    ws.Range("B11:J11").Font.Bold = True
    ws.Range("B11:J11").Interior.Color = GRIS_CLARO
    ws.Range("E7:E11").NumberFormat = FP
    bordes(ws.Range("B6:J11"))
    # Formato de nivel.
    for rango in (ws.Range("F7:F11"), ws.Range("H7:H11")):
        for nivel, color in (("Bloqueador", "F4C7C3"), ("En construcción", "FCE8B2"), ("Funcional", "D9EAD3"),
                             ("Impulsor", "B7E1CD")):
            fc = rango.FormatConditions.Add(1, 3, f'="{nivel}"')
            fc.Interior.Color = rgb(color)

    def bloque(fila, titulo_bloque, campo, categorias):
        ws.Range(f"B{fila}").Value = titulo_bloque
        ws.Range(f"B{fila}").Font.Bold = True
        ws.Range(f"B{fila + 1}:G{fila + 1}").Value = (campo, "Enunciados", "Promedio actual", "Promedio mes 24",
                                                      "Mejora", "Causas críticas")
        encabezado(ws.Range(f"B{fila + 1}:G{fila + 1}"))
        for i, c in enumerate(categorias):
            r = fila + 2 + i
            ws.Range(f"B{r}").Value = c
            ws.Range(f"C{r}").Formula2 = f"=COUNTIFS({t}[{campo}],$B{r})"
            ws.Range(f"D{r}").Formula2 = f"=IFERROR(AVERAGEIFS({t}[Puntaje],{t}[{campo}],$B{r}),\"—\")"
            ws.Range(f"E{r}").Formula2 = f"=IFERROR(AVERAGEIFS({t}[Puntaje mes 24],{t}[{campo}],$B{r}),\"—\")"
            ws.Range(f"F{r}").Formula2 = f"=IFERROR(E{r}-D{r},\"—\")"
            ws.Range(f"G{r}").Formula2 = f"=COUNTIFS({t}[{campo}],$B{r},{t}[Es crítico],1)"
        fin = fila + 1 + len(categorias)
        ws.Range(f"D{fila + 2}:F{fin}").NumberFormat = F1
        bordes(ws.Range(f"B{fila + 1}:G{fin}"))
        return fila + 2, fin

    p0, p1 = bloque(14, "2. Promedio por perspectiva del BSC (0 a 10)", "Perspectiva BSC", PERSPECTIVAS)
    a0, a1 = bloque(p1 + 3, "3. Gobierno frente a gestión (según el objetivo de COBIT 2019)", "Ámbito",
                    ["Gobierno", "Gestión"])
    c0, c1 = bloque(a1 + 3, "4. Cobertura del PETI Colombia v1.0", "Cobertura del PETI", COBERTURAS)
    r0, r1 = bloque(c1 + 3, "5. Respaldo del puntaje (tipo de evidencia del sustento)", "Respaldo", RESPALDOS)
    ws.Columns("A").ColumnWidth = 2
    ws.Columns("B").ColumnWidth = 32
    for col in "CDEFGHIJ":
        ws.Columns(col).ColumnWidth = 13
    ws.Range("B6:J6").RowHeight = 30

    # Radar: el gráfico que pide el formato, ahora con la proyección.
    izq = ws.Range("L5").Left
    co = ws.ChartObjects().Add(izq, ws.Range("L5").Top, 430, 300)
    ch = co.Chart
    ch.ChartType = XL_RADAR_MARKERS
    sc = ch.SeriesCollection().NewSeries()
    sc.Name = "='Resumen'!$C$6"
    sc.Values = "='Resumen'!$C$7:$C$10"
    sc.XValues = "='Resumen'!$B$7:$B$10"
    sc.Format.Line.ForeColor.RGB = AZUL
    sc.Format.Line.Weight = 2.5
    s2 = ch.SeriesCollection().NewSeries()
    s2.Name = "='Resumen'!$G$6"
    s2.Values = "='Resumen'!$G$7:$G$10"
    s2.XValues = "='Resumen'!$B$7:$B$10"
    s2.Format.Line.ForeColor.RGB = NARANJA
    s2.Format.Line.Weight = 2.5
    s2.Format.Line.DashStyle = 4
    ch.HasTitle = True
    ch.ChartTitle.Text = "Los cuatro elementos: hoy y al mes 24 (sobre 100)"
    ch.ChartTitle.Font.Size = 12
    ch.Axes(2).MinimumScale = 0
    ch.Axes(2).MaximumScale = 100
    ch.Axes(2).MajorUnit = 20
    ch.HasLegend = True
    ch.Legend.Position = -4107  # abajo
    co.Name = "Radar"

    co2 = ws.ChartObjects().Add(izq, ws.Range("L5").Top + 315, 430, 260)
    ch2 = co2.Chart
    ch2.ChartType = XL_COLUMN
    s = ch2.SeriesCollection().NewSeries()
    s.Name = "Promedio actual"
    s.Values = f"='Resumen'!$D${p0}:$D${p1}"
    s.XValues = f"='Resumen'!$B${p0}:$B${p1}"
    s.Format.Fill.ForeColor.RGB = AZUL
    s = ch2.SeriesCollection().NewSeries()
    s.Name = "Promedio mes 24"
    s.Values = f"='Resumen'!$E${p0}:$E${p1}"
    s.XValues = f"='Resumen'!$B${p0}:$B${p1}"
    s.Format.Fill.ForeColor.RGB = NARANJA
    ch2.HasTitle = True
    ch2.ChartTitle.Text = "Promedio por perspectiva del BSC (0 a 10)"
    ch2.ChartTitle.Font.Size = 12
    ch2.Axes(2).MinimumScale = 0
    ch2.Axes(2).MaximumScale = 10
    ch2.Axes(2).TickLabels.NumberFormat = "0"
    ch2.HasLegend = True
    ch2.Legend.Position = -4107
    co2.Name = "Perspectivas"
    return {"persp": (p0, p1), "ambito": (a0, a1), "cob": (c0, c1), "respaldo": (r0, r1)}


def hoja_prioridades(ws):
    ws.Name = "Prioridades"
    t = "tblDiagnostico"
    titulo(ws, "B2", "Prioridades: lo que el PETI deja sin cerrar")
    ws.Range("B3").Value = ("Fórmulas dinámicas (FILTER y SORT) sobre la hoja Datos. Se recalculan si cambia un "
                            "puntaje, una cobertura o el umbral de la hoja Parámetros.")
    ws.Range("B5").Value = ("1. Brecha que queda al mes 24 en los enunciados que dependen de TI "
                            "(sin los que están fuera del alcance de TI), de mayor a menor")
    ws.Range("B5").Font.Bold = True
    cab2 = ("N.º", "Tema", "Elemento", "Puntaje", "Mes 24", "Brecha mes 24", "Cobertura del PETI",
            "Respuesta del PETI")
    ws.Range("B6:I6").Value = cab2
    encabezado(ws.Range("B6:I6"))
    ws.Range("B7").Formula2 = (
        f"=LET(d,CHOOSECOLS({t},1,5,2,6,7,10,18,17),"
        f"f,FILTER(d,{t}[Cobertura del PETI]<>\"Fuera del alcance de TI\"),"
        f"SORTBY(f,CHOOSECOLS(f,6),-1,CHOOSECOLS(f,1),1))")
    ws.Range("B42").Value = "2. Causas críticas (puntaje igual o menor al umbral de Parámetros), de menor a mayor puntaje"
    ws.Range("B42").Font.Bold = True
    cab = ("N.º", "Tema", "Elemento", "Puntaje", "Mes 24", "Cobertura del PETI", "Respuesta del PETI")
    ws.Range("B43:H43").Value = cab
    encabezado(ws.Range("B43:H43"))
    ws.Range("B44").Formula2 = (
        f"=LET(d,CHOOSECOLS({t},1,5,2,6,7,18,17),f,FILTER(d,{t}[Es crítico]=1,\"Sin causas críticas\"),"
        f"SORTBY(f,CHOOSECOLS(f,4),1,CHOOSECOLS(f,1),1))")
    for col, ancho in zip("ABCDEFGHI", (2, 6, 40, 28, 9, 9, 12, 22, 50)):
        ws.Columns(col).ColumnWidth = ancho
    ws.Range("B7:I90").VerticalAlignment = XL_TOP
    ws.Range("I7:I39").WrapText = True
    ws.Range("H44:H90").WrapText = True
    fc = ws.Range("B7:I39").FormatConditions.Add(2, 1, "=$G7*1>=6")
    # xlExpression. La fórmula de un formato condicional se lee en el idioma de Excel (español: ";" y nombres
    # traducidos); por eso va sin funciones. Una celda vacía da error al multiplicar y no se colorea.
    fc.Interior.Color = rgb("FBE3E0")
    # Gráfico de las doce brechas mayores al mes 24.
    co = ws.ChartObjects().Add(ws.Range("K6").Left, ws.Range("K6").Top, 470, 330)
    ch = co.Chart
    ch.ChartType = XL_BAR
    s = ch.SeriesCollection().NewSeries()
    s.Name = "Brecha mes 24"
    s.Values = "='Prioridades'!$G$7:$G$18"
    s.XValues = "='Prioridades'!$C$7:$C$18"
    s.Format.Fill.ForeColor.RGB = ROJO
    ch.Axes(1).ReversePlotOrder = True
    ch.Axes(2).MinimumScale = 0
    ch.Axes(2).MaximumScale = 10
    ch.HasTitle = True
    ch.ChartTitle.Text = "Doce brechas mayores al mes 24 (10 menos el puntaje proyectado)"
    ch.ChartTitle.Font.Size = 11
    ch.HasLegend = False
    co.Name = "Brechas"


def crear_pivote(wb, cache, ws, celda, nombre, filas, datos, columnas=(), detalle=False):
    pt = cache.CreatePivotTable(ws.Range(celda), nombre)
    pt.RowAxisLayout(XL_TABULAR)
    pt.ShowDrillIndicators = False
    for i, f in enumerate(filas, start=1):
        pf = pt.PivotFields(f)
        pf.Orientation = XL_ROW
        pf.Position = i
        pf.Subtotals = tuple([False] * 12)
    for f in columnas:
        pt.PivotFields(f).Orientation = XL_COL
    for campo, funcion, leyenda, formato in datos:
        df = pt.AddDataField(pt.PivotFields(campo), leyenda, funcion)
        df.NumberFormat = formato
    if detalle:
        pt.ColumnGrand = False
    return pt


def ordenar(pt, campo, items):
    pf = pt.PivotFields(campo)
    existentes = {pf.PivotItems(i).Name for i in range(1, pf.PivotItems().Count + 1)}
    pos = 1
    for it in items:
        if it in existentes:  # una banda sin enunciados no aparece en el pivote
            pf.PivotItems(it).Position = pos
            pos += 1


def grafico_pivote(ws, pt, rango, tipo, titulo_g, colores, eje_max=None):
    izq, arr = rango.Left, rango.Top
    shp = ws.Shapes.AddChart2(-1, tipo, izq, arr, rango.Width, rango.Height)
    ch = shp.Chart
    ch.SetSourceData(pt.TableRange1)
    ch.ShowAllFieldButtons = False
    ch.HasTitle = True
    ch.ChartTitle.Text = titulo_g
    ch.ChartTitle.Font.Size = 11
    ch.ChartTitle.Font.Bold = True
    for i, color in enumerate(colores, start=1):
        if i <= ch.SeriesCollection().Count:
            ch.SeriesCollection(i).Format.Fill.ForeColor.RGB = color
    if eje_max is not None:
        ch.Axes(2).MinimumScale = 0
        ch.Axes(2).MaximumScale = eje_max
    ch.Axes(2).TickLabels.NumberFormat = "0"
    ch.HasLegend = ch.SeriesCollection().Count > 1
    if ch.HasLegend:
        ch.Legend.Position = -4160  # arriba
    return ch


def tarjeta(ws, rango, etiqueta, formula, formato, nota):
    r = ws.Range(rango)
    c1 = r.Columns(1).Column
    c2 = c1 + r.Columns.Count - 1
    f = r.Row
    def fila(k):
        return ws.Range(ws.Cells(f + k, c1), ws.Cells(f + k, c2))
    for k in range(4):
        fila(k).Merge()
        fila(k).HorizontalAlignment = XL_CENTER
    fila(0).Value = etiqueta
    fila(0).Font.Size = 9
    fila(0).Font.Color = GRIS
    fila(1).Formula2 = formula
    fila(1).NumberFormat = formato
    fila(1).Font.Size = 22
    fila(1).Font.Bold = True
    fila(1).Font.Color = AZUL
    ws.Rows(f + 1).RowHeight = 32
    fila(2).Font.Size = 9
    fila(3).Value = nota
    fila(3).Font.Size = 8
    fila(3).Font.Color = GRIS
    ws.Range(ws.Cells(f, c1), ws.Cells(f + 3, c2)).Interior.Color = GRIS_CLARO
    return fila(2)


def hoja_tablero(wb, ws, wpiv):
    ws.Name = "Tablero"
    xl = wb.Application
    ws.Activate()
    xl.ActiveWindow.DisplayGridlines = False
    ws.Columns("A").ColumnWidth = 1.5
    for col in ("B", "C", "D"):
        ws.Columns(col).ColumnWidth = 10
    ws.Columns("E").ColumnWidth = 2
    for i in range(6, 26):
        ws.Columns(i).ColumnWidth = 8.5
    titulo(ws, "B1", "Diagnóstico BSC de gestión y gobierno de TI: Perficient, operación en Colombia", 16)
    ws.Range("B2").Value = ("Tablero interactivo: las segmentaciones de la izquierda filtran tarjetas, gráficos y "
                            "listado. Puntajes de 0 a 10 por enunciado. Mes 24: proyección si se ejecuta el PETI "
                            "Colombia v1.0 como está escrito.")
    ws.Range("B2").Font.Color = GRIS
    ws.Range("B2").Font.Size = 9

    cache = wb.PivotCaches().Create(XL_DATABASE, "tblDiagnostico", 5)
    pk = crear_pivote(wb, cache, wpiv, "B4", "ptKPI", [],
                      [("Puntaje", XL_SUM, "Puntos", "0"), ("N.º", XL_COUNT, "Enunciados", "0"),
                       ("Puntaje mes 24", XL_SUM, "Puntos mes 24", "0"),
                       ("Es crítico", XL_SUM, "Críticos", "0")])
    wpiv.Range("B2").Value = "Tablas dinámicas que alimentan el tablero (no editar; se actualizan con Datos > Actualizar todo)"
    wpiv.Range("B2").Font.Bold = True
    pe = crear_pivote(wb, cache, wpiv, "B12", "ptElemento", ["Elemento"],
                      [("Puntaje", XL_AVG, "Promedio actual", F1),
                       ("Puntaje mes 24", XL_AVG, "Promedio mes 24", F1)])
    pp = crear_pivote(wb, cache, wpiv, "B22", "ptPerspectiva", ["Perspectiva BSC"],
                      [("Puntaje", XL_AVG, "Promedio actual ", F1),
                       ("Puntaje mes 24", XL_AVG, "Promedio mes 24 ", F1)])
    ordenar(pp, "Perspectiva BSC", PERSPECTIVAS)
    pc = crear_pivote(wb, cache, wpiv, "B33", "ptCobertura", ["Cobertura del PETI"],
                      [("N.º", XL_COUNT, "Cantidad", "0")], columnas=["Crítico"])
    ordenar(pc, "Cobertura del PETI", COBERTURAS)
    ordenar(pc, "Crítico", ["Sí", "No"])
    pb = crear_pivote(wb, cache, wpiv, "B43", "ptBanda", ["Banda"], [("N.º", XL_COUNT, "Enunciados ", "0")])
    ordenar(pb, "Banda", [b[1] for b in BANDAS])
    pa = crear_pivote(wb, cache, wpiv, "B54", "ptAmbito", ["Ámbito"],
                      [("Puntaje", XL_AVG, "Promedio actual  ", F1),
                       ("Puntaje mes 24", XL_AVG, "Promedio mes 24  ", F1)])
    for nombre in ("ptElemento", "ptPerspectiva", "ptBanda", "ptAmbito"):
        wpiv.PivotTables(nombre).ColumnGrand = False
        wpiv.PivotTables(nombre).RowGrand = False
    pc.RowGrand = True
    for p in (pk, pe, pp, pc, pb, pa):
        p.PivotCache().MissingItemsLimit = 0  # xlMissingItemsNone
        p.ShowValuesRow = False
    wpiv.Columns("B").ColumnWidth = 30
    for col in "CDEF":
        wpiv.Columns(col).ColumnWidth = 16

    # Tarjetas (GETPIVOTDATA sobre ptKPI: responden a las segmentaciones).
    k = "'Pivotes'!$B$4"
    gp = lambda campo: f'IFERROR(GETPIVOTDATA("{campo}",{k}),0)'
    tarjeta(ws, "F4:H4", "Puntos actuales", f"={gp('Puntos')}", "0", "")
    ws.Range("F6").Formula2 = f'="de "&{gp("Enunciados")}*10&" posibles"'
    tarjeta(ws, "I4:K4", "Porcentaje actual", f"=IFERROR({gp('Puntos')}/({gp('Enunciados')}*10),0)", FP, "")
    ws.Range("I6").Formula2 = (f'="Nivel: "&XLOOKUP(IFERROR({gp("Puntos")}/({gp("Enunciados")}*10),0)*100,'
                               'NivelDesde,NivelNombre,"",-1)')
    tarjeta(ws, "L4:N4", "Promedio por enunciado", f"=IFERROR({gp('Puntos')}/{gp('Enunciados')},0)", F1, "")
    ws.Range("L6").Formula2 = f'={gp("Enunciados")}&" enunciados en el filtro"'
    tarjeta(ws, "O4:Q4", "Causas críticas", f"={gp('Críticos')}", "0", "")
    ws.Range("O6").Formula2 = '="puntaje de "&UmbralCritico&" o menos"'
    tarjeta(ws, "R4:T4", "Porcentaje al mes 24",
            f"=IFERROR({gp('Puntos mes 24')}/({gp('Enunciados')}*10),0)", FP, "")
    ws.Range("R6").Formula2 = (f'="Nivel: "&XLOOKUP(IFERROR({gp("Puntos mes 24")}/({gp("Enunciados")}*10),0)*100,'
                               'NivelDesde,NivelNombre,"",-1)')
    tarjeta(ws, "U4:W4", "Mejora con el PETI", f"={gp('Puntos mes 24')}-{gp('Puntos')}", "+0;-0;0", "")
    ws.Range("U6").Value = "puntos si se ejecuta"
    for c in ("F7", "I7", "L7", "O7", "R7", "U7"):
        ws.Range(c).Value = ""
    ws.Rows(7).RowHeight = 4

    # Gráficos dinámicos.
    grafico_pivote(ws, pe, ws.Range("F9:N24"), XL_COLUMN, "Promedio por elemento (0 a 10)", [AZUL, NARANJA], 10)
    grafico_pivote(ws, pp, ws.Range("O9:W24"), XL_COLUMN, "Promedio por perspectiva del BSC (0 a 10)",
                   [AZUL, NARANJA], 10)
    grafico_pivote(ws, pc, ws.Range("F26:N41"), XL_COLUMN_STACKED,
                   "Cobertura del PETI: enunciados críticos (Sí) y no críticos", [ROJO, rgb("9AA5B1")])
    grafico_pivote(ws, pb, ws.Range("O26:S41"), XL_COLUMN, "Distribución por banda de la rúbrica", [AZUL])
    grafico_pivote(ws, pa, ws.Range("T26:W41"), XL_COLUMN, "Gobierno frente a gestión", [AZUL, NARANJA], 10)

    # Listado filtrable.
    ws.Columns("X").ColumnWidth = 2
    ws.Range("Y9").Value = "Enunciados del filtro, de menor a mayor puntaje"
    ws.Range("Y9").Font.Bold = True
    ws.Range("Y9").Font.Color = AZUL
    pd = crear_pivote(wb, cache, ws, "Y10", "ptDetalle", ["N.º", "Tema", "Cobertura del PETI"],
                      [("Puntaje", XL_SUM, "Puntaje ", "0"), ("Puntaje mes 24", XL_SUM, "Mes 24", "0")],
                      detalle=True)
    pd.PivotFields("N.º").AutoSort(XL_ASC, "Puntaje ")
    pd.RowGrand = False
    pd.ColumnGrand = False
    pd.TableStyle2 = "PivotStyleLight16"
    pd.PivotCache().MissingItemsLimit = 0

    # Segmentaciones conectadas a todas las tablas dinámicas.
    pts = [pk, pe, pp, pc, pb, pa, pd]
    izq = ws.Range("B4").Left
    ancho = ws.Range("B4:D4").Width
    arriba = ws.Range("B4").Top
    for campo, leyenda, alto in (("Elemento", "Elemento del método", 105), ("Perspectiva BSC", "Perspectiva BSC", 122),
                                 ("Ámbito", "Gobierno o gestión", 70), ("Cobertura del PETI", "Cobertura del PETI", 105),
                                 ("Crítico", "Causa crítica", 70), ("Respaldo", "Respaldo del puntaje", 105)):
        sc = wb.SlicerCaches.Add2(pk, campo)
        sl = sc.Slicers.Add(SlicerDestination=ws, Name=f"seg_{re.sub(r'[^A-Za-z]', '', campo)}", Caption=leyenda)
        # La posición se fija después: con argumentos con nombre, Excel ignora Top y Left.
        sl.Top, sl.Left, sl.Width, sl.Height = arriba, izq, ancho, alto
        sl.Style = "SlicerStyleLight1"
        sl.RowHeight = 15
        for p in pts[1:]:
            sc.PivotTables.AddPivotTable(p)
        arriba += alto + 8
    ws.Range("B1").Select()
    return pts


def main(formato, fuente_diag, fuente_clasif, salida):
    enunciados = leer_enunciados(formato)
    calif = tabla_md(open(fuente_diag, encoding="utf8").read(), "calificaciones", 3)
    clasif = tabla_md(open(fuente_clasif, encoding="utf8").read(), "clasificacion", 8)
    filas = construir_filas(enunciados, calif, clasif)
    res = resumen_python(filas)
    esperado = {"1. Enfoque estratégico": 57, "2. Traslado hacia el BSC": 46,
                "3. Sincronización y despliegue": 36, "4. Cultura de ejecución": 43}
    if {e: v[0] for e, v in res["elemento"].items()} != esperado:
        sys.exit(f"Los puntajes no suman lo del diagnóstico: {res['elemento']}")

    salida = os.path.abspath(salida)
    carpeta = os.path.dirname(os.path.abspath(fuente_clasif))
    if os.path.exists(salida):
        os.remove(salida)
    xl = win32com.client.DispatchEx("Excel.Application")
    xl.Visible = False
    xl.DisplayAlerts = False
    xl.ScreenUpdating = False
    global F1, FP
    dec = xl.International[2]  # xlDecimalSeparator (3); pywin32 devuelve la lista completa, desde 0
    if dec not in (",", "."):
        sys.exit(f"Separador decimal inesperado: {dec!r}")
    F1, FP = f"0{dec}0", f"0{dec}0%"
    try:
        wb = xl.Workbooks.Add()
        while wb.Worksheets.Count < 7:
            wb.Worksheets.Add(After=wb.Worksheets(wb.Worksheets.Count))
        w_ini, w_tab, w_res, w_pri, w_dat, w_par, w_piv = [wb.Worksheets(i) for i in range(1, 8)]
        w_piv.Name = "Pivotes"
        for w in (w_ini, w_tab, w_res, w_pri, w_dat, w_par, w_piv):
            w.Cells.Font.Name = "Calibri"
            w.Cells.Font.Size = 10
        hoja_parametros(wb, w_par)
        hoja_datos(w_dat, filas)
        filas_res = hoja_resumen(wb, w_res)
        hoja_prioridades(w_pri)
        hoja_tablero(wb, w_tab, w_piv)
        hoja_inicio(w_ini, res)
        xl.CalculateFull()
        wb.RefreshAll()

        # Comprobación: el libro reproduce las cifras calculadas en Python.
        libro = {w_res.Range(f"B{7 + i}").Value: (int(w_res.Range(f"C{7 + i}").Value),
                                                 int(w_res.Range(f"G{7 + i}").Value)) for i in range(4)}
        if libro != res["elemento"]:
            sys.exit(f"El libro calculó {libro} y Python {res['elemento']}")
        if int(w_res.Range("J11").Value) != len(res["criticos"]):
            sys.exit("El número de causas críticas del libro no coincide")
        tarjeta_pts = int(w_tab.Range("F5").Value)
        if tarjeta_pts != res["total"][0]:
            sys.exit(f"La tarjeta de puntos dice {tarjeta_pts} y el total es {res['total'][0]}")

        # Imágenes para el Word.
        xl.ScreenUpdating = True
        exportar(xl, w_tab, w_tab.Range("B1:W46"), os.path.join(carpeta, "tablero.png"))
        exportar(xl, w_res, w_res.Range(f"B5:S{filas_res['respaldo'][1]}"), os.path.join(carpeta, "resumen.png"))
        png = os.path.join(carpeta, "prioridades.png")
        w_pri.ChartObjects("Brechas").Chart.Export(png)  # la tabla completa no se lee a 16 cm de ancho
        print("ok", png)

        for w in (w_res, w_pri, w_par, w_piv, w_tab, w_ini):
            w.Activate()
            w.Range("A1").Select()
            xl.ActiveWindow.ScrollRow = 1
            xl.ActiveWindow.ScrollColumn = 1
        inmovilizar_datos(w_dat)
        w_dat.Range("A1").Select()
        w_ini.Activate()
        wb.SaveAs(salida, 51)  # xlOpenXMLWorkbook
        wb.Close(False)
    finally:
        xl.Quit()

    imprimir(res)
    print("ok", salida)


def exportar(xl, ws, rango, png):
    ws.Activate()
    rango.CopyPicture(1, 2)  # xlScreen, xlBitmap
    tmp = xl.Workbooks.Add()
    co = tmp.Worksheets(1).ChartObjects().Add(0, 0, rango.Width, rango.Height)
    co.Chart.ChartArea.Format.Line.Visible = False
    co.Activate()
    co.Chart.Paste()
    co.Chart.Export(png)
    tmp.Close(False)
    print("ok", png)


def pct(x):
    return f"{x:.1f}".replace(".", ",") + " %"


def hoja_inicio(ws, res):
    ws.Name = "Inicio"
    xl = ws.Application
    ws.Activate()
    xl.ActiveWindow.DisplayGridlines = False
    ws.Columns("A").ColumnWidth = 2
    ws.Columns("B").ColumnWidth = 26
    ws.Columns("C").ColumnWidth = 100
    titulo(ws, "B2", "Análisis del diagnóstico BSC de gestión y gobierno de TI", 18)
    ws.Range("B3").Value = ("Perficient Inc., operación en Colombia. Trabajo académico del curso Gobierno y "
                            "Servicios de TI, Universidad Santiago de Cali. Equipo Firmes por la Gobernanza. "
                            "16 de noviembre de 2026.")
    ws.Range("B3").Font.Color = GRIS
    filas = [
        ("Qué es", "El diagnóstico situacional de los cuatro elementos de la gestión basada en BSC (enfoque "
                   "estratégico, traslado hacia el BSC, sincronización y despliegue, cultura de ejecución), "
                   "pasado de un formulario a un modelo de datos que se analiza con tablas dinámicas, "
                   "segmentaciones y fórmulas."),
        ("Proceso de análisis", "1. Captura: un registro por enunciado con su puntaje y su sustento (hoja Datos).\n"
                                "2. Clasificación: a cada enunciado se le agregan cinco dimensiones: perspectiva "
                                "del BSC, objetivo de COBIT 2019 (y de él, gobierno o gestión), respuesta y "
                                "cobertura del PETI Colombia v1.0, tipo de evidencia y puntaje proyectado al mes 24.\n"
                                "3. Cálculo: fórmulas de la tabla para banda, causa crítica y brechas; resumen con "
                                "SUMIFS y AVERAGEIFS (hoja Resumen).\n"
                                "4. Exploración: tablas dinámicas con seis segmentaciones (hoja Tablero).\n"
                                "5. Priorización: lo que el PETI deja abierto, con FILTER y SORT (hoja Prioridades)."),
        ("Cómo usarlo", "En Tablero, haga clic en una o varias opciones de las segmentaciones (Ctrl + clic para "
                        "varias). El botón del embudo con la X de cada segmentación quita el filtro. En Parámetros "
                        "se cambia el umbral de causa crítica. Si cambia un dato de la hoja Datos, use "
                        "Datos > Actualizar todo para que las tablas dinámicas lo tomen."),
        ("Hojas", "Tablero: tarjetas, gráficos y listado filtrables.\nResumen: resultado por elemento con el "
                  "radar que pide el formato y promedios por perspectiva, ámbito, cobertura y respaldo.\n"
                  "Prioridades: causas críticas y brechas que quedan al mes 24.\nDatos: los 40 registros.\n"
                  "Parámetros: umbral, rúbrica y niveles.\nPivotes: tablas dinámicas que alimentan el tablero."),
        ("Resultado", f"{res['total'][0]} de 400 puntos ({pct(res['total'][0] / 4)}), nivel en construcción. "
                      f"Proyección al mes 24 con el PETI: {res['total'][1]} puntos ({pct(res['total'][1] / 4)}). "
                      f"Causas críticas: {len(res['criticos'])} (enunciados "
                      f"{', '.join(str(n) for n in res['criticos'])})."),
        ("Fuentes y límites", "Los puntajes son valoración del equipo (INT-001) con la rúbrica de la hoja "
                              "Parámetros; no son una encuesta al personal de Perficient. PUB- son fuentes "
                              "públicas; PRV-001 son entrevistas de una cuenta de cliente y describen esa cuenta, "
                              "no una política de Perficient. La proyección al mes 24 supone que los 25 proyectos "
                              "del PETI se ejecutan como están escritos; no es una meta aprobada."),
    ]
    for i, (a, b) in enumerate(filas):
        r = 5 + i
        ws.Range(f"B{r}").Value = a
        ws.Range(f"B{r}").Font.Bold = True
        ws.Range(f"B{r}").Font.Color = AZUL
        ws.Range(f"C{r}").Value = b
        ws.Range(f"B{r}:C{r}").VerticalAlignment = XL_TOP
        ws.Range(f"C{r}").WrapText = True
    bordes(ws.Range(f"B5:C{4 + len(filas)}"))
    ws.Range(f"B5:C{4 + len(filas)}").Rows.AutoFit()
    for i in range(len(filas)):
        ws.Rows(5 + i).RowHeight = ws.Rows(5 + i).RowHeight + 6


def imprimir(res):
    print("Elementos (actual, mes 24):")
    for e, v in res["elemento"].items():
        print(f"  {e}: {v[0]} -> {v[1]}")
    print(f"  Total: {res['total'][0]} -> {res['total'][1]}")
    for clave in ("persp", "ambito"):
        print(clave)
        for k, v in res[clave].items():
            print(f"  {k}: n={v[0]} actual={v[1]:.2f} mes24={v[2]:.2f} criticos={v[3]}")
    print("cobertura", dict(res["cob"]))
    print("respaldo", dict(res["respaldo"]))
    print("criticos", res["criticos"])


if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(__doc__)
    main(*sys.argv[1:5])
