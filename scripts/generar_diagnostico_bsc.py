"""Diligencia el formato del docente "Diagnóstico estratégico enfocado en la gestión y gobierno TI mediante BSC".

Uso:
    python scripts/generar_diagnostico_bsc.py <formato .doc o .docx> <fuente .md> <salida .docx> [grafico.png]

Toma de la fuente Markdown (docs/entregas-2026-10-22/diagnostico-bsc.md) tres bloques marcados con
comentarios HTML: <!-- antes --> (se inserta antes del primer cuestionario), <!-- calificaciones -->
(tabla N.º | Puntaje | Sustento, 40 filas) y <!-- resultado --> (se agrega al final, en el punto 5).
Suma los puntajes, llena los cuatro cuestionarios, los "TOTAL:" y la tabla final, y reemplaza el
marcador [[GRAFICO]] por un radar nativo de Word con scripts/word_com_bsc.ps1 (necesita Word).
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile

import docx
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

AZUL = RGBColor(0x1F, 0x3A, 0x5F)
PS1 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "word_com_bsc.ps1")
ELEMENTOS = ["1. Enfoque estratégico", "2. Traslado hacia el BSC",
             "3. Sincronización y despliegue", "4. Cultura de ejecución"]
NIVELES = [(80, "Impulsor"), (60, "Funcional"), (40, "En construcción"), (0, "Bloqueador")]


def nivel(puntos, maximo=100):
    pct = puntos * 100 / maximo
    return next(n for tope, n in NIVELES if pct >= tope)


def word(*args):
    subprocess.run(["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", PS1, *args],
                   check=True, timeout=300)


def bloque(md, nombre):
    m = re.search(rf"<!-- {nombre} -->(.*?)<!-- fin-{nombre} -->", md, re.S)
    if not m:
        sys.exit(f"Falta el bloque <!-- {nombre} --> en la fuente")
    return m.group(1).strip().splitlines()


def formato(p, texto, tam=10, color=None):
    for t in re.split(r"(\*\*[^*]+\*\*|\*[^*]+\*|`[^`]+`)", texto):
        if not t:
            continue
        if t.startswith("**"):
            r = p.add_run(t[2:-2]); r.bold = True
        elif t.startswith("*"):
            r = p.add_run(t[1:-1]); r.italic = True
        elif t.startswith("`"):
            r = p.add_run(t[1:-1])
        else:
            r = p.add_run(t)
        r.font.size = Pt(tam)
        r.font.name = "Calibri"
        if color:
            r.font.color.rgb = color


def sombra(celda, color):
    tc = celda._element.get_or_add_tcPr()
    s = OxmlElement("w:shd")
    s.set(qn("w:val"), "clear"); s.set(qn("w:color"), "auto"); s.set(qn("w:fill"), color)
    tc.append(s)


def bordes(tabla):
    tblPr = tabla._tbl.tblPr
    b = OxmlElement("w:tblBorders")
    for lado in ("top", "left", "bottom", "right", "insideH", "insideV"):
        e = OxmlElement(f"w:{lado}")
        e.set(qn("w:val"), "single"); e.set(qn("w:sz"), "4"); e.set(qn("w:color"), "808080")
        b.append(e)
    # El esquema exige tblBorders antes de shd, tblLayout, tblCellMar y tblLook; fuera de orden,
    # Word declara el archivo dañado y abre un diálogo de recuperación que bloquea la automatización.
    siguiente = next((c for c in tblPr if c.tag in {qn(f"w:{x}") for x in
                      ("shd", "tblLayout", "tblCellMar", "tblLook", "tblCaption", "tblDescription")}), None)
    if siguiente is not None:
        siguiente.addprevious(b)
    else:
        tblPr.append(b)


def ancho(celda, cm):
    celda.width = Cm(cm)


def tabla_md(d, filas):
    filas = [f for f in filas if not all(re.fullmatch(r":?-+:?", c.strip() or "-") for c in f)]
    n = max(len(f) for f in filas)
    t = d.add_table(rows=0, cols=n)
    bordes(t)
    for i, f in enumerate(filas):
        cs = t.add_row().cells
        for j in range(n):
            p = cs[j].paragraphs[0]
            formato(p, f[j] if j < len(f) else "", 9,
                    RGBColor(0xFF, 0xFF, 0xFF) if i == 0 else None)
            if i == 0:
                for r in p.runs:
                    r.bold = True
                sombra(cs[j], "1F3A5F")
    # Ancho proporcional al texto promedio de cada columna, sobre 17 cm útiles.
    pesos = [max(6, sum(len(f[j]) if j < len(f) else 0 for f in filas) / len(filas)) for j in range(n)]
    for fila in t.rows:
        for j, celda in enumerate(fila.cells):
            ancho(celda, 17 * pesos[j] / sum(pesos))
    d.add_paragraph()


def escribir_md(d, lineas):
    filas = []
    for linea in lineas + [""]:
        if linea.strip().startswith("|"):
            filas.append([c.strip() for c in linea.strip().strip("|").split("|")])
            continue
        if filas:
            tabla_md(d, filas); filas = []
        s = linea.rstrip()
        if not s.strip():
            continue
        m = re.match(r"^(#{2,4})\s+(.*)", s)
        if m:
            p = d.add_paragraph()
            p.paragraph_format.space_before = Pt(10)
            p.paragraph_format.keep_with_next = True
            formato(p, m.group(2), 13 if len(m.group(1)) == 2 else 11.5, AZUL)
            for r in p.runs:
                r.bold = True
        elif s.strip() == "[[GRAFICO]]":
            p = d.add_paragraph("[[GRAFICO]]")
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        elif re.match(r"^\s*[-*]\s+", s):
            p = d.add_paragraph()
            p.paragraph_format.left_indent = Cm(0.6)
            formato(p, "•  " + re.sub(r"^\s*[-*]\s+", "", s))
        else:
            p = d.add_paragraph()
            p.paragraph_format.space_after = Pt(6)
            formato(p, s)


def insertar_antes(d, ancla, lineas):
    """Escribe las líneas al final del documento y mueve lo escrito antes del elemento ancla."""
    body = d.element.body
    if body[-1].tag != qn("w:sectPr"):
        sys.exit("Se esperaba w:sectPr al final del cuerpo")
    # Lo nuevo queda entre el último elemento previo y w:sectPr. No se compara por id():
    # lxml crea proxies nuevos en cada recorrido y los id() no identifican los nodos.
    n_previos = len(body) - 1
    escribir_md(d, lineas)
    for e in list(body)[n_previos:-1]:
        ancla.addprevious(e)


def leer_calificaciones(lineas):
    cal = {}
    for linea in lineas:
        c = [x.strip() for x in linea.strip().strip("|").split("|")]
        if len(c) == 3 and c[0].isdigit():
            puntaje = int(c[1])
            if not 0 <= puntaje <= 10:
                sys.exit(f"Puntaje fuera de escala en el enunciado {c[0]}")
            cal[int(c[0])] = (puntaje, c[2])
    if sorted(cal) != list(range(1, 41)):
        sys.exit("La tabla de calificaciones debe tener los enunciados 1 a 40")
    return cal


def main(formato_docente, fuente, salida, png=None):
    md = open(fuente, encoding="utf8").read()
    cal = leer_calificaciones(bloque(md, "calificaciones"))
    totales = [sum(cal[i][0] for i in range(k * 10 + 1, k * 10 + 11)) for k in range(4)]

    tmp = tempfile.mkdtemp()
    if formato_docente.lower().endswith(".doc"):
        base = os.path.join(tmp, "formato.docx")
        word("-Accion", "convertir", "-Entrada", os.path.abspath(formato_docente), "-Salida", base)
    else:
        base = formato_docente
    d = docx.Document(base)
    tablas = d.tables
    cuestionarios = [tablas[1], tablas[3], tablas[5], tablas[7]]

    insertar_antes(d, tablas[0]._tbl, bloque(md, "antes"))

    for k, t in enumerate(cuestionarios):
        t.add_column(Cm(6.5))
        enc = t.rows[0].cells
        for celda, texto in ((enc[2], "Puntaje (0-10)"), (enc[3], "Sustento (evidencia)")):
            celda.text = ""
            formato(celda.paragraphs[0], texto, 9)
            celda.paragraphs[0].runs[0].bold = True
        for i, fila in enumerate(t.rows[1:], start=1):
            puntaje, sustento = cal[k * 10 + i]
            c = fila.cells
            c[2].text = ""
            formato(c[2].paragraphs[0], str(puntaje), 12)
            c[2].paragraphs[0].runs[0].bold = True
            c[2].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
            formato(c[3].paragraphs[0], sustento, 7.5)
        for fila in t.rows:
            for celda, cm in zip(fila.cells, (0.8, 7.4, 1.6, 7.2)):
                ancho(celda, cm)

    rotulos = [p for p in d.paragraphs if p.text.strip().rstrip("\xa0").strip() == "TOTAL:"]
    if len(rotulos) != 4:
        sys.exit(f"Se esperaban 4 rótulos TOTAL: y hay {len(rotulos)}")
    for p, tot in zip(rotulos, totales):
        fuente = next((x.font.name for x in p.runs if x.font.name), None)
        r = p.add_run(f" {tot} / 100 ({nivel(tot).lower()})")
        r.bold = True; r.font.size = Pt(12); r.font.color.rgb = AZUL
        if fuente:
            r.font.name = fuente

    final = tablas[8]
    final.add_column(Cm(4))
    modelo = next(r for r in final.rows[0].cells[1].paragraphs[0].runs if r.text.strip())
    formato(final.rows[0].cells[2].paragraphs[0], "NIVEL", modelo.font.size.pt if modelo.font.size else 12)
    r = final.rows[0].cells[2].paragraphs[0].runs[0]
    r.bold = modelo.bold
    r.font.name = modelo.font.name
    for fila, tot in zip(final.rows[1:], totales):
        formato(fila.cells[1].paragraphs[0], f"{tot} / 100", 11)
        formato(fila.cells[2].paragraphs[0], nivel(tot), 11)
    fila = final.add_row().cells
    total = sum(totales)
    for celda, texto in zip(fila, ("TOTAL GENERAL", f"{total} / 400 ({total / 4:.1f} %)".replace(".", ","),
                                   nivel(total, 400))):
        formato(celda.paragraphs[0], texto, 11)
        celda.paragraphs[0].runs[0].bold = True

    texto_resultado = "\n".join(bloque(md, "resultado"))
    for nombre, tot in zip(ELEMENTOS, totales):
        if f"({tot})" not in texto_resultado and f"{tot}" not in texto_resultado:
            sys.exit(f"El análisis no menciona el puntaje {tot} de {nombre}; revisa la fuente")
    escribir_md(d, bloque(md, "resultado"))

    s = d.sections[-1]
    if not s.footer.paragraphs[0].text.strip():
        s.footer.paragraphs[0].text = ("Diagnóstico BSC — Perficient, operación en Colombia — "
                                       "Trabajo académico, Equipo Firmes por la Gobernanza")
        s.footer.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in s.footer.paragraphs[0].runs:
            r.font.size = Pt(8)

    intermedio = os.path.join(tmp, "diligenciado.docx")
    d.save(intermedio)
    args = ["-Accion", "grafico", "-Entrada", intermedio, "-Valores", ",".join(map(str, totales))]
    if png:
        args += ["-Png", os.path.abspath(png)]
    word(*args)
    shutil.copyfile(intermedio, salida)
    shutil.rmtree(tmp, ignore_errors=True)
    print("ok", salida, "totales", totales, "general", total)


if __name__ == "__main__":
    main(*sys.argv[1:])
