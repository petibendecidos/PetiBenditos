"""Genera el lienzo Canvas del modelo de negocio del área de TI (PETI Colombia).

Uso:
    python scripts/generar_canvas_modelo_negocio.py docs/entregas-2026-10-21/Modelo_Negocio_TI_Canvas_Perficient_Colombia.pptx

Dos diapositivas: el lienzo de 9 bloques y su lectura. El contenido de cada bloque está en
el diccionario BLOQUES. Requiere python-pptx.
"""
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

salida = sys.argv[1]
AZUL = RGBColor(0x1F, 0x3A, 0x5F)
GRIS = RGBColor(0x40, 0x40, 0x40)

BLOQUES = {
    "socios": ("8. Socios clave", RGBColor(0xE8, 0xEE, 0xF6), [
        "Microsoft, Databricks, Snowflake, Gradial y Lovable: plataformas, formación y certificaciones (PUB-005 a PUB-010)",
        "A-Lign: auditoría de ISO/IEC 27001 (PUB-002)",
        "Servicio externo de pruebas de seguridad (PRV-001)",
        "Proveedores de nube y de modelos de IA",
        "Legal y Talento humano de la compañía",
        "Clientes: corresponsables de la infraestructura en nube",
    ]),
    "actividades": ("7. Actividades clave", RGBColor(0xE8, 0xF3, 0xEC), [
        "Operar y recertificar el SGSI",
        "Gobernar la IA: inventario, permisos para agentes y licencias",
        "Estandarizar la entrega: CI/CD seguro, IaC y observabilidad",
        "Conciliar horas y tareas para facturar",
        "Formar y certificar al personal por rol",
    ]),
    "recursos": ("6. Recursos clave", RGBColor(0xE8, 0xF3, 0xEC), [
        "SGSI certificado ISO/IEC 27001:2022",
        "Talento técnico certificado",
        "Plataforma ALM, pipelines, observabilidad y registro de tiempos",
        "Centro de excelencia de IA (propuesto, P1.8)",
    ]),
    "propuesta": ("2. Propuesta de valor", RGBColor(0xFD, 0xF1, 0xE3), [
        "Herramientas y ambientes listos para entregar software desde el primer día",
        "IA aprobada y controlada: se puede usar sin exponer código ni datos del cliente",
        "Controles que el cliente puede verificar: ISO/IEC 27001, informe SOC 2 y, después, ISO/IEC 42001",
        "Entrega medible: horas conciliadas, vulnerabilidades cerradas a tiempo y costo de nube visible",
        "Talento certificado en IA, nube y datos",
    ]),
    "relaciones": ("4. Relación con los clientes", RGBColor(0xF6, 0xE9, 0xF3), [
        "Autoservicio con plantillas y pipelines estándar",
        "Acompañamiento del centro de excelencia de IA",
        "Comités Directivo (trimestral), Táctico (mensual) y por célula (semanal)",
        "Acuerdo previo con el cliente para todo cambio en su infraestructura",
    ]),
    "canales": ("3. Canales", RGBColor(0xF6, 0xE9, 0xF3), [
        "Catálogo de servicios de TI y procedimiento de licencias de IA",
        "Wiki, plataforma de colaboración e intranet",
        "Capacitación e inducción",
        "Informe anual de auditoría a los clientes",
    ]),
    "segmentos": ("1. Segmentos de clientes", RGBColor(0xE8, 0xEE, 0xF6), [
        "Internos: células de entrega (desarrolladores y Technical Leads)",
        "Product Managers y Line Managers",
        "Dirección de la operación y Comité Directivo del PETI",
        "Externos (indirectos): clientes de Norteamérica, muchos regulados, que reciben el software y exigen los controles",
    ]),
    "costos": ("9. Estructura de costos", RGBColor(0xF2, 0xF2, 0xF2), [
        "Nómina del personal de TI: el costo principal",
        "Licencias de herramientas y de IA; consumo de nube",
        "Auditorías (ISO, SOC 2) y pruebas de penetración",
        "Formación y certificaciones",
        "Portafolio del PETI: USD 1,4 a 6,65 millones en dos años (orden de magnitud, por validar)",
    ]),
    "ingresos": ("5. Fuentes de ingresos (cómo capta valor)", RGBColor(0xF2, 0xF2, 0xF2), [
        "Horas facturables: el registro de tiempos es la base de la facturación",
        "Contratos con clientes regulados que exigen certificaciones vigentes",
        "Nuevas líneas: casos de IA en producción (KPI-03) y plataformas de datos",
        "Ahorros: costo de nube (KPI-02) y horas recuperadas al conciliar (KPI-06)",
        "Financiación: presupuesto de la operación (guía de presupuesto propuesta, COBIT APO06)",
    ]),
}


def caja(slide, clave, x, y, w, h, tam=11):
    titulo, color, items = BLOQUES[clave]
    forma = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, int(x), int(y), int(w), int(h))
    forma.fill.solid()
    forma.fill.fore_color.rgb = color
    forma.line.color.rgb = AZUL
    forma.line.width = Pt(1)
    tf = forma.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = MSO_ANCHOR.TOP
    for m in ("margin_left", "margin_right"):
        setattr(tf, m, Inches(0.08))
    tf.margin_top = Inches(0.05)
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = titulo
    r.font.bold = True
    r.font.size = Pt(tam + 2)
    r.font.color.rgb = AZUL
    for it in items:
        q = tf.add_paragraph()
        q.space_before = Pt(2)
        rr = q.add_run()
        rr.text = "• " + it
        rr.font.size = Pt(tam)
        rr.font.color.rgb = GRIS


def texto(slide, x, y, w, h, contenido, tam, negrita=False, color=AZUL, alin=PP_ALIGN.LEFT):
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.alignment = alin
    r = p.add_run()
    r.text = contenido
    r.font.size = Pt(tam)
    r.font.bold = negrita
    r.font.color.rgb = color
    return tb


prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
s = prs.slides.add_slide(prs.slide_layouts[6])

texto(s, Inches(0.3), Inches(0.1), Inches(12.7), Inches(0.45),
      "Modelo de negocio del área de TI — Perficient, operación en Colombia (lienzo Canvas)", 20, True)
texto(s, Inches(0.3), Inches(0.52), Inches(12.7), Inches(0.3),
      "El área de TI como proveedor interno: plataformas, seguridad, herramientas e IA para los equipos que entregan software a clientes de Norteamérica. Propuesta del equipo para el PETI 2026-2028.",
      10, False, GRIS)

X0, Y0 = Inches(0.3), Inches(0.9)
W = Inches(12.733) / 5
HT = Inches(4.35)
HB = Inches(1.95)
caja(s, "socios", X0, Y0, W, HT)
caja(s, "actividades", X0 + W, Y0, W, HT / 2)
caja(s, "recursos", X0 + W, Y0 + HT / 2, W, HT / 2)
caja(s, "propuesta", X0 + 2 * W, Y0, W, HT, 13)
caja(s, "relaciones", X0 + 3 * W, Y0, W, HT / 2)
caja(s, "canales", X0 + 3 * W, Y0 + HT / 2, W, HT / 2)
caja(s, "segmentos", X0 + 4 * W, Y0, W, HT)
caja(s, "costos", X0, Y0 + HT, W * 2.5, HB)
caja(s, "ingresos", X0 + W * 2.5, Y0 + HT, W * 2.5, HB)

texto(s, Inches(0.3), Inches(7.2), Inches(12.7), Inches(0.3),
      "PUB- y PRV- remiten al registro de evidencias del proyecto; PRV-001 es una cuenta de cliente analizada, no una política de Perficient. P y KPI remiten al portafolio y a los indicadores del PETI Colombia. Trabajo académico — Equipo Firmes por la Gobernanza, 21 de octubre de 2026.",
      7, False, GRIS)

s.notes_slide.notes_text_frame.text = (
    "Cómo leer el lienzo: el área de TI no vende al mercado; habilita la venta. Sus clientes directos son los equipos internos, "
    "y sus clientes indirectos son las empresas de Norteamérica que reciben el software y piden controles. Por eso sus 'ingresos' "
    "se leen como el valor que capta para la operación: horas facturables, contratos que exigen certificaciones y ahorros. "
    "La tensión del modelo es la misma de la DOFA: la propuesta de valor promete IA controlada (F2), pero hoy falta el sistema de gestión de IA (D1). "
    "Los bloques marcados como propuestos dependen de la aprobación del Comité Directivo del PETI."
)

# Diapositiva 2: lectura del modelo
s2 = prs.slides.add_slide(prs.slide_layouts[6])
texto(s2, Inches(0.5), Inches(0.3), Inches(12.3), Inches(0.6), "Cómo se lee este modelo de negocio", 24, True)
puntos = [
    ("El área de TI no vende: habilita la venta.",
     "En una firma de servicios, la plataforma de entrega, los pipelines y el registro de tiempos son la línea de producción. Sin ellos no hay horas que facturar."),
    ("Su propuesta de valor responde al poder de los compradores.",
     "Los clientes regulados eligen proveedor por lo que puede demostrar: certificaciones vigentes, informe SOC 2 e IA controlada. Esa es la fuerza de Porter que más exige a TI."),
    ("El bloque débil es el de recursos frente a la propuesta.",
     "El lienzo promete IA controlada, pero hoy no hay sistema de gestión de IA, inventario ni permisos para agentes (D1). Los proyectos P1.2 a P1.6 cierran esa distancia."),
    ("Los ingresos no se pueden medir todavía.",
     "No hay presupuesto de TI ni indicadores de costo y valor (D2, D4). El equipo propone medir el costo de TI por hora facturada, el ahorro de nube y las horas recuperadas."),
]
y = Inches(1.2)
for t, d in puntos:
    texto(s2, Inches(0.6), y, Inches(12.0), Inches(0.4), t, 16, True)
    texto(s2, Inches(0.6), y + Inches(0.42), Inches(12.0), Inches(0.8), d, 13, False, GRIS)
    y += Inches(1.45)

prs.save(salida)
print("ok", salida)
