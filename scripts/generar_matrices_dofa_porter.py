"""Genera el libro de matrices de la entrega DOFA y Porter (PETI Colombia).

Uso:
    python scripts/generar_matrices_dofa_porter.py docs/entregas-2026-10-21/Matrices_DOFA_Porter_Perficient_Colombia.xlsx

Consolida las plantillas del curso 'Matrices-Gerencia-Estrategica.xls' y
'Plantillas_Herramientas_Diagnostico.xlsx' en 8 hojas con fórmulas: guía, DOFA, MEFI, MEFE,
DOFA cruzada, cinco fuerzas, perfil competitivo y seguimiento. Los factores, importancias y
calificaciones están en las listas INTERNOS, EXTERNOS, EST, FZ, MPC y SEG. Requiere openpyxl.
openpyxl no calcula fórmulas: abrir el archivo en Excel para ver los totales.
"""
import sys
from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule

salida = sys.argv[1]
AZUL = "1F3A5F"
F_TIT = Font(bold=True, size=14, color=AZUL)
F_SUB = Font(italic=True, size=9, color="555555")
F_HDR = Font(bold=True, color="FFFFFF")
FILL_HDR = PatternFill("solid", fgColor=AZUL)
FILLS = {
    "F": PatternFill("solid", fgColor="E2F0D9"), "D": PatternFill("solid", fgColor="FBE4E4"),
    "O": PatternFill("solid", fgColor="DEEAF6"), "A": PatternFill("solid", fgColor="FDEBD3"),
    "T": PatternFill("solid", fgColor="EDEDED"), "IN": PatternFill("solid", fgColor="FFF9DB"),
}
LADO = Side(style="thin", color="999999")
BORDE = Border(left=LADO, right=LADO, top=LADO, bottom=LADO)
WRAP = Alignment(wrap_text=True, vertical="top")
CENT = Alignment(horizontal="center", vertical="center", wrap_text=True)


def titulo(ws, texto, sub, ancho):
    ws["A1"] = texto
    ws["A1"].font = F_TIT
    ws["A2"] = sub
    ws["A2"].font = F_SUB
    ws["A2"].alignment = WRAP
    ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=ancho)
    ws.row_dimensions[2].height = 45


def encabezado(ws, fila, textos):
    for j, t in enumerate(textos, 1):
        c = ws.cell(fila, j, t)
        c.font = F_HDR
        c.fill = FILL_HDR
        c.alignment = CENT
        c.border = BORDE


def celda(ws, f, c, v, fill=None, alin=WRAP, bold=False, fmt=None):
    x = ws.cell(f, c, v)
    x.alignment = alin
    x.border = BORDE
    if fill:
        x.fill = fill
    if bold:
        x.font = Font(bold=True)
    if fmt:
        x.number_format = fmt
    return x


def anchos(ws, lista):
    for i, w in enumerate(lista):
        ws.column_dimensions[chr(65 + i)].width = w


# ---------------------------------------------------------------- datos
INTERNOS = [
    ("F1", "F", "SGSI certificado en ISO/IEC 27001:2022, certificado ISMS-PE-101123 de A-Lign", "PUB-002", 5, 4, "Fortaleza mayor: el SGSI existe y está certificado; el riesgo de la renovación se trata en A1"),
    ("F2", "F", "Posicionamiento \"AI-native\" y alianzas de IA con Lovable y Gradial", "PUB-003, PUB-009, PUB-010", 4, 3, "Fortaleza menor: es un mandato declarado, todavía sin controles que lo respalden"),
    ("F3", "F", "Alianzas con Microsoft, Databricks y Snowflake", "PUB-005 a PUB-008", 3, 3, "Fortaleza menor: da acceso a plataformas y formación; no prueba uso en Colombia"),
    ("F4", "F", "Pruebas de seguridad continuas y análisis de dependencias en la cuenta analizada", "PRV-001", 3, 3, "Fortaleza menor: observada en una sola cuenta"),
    ("F5", "F", "Roles definidos, Scrum y ambientes separados en la cuenta analizada", "PRV-001", 2, 3, "Fortaleza menor: base para asignar responsabilidades"),
    ("F6", "F", "Formación en línea, patrocinio de certificaciones y capacitaciones obligatorias en la cuenta analizada", "PRV-001", 3, 3, "Fortaleza menor: mecanismo existente para el plan de certificaciones"),
    ("D1", "D", "Uso de IA sin sistema de gestión, sin inventario y sin permisos para agentes", "INT-001; PRV-001", 5, 1, "Debilidad mayor: contradice F2 y expone código y datos de clientes"),
    ("D2", "D", "Sin comité de TI, RACI, matriz de riesgos ni presupuesto de TI", "INT-001", 4, 1, "Debilidad mayor: nadie aprueba ni mide el plan"),
    ("D3", "D", "Transferencias internacionales de datos sin registro por proyecto; obligaciones tras la privatización sin concepto legal", "INT-001; PUB-004", 4, 1, "Debilidad mayor: exposición legal directa (Ley 1581)"),
    ("D4", "D", "Sin misión, visión, catálogo de servicios ni tablero de TI", "INT-001", 3, 2, "Debilidad menor: el propio PETI la corrige"),
    ("D5", "D", "Hallazgos de seguridad y horas se pasan a mano entre herramientas (cuenta analizada)", "PRV-001", 3, 2, "Debilidad menor: retrasa la corrección y genera errores de conciliación"),
    ("D6", "D", "Sin infraestructura como código ni control de costos de nube", "INT-001", 2, 2, "Debilidad menor: costo creciente, depende del cliente"),
    ("D7", "D", "Adopción de IA no medida y canal de licencias no estandarizado", "PRV-001; INT-001", 3, 2, "Debilidad menor: empuja al uso de herramientas no aprobadas"),
]
EXTERNOS = [
    ("O1", "O", "Clientes que piden IA gobernada y auditable", "INT-001; Softtek ISO/IEC 42001", 4, 2, "Respuesta media: no hay sistema de gestión de IA que mostrar"),
    ("O2", "O", "ISO/IEC 42001 y NIST AI RMF para ordenar y demostrar el gobierno de la IA", "ISO/IEC 42001:2023", 4, 1, "Respuesta deficiente: ninguno de los dos marcos está adoptado"),
    ("O3", "O", "Informe SOC 2 tipo II con controles de IA, que los clientes piden a sus proveedores", "AICPA", 4, 2, "Respuesta media: no hay evidencia pública del alcance de un informe SOC 2"),
    ("O4", "O", "Plataformas, formación y certificaciones de los socios", "PUB-005 a PUB-008", 3, 3, "Respuesta superior a la media: las alianzas existen y tienen programas de formación"),
    ("O5", "O", "Prácticas maduras de DevSecOps, infraestructura como código y observabilidad", "Matriz de tendencias del PETI (§6.3)", 3, 2, "Respuesta media: hay pruebas de seguridad, pero no IaC"),
    ("O6", "O", "COBIT 2019 como referencia para el gobierno y el presupuesto de TI", "ISACA", 2, 1, "Respuesta deficiente: no se usa"),
    ("A1", "A", "Vencimiento del certificado ISO sin evidencia pública de recertificación (fecha más temprana: 11 de octubre de 2026)", "PUB-002; R02", 5, 1, "Respuesta deficiente: la fecha más temprana ya pasó y no hay confirmación"),
    ("A2", "A", "Fuga de código o datos e inyección de instrucciones por herramientas de IA", "OWASP LLM Top 10 2025; R01, R05", 5, 1, "Respuesta deficiente: no hay permisos ni inventario"),
    ("A3", "A", "Sanción por incumplir la Ley 1581 y leyes de datos de la región", "SIC 2025; PUB-013, PUB-014; R04", 4, 2, "Respuesta media: falta el registro por proyecto"),
    ("A4", "A", "Competidores nearshore con gobierno de IA certificado (Softtek, ISO/IEC 42001)", "Softtek, 6 de noviembre de 2025", 4, 1, "Respuesta deficiente: Perficient no puede demostrar lo mismo"),
    ("A5", "A", "Vulnerabilidades heredadas de dependencias de código abierto", "Black Duck OSSRA 2026; R03", 3, 3, "Respuesta superior a la media: la cuenta analizada ya detecta (F4)"),
    ("A6", "A", "Rotación de personal hacia empleadores del exterior", "Deel / ENTER.CO 2026; R06", 4, 2, "Respuesta media: hay certificaciones, sin plan de retención"),
    ("A7", "A", "El cliente no autoriza cambios en su infraestructura; sobrecosto de nube", "PRV-001; R07, R08", 2, 2, "Respuesta media: se negocia cuenta por cuenta"),
]

wb = Workbook()

# ---------------------------------------------------------------- 0 Guía
g = wb.active
g.title = "0 Guía"
titulo(g, "Matrices de diagnóstico: DOFA y Porter — Perficient, operación en Colombia",
       "Trabajo académico de Gobierno y Servicios de TI (PETI 2026-2028). Equipo Firmes por la Gobernanza, 21 de octubre de 2026. "
       "Consolida las plantillas 'Matrices-Gerencia-Estrategica.xls' y 'Plantillas_Herramientas_Diagnostico.xlsx'. "
       "Las celdas amarillas son datos del equipo; las demás se calculan solas.", 4)
encabezado(g, 4, ["Hoja", "Qué hace", "De qué plantilla viene", "Qué se ajustó"])
filas = [
    ("1 DOFA", "Lista de factores con su evidencia", "Ambas (DAFO y 2a)", "Cada factor lleva ID de evidencia y peso de 1 a 5"),
    ("2 MEFI", "Matriz de evaluación de factores internos: peso × calificación", "Matriz EFI (.xls) y 2e MEFI (.xlsx)", "El peso se calcula a partir de la importancia 1-5, así la suma siempre da 1. Se usa la escala de David (1 = debilidad mayor, 2 = debilidad menor, 3 = fortaleza menor, 4 = fortaleza mayor); el .xls tenía invertidos el 1 y el 2"),
    ("3 MEFE", "Matriz de evaluación de factores externos", "Matriz EFE (.xls) y 2f MEFE (.xlsx)", "La calificación mide qué tan bien responde hoy la organización (1 deficiente a 4 superior), no la importancia del factor, que ya está en el peso"),
    ("4 DOFA cruzada", "Estrategias FO, DO, FA y DA con sus acciones y su puntaje", "2d Estrategias FODA (.xlsx) y material 'Estrategias FA FO DA DO'", "Nombres según el material de clase: FO atacar (maxi-maxi), DO movilizar (mini-maxi), FA defender (maxi-mini), DA reforzar o sobrevivir (mini-mini)"),
    ("5 Cinco fuerzas", "Intensidad de cada fuerza a partir de sus determinantes", "3b 5 Fuerzas (.xlsx)", "Las variables genéricas se reemplazaron por los determinantes con evidencia del diagnóstico de Porter del equipo"),
    ("6 Perfil competitivo", "Comparación con Globant y Softtek en los factores críticos de éxito", "Matriz de Perfil Competitivo (.xls) y 3a MPC (.xlsx)", "Escala de 1 a 4, igual que MEFI y MEFE. Las calificaciones de los competidores son valoración del equipo"),
    ("7 Seguimiento", "Control de la estrategia: actividad, indicador, meta, responsable y fechas", "Evaluación de la Estrategia y Plan de Mejoramiento (.xls); 7e Plan de actuación (.xlsx)", "Se usan los proyectos e indicadores del PETI Colombia"),
]
for i, f in enumerate(filas, 5):
    for j, v in enumerate(f, 1):
        celda(g, i, j, v)
r = 13
g.cell(r, 1, "Qué no se usó y por qué").font = Font(bold=True, color=AZUL)
no_usadas = [
    ("Matriz PEYEA (.xls)", "Pide solvencia, liquidez, flujo de caja y capital de trabajo. Perficient es privada desde octubre de 2024 y no publica estados financieros de la operación colombiana (PUB-001)."),
    ("Matriz cuantitativa de planificación estratégica (.xls)", "El orden de las 13 estrategias ya sale del puntaje de la hoja 4. Calificar 13 estrategias contra 26 factores sin datos agregaría números sin respaldo."),
    ("BCG, ADL, McKinsey, Ansoff (.xlsx)", "Requieren ventas y cuota de mercado por unidad de negocio, que no son públicas."),
    ("Misión, visión, valores, Canvas y cadena de valor (.xlsx)", "Corresponden a otras entregas del curso."),
]
for i, (a, b) in enumerate(no_usadas, r + 1):
    celda(g, i, 1, a, bold=True)
    celda(g, i, 2, b)
    g.merge_cells(start_row=i, start_column=2, end_row=i, end_column=4)
    g.row_dimensions[i].height = 32
r = r + len(no_usadas) + 2
g.cell(r, 1, "Convenciones").font = Font(bold=True, color=AZUL)
conv = [
    "PUB-, PRV- e INT- remiten al registro de evidencias del proyecto. PRV-001 es una cuenta de cliente analizada: describe esa cuenta, no una política de Perficient.",
    "R01 a R08, P1.1 a P4.3 y KPI-01 a KPI-14 remiten a los riesgos, proyectos e indicadores del PETI Colombia.",
    "Pesos, calificaciones e intensidades son valoraciones del equipo (INT-001) con la evidencia citada; no salen de una encuesta.",
]
for i, t in enumerate(conv, r + 1):
    celda(g, i, 1, t)
    g.merge_cells(start_row=i, start_column=1, end_row=i, end_column=4)
    g.row_dimensions[i].height = 30
anchos(g, [24, 48, 38, 60])
for i in range(5, 12):
    g.row_dimensions[i].height = 48

# ---------------------------------------------------------------- 1 DOFA
d = wb.create_sheet("1 DOFA")
titulo(d, "Matriz DOFA", "Factores de la DOFA final (8 de octubre de 2026), actualizados al 21 de octubre. Dentro de cada cuadrante, en orden de prioridad.", 4)
encabezado(d, 4, ["ID", "Factor", "Evidencia", "Importancia (1-5)"])
fila = 5
for grupo, nombre in (("F", "FORTALEZAS (internas, favorables)"), ("D", "DEBILIDADES (internas, desfavorables)"),
                      ("O", "OPORTUNIDADES (externas, favorables)"), ("A", "AMENAZAS (externas, desfavorables)")):
    c = d.cell(fila, 1, nombre)
    c.font = Font(bold=True)
    c.fill = FILLS[grupo]
    d.merge_cells(start_row=fila, start_column=1, end_row=fila, end_column=4)
    fila += 1
    for f in INTERNOS + EXTERNOS:
        if f[1] != grupo:
            continue
        celda(d, fila, 1, f[0], FILLS[grupo], CENT, True)
        celda(d, fila, 2, f[2])
        celda(d, fila, 3, f[3])
        celda(d, fila, 4, f[4], FILLS["IN"], CENT)
        fila += 1
anchos(d, [8, 80, 34, 16])


# ---------------------------------------------------------------- MEFI / MEFE
def matriz_ev(nombre, tit, sub, datos, escala, lectura_alta, lectura_baja):
    ws = wb.create_sheet(nombre)
    titulo(ws, tit, sub, 7)
    encabezado(ws, 4, ["ID", "Factor crítico", "Importancia (1-5)", "Peso", "Calificación (1-4)", "Ponderado", "Por qué esa calificación"])
    ini = 5
    n = len(datos)
    fin = ini + n - 1
    for i, f in enumerate(datos):
        r = ini + i
        celda(ws, r, 1, f[0], FILLS[f[1]], CENT, True)
        celda(ws, r, 2, f[2])
        celda(ws, r, 3, f[4], FILLS["IN"], CENT)
        celda(ws, r, 4, f"=C{r}/SUM($C${ini}:$C${fin})", None, CENT, fmt="0.000")
        celda(ws, r, 5, f[5], FILLS["IN"], CENT)
        celda(ws, r, 6, f"=D{r}*E{r}", None, CENT, fmt="0.000")
        celda(ws, r, 7, f[6])
    t = fin + 1
    celda(ws, t, 2, "TOTAL", FILLS["T"], bold=True)
    celda(ws, t, 4, f"=SUM(D{ini}:D{fin})", FILLS["T"], CENT, True, "0.00")
    celda(ws, t, 6, f"=SUM(F{ini}:F{fin})", FILLS["T"], CENT, True, "0.00")
    celda(ws, t + 1, 2, "Lectura del total", FILLS["T"], bold=True)
    c = celda(ws, t + 1, 3, f'=IF(F{t}>=2.5,"{lectura_alta}","{lectura_baja}")', None, WRAP)
    ws.merge_cells(start_row=t + 1, start_column=3, end_row=t + 1, end_column=7)
    ws.row_dimensions[t + 1].height = 34
    dv = DataValidation(type="whole", operator="between", formula1=1, formula2=4, showErrorMessage=True,
                        errorTitle="Calificación", error="Debe ser un entero entre 1 y 4")
    ws.add_data_validation(dv)
    dv.add(f"E{ini}:E{fin}")
    dv5 = DataValidation(type="whole", operator="between", formula1=1, formula2=5, showErrorMessage=True,
                         error="Debe ser un entero entre 1 y 5")
    ws.add_data_validation(dv5)
    dv5.add(f"C{ini}:C{fin}")
    e = t + 3
    ws.cell(e, 2, "Escala de calificación").font = Font(bold=True, color=AZUL)
    for i, (v, txt) in enumerate(escala):
        celda(ws, e + 1 + i, 2, txt)
        celda(ws, e + 1 + i, 3, v, None, CENT)
    celda(ws, e + 6, 2, "Promedio de referencia: 2,5. El total va de 1 (muy débil) a 4 (muy fuerte). Pesos = importancia / suma de importancias, por eso siempre suman 1.")
    ws.merge_cells(start_row=e + 6, start_column=2, end_row=e + 6, end_column=7)
    anchos(ws, [7, 62, 13, 9, 13, 11, 58])
    return ws, t


mefi, t_efi = matriz_ev("2 MEFI", "Matriz de evaluación de factores internos (MEFI)",
                        "Peso: qué tanto pesa el factor en el éxito de TI en la operación. Calificación: 1 debilidad mayor, 2 debilidad menor, 3 fortaleza menor, 4 fortaleza mayor.",
                        INTERNOS, [(4, "Fortaleza mayor"), (3, "Fortaleza menor"), (2, "Debilidad menor"), (1, "Debilidad mayor")],
                        "Posición interna por encima del promedio: las fortalezas compensan las debilidades.",
                        "Posición interna por debajo del promedio (2,5): las debilidades de gobierno, IA y datos pesan más que las fortalezas de seguridad y alianzas.")
mefe, t_efe = matriz_ev("3 MEFE", "Matriz de evaluación de factores externos (MEFE)",
                        "Peso: qué tanto pesa el factor del entorno en el éxito de TI. Calificación: qué tan bien responde hoy la operación (1 deficiente, 2 media, 3 superior a la media, 4 superior).",
                        EXTERNOS, [(4, "Respuesta superior"), (3, "Respuesta superior a la media"), (2, "Respuesta media"), (1, "Respuesta deficiente")],
                        "La operación responde por encima del promedio a su entorno.",
                        "La operación responde por debajo del promedio (2,5): no aprovecha las oportunidades de gobierno de IA y no está protegida frente a las amenazas más pesadas (A1, A2, A4).")

# ---------------------------------------------------------------- 4 DOFA cruzada
x = wb.create_sheet("4 DOFA cruzada")
titulo(x, "Matriz DOFA cruzada: estrategias FO, DO, FA y DA",
       "Puntaje = importancia promedio de los factores internos cruzados + importancia promedio de los externos (de 2 a 10). Se calcula desde la hoja 1 DOFA. El orden de ejecución sale del puntaje; en empate va primero la que tiene fecha externa o es requisito de otra.", 9)
encabezado(x, 4, ["ID", "Tipo", "Factores internos", "Factores externos", "Estrategia", "Acciones", "Proyecto y meta (PETI)", "Puntaje", "Orden"])
EST = [
    ("FO1", "FO atacar (maxi-maxi)", ["F1"], ["O2", "O3"], "Extender el SGSI certificado a un sistema de gestión de IA y mostrar sus controles en un informe SOC 2", "Reutilizar políticas y auditoría del SGSI; aprobar el manual de IA responsable; auditar internamente; incluir controles de IA en el SOC 2", "P1.2, P4.2, P4.1. Manual en el mes 6; informe sin salvedades en el mes 24 (KPI-08, KPI-13)", 4),
    ("FO2", "FO atacar (maxi-maxi)", ["F2"], ["O1"], "Crear un centro de excelencia de IA en Colombia y llevar casos de RAG y agentes a producción", "Aprobar la carta del centro; pruebas de concepto con clientes; producción solo con los controles de P1.2", "P1.8, P3.1, P3.3. 5 casos en producción en el mes 24 (KPI-03)", 7),
    ("FO3", "FO atacar (maxi-maxi)", ["F3", "F6"], ["O4"], "Plan de certificaciones por rol con los programas de los socios", "Currículo por rol; rutas de formación de los socios; seguimiento trimestral", "P1.7, P3.4. 70 % certificado en el mes 12 y 90 % en el 24 (KPI-09)", 9),
    ("FO4", "FO atacar (maxi-maxi)", ["F3"], ["O4"], "Construir la plataforma y el catálogo de datos sobre la tecnología de los socios", "Elegir plataforma de un socio; catálogo único; dueño por conjunto de datos", "P3.5. Plataforma en operación en el mes 18", 11),
    ("DO1", "DO movilizar (mini-maxi)", ["D1"], ["O2"], "Levantar el inventario de IA según ISO/IEC 42001", "Levantamiento por célula; responsable por sistema; evaluación automática de modelos", "P1.3, P3.2. 90 % inventariado en el año 1 (KPI-08)", 3),
    ("DO2", "DO movilizar (mini-maxi)", ["D2", "D4"], ["O6"], "Formalizar comités, RACI, presupuesto y estrategia de TI con COBIT 2019", "Comité Directivo con acta; RACI y matriz de riesgos; guía de presupuesto (APO06); balance en la fase 4", "P2.8, P4.3. 90 % de sesiones con acta (KPI-14)", 12),
    ("DO3", "DO movilizar (mini-maxi)", ["D5", "D6"], ["O5"], "Automatizar la conciliación, estandarizar la observabilidad, usar IaC y controlar el costo de nube", "Conciliación automática; objetivos de servicio; IaC con acuerdo del cliente; tablero de costos", "P2.4 a P2.7. 95 % conciliado, 100 % IaC, −15 % costo de nube (KPI-06, KPI-11, KPI-02)", 13),
    ("FA1", "FA defender (maxi-mini)", ["F1"], ["A1"], "Confirmar el estado del certificado ISO/IEC 27001 y cerrar la recertificación", "Pedir a A-Lign confirmación escrita; programar auditoría si no está renovado; avisar a clientes regulados", "P1.1. Certificado vigente, 0 no conformidades mayores (KPI-07)", 1),
    ("FA2", "FA defender (maxi-mini)", ["F4"], ["A5"], "Integrar las pruebas de seguridad al pipeline de CI/CD", "Hallazgos automáticos a la ALM; bloquear dependencias críticas; medir remediación", "P2.2, P2.3. Críticas en < 72 h (mes 12) y < 24 h (mes 24) (KPI-05)", 10),
    ("FA3", "FA defender (maxi-mini)", ["F6"], ["A6"], "Retener talento con certificaciones visibles y conservar el conocimiento", "Plan de certificaciones como ruta de carrera; plantillas ALM homologadas; rotación entre células", "P1.7, P2.1. Rotación planificada 100 % al mes 24 (KPI-10)", 8),
    ("DA1", "DA reforzar/sobrevivir (mini-mini)", ["D1"], ["A2"], "Permisos como código para los agentes y capacitación del personal en IA y datos", "Limitar y registrar acciones de agentes; capacitar a todo el personal; solo herramientas aprobadas", "P1.4, P1.5. 100 % capacitado en el mes 8", 2),
    ("DA2", "DA reforzar/sobrevivir (mini-mini)", ["D3"], ["A3"], "Concepto legal y registro de transferencias internacionales por proyecto", "Concepto de Legal (Ley 1581 y obligaciones tras la privatización); registro por proyecto", "P1.9. Concepto emitido en el mes 3", 5),
    ("DA3", "DA reforzar/sobrevivir (mini-mini)", ["D7"], ["A2"], "Procedimiento único para pedir y aprobar licencias de IA", "Publicar el procedimiento; medir células con IA y licencia", "P1.6. Publicado en el mes 3; 85 % de células en el mes 12 (KPI-04)", 6),
]
# mapa ID -> celda de importancia en la hoja 1 DOFA
mapa = {}
for row in d.iter_rows(min_row=5):
    if row[0].value and isinstance(row[0].value, str) and len(row[0].value) == 2:
        mapa[row[0].value] = f"'1 DOFA'!D{row[0].row}"
tipo_fill = {"FO": FILLS["O"], "DO": FILLS["D"], "FA": FILLS["F"], "DA": FILLS["A"]}
for i, e in enumerate(EST):
    r = 5 + i
    celda(x, r, 1, e[0], tipo_fill[e[0][:2]], CENT, True)
    celda(x, r, 2, e[1], tipo_fill[e[0][:2]])
    celda(x, r, 3, " + ".join(e[2]), None, CENT)
    celda(x, r, 4, " + ".join(e[3]), None, CENT)
    celda(x, r, 5, e[4])
    celda(x, r, 6, e[5])
    celda(x, r, 7, e[6])
    prom_i = "AVERAGE(" + ",".join(mapa[k] for k in e[2]) + ")"
    prom_e = "AVERAGE(" + ",".join(mapa[k] for k in e[3]) + ")"
    celda(x, r, 8, f"={prom_i}+{prom_e}", FILLS["T"], CENT, True, "0.0")
    celda(x, r, 9, e[7], FILLS["IN"], CENT)
    x.row_dimensions[r].height = 62
x.conditional_formatting.add("H5:H17", CellIsRule(operator="greaterThanOrEqual", formula=["9"], fill=PatternFill("solid", fgColor="F4B183")))
anchos(x, [7, 20, 11, 11, 40, 48, 40, 9, 8])
r = 19
x.cell(r, 1, "Cómo leer los cuatro tipos (material de clase)").font = Font(bold=True, color=AZUL)
lect = [
    ("FO atacar (maxi-maxi)", "Usar las fortalezas para aprovechar las oportunidades. Es la posición que toda organización quisiera tener."),
    ("DO movilizar (mini-maxi)", "Superar las debilidades aprovechando las oportunidades: el entorno ofrece algo que la organización todavía no puede explotar."),
    ("FA defender (maxi-mini)", "Usar las fortalezas para evitar o reducir el efecto de las amenazas, con cuidado y discreción."),
    ("DA reforzar o sobrevivir (mini-mini)", "Reducir las debilidades y evitar las amenazas. Una organización con muchas estrategias aquí está en situación precaria."),
]
for i, (a, b) in enumerate(lect, r + 1):
    celda(x, i, 1, a, bold=True)
    x.merge_cells(start_row=i, start_column=1, end_row=i, end_column=2)
    celda(x, i, 3, b)
    x.merge_cells(start_row=i, start_column=3, end_row=i, end_column=7)
    x.row_dimensions[i].height = 30

# ---------------------------------------------------------------- 5 Cinco fuerzas
p = wb.create_sheet("5 Cinco fuerzas")
titulo(p, "Cinco fuerzas de Porter: intensidad por determinantes",
       "Industria: servicios de ingeniería de software, datos e IA prestados desde Colombia a clientes de Norteamérica (nearshore). Cada determinante se califica de 1 (casi no presiona) a 5 (presiona mucho) sobre la capacidad de sostener precios y márgenes. La intensidad de la fuerza es el promedio.", 6)
encabezado(p, 4, ["Fuerza", "Determinante", "Evidencia", "Presión (1-5)", "Intensidad de la fuerza", "Lectura"])
FZ = [
    ("Rivalidad entre competidores", [
        ("Número y tamaño de los rivales (Accenture, EPAM, Globant, Endava, Infosys, Cognizant…)", "10-K 2023 de Perficient", 5),
        ("Rivales con escala en Colombia: Globant con más de 6.000 empleados; Softtek con centro en Bogotá", "Forbes Colombia 2024; Softtek 2021", 5),
        ("Diferenciación de rivales en gobierno de IA (Softtek ISO/IEC 42001)", "Softtek, noviembre de 2025", 4),
        ("Mercado local que crece pero se reparte entre 6.805 empresas", "Fedesoft / Portafolio 2025", 3),
        ("Precios contratados a la baja", "ISG, octubre de 2025", 5)]),
    ("Poder de los compradores", [
        ("Grandes empresas de EE. UU. con compras profesionales (cerca del 96 % de ingresos en 2023)", "10-K 2023", 4),
        ("Concentración: el cliente más grande, cerca del 7 % de ingresos", "10-K 2023", 2),
        ("Presión para trasladar al precio el ahorro de la IA", "ISG 2025", 5),
        ("Exigencia de controles demostrables (SOC 2, certificaciones) y control de la infraestructura", "AICPA; PRV-001", 5),
        ("Costo de cambio alto dentro del contrato (92 % de ingresos de clientes recurrentes)", "10-K 2023", 2)]),
    ("Poder de los proveedores", [
        ("Talento técnico disputado por empleadores del exterior (+49 % en 2025) y alza del salario mínimo 2026", "Deel / ENTER.CO; Portafolio 2026", 5),
        ("Nube concentrada: tres proveedores con el 63 % del gasto mundial", "Synergy Research 2025", 4),
        ("Socios tecnológicos que exigen personal certificado", "10-K 2023; PUB-005 a PUB-008", 4),
        ("Modelos de IA: tres proveedores con cerca del 77 % del uso empresarial", "Menlo Ventures 2025", 3)]),
    ("Amenaza de sustitutos", [
        ("Centros de capacidad propios de los clientes (GCC)", "Everest Group 2026", 4),
        ("Contratación directa de ingenieros colombianos", "Deel / ENTER.CO 2026", 4),
        ("Herramientas de IA que reducen horas compradas (magnitud no medida)", "ISG 2025", 3),
        ("Costo y dificultad de montar un centro propio", "Everest Group 2026", 2)]),
    ("Amenaza de nuevos entrantes", [
        ("Barreras formales bajas", "10-K 2023", 4),
        ("Llegada de inversión extranjera en software (11 % de 178 proyectos en 2025)", "ProColombia / Valora Analitik", 4),
        ("Exigencias del cliente regulado: certificaciones, informes y niveles de socio", "AICPA; PUB-002; PUB-005 a PUB-008", 2),
        ("Relación con clientes actuales (92 % recurrentes)", "10-K 2023", 2)]),
]
r = 5
resumen = []
for fuerza, dets in FZ:
    ini = r
    for det, ev, v in dets:
        celda(p, r, 2, det)
        celda(p, r, 3, ev)
        celda(p, r, 4, v, FILLS["IN"], CENT)
        p.row_dimensions[r].height = 30
        r += 1
    fin = r - 1
    p.merge_cells(start_row=ini, start_column=1, end_row=fin, end_column=1)
    celda(p, ini, 1, fuerza, FILLS["T"], CENT, True)
    p.merge_cells(start_row=ini, start_column=5, end_row=fin, end_column=5)
    celda(p, ini, 5, f"=AVERAGE(D{ini}:D{fin})", FILLS["T"], CENT, True, "0.0")
    p.merge_cells(start_row=ini, start_column=6, end_row=fin, end_column=6)
    celda(p, ini, 6, f'=IF(E{ini}>=4.2,"Muy alta",IF(E{ini}>=3.4,"Alta",IF(E{ini}>=2.6,"Media",IF(E{ini}>=1.8,"Baja","Muy baja"))))', None, CENT, True)
    resumen.append((fuerza, ini))
dv = DataValidation(type="whole", operator="between", formula1=1, formula2=5, showErrorMessage=True, error="Entero entre 1 y 5")
p.add_data_validation(dv)
dv.add(f"D5:D{r-1}")
r += 1
p.cell(r, 1, "Resumen").font = Font(bold=True, color=AZUL)
encabezado(p, r + 1, ["Fuerza", "Intensidad", "Nivel", "Cómo le llega al área de TI", "", ""])
llega = {
    "Rivalidad entre competidores": "Indirectamente: los rivales compiten con credenciales que TI tiene que producir",
    "Poder de los compradores": "Directamente: el cliente exige controles, es dueño de la infraestructura y pide el ahorro de la IA en el precio. Es el mayor desafío para TI",
    "Poder de los proveedores": "En el talento, y en parte en las plataformas de nube y de IA",
    "Amenaza de sustitutos": "En las herramientas de IA que reemplazan horas de trabajo",
    "Amenaza de nuevos entrantes": "Poco: la barrera son las certificaciones que TI mantiene",
}
for i, (fz, ini) in enumerate(resumen, r + 2):
    celda(p, i, 1, fz, bold=True)
    celda(p, i, 2, f"=E{ini}", None, CENT, fmt="0.0")
    celda(p, i, 3, f"=F{ini}", None, CENT)
    celda(p, i, 4, llega[fz])
    p.merge_cells(start_row=i, start_column=4, end_row=i, end_column=6)
    p.row_dimensions[i].height = 30
celda(p, r + 8, 1, "Escala de intensidad: 4,2 a 5 muy alta; 3,4 a 4,19 alta; 2,6 a 3,39 media; 1,8 a 2,59 baja; menos de 1,8 muy baja.")
p.merge_cells(start_row=r + 8, start_column=1, end_row=r + 8, end_column=6)
anchos(p, [26, 62, 34, 12, 14, 30])

# ---------------------------------------------------------------- 6 Perfil competitivo
m = wb.create_sheet("6 Perfil competitivo")
titulo(m, "Matriz de perfil competitivo (MPC)",
       "Factores críticos de éxito que salen del diagnóstico de Porter. Calificación de 1 (debilidad mayor) a 4 (fortaleza mayor). Las calificaciones de Globant y Softtek son valoración del equipo con la evidencia pública indicada; lo que no se pudo comprobar se marca.", 9)
encabezado(m, 4, ["Factor crítico de éxito", "Peso", "Perficient Col.", "Pond.", "Globant", "Pond.", "Softtek", "Pond.", "Evidencia y supuestos"])
MPC = [
    ("Certificación de seguridad vigente (ISO/IEC 27001)", 0.20, 3, 3, 3, "Perficient: certificado publicado (PUB-002), renovación sin confirmar. Competidores: [EVIDENCIA: confirmar certificados vigentes]; se asume promedio"),
    ("Gobierno de IA certificado (ISO/IEC 42001)", 0.20, 1, 2, 4, "Softtek certificada en noviembre de 2025. Perficient sin sistema de gestión de IA (D1). Globant: [EVIDENCIA: no revisada]"),
    ("Escala de talento en Colombia", 0.15, 3, 4, 3, "Globant más de 6.000 empleados en Colombia (2024). Perficient: PSL, Talos y Overactive (PUB-016 a PUB-018), sin cifra actual. Softtek: centro en Bogotá (2021)"),
    ("Alianzas con plataformas de nube, datos e IA", 0.15, 4, 3, 3, "Perficient: Microsoft, Databricks, Snowflake, AWS, Gradial, Lovable (PUB-005 a PUB-010, PUB-021). Competidores: [EVIDENCIA: no revisada]"),
    ("Entrega medible (pipelines, conciliación, costos)", 0.15, 2, 3, 3, "Perficient: flujos manuales en la cuenta analizada (D5, D6). Competidores: supuesto del equipo"),
    ("Retención y certificación del talento", 0.15, 3, 3, 3, "Perficient: patrocinio de certificaciones (F6). Todos compiten por el mismo talento (A6)"),
]
for i, f in enumerate(MPC):
    r = 5 + i
    celda(m, r, 1, f[0])
    celda(m, r, 2, f[1], FILLS["IN"], CENT, fmt="0.00")
    for k, col in enumerate((3, 5, 7)):
        L = chr(64 + col)
        celda(m, r, col, f[2 + k], FILLS["IN"], CENT)
        celda(m, r, col + 1, f"=$B{r}*{L}{r}", None, CENT, fmt="0.00")
    celda(m, r, 9, f[5])
    m.row_dimensions[r].height = 45
t = 5 + len(MPC)
celda(m, t, 1, "TOTAL", FILLS["T"], bold=True)
celda(m, t, 2, f"=SUM(B5:B{t-1})", FILLS["T"], CENT, True, "0.00")
for col in (4, 6, 8):
    L = chr(64 + col)
    celda(m, t, col, f"=SUM({L}5:{L}{t-1})", FILLS["T"], CENT, True, "0.00")
celda(m, t + 2, 1, "Lectura: Perficient compite en escala y alianzas, pero queda detrás de Softtek en el factor que hoy diferencia ante el cliente regulado (gobierno de IA certificado). Ese factor depende de TI (P1.2, P1.3, P4.2).")
m.merge_cells(start_row=t + 2, start_column=1, end_row=t + 2, end_column=9)
m.row_dimensions[t + 2].height = 32
dv = DataValidation(type="whole", operator="between", formula1=1, formula2=4, showErrorMessage=True, error="Entero entre 1 y 4")
m.add_data_validation(dv)
dv.add(f"C5:C{t-1}")
dv.add(f"E5:E{t-1}")
dv.add(f"G5:G{t-1}")
anchos(m, [38, 8, 13, 8, 10, 8, 10, 8, 70])

# ---------------------------------------------------------------- 7 Seguimiento
s = wb.create_sheet("7 Seguimiento")
titulo(s, "Control y seguimiento de la estrategia",
       "Une la hoja 'Evaluación de la Estrategia' y el 'Plan de Mejoramiento' del .xls con el plan de actuación del .xlsx. Una fila por estrategia, en orden de ejecución. Todo es propuesto y depende del Comité Directivo del PETI. Mes 1 = octubre de 2026.", 9)
encabezado(s, 4, ["Orden", "Estrategia", "Hallazgo que la origina", "Actividad estratégica", "Indicador", "Meta", "Responsable propuesto", "Inicio (mes)", "Fin (mes)"])
SEG = [
    (1, "FA1", "A1 + F1: certificado sin renovación confirmada", "Recertificación de ISO/IEC 27001:2022 (P1.1)", "KPI-07 No conformidades mayores", "0", "CISO", 0, 5),
    (2, "DA1", "D1 + A2: IA sin permisos ni capacitación", "Permisos como código para agentes (P1.4) y capacitación (P1.5)", "% del personal capacitado", "100 % en el mes 8", "DevSecOps; Talento humano con CISO", 1, 8),
    (3, "DO1", "D1 + O2: no hay inventario de IA", "Inventario de sistemas de IA (P1.3)", "KPI-08 Cobertura del inventario", "90 % año 1; 100 % año 2", "Arquitectura", 1, 4),
    (4, "FO1", "F1 + O2 + O3: SGSI listo para extender", "Sistema de gestión de IA (P1.2) e informe SOC 2 (P4.1)", "KPI-13 Informe SOC 2 sin salvedades", "Sí, mes 24", "CISO, con CTO", 1, 24),
    (5, "DA2", "D3 + A3: transferencias sin registro", "Concepto legal y registro de obligaciones (P1.9)", "Concepto emitido", "Mes 3", "CTO, con Legal", 1, 3),
    (6, "DA3", "D7 + A2: licencias de IA sin canal", "Procedimiento de licencias de IA (P1.6)", "KPI-04 Adopción de IA", "85 % mes 12; 95 % mes 24", "PM y Line Manager, con CTO", 1, 3),
    (7, "FO2", "F2 + O1: mandato AI-native sin casos", "Centro de excelencia (P1.8); RAG y agente en producción (P3.1, P3.3)", "KPI-03 Casos de IA en producción", "5 al mes 24", "CTO; CoE de IA", 3, 18),
    (8, "FA3", "F6 + A6: rotación hacia el exterior", "Plan de certificaciones (P1.7) y plantillas ALM (P2.1)", "KPI-10 Rotación entre células", "100 % al mes 24", "Talento humano; Technical Leads", 1, 10),
    (9, "FO3", "F3 + F6 + O4: formación de socios", "Plan y cierre de certificaciones (P1.7, P3.4)", "KPI-09 Personal certificado", "70 % mes 12; 90 % mes 24", "Talento humano", 1, 18),
    (10, "FA2", "F4 + A5: dependencias vulnerables", "Pruebas de seguridad en la ALM y CI/CD (P2.2, P2.3)", "KPI-05 Remediación de críticas", "< 72 h mes 12; < 24 h mes 24", "DevSecOps", 8, 12),
    (11, "FO4", "F3 + O4: sin plataforma de datos", "Plataforma y catálogo de datos (P3.5)", "Plataforma en operación", "Mes 18", "Arquitectura de datos", 13, 18),
    (12, "DO2", "D2 + D4 + O6: sin gobierno formal", "Gobierno y estrategia de TI (P2.8); balance (P4.3)", "KPI-14 Sesiones con acta", "90 %", "CTO", 7, 24),
    (13, "DO3", "D5 + D6 + O5: flujos manuales y nube sin control", "Conciliación, observabilidad, IaC y costos (P2.4 a P2.7)", "KPI-06, KPI-11, KPI-02", "95 %; 100 %; −15 %", "Operaciones; SRE; Arquitectura de nube; FinOps", 7, 12),
]
for i, f in enumerate(SEG):
    r = 5 + i
    for j, v in enumerate(f, 1):
        celda(s, r, j, v, tipo_fill[f[1][:2]] if j == 2 else None, CENT if j in (1, 2, 8, 9) else WRAP, j == 2)
    s.row_dimensions[r].height = 34
anchos(s, [7, 9, 34, 42, 28, 22, 26, 10, 9])

for ws in wb.worksheets:
    ws.sheet_view.showGridLines = False
    ws.freeze_panes = "A5"
wb.save(salida)
print("ok", salida)
