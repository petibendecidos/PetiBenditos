"""Llena el diagnóstico de sensibilización gerencial y el diagnóstico de control en TI (COBIT 2019) con Excel.

Uso:
    python scripts/generar_diagnosticos_cobit.py <formato_sensibilizacion.xls> <formato_control.xlsx> \
        <fuente.md> <salida_sensibilizacion.xls> <salida_control.xlsx>

Lee de la fuente dos tablas:
- entre <!-- sensibilizacion --> y <!-- fin-sensibilizacion -->: código, objetivo, importancia (1-5),
  desempeño (1 = muy bien, 5 = no se sabe o mal), quién lo hace (TI, Otra área, Externo, No se sabe,
  separados por coma), formalidad y auditado (Yes, No o ?) y responsable;
- entre <!-- control --> y <!-- fin-control -->: código, proceso, nivel actual (0-5), nivel objetivo al
  mes 24 y observaciones.

Escribe:
- el .xls de sensibilización: marcas y valores en la hoja del formato (corrige dos erratas del formato) y
  una hoja "Riesgo" con riesgo = importancia × desempeño en fórmulas;
- el .xlsx de control: reescribe las filas con los 40 objetivos de COBIT 2019 (el formato traía 37 con
  códigos corridos), llena nivel y observaciones, agrega una nota y arma la hoja "Resultados" con fórmulas
  y un gráfico, que exporta como resultados.png junto a la fuente;
- las tablas entre <!-- resultado-sensibilizacion --> y <!-- resultado-control --> de la fuente.

Se usa Excel por COM para conservar el formato .xls y los estilos del docente. Al final relee lo que
calculó Excel y se detiene si no coincide con lo que calculó el script.
"""
import os
import re
import shutil
import sys

import win32com.client

DOMINIOS = [
    ("EDM", "EDM: Evaluar, dirigir y monitorear", "Gobierno: Evaluar, Dirigir y Monitorear (EDM)",
     ["EDM01", "EDM02", "EDM03", "EDM04", "EDM05"]),
    ("APO", "APO: Alinear, planificar y organizar", "Gestión: Alinear, Planificar y Organizar (APO)",
     [f"APO{i:02d}" for i in range(1, 15)]),
    ("BAI", "BAI: Construir, adquirir e implementar", "Gestión: Construir, Adquirir e Implementar (BAI)",
     [f"BAI{i:02d}" for i in range(1, 12)]),
    ("DSS", "DSS: Entregar, dar servicio y soporte", "Gestión: Entregar, Dar Servicio y Soporte (DSS)",
     [f"DSS{i:02d}" for i in range(1, 7)]),
    ("MEA", "MEA: Monitorear, evaluar y valorar", "Gestión: Monitorear, Evaluar y Valorar (MEA)",
     [f"MEA{i:02d}" for i in range(1, 5)]),
]
CODIGOS = [c for d in DOMINIOS for c in d[3]]
QUIEN = {"TI": 4, "Otra área": 5, "Externo": 6, "No se sabe": 7}  # columnas D a G del formato
SI_NO = {"Yes", "No", "?"}

NOTA_CONTROL = (
    "Nota del equipo: el formato recibido mezclaba nombres de COBIT 5 con códigos de COBIT 2019 (APO09 a "
    "APO12 corridos, BAI11 como problemas, MEA02 y MEA03 invertidos) y tenía 37 filas. Se corrigieron "
    "códigos y nombres y se agregaron APO13, APO14 y MEA04 para cubrir los 40 objetivos de COBIT 2019 "
    "(ISACA). Los IDs entre paréntesis (PUB-, PRV-, INT-) son del registro de evidencias del equipo; los "
    "BRE-, P y KPI- son brechas, proyectos e indicadores del PETI Colombia v1.0. Elaboró: Equipo Firmes "
    "por la Gobernanza, 16 de noviembre de 2026."
)


def tabla(texto, marca, columnas):
    bloque = re.search(rf"<!-- {marca} -->(.*?)<!-- fin-{marca} -->", texto, re.S).group(1)
    filas = []
    for linea in bloque.splitlines():
        celdas = [c.strip() for c in linea.strip().strip("|").split("|")]
        if len(celdas) == columnas and re.fullmatch(r"[A-Z]{3}\d\d", celdas[0]):
            filas.append(celdas)
    if [f[0] for f in filas] != CODIGOS:
        sys.exit(f"La tabla '{marca}' debe traer los 40 objetivos de COBIT 2019 en orden")
    return filas


def leer(texto):
    sens = tabla(texto, "sensibilizacion", 8)
    ctrl = tabla(texto, "control", 5)
    for c, _, imp, des, quien, form, aud, resp in sens:
        if not (imp.isdigit() and des.isdigit() and 1 <= int(imp) <= 5 and 1 <= int(des) <= 5):
            sys.exit(f"{c}: importancia y desempeño van de 1 a 5")
        if any(q.strip() not in QUIEN for q in quien.split(",")):
            sys.exit(f"{c}: 'Quién lo hace' admite {list(QUIEN)}")
        if form not in SI_NO or aud not in SI_NO:
            sys.exit(f"{c}: formalidad y auditado admiten Yes, No o ?")
        if not resp:
            sys.exit(f"{c}: falta el responsable (o 'No se sabe')")
    for c, _, act, obj, obs in ctrl:
        if not (act.isdigit() and obj.isdigit() and 0 <= int(act) <= int(obj) <= 5):
            sys.exit(f"{c}: los niveles van de 0 a 5 y el objetivo no puede ser menor que el actual")
        if not obs:
            sys.exit(f"{c}: faltan observaciones")
    return sens, ctrl


def riesgo(imp, des):
    r = imp * des
    return r, "Alto" if r >= 20 else "Medio" if r >= 12 else "Bajo"


def num(x, dec=1):
    return f"{x:.{dec}f}".replace(".", ",")


def resultados(sens, ctrl):
    """Tablas de resultado en Markdown y cifras para comprobar contra Excel."""
    s = {f[0]: f for f in sens}
    k = {f[0]: f for f in ctrl}
    t1 = ["| Dominio | Objetivos | Importancia promedio | Desempeño promedio | Riesgo alto | Riesgo medio | "
          "Riesgo bajo | Formalizados (Yes) | Auditados (Yes) | Responsable \"No se sabe\" |",
          "|---|---|---|---|---|---|---|---|---|---|"]
    t2 = ["| Dominio | Objetivos | Nivel actual promedio | Nivel objetivo promedio (mes 24) | Nivel 0 | "
          "Nivel 1 | Nivel 2 | Nivel 3 o más |", "|---|---|---|---|---|---|---|---|"]
    cifras = {}

    def fila_dom(nombre, cods):
        imp = [int(s[c][2]) for c in cods]
        des = [int(s[c][3]) for c in cods]
        niv = [riesgo(int(s[c][2]), int(s[c][3]))[1] for c in cods]
        act = [int(k[c][2]) for c in cods]
        obj = [int(k[c][3]) for c in cods]
        n = len(cods)
        t1.append(f"| {nombre} | {n} | {num(sum(imp) / n)} | {num(sum(des) / n)} | {niv.count('Alto')} | "
                  f"{niv.count('Medio')} | {niv.count('Bajo')} | {sum(s[c][5] == 'Yes' for c in cods)} | "
                  f"{sum(s[c][6] == 'Yes' for c in cods)} | {sum(s[c][7] == 'No se sabe' for c in cods)} |")
        t2.append(f"| {nombre} | {n} | {num(sum(act) / n, 2)} | {num(sum(obj) / n, 2)} | {act.count(0)} | "
                  f"{act.count(1)} | {act.count(2)} | {sum(a >= 3 for a in act)} |")
        cifras[nombre] = (round(sum(act) / n, 4), round(sum(obj) / n, 4), round(sum(i * d for i, d in zip(imp, des)), 4))

    for _, nombre, _, cods in DOMINIOS:
        fila_dom(nombre, cods)
    fila_dom("**Total**", CODIGOS)

    altos = sorted((f for f in sens if riesgo(int(f[2]), int(f[3]))[1] == "Alto"),
                   key=lambda f: (-int(f[2]) * int(f[3]), CODIGOS.index(f[0])))
    t3 = ["| Código | Objetivo | Importancia | Desempeño | Riesgo | Quién lo hace | Responsable | Nivel actual |",
          "|---|---|---|---|---|---|---|---|"]
    for f in altos:
        t3.append(f"| {f[0]} | {f[1]} | {f[2]} | {f[3]} | {int(f[2]) * int(f[3])} | {f[4]} | {f[7]} | {k[f[0]][2]} |")
    sens_md = "\n".join(t1) + "\n\nObjetivos de riesgo alto (20 o más), de mayor a menor:\n\n" + "\n".join(t3)
    return sens_md, "\n".join(t2), cifras


def reemplazar(texto, marca, contenido):
    patron = rf"(<!-- resultado-{marca} -->\n).*?(<!-- fin-resultado-{marca} -->)"
    return re.sub(patron, lambda m: m.group(1) + "\n" + contenido + "\n\n" + m.group(2), texto, flags=re.S)


def llenar_sensibilizacion(xl, ruta, sens):
    wb = xl.Workbooks.Open(ruta)
    ws = wb.Worksheets(1)
    filas = {}
    for r in range(1, 60):
        v = str(ws.Cells(r, 3).Value or "").strip()
        if v.startswith("Build, Acquire"):
            ws.Cells(r, 3).Value = "Build, Acquire and Implement"
        m = re.match(r"([A-Z]{3}\d\d)\s", v)
        if m:
            filas[m.group(1)] = r
            if m.group(1) == "APO13":
                ws.Cells(r, 3).Value = "APO13  Managed Security"
    if sorted(filas) != sorted(CODIGOS):
        sys.exit("El formato de sensibilización no trae los 40 objetivos esperados")
    for c, _, imp, des, quien, form, aud, resp in sens:
        r = filas[c]
        ws.Cells(r, 1).Value = int(imp)
        ws.Cells(r, 2).Value = int(des)
        for q in quien.split(","):
            ws.Cells(r, QUIEN[q.strip()]).Value = "X"
        ws.Cells(r, 8).Value = aud
        ws.Cells(r, 9).Value = form
        ws.Cells(r, 10).Value = resp
        for col in (1, 2, 4, 5, 6, 7, 8, 9):  # la columna C (nombre del objetivo) conserva su formato
            ws.Cells(r, col).HorizontalAlignment = -4108  # centrado
            ws.Cells(r, col).WrapText = False
            ws.Cells(r, col).Orientation = -4128  # xlHorizontal: el formato trae texto apilado en H e I
        ws.Range(ws.Cells(r, 8), ws.Cells(r, 9)).Font.Size = 8  # "Yes" cabe en las columnas angostas
        ws.Range(ws.Cells(r, 1), ws.Cells(r, 10)).VerticalAlignment = -4108  # centrado vertical
        ws.Cells(r, 10).WrapText = True
        ws.Cells(r, 10).Font.Size = 9
    for r in filas.values():
        ws.Rows(r).AutoFit()

    # Hoja de riesgo con fórmulas que leen la hoja del formato.
    hr = wb.Worksheets.Add(None, ws)  # (Before, After): después de la hoja del formato
    hr.Name = "Riesgo"
    hr.Range("A1").Value = "Riesgo por objetivo = Importancia × Desempeño (1 a 25)"
    hr.Range("A2").Value = ("En este formato el desempeño va de 1 (muy bien) a 5 (no se sabe o mal), así que el "
                            "producto crece con la importancia y con el mal desempeño. Alto: 20 a 25; medio: 12 a 16; "
                            "bajo: 10 o menos.")
    enc = ["Código", "Objetivo", "Importancia", "Desempeño", "Riesgo", "Nivel de riesgo"]
    for j, e in enumerate(enc, 1):
        hr.Cells(4, j).Value = e
    nombre_hoja = ws.Name
    for i, (c, *_rest) in enumerate(sens):
        r, f = 5 + i, filas[c]
        hr.Cells(r, 1).Value = c
        hr.Cells(r, 2).Formula = f"=TRIM(MID('{nombre_hoja}'!C{f},6,200))"
        hr.Cells(r, 3).Formula = f"='{nombre_hoja}'!A{f}"
        hr.Cells(r, 4).Formula = f"='{nombre_hoja}'!B{f}"
        hr.Cells(r, 5).Formula = f"=C{r}*D{r}"
        hr.Cells(r, 6).Formula = f'=IF(E{r}>=20,"Alto",IF(E{r}>=12,"Medio","Bajo"))'
    ult = 4 + len(sens)
    hr.Cells(ult + 2, 1).Value = "Alto"
    hr.Cells(ult + 2, 2).Formula = f'=COUNTIF(F5:F{ult},"Alto")'
    hr.Cells(ult + 3, 1).Value = "Medio"
    hr.Cells(ult + 3, 2).Formula = f'=COUNTIF(F5:F{ult},"Medio")'
    hr.Cells(ult + 4, 1).Value = "Bajo"
    hr.Cells(ult + 4, 2).Formula = f'=COUNTIF(F5:F{ult},"Bajo")'
    hr.Range("A4:F4").Font.Bold = True
    hr.Range("A4:F4").Interior.Color = 0x5F3A1F  # azul oscuro (BGR)
    hr.Range("A4:F4").Font.Color = 0xFFFFFF
    hr.Range("A1").Font.Bold = True
    hr.Range("A1").Font.Size = 12
    hr.Columns("A").ColumnWidth = 10
    hr.Columns("B").ColumnWidth = 58
    hr.Columns("C:F").ColumnWidth = 14
    hr.Range(f"C5:F{ult}").HorizontalAlignment = -4108
    hr.Range(f"A4:F{ult}").Borders.LineStyle = 1
    cf = hr.Range(f"F5:F{ult}").FormatConditions
    for valor, color in (("Alto", 0x9C9CFF), ("Medio", 0x9CEBFF), ("Bajo", 0xCEEFC6)):
        regla = cf.Add(1, 3, f'="{valor}"')  # xlCellValue, xlEqual
        regla.Interior.Color = color
    xl.CalculateFull()
    calculado = {hr.Cells(5 + i, 1).Value: int(hr.Cells(5 + i, 5).Value) for i in range(len(sens))}
    esperado = {c: int(i) * int(d) for c, _, i, d, *_r in sens}
    if calculado != esperado:
        sys.exit(f"La hoja Riesgo calculó otra cosa: {calculado}")
    ws.Activate()
    ws.Range("A1").Select()
    wb.Save()
    wb.Close(False)


def llenar_control(xl, ruta, sens, ctrl, png):
    wb = xl.Workbooks.Open(ruta)
    ws = wb.Worksheets(1)
    if str(ws.Range("A12").Value).strip() != "EDM01" or str(ws.Range("A52").Value).strip() != "MEA03":
        sys.exit("El formato de control no tiene la disposición esperada (EDM01 en A12, MEA03 en A52)")
    # Filas que faltan: dos al final de APO (antes del encabezado de BAI, fila 30) y una al final de MEA.
    ws.Rows("30:31").Insert()
    ws.Rows(55).Insert()
    ws.Rows(54).Copy()
    ws.Rows(55).PasteSpecial(-4122)  # xlPasteFormats
    xl.CutCopyMode = False
    k = {f[0]: f for f in ctrl}
    r = 11
    filas = {}
    for _, _, encabezado, cods in DOMINIOS:
        ws.Cells(r, 1).Value = encabezado
        r += 1
        for c in cods:
            ws.Cells(r, 1).Value = c
            ws.Cells(r, 2).Value = k[c][1]
            ws.Cells(r, 3).Value = int(k[c][2])
            ws.Cells(r, 4).Value = k[c][4]
            filas[c] = r
            r += 1
    if r != 56:
        sys.exit(f"Se esperaba terminar en la fila 55 y se terminó en {r - 1}")
    ws.Columns("B").ColumnWidth = 52
    ws.Columns("D").ColumnWidth = 90
    ws.Range("B12:D55").WrapText = True
    ws.Range("B12:D55").VerticalAlignment = -4160  # arriba
    ws.Range("C12:C55").HorizontalAlignment = -4108
    ws.Range("D12:D55").Font.Size = 9
    for fila in filas.values():
        ws.Rows(fila).AutoFit()
    nota = ws.Range("A57:D57")
    nota.Merge()
    nota.Value = NOTA_CONTROL
    nota.WrapText = True
    nota.Font.Italic = True
    nota.Font.Size = 9
    nota.VerticalAlignment = -4160
    ws.Rows(57).RowHeight = 48

    # Hoja Resultados (en el formato se llama "Resultados " y viene vacía).
    rs = wb.Worksheets(2)
    rs.Cells.Clear()
    rs.Range("A1").Value = "Resultados del diagnóstico de control en TI (COBIT 2019) - Perficient, operación en Colombia"
    rs.Range("A1").Font.Bold = True
    rs.Range("A1").Font.Size = 13
    rs.Range("A2").Value = ("Nivel actual: de la hoja Sheet1. Nivel objetivo: el que alcanzaría cada objetivo al mes 24 "
                            "si se ejecuta el PETI Colombia v1.0 (estimación del equipo). Importancia y desempeño: "
                            "del diagnóstico de sensibilización gerencial.")
    enc = ["Dominio", "Objetivos", "Nivel actual promedio", "Nivel objetivo promedio (mes 24)",
           "Nivel 0", "Nivel 1", "Nivel 2", "Nivel 3 o más"]
    for j, e in enumerate(enc, 1):
        rs.Cells(4, j).Value = e
    # Detalle por objetivo desde la fila 13.
    det0 = 13
    det_enc = ["Código", "Proceso", "Nivel actual", "Nivel objetivo (mes 24)", "Brecha",
               "Importancia", "Desempeño", "Riesgo (I x D)"]
    for j, e in enumerate(det_enc, 1):
        rs.Cells(det0 - 1, j).Value = e
    s = {f[0]: f for f in sens}
    rangos = {}
    i = 0
    for pref, nombre, _, cods in DOMINIOS:
        ini = det0 + i
        for c in cods:
            fr = det0 + i
            rs.Cells(fr, 1).Value = c
            rs.Cells(fr, 2).Formula = f"=Sheet1!B{filas[c]}"
            rs.Cells(fr, 3).Formula = f"=Sheet1!C{filas[c]}"
            rs.Cells(fr, 4).Value = int(k[c][3])
            rs.Cells(fr, 5).Formula = f"=D{fr}-C{fr}"
            rs.Cells(fr, 6).Value = int(s[c][2])
            rs.Cells(fr, 7).Value = int(s[c][3])
            rs.Cells(fr, 8).Formula = f"=F{fr}*G{fr}"
            i += 1
        rangos[nombre] = (ini, det0 + i - 1)
    fin = det0 + i - 1
    for n, (nombre, (a, b)) in enumerate(rangos.items()):
        fr = 5 + n
        rs.Cells(fr, 1).Value = nombre
        rs.Cells(fr, 2).Formula = f"=COUNTA(A{a}:A{b})"
        rs.Cells(fr, 3).Formula = f"=AVERAGE(C{a}:C{b})"
        rs.Cells(fr, 4).Formula = f"=AVERAGE(D{a}:D{b})"
        for j, nivel in enumerate((0, 1, 2)):
            rs.Cells(fr, 5 + j).Formula = f"=COUNTIF(C{a}:C{b},{nivel})"
        rs.Cells(fr, 8).Formula = f'=COUNTIF(C{a}:C{b},">=3")'
    tot = 5 + len(rangos)
    rs.Cells(tot, 1).Value = "Total"
    rs.Cells(tot, 2).Formula = f"=COUNTA(A{det0}:A{fin})"
    rs.Cells(tot, 3).Formula = f"=AVERAGE(C{det0}:C{fin})"
    rs.Cells(tot, 4).Formula = f"=AVERAGE(D{det0}:D{fin})"
    for j in range(5, 9):
        col = "EFGH"[j - 5]
        rs.Cells(tot, j).Formula = f"=SUM({col}5:{col}{tot - 1})"
    # Formato
    for rango in (f"A4:H4", f"A{det0 - 1}:H{det0 - 1}"):
        rs.Range(rango).Font.Bold = True
        rs.Range(rango).Font.Color = 0xFFFFFF
        rs.Range(rango).Interior.Color = 0x5F3A1F
        rs.Range(rango).WrapText = True
    rs.Range(f"A{tot}:H{tot}").Font.Bold = True
    rs.Range(f"A4:H{tot}").Borders.LineStyle = 1
    rs.Range(f"A{det0 - 1}:H{fin}").Borders.LineStyle = 1
    rs.Range(f"B5:H{tot}").HorizontalAlignment = -4108
    rs.Range(f"C{det0}:H{fin}").HorizontalAlignment = -4108
    rs.Columns("A").ColumnWidth = 38
    rs.Columns("B").ColumnWidth = 52
    rs.Columns("C:H").ColumnWidth = 13
    rs.Range(f"B{det0}:B{fin}").WrapText = True
    rs.Rows(4).RowHeight = 46
    rs.Rows(det0 - 1).RowHeight = 32
    escala = rs.Range(f"H{det0}:H{fin}").FormatConditions.AddColorScale(3)
    escala.ColorScaleCriteria(1).FormatColor.Color = 0xCEEFC6
    escala.ColorScaleCriteria(2).FormatColor.Color = 0x9CEBFF
    escala.ColorScaleCriteria(3).FormatColor.Color = 0x9C9CFF

    xl.CalculateFull()
    # Los formatos de número de los gráficos se dan en la configuración regional de Excel (en español,
    # "0.00" se lee como miles y muestra "003").
    dec = xl.International[2]  # xlDecimalSeparator
    fmt2 = f"0{dec}00"
    rs.Range(f"C5:D{tot}").NumberFormatLocal = fmt2

    # El formato del docente trae en esta hoja un gráfico de columnas por proceso que leía Sheet1!C12:C52.
    # Se conserva y se apunta a la tabla de detalle (40 objetivos, nivel actual y objetivo).
    if rs.ChartObjects().Count:
        cp = rs.ChartObjects(1)
        chp = cp.Chart
        while chp.SeriesCollection().Count:
            chp.SeriesCollection(1).Delete()
        for col, nombre in (("C", "Nivel actual"), ("D", "Nivel objetivo (mes 24)")):
            serie = chp.SeriesCollection().NewSeries()
            serie.Name = nombre
            serie.XValues = rs.Range(f"A{det0}:A{fin}")
            serie.Values = rs.Range(f"{col}{det0}:{col}{fin}")
        chp.SeriesCollection(1).Format.Fill.ForeColor.RGB = 0x5F3A1F
        chp.SeriesCollection(2).Format.Fill.ForeColor.RGB = 0x4DA6F2
        chp.Axes(2).MinimumScale = 0
        chp.Axes(2).MaximumScale = 5
        chp.Axes(2).MajorUnit = 1
        chp.Axes(2).TickLabels.NumberFormatLocal = "0"
        chp.Axes(1).TickLabelSpacing = 1
        chp.Axes(1).TickLabels.Font.Size = 7
        chp.HasLegend = True
        chp.Legend.Position = -4107
        cp.Left = rs.Range("J26").Left
        cp.Top = rs.Range("J26").Top
        cp.Width = 760
        cp.Height = 320

    # Gráfico nuevo: nivel actual y objetivo por dominio.
    izq = rs.Range("J4").Left
    arriba = rs.Range("J4").Top
    co = rs.ChartObjects().Add(izq, arriba, 520, 300)
    ch = co.Chart
    ch.ChartType = 57  # xlBarClustered
    # Union y no "A4:A9,C4:D9": con Excel en español la coma del rango de varias áreas falla por COM.
    ch.SetSourceData(xl.Union(rs.Range(f"A4:A{tot - 1}"), rs.Range(f"C4:D{tot - 1}")))
    ch.HasTitle = True
    ch.ChartTitle.Text = "Nivel de capacidad por dominio de COBIT 2019 (0 a 5)"
    ch.ChartTitle.Font.Size = 12
    ch.Axes(2).MinimumScale = 0
    ch.Axes(2).MaximumScale = 5
    ch.Axes(2).MajorUnit = 1
    ch.Axes(2).TickLabels.NumberFormatLocal = "0"
    ch.Axes(1).ReversePlotOrder = True
    ch.HasLegend = True
    ch.Legend.Position = -4107  # abajo
    ch.SeriesCollection(1).Format.Fill.ForeColor.RGB = 0x5F3A1F
    ch.SeriesCollection(2).Format.Fill.ForeColor.RGB = 0x4DA6F2
    for n in (1, 2):
        ch.SeriesCollection(n).HasDataLabels = True
        ch.SeriesCollection(n).DataLabels().NumberFormatLocal = fmt2
    ch.Export(png)
    if rs.ChartObjects().Count > 1:
        rs.ChartObjects(1).Chart.Export(png.replace(".png", "_por_proceso.png"))

    # Comprobación contra lo que calculó el script.
    leido = {}
    for n, nombre in enumerate(rangos):
        fr = 5 + n
        leido[nombre] = (round(rs.Cells(fr, 3).Value, 4), round(rs.Cells(fr, 4).Value, 4))
    rs.Activate()
    rs.Range("A1").Select()
    ws.Activate()
    ws.Range("A1").Select()
    wb.Save()
    wb.Close(False)
    return leido


def main(f_sens, f_ctrl, fuente, s_sens, s_ctrl):
    texto = open(fuente, encoding="utf8").read()
    sens, ctrl = leer(texto)
    sens_md, ctrl_md, cifras = resultados(sens, ctrl)
    texto = reemplazar(texto, "sensibilizacion", sens_md)
    texto = reemplazar(texto, "control", ctrl_md)
    open(fuente, "w", encoding="utf8", newline="\n").write(texto)
    print(sens_md, "\n\n", ctrl_md, sep="")

    s_sens, s_ctrl = os.path.abspath(s_sens), os.path.abspath(s_ctrl)
    png = os.path.join(os.path.dirname(os.path.abspath(fuente)), "resultados.png")
    shutil.copyfile(f_sens, s_sens)
    shutil.copyfile(f_ctrl, s_ctrl)
    xl = win32com.client.DispatchEx("Excel.Application")
    xl.Visible = False
    xl.DisplayAlerts = False
    try:
        llenar_sensibilizacion(xl, s_sens, sens)
        leido = llenar_control(xl, s_ctrl, sens, ctrl, png)
    finally:
        xl.Quit()
    for nombre, (act, obj) in leido.items():
        if (act, obj) != cifras[nombre][:2]:
            sys.exit(f"{nombre}: Excel calculó {act}/{obj} y el script {cifras[nombre][:2]}")
    print("ok", s_sens)
    print("ok", s_ctrl)
    print("ok", png)


if __name__ == "__main__":
    main(*sys.argv[1:6])
