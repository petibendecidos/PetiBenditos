"""Markdown a .docx con estilos neutros (sin la plantilla del MinTIC), para entregas del curso.

Uso:
    python scripts/md_a_docx_simple.py <entrada.md> <salida.docx> "<texto del pie de página>"

Soporta '#'-'####', párrafos, viñetas, listas numeradas, tablas con '|', **negrita**, *cursiva*,
`código` e imágenes en línea propia (![leyenda](ruta relativa al .md)). Omite los comentarios HTML.
Para el PETI se usa .claude/skills/guia-peti/scripts/md_a_docx.py (plantilla MinTIC).
"""
import os
import re
import sys

import docx
from docx.enum.section import WD_ORIENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

AZUL = RGBColor(0x1F, 0x3A, 0x5F)


def formato(p, texto, tam=None):
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
        if tam:
            r.font.size = Pt(tam)


def sombra(c, color):
    tc = c._element.get_or_add_tcPr()
    s = OxmlElement("w:shd")
    s.set(qn("w:val"), "clear"); s.set(qn("w:color"), "auto"); s.set(qn("w:fill"), color)
    tc.append(s)


def tabla(d, filas):
    filas = [f for f in filas if not all(re.fullmatch(r":?-+:?", c.strip() or "-") for c in f)]
    n = max(len(f) for f in filas)
    t = d.add_table(rows=0, cols=n)
    t.style = d.styles["Table Grid"]
    tam = 8 if n >= 6 else 9
    for i, f in enumerate(filas):
        cs = t.add_row().cells
        for j in range(n):
            p = cs[j].paragraphs[0]
            formato(p, f[j] if j < len(f) else "", tam)
            if i == 0:
                for r in p.runs:
                    r.bold = True; r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
                sombra(cs[j], "1F3A5F")
    d.add_paragraph()


def convertir(entrada, salida, pie):
    d = docx.Document()
    st = d.styles["Normal"]
    st.font.name = "Calibri"
    st.font.size = Pt(10.5)
    for nivel, tam in ((1, 16), (2, 13), (3, 11.5)):
        h = d.styles[f"Heading {nivel}"]
        h.font.color.rgb = AZUL
        h.font.size = Pt(tam)
    for s in d.sections:
        s.left_margin = s.right_margin = Cm(2)
        s.top_margin = s.bottom_margin = Cm(2)
        s.footer.paragraphs[0].text = pie
        s.footer.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in s.footer.paragraphs[0].runs:
            r.font.size = Pt(8)
    filas = []
    texto = re.sub(r"<!--.*?-->", "", open(entrada, encoding="utf8").read(), flags=re.S)
    for linea in texto.splitlines() + [""]:
        if linea.strip().startswith("|"):
            filas.append([c.strip() for c in linea.strip().strip("|").split("|")])
            continue
        if filas:
            tabla(d, filas); filas = []
        s = linea.rstrip()
        if not s.strip():
            continue
        img = re.match(r"^!\[([^\]]*)\]\(([^)]+)\)$", s.strip())
        if img:
            ruta = os.path.join(os.path.dirname(os.path.abspath(entrada)), img.group(2))
            d.add_picture(ruta, width=Cm(16))
            d.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
            leyenda = d.add_paragraph()
            formato(leyenda, f"*{img.group(1)}*", 9)
            leyenda.alignment = WD_ALIGN_PARAGRAPH.CENTER
            continue
        m = re.match(r"^(#{1,4})\s+(.*)", s)
        if m:
            n = len(m.group(1))
            if n == 1:
                p = d.add_paragraph(style="Title")
                r = p.add_run(m.group(2)); r.font.size = Pt(22); r.font.color.rgb = AZUL
            else:
                d.add_heading(m.group(2), level=n - 1)
        elif re.match(r"^\s*[-*]\s+", s):
            formato(d.add_paragraph(style="List Bullet"), re.sub(r"^\s*[-*]\s+", "", s))
        elif re.match(r"^\d+\.\s", s):
            formato(d.add_paragraph(style="List Number"), re.sub(r"^\d+\.\s+", "", s))
        else:
            formato(d.add_paragraph(), s)
    d.save(salida)
    print("ok", salida)


if __name__ == "__main__":
    convertir(sys.argv[1], sys.argv[2], sys.argv[3])
