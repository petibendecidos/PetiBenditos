"""Genera el mapa estratégico de TI (BSC de TI) del PETI Colombia en formato draw.io.

Uso:
    python scripts/generar_mapa_estrategico_bsc.py docs/entregas-2026-10-29/Mapa_estrategico_TI_BSC_Perficient_Colombia.drawio

Sigue los 8 pasos de BSC Designer sobre las cuatro perspectivas del BSC de TI (contribución al
negocio, usuario, interna, innovación). Objetivos, indicadores, metas y proyectos salen de §5.2,
§7, §9 y §10 del PETI Colombia v1.0; el contenido está en PERSPECTIVAS, OBJETIVOS y CAUSAS.
"""
import sys
from html import escape

salida = sys.argv[1]
FECHA = "29 de octubre de 2026"

ANCHO, ALTO = 2000, 1520
X_OBJ, W_OBJ, GAP = 335, 262, 40     # columna 0 de objetivos, ancho y separación entre columnas
Y_CARRILES, H_CARRIL = 320, 250
H_OBJ = 214
AMARILLO = "#F2C94C"
AZUL = "#1F3A5F"

# Prioridades estratégicas (objetivos de TI del PETI, §7): color de relleno y de borde
TEMAS = {
    "OETI01": ("Gobernar el uso de la IA en la operación colombiana", "#E1D5E7", "#9673A6"),
    "OETI02": ("Mantener la certificación de seguridad y cumplir la Ley 1581", "#DAE8FC", "#6C8EBF"),
    "OETI03": ("Estandarizar la entrega de software, su gobierno y su costo", "#FFE6CC", "#D79B00"),
    "OETI04": ("Desarrollar las capacidades del talento en IA, nube y datos", "#D5E8D4", "#82B366"),
}

# (nombre, pregunta de la perspectiva, equivalencia con el BSC de Kaplan y Norton, fondo del carril)
PERSPECTIVAS = [
    ("Contribución al negocio", "¿Cómo ve la dirección al área de TI?", "financiera", "#FBFBFB"),
    ("Perspectiva del usuario", "¿Cómo ven los usuarios al área de TI?", "del cliente", "#F3F3F3"),
    ("Perspectiva interna", "¿Cuán efectivos y eficientes son los procesos del área de TI?", "de procesos internos", "#FBFBFB"),
    ("Perspectiva de innovación", "¿Cómo está posicionada el área de TI con respecto a las necesidades futuras del negocio?", "de aprendizaje y crecimiento", "#F3F3F3"),
]

# id: (perspectiva, columna, tema, objetivos corporativos, enunciado, métricas, iniciativas)
# métrica: (tipo R = resultado / A = actuación, KPI o None si es propuesta, nombre, meta)
OBJETIVOS = {
    "CN1": (0, 0, "OETI02", "OC02", "Conservar la confianza de los clientes regulados", [
        ("R", "KPI-07", "No conformidades mayores ISO/IEC 27001", "Año 1: 0 · Año 2: 0"),
        ("R", "KPI-13", "Informe SOC 2 tipo II sin salvedades", "Año 2: sí"),
    ], "P1.1 · P4.1"),
    "CN2": (0, 1, "OETI01", "OC01", "Llevar la IA a producción con los clientes", [
        ("R", "KPI-03", "Casos de IA en producción con clientes", "Año 1: 1 · Año 2: 5"),
    ], "P3.1 · P3.3"),
    "CN3": (0, 2, "OETI03", "OC03", "Operar con un costo de TI controlado y trazable", [
        ("R", "KPI-02", "Variación del costo de nube administrada", "Año 1: −5 % · Año 2: −15 %"),
        ("R", None, "Costo de TI por hora facturada", "Propuesta: sin línea base ni KPI en el PETI"),
    ], "P2.7"),
    "CN4": (0, 3, "OETI03", "OC01 a OC04", "Cumplir el plan de TI que aprobó la dirección", [
        ("R", "KPI-01", "Ejecución acumulada del PETI", "Año 1: 55 % · Año 2: 95 %"),
    ], "P4.3"),
    "US3": (1, 0, "OETI03", "OC02", "Conocer la satisfacción de usuarios y clientes con TI", [
        ("R", None, "Índice de satisfacción con los servicios de TI", "Propuesta: sin KPI en el PETI"),
    ], "Sin proyecto en el PETI"),
    "US1": (1, 1, "OETI01", "OC01", "Dar a las células acceso ordenado a la IA", [
        ("A", "KPI-04", "Células con IA activa y licencia aprobada", "Año 1: 85 % · Año 2: 95 %"),
    ], "P1.6"),
    "US2": (1, 2, "OETI03", "OC03", "Entregar al cliente horas conciliadas con las tareas", [
        ("A", "KPI-06", "Conciliación de horas y tareas", "Año 1: 90 % · Año 2: 95 %"),
    ], "P2.4"),
    "PI2": (2, 0, "OETI02", "OC02", "Cerrar a tiempo las vulnerabilidades críticas", [
        ("A", "KPI-05", "Horas promedio entre detección y cierre", "Año 1: < 72 h · Año 2: < 24 h"),
    ], "P2.2 · P2.3"),
    "PI1": (2, 1, "OETI01", "OC01 · OC02", "Gobernar el uso de la IA con un sistema certificable", [
        ("A", "KPI-08", "Cobertura del inventario de IA", "Año 1: 90 % · Año 2: 100 %"),
    ], "P1.2 · P1.3 · P1.4 · P3.2 · P4.2"),
    "PI3": (2, 2, "OETI03", "OC03", "Estandarizar los ambientes y la entrega de software", [
        ("A", "KPI-11", "Ambientes con infraestructura como código", "Año 1: 60 % · Año 2: 100 %"),
    ], "P2.1 · P2.5 · P2.6"),
    "PI4": (2, 3, "OETI03", "OC02 · OC03", "Formalizar el gobierno de TI y el registro de obligaciones legales", [
        ("A", "KPI-14", "Sesiones de comité con acta", "Año 1: 90 % · Año 2: 90 %"),
    ], "P2.8 · P1.9"),
    "IF3": (3, 0, "OETI01", "OC01", "Preparar la plataforma de datos e IA que pedirán los clientes", [
        ("A", None, "Pruebas de concepto evaluadas por el CoE", "Propuesta: sin KPI en el PETI"),
    ], "P1.8 · P3.5"),
    "IF1": (3, 1, "OETI04", "OC04", "Certificar al personal técnico en IA, nube y datos", [
        ("A", "KPI-09", "Personal técnico certificado", "Año 1: 70 % · Año 2: 90 %"),
    ], "P1.5 · P1.7 · P3.4"),
    "IF2": (3, 2, "OETI04", "OC04", "Rotar al personal entre células", [
        ("A", "KPI-10", "Personal rotado entre células", "Año 1: 50 % · Año 2: 100 %"),
    ], "Sin proyecto propio en el PETI"),
}

# Relaciones causa-efecto, de abajo hacia arriba: (origen, destino, razonamiento)
CAUSAS = [
    ("IF1", "PI1", "El personal certificado en IA y seguridad aplica los controles del sistema de gestión de IA."),
    ("IF1", "PI3", "El personal certificado en nube automatiza los ambientes con infraestructura como código."),
    ("IF2", "PI3", "La rotación lleva las mismas plantillas y prácticas a todas las células."),
    ("IF3", "US1", "El centro de excelencia prueba las herramientas de IA antes de que lleguen a las células."),
    ("PI1", "US1", "Con inventario y reglas claras, las licencias de IA se aprueban sin frenar a las células."),
    ("PI1", "CN1", "El sistema de gestión de IA aporta los controles de IA que incluirá el informe SOC 2 (P4.1)."),
    ("PI2", "CN1", "Cerrar a tiempo las vulnerabilidades críticas evita no conformidades en la auditoría ISO/IEC 27001."),
    ("PI3", "US2", "Las plantillas ALM homologadas permiten conciliar horas y tareas (P2.1 precede a P2.4)."),
    ("PI3", "CN3", "Con infraestructura como código y observabilidad, el costo de nube se mide por ambiente y se puede recortar."),
    ("PI4", "CN4", "Los comités con acta revisan el portafolio cada mes y corrigen los desvíos a tiempo."),
    ("US1", "CN2", "Las células que ya usan IA con licencia generan los casos que llegan a producción."),
    ("US2", "CN3", "Las horas conciliadas con tareas muestran en qué se va el costo de la operación."),
    ("US3", "CN1", "Medir la satisfacción avisa antes de que un cliente pierda la confianza (hipótesis del equipo)."),
]

# Rutas de las flechas: (salida x, y), (entrada x, y), puntos intermedios. Las que saltan un carril
# suben por el espacio entre columnas para no cruzar otros objetivos.
def gap_x(col, k):
    """x dentro del espacio a la izquierda de la columna col; k = 1, 2, 3 separa flechas paralelas."""
    return X_OBJ + col * (W_OBJ + GAP) - GAP + k * 10

def caja(oid):
    p, c = OBJETIVOS[oid][0], OBJETIVOS[oid][1]
    return X_OBJ + c * (W_OBJ + GAP), Y_CARRILES + p * H_CARRIL + 22

def ruta(o, d):
    ox, oy = caja(o)
    dx, dy = caja(d)
    rutas = {
        ("PI2", "CN1"): ((1, 0.25), (1, 0.85), [(gap_x(1, 1), oy + 0.25 * H_OBJ), (gap_x(1, 1), dy + 0.85 * H_OBJ)]),
        ("PI1", "CN1"): ((0, 0.12), (1, 0.6), [(gap_x(1, 2), oy + 0.12 * H_OBJ), (gap_x(1, 2), dy + 0.6 * H_OBJ)]),
        ("IF3", "US1"): ((1, 0.25), (0, 0.85), [(gap_x(1, 3), oy + 0.25 * H_OBJ), (gap_x(1, 3), dy + 0.85 * H_OBJ)]),
        ("PI3", "CN3"): ((1, 0.25), (1, 0.85), [(gap_x(3, 2), oy + 0.25 * H_OBJ), (gap_x(3, 2), dy + 0.85 * H_OBJ)]),
        ("IF1", "PI3"): ((0.85, 0), (0.2, 1), [(ox + 0.85 * W_OBJ, oy - 14), (dx + 0.2 * W_OBJ, oy - 14)]),
        ("IF2", "PI3"): ((0.6, 0), (0.6, 1), []),
        ("PI1", "US1"): ((0.5, 0), (0.5, 1), []),
    }
    return rutas.get((o, d), ((0.5, 0), (0.5, 1), []))


celdas = []
_n = [0]

def nuevo_id():
    _n[0] += 1
    return f"m{_n[0]}"

def vertice(x, y, w, h, valor, estilo, padre="1"):
    i = nuevo_id()
    celdas.append(f'<mxCell id="{i}" value="{escape(valor, quote=True)}" style="{estilo}" vertex="1" parent="{padre}">'
                  f'<mxGeometry x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}" as="geometry"/></mxCell>')
    return i

def arista(origen, destino, valor, estilo, puntos=()):
    i = nuevo_id()
    pts = "".join(f'<mxPoint x="{x:g}" y="{y:g}"/>' for x, y in puntos)
    pts = f'<Array as="points">{pts}</Array>' if pts else ""
    celdas.append(f'<mxCell id="{i}" value="{escape(valor, quote=True)}" style="{estilo}" edge="1" parent="1" source="{origen}" target="{destino}">'
                  f'<mxGeometry relative="1" as="geometry">{pts}</mxGeometry></mxCell>')
    return i

TEXTO = "text;html=1;whiteSpace=wrap;align=left;verticalAlign=top;fontColor=#333333;"
CAJA = "rounded=1;arcSize=4;html=1;whiteSpace=wrap;align=left;verticalAlign=top;spacing=8;"

def paso(x, y, n, texto=None, ancho=520):
    vertice(x, y, 28, 28, str(n), f"rounded=0;html=1;fillColor={AMARILLO};strokeColor=none;fontStyle=1;fontSize=14;fontColor=#333333;")
    if texto:
        vertice(x + 34, y + 2, ancho, 24, texto, TEXTO + "fontSize=12;verticalAlign=middle;")


# Fondo y encabezado
vertice(0, 0, ANCHO, ALTO, "", "rounded=0;fillColor=#FFFFFF;strokeColor=none;")
vertice(40, 18, 1300, 64,
        "<b>Mapa estratégico de TI (BSC de TI)</b><br><font style=\"font-size:13px\">Perficient, operación en Colombia · PETI 2026-2028 · octubre de 2026 a septiembre de 2028</font>",
        TEXTO + "fontSize=24;")
vertice(1440, 18, 520, 64,
        f"Equipo Firmes por la Gobernanza<br>Gobierno y Servicios de TI · Universidad Santiago de Cali<br>{FECHA}",
        TEXTO + "fontSize=11;align=right;fontColor=#555555;")

# Paso 1: misión, visión y valores
paso(6, 95, 1)
vertice(40, 95, 640, 125,
        "<b>Misión de TI</b> (PETI §7, propuesta)<br>Proveer y gobernar las plataformas, herramientas y controles con los que la operación colombiana entrega software y soluciones de IA a sus clientes, de forma segura, medible y conforme con la ley.",
        CAJA + "fillColor=#F7F7F7;strokeColor=#999999;fontSize=12;")
vertice(695, 95, 640, 125,
        "<b>Visión de TI</b> (PETI §7, propuesta)<br>En septiembre de 2028, la operación de Perficient en Colombia gestionará el uso de la IA con un sistema certificable, entregará software con pipelines y ambientes estandarizados y medirá su desempeño cada trimestre.",
        CAJA + "fillColor=#F7F7F7;strokeColor=#999999;fontSize=12;")
vertice(1350, 95, 610, 125,
        "<b>Valores de TI</b> (propuestos por el equipo; el PETI no los define)<br>"
        "• Seguridad desde el diseño: los controles se definen antes de entregar.<br>"
        "• Decidir con datos: cada objetivo tiene indicador, meta y responsable.<br>"
        "• Cumplimiento demostrable: lo que se promete al cliente se puede auditar.<br>"
        "• Aprendizaje continuo: certificación y rotación del talento.",
        CAJA + "fillColor=#F7F7F7;strokeColor=#999999;fontSize=12;")

# Paso 3: prioridades estratégicas
paso(6, 236, 3)
vertice(40, 232, 285, 50, "<b>Prioridades estratégicas</b><br>Objetivos de TI del PETI (§7); color de cada objetivo del mapa",
        TEXTO + "fontSize=11;verticalAlign=middle;")
for k, (oeti, (nombre, relleno, borde)) in enumerate(TEMAS.items()):
    vertice(X_OBJ + k * (W_OBJ + GAP), 232, W_OBJ, 50, f"<b>{oeti}</b> {nombre}",
            f"rounded=1;arcSize=20;html=1;whiteSpace=wrap;fillColor={relleno};strokeColor={borde};strokeWidth=2;fontSize=11;fontColor=#333333;spacing=6;")

# Encabezados de columnas (pasos 2, 4, 6, 7 y 5)
paso(6, 290, 2, "<b>Paso 2.</b> Perspectivas del BSC de TI", 290)
paso(X_OBJ, 290, 4, "<b>Paso 4.</b> Objetivos estratégicos  ·  <b>Paso 6.</b> Métricas y metas  ·  <b>Paso 7.</b> Iniciativas (proyectos del PETI)", 900)
paso(1540, 290, 5, "<b>Paso 5.</b> Razonamiento causa-efecto", 380)

# Carriles de las perspectivas
for p, (nombre, pregunta, kaplan, fondo) in enumerate(PERSPECTIVAS):
    y = Y_CARRILES + p * H_CARRIL
    vertice(40, y, 1480, H_CARRIL - 6, "", f"rounded=0;fillColor={fondo};strokeColor=#DDDDDD;")
    vertice(40, y, 46, H_CARRIL - 6, f"<b>{nombre}</b>",
            f"rounded=0;html=1;whiteSpace=wrap;horizontal=0;fillColor={AZUL};strokeColor=none;fontColor=#FFFFFF;fontSize=13;")
    vertice(94, y + 22, 230, H_OBJ,
            f"<i>{pregunta}</i><br><br><font color=\"#777777\" style=\"font-size:10px\">Equivale a la perspectiva {kaplan} del BSC de Kaplan y Norton.</font>",
            TEXTO + "fontSize=13;verticalAlign=middle;")

# Objetivos con sus métricas e iniciativas
ids = {}
for oid, (p, c, tema, oc, enunciado, metricas, iniciativas) in OBJETIVOS.items():
    x, y = caja(oid)
    relleno, borde = TEMAS[tema][1], TEMAS[tema][2]
    cont = vertice(x, y, W_OBJ, H_OBJ, "",
                   f"rounded=0;html=1;container=1;collapsible=0;fillColor=#FFFFFF;strokeColor={borde};strokeWidth=2;")
    ids[oid] = cont
    vertice(0, 0, W_OBJ, 46, f"<b>{oid} · {enunciado}</b>",
            f"rounded=0;html=1;whiteSpace=wrap;fillColor={relleno};strokeColor=none;fontSize=11;fontColor=#222222;spacing=4;", cont)
    vertice(6, 47, W_OBJ - 12, 18, f"Apoya {oc} · {tema}", TEXTO + "fontSize=9;fontColor=#666666;verticalAlign=middle;", cont)
    for k, (tipo, kpi, nombre, meta) in enumerate(metricas):
        ym = 68 + k * 50
        vertice(6, ym + 12, 22, 22, tipo,
                f"rounded=0;html=1;fillColor={'#333333' if tipo == 'R' else '#FFFFFF'};strokeColor=#333333;"
                f"fontColor={'#FFFFFF' if tipo == 'R' else '#333333'};fontStyle=1;fontSize=11;", cont)
        rotulo = f"<b>{kpi}</b> {nombre}" if kpi else f"<b>Propuesta</b> {nombre}"
        borde_m = "dashed=1;strokeColor=#999999;" if kpi is None else "strokeColor=#DDDDDD;"
        vertice(32, ym, W_OBJ - 38, 46, f"{rotulo}<br><font color=\"#555555\">{meta}</font>",
                f"rounded=0;html=1;whiteSpace=wrap;align=left;verticalAlign=middle;spacing=4;fillColor=#FFFFFF;{borde_m}fontSize=10;fontColor=#222222;", cont)
    vertice(0, H_OBJ - 36, W_OBJ, 36, f"<b>Iniciativas:</b> {iniciativas}",
            "rounded=0;html=1;whiteSpace=wrap;align=left;verticalAlign=middle;spacing=6;fillColor=#F1F1F1;strokeColor=none;fontSize=10;fontColor=#222222;", cont)

# Flechas causa-efecto numeradas
FLECHA = ("edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;endFill=1;strokeColor=#444444;strokeWidth=1.6;"
          "fontSize=10;fontStyle=1;fontColor=#222222;labelBackgroundColor=#FFF2B3;labelBorderColor=#444444;")
for n, (o, d, _) in enumerate(CAUSAS, 1):
    (sx, sy), (tx, ty), puntos = ruta(o, d)
    arista(ids[o], ids[d], str(n),
           FLECHA + f"exitX={sx};exitY={sy};exitDx=0;exitDy=0;entryX={tx};entryY={ty};entryDx=0;entryDy=0;", puntos)

# Paso 5: razonamiento
lineas = "".join(f"<b>{n}.</b> {o} → {d}: {t}<br>" for n, (o, d, t) in enumerate(CAUSAS, 1))
vertice(1540, Y_CARRILES, 420, 4 * H_CARRIL - 6,
        "Se lee de abajo hacia arriba: el talento (innovación) mejora los procesos de TI (interna); los procesos dan a usuarios y clientes "
        "lo que necesitan (usuario), y eso sostiene lo que la dirección espera de TI (contribución al negocio).<br><br>" + lineas
        + "<br><b>Vacíos que muestra el mapa</b> (para la versión 1.1 del PETI)<br>"
        "• La contribución al negocio tiene un solo indicador de costo (KPI-02); falta el costo de TI por hora facturada.<br>"
        "• US3 e IF2 no tienen proyecto; CN3, US3 e IF3 dependen de métricas que el PETI todavía no define.<br>"
        "• Los indicadores siguen a los objetivos de TI, no a los procesos: faltan objetivos e indicadores por proceso "
        "(diagnóstico BSC, enunciados 22 a 24).",
        CAJA + "fillColor=#FFFDF2;strokeColor=#E0C060;fontSize=11;spacing=10;")

# Paso 8: cascada
yb = Y_CARRILES + 4 * H_CARRIL + 18
paso(6, yb, 8, "<b>Paso 8.</b> Cascada: el mapa baja a cada nivel con sus propios objetivos e indicadores (propuesto, P2.8)", 900)
niveles = [
    "<b>Corporativo</b><br>Objetivos OC01 a OC04 (PETI §5.2)",
    "<b>TI Colombia</b><br>Este mapa · Comité Directivo del PETI, trimestral",
    "<b>Táctico</b><br>Comité Táctico de TI, mensual: proyectos, KPI y riesgos",
    "<b>Célula</b><br>Comité por célula, semanal: KPI-04, KPI-05 y KPI-06 de la célula",
]
prev = None
for k, t in enumerate(niveles):
    v = vertice(40 + k * 290, yb + 36, 250, 66, t, CAJA + "fillColor=#E8EEF6;strokeColor=#6C8EBF;fontSize=11;align=center;verticalAlign=middle;")
    if prev:
        arista(prev, v, "", "edgeStyle=none;html=1;endArrow=block;endFill=1;strokeColor=#6C8EBF;strokeWidth=1.6;")
    prev = v

# Leyenda
xl = 1220
vertice(xl, yb, 740, 112, "", "rounded=0;fillColor=#FFFFFF;strokeColor=#CCCCCC;")
vertice(xl + 10, yb + 4, 200, 20, "<b>Leyenda</b>", TEXTO + "fontSize=11;")
vertice(xl + 12, yb + 30, 20, 20, "R", "rounded=0;html=1;fillColor=#333333;strokeColor=#333333;fontColor=#FFFFFF;fontStyle=1;fontSize=11;")
vertice(xl + 38, yb + 30, 320, 20, "Métrica de resultado: muestra si el objetivo se logró", TEXTO + "fontSize=10;verticalAlign=middle;")
vertice(xl + 12, yb + 56, 20, 20, "A", "rounded=0;html=1;fillColor=#FFFFFF;strokeColor=#333333;fontColor=#333333;fontStyle=1;fontSize=11;")
vertice(xl + 38, yb + 56, 320, 20, "Métrica de actuación: se mueve antes y anticipa el resultado", TEXTO + "fontSize=10;verticalAlign=middle;")
vertice(xl + 12, yb + 82, 70, 20, "", "rounded=0;dashed=1;fillColor=#FFFFFF;strokeColor=#999999;")
vertice(xl + 88, yb + 82, 270, 20, "Métrica propuesta por el equipo, sin KPI en el PETI", TEXTO + "fontSize=10;verticalAlign=middle;")
vertice(xl + 380, yb + 30, 20, 20, "1", "rounded=0;html=1;fillColor=#FFF2B3;strokeColor=#444444;fontStyle=1;fontSize=10;")
vertice(xl + 406, yb + 30, 320, 20, "Relación causa-efecto; el número remite al Paso 5", TEXTO + "fontSize=10;verticalAlign=middle;")
vertice(xl + 380, yb + 56, 70, 20, "", "rounded=0;fillColor=#F1F1F1;strokeColor=none;")
vertice(xl + 456, yb + 56, 280, 20, "Iniciativas: proyectos del portafolio (PETI §9)", TEXTO + "fontSize=10;verticalAlign=middle;")
vertice(xl + 380, yb + 82, 350, 20, "Metas: año 1 = septiembre de 2027; año 2 = septiembre de 2028",
        TEXTO + "fontSize=10;verticalAlign=middle;")

# Fuente
vertice(40, ALTO - 50, 1920, 40,
        "Fuente: PETI Colombia v1.0 (§5.2, §7, §9 y §10) y diagnóstico BSC del 22 de octubre de 2026. Todo el mapa es una propuesta del equipo (INT-001) "
        "y depende de la aprobación del Comité Directivo del PETI. Perspectivas del BSC de TI según Van Grembergen y Van Bruggen (1997); "
        "pasos según BSC Designer, \"8 pasos para crear un mapa estratégico\". Trabajo académico; no es un documento oficial de Perficient.",
        TEXTO + "fontSize=10;fontColor=#666666;")

xml = (f'<mxfile host="app.diagrams.net"><diagram id="mapa-bsc-ti" name="Mapa estratégico de TI">'
       f'<mxGraphModel dx="{ANCHO}" dy="{ALTO}" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" '
       f'page="1" pageScale="1" pageWidth="{ANCHO}" pageHeight="{ALTO}" math="0" shadow="0"><root>'
       '<mxCell id="0"/><mxCell id="1" parent="0"/>' + "".join(celdas) + "</root></mxGraphModel></diagram></mxfile>")
open(salida, "w", encoding="utf-8").write(xml)
print(f"{salida}: {len(OBJETIVOS)} objetivos, {len(CAUSAS)} relaciones causa-efecto")
