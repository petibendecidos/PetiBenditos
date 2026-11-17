"""Genera el modelo de datos en estrella (Excel) y el CSV de control al corte del mes 12
para el dashboard de gobierno de datos, IA y TI (ISO/IEC 38500:2024) en Power BI.

Uso:
    python scripts/powerbi_iso38500_datos.py <carpeta_sinteticos> <carpeta_salida>

Solo usa biblioteca estándar y openpyxl (sin pandas ni numpy). Semilla fija 38500.
"""
from __future__ import annotations

import argparse
import csv
import random
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

import openpyxl
from openpyxl.styles import Font

SCRIPTS_DIR = Path(__file__).resolve().parent
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from dashboard_construir import COSTO_NUBE, INICIO, PORTAFOLIO  # noqa: E402


MESES_ES = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"]

TILDES_CSV = {
    "Si": "Sí",
    "Critica": "Crítica",
}

LINEAS_SERVICIO = {
    "C01": "Desarrollo de software",
    "C02": "Desarrollo de software",
    "C03": "Desarrollo de software",
    "C04": "Datos e IA",
    "C05": "Datos e IA",
    "C06": "Datos e IA",
    "C07": "Nube y DevOps",
    "C08": "Nube y DevOps",
    "C09": "Nube y DevOps",
    "C10": "Calidad y pruebas",
    "C11": "Calidad y pruebas",
    "C12": "Calidad y pruebas",
    "OPE": "Toda la operación",
}

PRINCIPIOS = [
    ("5.2", 1, "Propósito", "Purpose", "Definir la necesidad del gobierno de TI como parte de los requisitos de la organización"),
    ("5.3", 2, "Generación de valor", "Value generation", "Objetivos de valor de la TI en sincronía con los de la organización"),
    ("5.4", 3, "Estrategia", "Strategy", "Dirigir y comprometerse con la estrategia para cumplir los objetivos de negocio"),
    ("5.5", 4, "Supervisión", "Oversight", "Revisar el desempeño de la TI frente a las expectativas, el comportamiento ético y el cumplimiento"),
    ("5.6", 5, "Rendición de cuentas", "Accountability", "Demostrar la rendición de cuentas de la organización y exigirla a quien recibe delegación"),
    ("5.7", 6, "Participación de las partes interesadas", "Stakeholder engagement", "Cumplir el compromiso esperado con las partes interesadas"),
    ("5.8", 7, "Liderazgo", "Leadership", "Liderazgo ético y eficaz del gobierno de TI"),
    ("5.9", 8, "Datos y decisiones", "Data and decisions", "Reconocer los datos como activo para decidir"),
    ("5.10", 9, "Gobierno del riesgo", "Risk governance", "Considerar el efecto de la incertidumbre en el propósito y los resultados"),
    ("5.11", 10, "Responsabilidad social", "Social responsibility", "Decisiones transparentes y alineadas con las expectativas de la sociedad"),
    ("5.12", 11, "Viabilidad y desempeño en el tiempo", "Viability and performance over time", "Que la organización siga siendo viable sin comprometer sus compromisos actuales y futuros"),
]

TAREAS = [
    (1, "Involucrar a las partes interesadas", "6.2.1"),
    (2, "Evaluar", "6.2.2"),
    (3, "Dirigir", "6.2.3"),
    (4, "Monitorear", "6.2.4"),
]

PROYECTOS_META = {
    "P1.1": ("Recertificación de ISO/IEC 27001:2022", 1, "OETI02", "BRE-006", "KPI-07", "CISO"),
    "P1.2": ("Sistema de gestión de IA", 1, "OETI01", "BRE-001", "KPI-08", "CISO, con CTO"),
    "P1.3": ("Inventario de sistemas de IA", 1, "OETI01", "BRE-002", "KPI-08", "Arquitectura"),
    "P1.4": ("Permisos como código para agentes de IA", 1, "OETI01", "BRE-008", "KPI-08", "DevSecOps"),
    "P1.5": ("Capacitación en seguridad, IA y protección de datos", 1, "OETI04", "BRE-009", "KPI-09", "Talento humano, con CISO"),
    "P1.6": ("Procedimiento de licencias de IA", 1, "OETI01", "BRE-005", "KPI-04", "PM y Line Manager, con CTO"),
    "P1.7": ("Plan de certificaciones por rol", 1, "OETI04", "BRE-009", "KPI-09", "Talento humano, con CTO"),
    "P1.8": ("Centro de excelencia de IA en Colombia", 1, "OETI01", "BRE-001, BRE-005", "KPI-04", "CTO"),
    "P1.9": ("Concepto legal y registro de obligaciones (Ley 1581, SOX residual)", 1, "OETI02", "BRE-016", "KPI-14", "CTO, con Legal"),
    "P2.1": ("Plantillas ALM homologadas", 2, "OETI03", "BRE-004", "KPI-01", "Technical Leads"),
    "P2.2": ("Integración de pruebas de seguridad con la ALM", 2, "OETI02", "BRE-003", "KPI-05", "DevSecOps"),
    "P2.3": ("Pipeline de CI/CD estandarizado", 2, "OETI02", "BRE-003, BRE-007", "KPI-05", "DevSecOps"),
    "P2.4": ("Conciliación de tiempos con la ALM", 2, "OETI03", "BRE-012", "KPI-06", "Operaciones"),
    "P2.5": ("Observabilidad estandarizada", 2, "OETI03", "BRE-013", "KPI-01", "SRE"),
    "P2.6": ("Infraestructura como código", 2, "OETI03", "BRE-007", "KPI-11", "Arquitectura de nube"),
    "P2.7": ("Tablero de costos de nube", 2, "OETI03", "BRE-013", "KPI-02", "FinOps"),
    "P2.8": ("Formalización del gobierno y la estrategia de TI", 2, "OETI03", "BRE-011, BRE-015", "KPI-14", "CTO"),
    "P3.1": ("RAG en producción para clientes", 3, "OETI01", "BRE-001", "KPI-03", "CoE de IA"),
    "P3.2": ("Evaluación automática de modelos de lenguaje", 3, "OETI01", "BRE-002", "KPI-08", "CoE de IA"),
    "P3.3": ("Agente conversacional en producción", 3, "OETI01", "BRE-008", "KPI-03", "CoE de IA y PM"),
    "P3.4": ("Cierre del plan de certificaciones", 3, "OETI04", "BRE-009", "KPI-09", "Talento humano"),
    "P3.5": ("Plataforma y catálogo de datos", 3, "OETI03", "BRE-010", "KPI-01", "Arquitectura de datos"),
    "P4.1": ("Informe SOC 2 tipo II con controles de IA", 4, "OETI02", "BRE-014", "KPI-13", "CISO"),
    "P4.2": ("Auditoría interna del sistema de gestión de IA", 4, "OETI01", "BRE-001", "KPI-08", "CISO y CoE de IA"),
    "P4.3": ("Balance del PETI y arquitectura 2028-2030", 4, "OETI03", "BRE-015", "KPI-01", "CTO"),
}

INDICADORES_DEF = [
    ("KPI-01", "Ejecución acumulada del PETI", "TI", "PETI §10", "OETI03", "METI07", "5.5", 4, "Desempeño",
     "Proyectos terminados / 25 × 100", "%", "mayor", 100, "0 %", 55, 95, "Trimestral", "CTO", "Operación",
     "Todo el portafolio", "Portafolio simulado de proyectos del PETI (meses 1 a 12)"),
    ("KPI-02", "Variación del costo de nube", "TI", "PETI §10", "OETI03", "METI11", "5.3", 2, "Desempeño",
     "(Costo del periodo − costo base) / costo base × 100", "%", "mayor", 100, "Por medir (P2.7)", -5, -15,
     "Trimestral", "FinOps", "Operación", "P2.7", "Serie simulada de costo de nube desde P2.7 (base promedio meses 7 a 9)"),
    ("KPI-03", "Casos de IA en producción", "IA", "PETI §10", "OETI01", "METI03", "5.3", 2, "Capacidad",
     "Número de casos con métricas", "número", "mayor", 1, "0", 1, 5, "Semestral", "CoE de IA", "Operación",
     "P3.1, P3.3", "Registro semestral simulado; P3.1 y P3.3 inician en el mes 13"),
    ("KPI-04", "Adopción de IA en células", "IA", "PETI §10", "OETI01", "METI02", "5.4", 3, "Capacidad",
     "Células con IA activa y licencia / total de células × 100", "%", "mayor", 100, "Por medir (mes 3)", 85, 95,
     "Mensual", "CoE de IA", "Célula", "P1.6, P1.8", "Reporte mensual sintético por célula (línea base en mes 3)"),
    ("KPI-05", "Remediación de vulnerabilidades críticas (h)", "TI", "PETI §10", "OETI02", "METI06", "5.10", 4, "Desempeño",
     "Promedio de horas entre detección y cierre", "h", "menor", 1, "Por medir (mes 3)", 72, 24,
     "Mensual", "DevSecOps", "Célula", "P2.2, P2.3", "sintetico_vulnerabilidades.csv (severidad Crítica, meses 3 a 12)"),
    ("KPI-06", "Conciliación de horas y tareas", "TI", "PETI §10", "OETI03", "METI09", "5.9", 4, "Desempeño",
     "Horas conciliadas / horas registradas × 100", "%", "mayor", 100, "Por medir (mes 6)", 90, 95,
     "Mensual", "Operaciones", "Operación", "P2.4", "Serie mensual simulada desde línea base en el mes 6"),
    ("KPI-07", "No conformidades mayores ISO/IEC 27001", "TI", "PETI §10", "OETI02", "METI04", "5.12", 4, "Rendición de cuentas",
     "Número por auditoría", "número", "menor", 1, "Último informe", 0, 0, "Anual", "CISO", "Operación",
     "P1.1", "Supone auditoría de recertificación en el mes 5 sin evidencia pública (PUB-002)"),
    ("KPI-08", "Cobertura del inventario de IA", "IA", "PETI §10", "OETI01", "METI01", "5.10", 2, "Política",
     "Sistemas registrados / identificados × 100", "%", "mayor", 100, "0 %", 90, 100,
     "Trimestral", "Arquitectura", "Célula", "P1.3", "Calculado desde fact_sistema_ia (registro trimestral)"),
    ("KPI-09", "Personal técnico certificado", "TI", "PETI §10", "OETI04", "METI12", "5.4", 3, "Capacidad",
     "Personal con más de 6 meses y al menos una certificación / ese personal × 100", "%", "mayor", 100,
     "Por medir (mes 3)", 70, 90, "Trimestral", "Talento humano", "Célula", "P1.7",
     "sintetico_personas.csv al mes 12; trimestres previos simulados de forma irregular"),
    ("KPI-10", "Rotación entre células", "TI", "PETI §10", "OETI04", "METI13", "5.10", 3, "Capacidad",
     "Personas rotadas / total × 100", "%", "mayor", 100, "Por medir (mes 6)", 50, 100,
     "Semestral", "Line Managers", "Célula", "P2.1 (R06)", "sintetico_personas.csv al mes 12 y corte semestral en mes 6"),
    ("KPI-11", "Ambientes con infraestructura como código", "TI", "PETI §10", "OETI03", "METI10", "5.12", 3, "Capacidad",
     "Ambientes con IaC / ambientes administrados × 100", "%", "mayor", 100, "0 %", 60, 100,
     "Trimestral", "Arquitectura de nube", "Operación", "P2.6", "Conteo trimestral simulado sobre 48 ambientes administrados"),
    ("KPI-13", "Informe SOC 2 sin salvedades", "TI", "PETI §10", "OETI02", "METI05", "5.7", 1, "Rendición de cuentas",
     "Informe emitido sin salvedades (sí o no)", "sí/no", "mayor", 1, "Por confirmar (P1.1)", None, 1,
     "Anual", "CISO", "Operación", "P4.1", "Sin meta en año 1; P4.1 inicia en el mes 13"),
    ("KPI-14", "Sesiones de comité con acta", "TI", "PETI §10", "OETI03", "METI08", "5.6", 4, "Rendición de cuentas",
     "Sesiones con acta / programadas × 100", "%", "mayor", 100, "0 %", 90, 90,
     "Trimestral", "CTO", "Operación", "P2.8", "Registro trimestral simulado de actas del Comité Directivo"),
    ("DAT-01", "Solicitudes de titulares respondidas en plazo", "Datos", "Complementario", "—", "—", "5.11", 1, "Rendición de cuentas",
     "Solicitudes respondidas dentro del plazo / solicitudes recibidas × 100", "%", "mayor", 100, "Por medir", 95, 98,
     "Mensual", "Legal con CISO", "Operación", "P1.9",
     "Calculado desde fact_solicitud_titular; plazos 10 y 15 días hábiles son supuesto pendiente en Ley 1581 (INT-001)"),
    ("DAT-02", "Activos de datos clasificados", "Datos", "Complementario", "—", "—", "5.9", 3, "Política",
     "Activos clasificados / activos inventariados × 100", "%", "mayor", 100, "0 %", 60, 90,
     "Trimestral", "Arquitectura de datos", "Operación", "P3.5", "Serie trimestral simulada (supuesto INT-001)"),
    ("DAT-03", "Proyectos con transferencias internacionales registradas", "Datos", "Complementario", "—", "—", "5.11", 4, "Rendición de cuentas",
     "Proyectos con transferencia registrada / proyectos que tratan datos personales × 100", "%", "mayor", 100, "0 %", 80, 100,
     "Trimestral", "CTO con Legal", "Operación", "P1.9", "Serie trimestral simulada tras cierre de P1.9 (supuesto INT-001)"),
    ("IA-01", "Sistemas de IA con evaluación de riesgo", "IA", "Complementario", "—", "—", "5.10", 2, "Política",
     "Sistemas registrados con evaluación de riesgo / sistemas registrados × 100", "%", "mayor", 100, "0 %", 80, 100,
     "Trimestral", "CISO", "Célula", "P1.2", "Calculado desde fact_sistema_ia (supuesto INT-001)"),
    ("IA-02", "Sistemas de IA con supervisión humana definida", "IA", "Complementario", "—", "—", "5.6", 3, "Delegación",
     "Sistemas registrados con responsable de supervisión humana / sistemas registrados × 100", "%", "mayor", 100, "0 %", 90, 100,
     "Trimestral", "CoE de IA", "Célula", "P1.2, P1.4", "Calculado desde fact_sistema_ia (supuesto INT-001)"),
]

RIESGOS_DEF = [
    ("R01", "Fuga de código o datos por herramientas de IA", "Media", "Crítico", "Alto",
     "Políticas, permisos como código, capacitación", "P1.2, P1.4, P1.5", "Medio",
     "P1.2, P1.4 y P1.5 cerrados al mes 8; controles activos sobre agentes"),
    ("R02", "Vencimiento del certificado ISO/IEC 27001 sin recertificación", "Alta", "Crítico", "Alto",
     "Recertificación en el mes 0", "P1.1", "Bajo",
     "Recertificación supuesta completada en el mes 5 sin no conformidades mayores (ver PUB-002)"),
    ("R03", "Vulnerabilidades heredadas de dependencias", "Alta", "Alto", "Alto",
     "Análisis de composición en el pipeline", "P2.2, P2.3", "Alto",
     "P2.2 y P2.3 siguen atrasados y KPI-05 continúa en nivel Bajo (217,9 h frente a 72 h)"),
    ("R04", "Sanción por incumplir la Ley 1581 en transferencias de datos", "Media", "Alto", "Medio",
     "Registro de transferencias y capacitación", "P1.5, P1.9", "Medio",
     "Registro contractual iniciado tras P1.9, pero DAT-01 sigue en Intermedio por demoras en reclamos"),
    ("R05", "Inyección de instrucciones o sesgos en modelos de IA", "Media", "Alto", "Medio",
     "Evaluación automática y controles NIST AI RMF", "P1.2, P3.2", "Medio",
     "P3.2 inicia en fase 3; se mantiene evaluación manual parcial"),
    ("R06", "Rotación de personal y pérdida de conocimiento", "Alta", "Medio", "Medio",
     "Rotación planificada y documentación", "P2.1", "Alto",
     "KPI-10 en 33,2 % frente a meta intermedia de 50 %; aumenta exposición operativa"),
    ("R07", "Sobrecosto de nube", "Media", "Medio", "Medio",
     "Tablero de costos y ajuste de capacidad", "P2.7", "Medio",
     "Variación de −4,4 % frente a meta de −5 % tras activar P2.7; tendencia favorable sin cierre de brecha"),
    ("R08", "El cliente no autoriza cambios en su infraestructura o herramientas", "Media", "Alto", "Medio",
     "Acuerdo previo; estándares presentados como propuesta", "P2.1, P2.6, P2.7", "Medio",
     "Sin variación al corte; persiste restricción en ambientes compartidos de P2.6"),
]

# 16 decisiones en lenguaje de acta (sin '@', <= 160 caracteres por campo de texto).
# Las 10 decisiones del mes 12 (2027-09) coinciden con el flujo de n8n (C02 y C07 quedan en amarillo).
DECISIONES_DEF = [
    (3, "OPE", "Estrategia", "P1.9 emite concepto preliminar de plazos para consultas y reclamos de titulares.",
     "Se adopta meta provisional de 10 y 15 días hábiles pendiente de revisión legal de Ley 1581.", "CTO", "Comité Táctico", "DAT-01", "P1.9"),
    (5, "OPE", "Riesgo", "La auditoría simulada de ISO/IEC 27001 cerró sin no conformidades mayores.",
     "Se rebaja R02 a nivel Bajo sujeto a adjuntar el certificado emitido en el repositorio.", "CISO", "Comité Directivo", "KPI-07", "P1.1"),
    (7, "OPE", "Priorización", "P1.8 no entregó la carta de constitución del CoE ni la hoja de pruebas en el mes 6.",
     "Se declara P1.8 atrasado y se reasigna seguimiento semanal directo al CTO.", "CTO", "Comité Directivo", "KPI-04", "P1.8"),
    (8, "C11", "Desempeño", "C11 omitió el reporte mensual de licencias de IA activas en mayo de 2027.",
     "Se registra C11 sin reporte en el mes 8 y se solicita conciliación con Line Manager.", "CoE de IA", "Comité Táctico", "KPI-04", "P1.8"),
    (9, "OPE", "Riesgo", "P1.2, P1.4 y P1.5 cerraron con permisos para agentes de IA aplicados al inventario.",
     "Se reduce R01 de Alto a Medio manteniendo monitoreo trimestral de evaluaciones de riesgo.", "CISO", "Comité Directivo", "IA-01", "P1.4"),
    (11, "OPE", "Priorización", "P2.6 acumula rezago y P3.1/P3.3 arrancan en mes 13 pese a la meta anual de METI03.",
     "Se prioriza P2.2 y P2.3 por R03; P2.6 pasa al siguiente trimestre y SOC 2 queda en fase 4.", "CTO", "Comité Directivo", "KPI-11", "P2.6"),
    (12, "C01", "Desempeño", "KPI-10: 17,6 % frente a 50 %.",
     "Aprobado plan correctivo para C01; C02 y C07 quedan en amarillo.", "Line Managers", "Comité Táctico", "KPI-10", "P2.1"),
    (12, "C03", "Desempeño", "KPI-05: 217,1 h frente a 72 h.",
     "Aprobado plan correctivo de remediación crítica para C03.", "DevSecOps", "Comité Táctico", "KPI-05", "P2.2"),
    (12, "C04", "Desempeño", "KPI-10: 29,4 % frente a 50 %.",
     "Aprobado plan correctivo de rotación de personal para C04.", "Line Managers", "Comité Táctico", "KPI-10", "P2.1"),
    (12, "C05", "Desempeño", "KPI-05: 396,8 h frente a 72 h.",
     "Aprobado plan correctivo urgente de remediación crítica para C05.", "DevSecOps", "Comité Táctico", "KPI-05", "P2.2"),
    (12, "C06", "Desempeño", "KPI-05: 168,3 h frente a 72 h.",
     "Aprobado plan correctivo de remediación crítica para C06.", "DevSecOps", "Comité Táctico", "KPI-05", "P2.3"),
    (12, "C08", "Desempeño", "KPI-05: 239,8 h frente a 72 h.",
     "Aprobado plan correctivo de remediación crítica para C08.", "DevSecOps", "Comité Táctico", "KPI-05", "P2.3"),
    (12, "C09", "Desempeño", "KPI-05: 450,2 h frente a 72 h.",
     "Aprobado plan correctivo urgente de remediación crítica para C09.", "DevSecOps", "Comité Táctico", "KPI-05", "P2.3"),
    (12, "C10", "Desempeño", "KPI-05: 169,4 h frente a 72 h.",
     "Aprobado plan correctivo de remediación crítica para C10.", "DevSecOps", "Comité Táctico", "KPI-05", "P2.2"),
    (12, "C11", "Desempeño", "KPI-05: 138,6 h frente a 72 h.",
     "Aprobado plan correctivo de remediación crítica para C11.", "DevSecOps", "Comité Táctico", "KPI-05", "P2.2"),
    (12, "C12", "Desempeño", "KPI-10: 33,3 % frente a 50 %.",
     "Aprobado plan correctivo de rotación de personal para C12.", "Line Managers", "Comité Táctico", "KPI-10", "P2.1"),
]


def fecha_mes(mes: int) -> date:
    idx = mes - 1
    return date(2026 + (9 + idx) // 12, (9 + idx) % 12 + 1, 1)


def etiqueta_mes(mes: int) -> str:
    d = fecha_mes(mes)
    return f"{MESES_ES[d.month - 1]} {d.year}"


def mes_de_fecha(texto: str) -> int:
    d = date.fromisoformat(texto[:10])
    return (d.year - 2026) * 12 + d.month - 10 + 1


def cumplimiento(valor: float | None, meta: float | None, sentido: str) -> float | None:
    if valor is None or meta is None:
        return None
    if sentido == "menor":
        if valor <= meta:
            return 100.0
        if meta == 0:
            return 0.0
        return round(100.0 * meta / valor, 1)
    if meta == 0:
        return 100.0 if valor >= 0 else 0.0
    return round(max(0.0, min(100.0, 100.0 * valor / meta)), 1)


def estado(cumpl: float | None) -> str:
    if cumpl is None:
        return "No evaluado"
    if cumpl >= 95.0:
        return "Bueno"
    if cumpl > 70.0:
        return "Intermedio"
    return "Bajo"


def _leer_csv(carpeta: Path, nombre: str) -> list[dict[str, str]]:
    with (carpeta / nombre).open(encoding="utf-8") as f:
        return [{k: TILDES_CSV.get(v, v) for k, v in fila.items()} for fila in csv.DictReader(f)]


def _construir_dimensiones() -> dict[str, list[dict]]:
    dim_fecha = []
    for m in range(1, 25):
        d = fecha_mes(m)
        dim_fecha.append({
            "mes": m,
            "fecha": d,
            "etiqueta": etiqueta_mes(m),
            "anio": d.year,
            "trimestre": f"T{(m - 1) // 3 + 1}",
            "fase": (m - 1) // 6 + 1,
        })

    dim_corte = [{"mes": m, "etiqueta": etiqueta_mes(m)} for m in range(1, 13)]

    dim_principio = [
        {
            "seccion": sec,
            "orden": orden,
            "nombre_es": n_es,
            "nombre_en": n_en,
            "descripcion": desc,
            "fuente": "PUB-026 nombre; PUB-029 descripción",
        }
        for sec, orden, n_es, n_en, desc in PRINCIPIOS
    ]

    dim_tarea = [{"id_tarea": i, "tarea": nom, "seccion": sec} for i, nom, sec in TAREAS]

    cols_ind = [
        "id_indicador", "nombre", "dominio", "origen", "objetivo", "meta_id",
        "seccion_principio", "id_tarea", "elemento_marco", "formula", "unidad",
        "sentido", "escala", "linea_base", "meta_mes12", "meta_mes24",
        "frecuencia", "responsable", "nivel", "proyecto_corrige", "fuente_dato",
    ]
    dim_indicador = [dict(zip(cols_ind, fila)) for fila in INDICADORES_DEF]

    dim_celula = [
        {
            "id_celula": f"C{i:02d}",
            "nombre": f"Célula {i:02d}",
            "linea": LINEAS_SERVICIO[f"C{i:02d}"],
        }
        for i in range(1, 13)
    ]
    dim_celula.append({"id_celula": "OPE", "nombre": "Toda la operación", "linea": LINEAS_SERVICIO["OPE"]})

    dim_proyecto = []
    for pid, fin_plan, fin_real in PORTAFOLIO:
        nombre, fase, objetivo, brecha, id_ind, resp = PROYECTOS_META[pid]
        dim_proyecto.append({
            "id_proyecto": pid,
            "nombre": nombre,
            "fase": fase,
            "objetivo": objetivo,
            "brecha": brecha,
            "id_indicador": id_ind,
            "responsable": resp,
            "mes_inicio": INICIO[pid],
            "mes_fin_plan": fin_plan,
            "mes_fin_real": fin_real,
        })

    cols_r = ["id_riesgo", "riesgo", "probabilidad", "impacto", "nivel", "tratamiento", "proyectos", "nivel_corte", "motivo_cambio"]
    dim_riesgo = [dict(zip(cols_r, r)) for r in RIESGOS_DEF]

    return {
        "dim_fecha": dim_fecha,
        "dim_corte": dim_corte,
        "dim_principio": dim_principio,
        "dim_tarea": dim_tarea,
        "dim_indicador": dim_indicador,
        "dim_celula": dim_celula,
        "dim_proyecto": dim_proyecto,
        "dim_riesgo": dim_riesgo,
    }


def _construir_proyectos_mes(dim_proyecto: list[dict]) -> list[dict]:
    filas = []
    for p in dim_proyecto:
        pid = p["id_proyecto"]
        ini = p["mes_inicio"]
        fplan = p["mes_fin_plan"]
        freal = p["mes_fin_real"]
        dur_plan = max(1, fplan - ini)
        for m in range(1, 13):
            if m < ini:
                av_plan = 0.0
            elif m >= fplan:
                av_plan = 100.0
            else:
                av_plan = round(100.0 * (m - ini + 1) / (dur_plan + 1), 1)

            if freal is not None and freal <= m:
                av_real = 100.0
            elif m < ini:
                av_real = 0.0
            elif pid in ("P1.8", "P2.2", "P2.3", "P2.6"):
                av_real = round(min(78.0, av_plan * 0.78), 1)
            elif freal is not None:
                # Cierre real (incluye P1.4 con leve rezago en mes 6 antes de cerrar en mes 7)
                dur_real = max(1, freal - ini)
                av_real = round(100.0 * (m - ini + 1) / (dur_real + 1), 1)
            else:
                av_real = av_plan

            if freal is not None and freal <= m:
                est = "Terminado"
            elif m < ini:
                est = "Por iniciar"
            elif m >= fplan or av_real < av_plan - 15:
                est = "Atrasado"
            else:
                est = "En ejecución"

            filas.append({
                "mes": m,
                "id_proyecto": pid,
                "avance_plan": av_plan,
                "avance_real": av_real,
                "estado": est,
            })
    return filas


def _construir_sistemas_ia(rng: random.Random) -> list[dict]:
    """Genera 50 sistemas de IA con cobertura de inventario, evaluación de riesgo y supervisión
    deterministas para cuadrar exactamente KPI-08 (Bueno: 92 %), IA-01 (Intermedio: 69.6 %)
    y IA-02 (Bueno: 91.3 %) al mes 12 y en los cortes trimestrales previos."""
    tipos = [
        "Asistente de código",
        "Búsqueda con documentos (RAG)",
        "Agente",
        "Clasificación o predicción",
    ]
    origenes = ["Servicio externo", "API de terceros", "Desarrollo propio"]
    riesgos = ["Alto", "Medio", "Bajo"]
    estados = ["Piloto", "Uso interno", "Producción"]
    celulas = [f"C{i:02d}" for i in range(1, 13)]

    # Bloques exactos para 50 sistemas:
    # Meses de identificación <= 3: 20 sistemas (reg <= 3: 8 -> 40 %)
    # Meses de identificación 4..6: 12 sistemas (acum 32; reg <= 6: 22 -> 68.8 %)
    # Meses de identificación 7..9: 10 sistemas (acum 42; reg <= 9: 35 -> 83.3 %)
    # Meses de identificación 10..12: 8 sistemas (acum 50; reg <= 12: 46 -> 92.0 % Bueno)
    id_meses = [rng.randint(1, 3) for _ in range(20)] + [rng.randint(4, 6) for _ in range(12)] + \
               [rng.randint(7, 9) for _ in range(10)] + [rng.randint(10, 12) for _ in range(8)]
    reg_meses = [1] * 4 + [3] * 4 + [4, 5] + [6] * 12 + [7, 8] + [9] * 11 + [10, 11] + [12] * 9 + [None] * 4
    # Para los 46 registrados al mes 12: 32 con evaluación de riesgo (69.6 % -> Intermedio),
    # distribuidos progresivamente en meses 6, 9 y 12.
    eval_meses = [6] * 11 + [9] * 10 + [12] * 11 + [None] * 14 + [None] * 4
    # Supervisión humana sobre los 46 registrados: 42 Sí (91.3 % -> Bueno), 4 No
    sup_flags = ["Sí"] * 42 + ["No"] * 4 + ["No"] * 4

    sistemas = []
    for idx in range(50):
        m_id = id_meses[idx]
        m_reg = reg_meses[idx]
        if m_reg is not None and m_reg < m_id:
            m_reg = m_id
        m_eval = eval_meses[idx]
        if m_eval is not None and m_reg is not None and m_eval < m_reg:
            m_eval = m_reg
        cel = celulas[idx % 12]
        if m_eval is None and idx == 45:
            cel = "C11"  # coherente con decisión de C11 en mes 11
        tipo = tipos[(idx + rng.randint(0, 3)) % len(tipos)]
        riesgo = riesgos[0 if tipo == "Agente" and idx % 3 == 0 else (1 + idx % 2)]
        est = "Uso interno" if idx < 35 else "Piloto"
        if m_reg is not None and idx % 7 == 0 and m_eval is not None:
            est = "Producción"  # uso interno/producción técnica interna (no casos cliente de KPI-03)
        sistemas.append({
            "id_sistema": f"IA-S{idx + 1:02d}",
            "id_celula": cel,
            "tipo": tipo,
            "origen": origenes[idx % len(origenes)],
            "mes_identificado": m_id,
            "mes_registrado": m_reg,
            "mes_evaluacion_riesgo": m_eval,
            "supervision_humana": sup_flags[idx],
            "usa_datos_personales": "Sí" if (idx % 3 == 0 or riesgo == "Alto") else "No",
            "nivel_riesgo": riesgo,
            "estado": est,
        })
    return sistemas


def _construir_solicitudes_titular(rng: random.Random) -> list[dict]:
    """Genera 3 a 10 solicitudes por mes (meses 1 a 12). Al mes 12: 7 de 8 en plazo (87.5 % -> Intermedio)."""
    conteos_mes = [4, 5, 6, 5, 7, 8, 6, 9, 7, 8, 6, 8]
    # Cuántas fuera de plazo por mes (al menos algunas reales y mes 12 = 1 de 8 -> 87.5 %)
    fuera_mes = [1, 1, 1, 1, 2, 1, 1, 2, 1, 2, 1, 1]
    filas = []
    sid = 0
    for m, (tot, fuera) in enumerate(zip(conteos_mes, fuera_mes), start=1):
        d_base = fecha_mes(m)
        indices_fuera = set(rng.sample(range(tot), fuera))
        for j in range(tot):
            sid += 1
            tipo = "Reclamo" if (j % 3 == 0) else "Consulta"
            plazo = 15 if tipo == "Reclamo" else 10
            if j in indices_fuera:
                dias = plazo + rng.randint(1, 4)
            else:
                dias = rng.randint(max(2, plazo - 6), plazo)
            dia_mes = min(28, 2 + j * 3 + rng.randint(0, 1))
            filas.append({
                "id_solicitud": f"SOL-{sid:03d}",
                "mes": m,
                "fecha_recibida": date(d_base.year, d_base.month, dia_mes),
                "tipo": tipo,
                "plazo_dias_habiles": plazo,
                "dias_habiles_respuesta": dias,
                "en_plazo": "Sí" if dias <= plazo else "No",
            })
    return filas


def _construir_mediciones(
    rng: random.Random,
    personas: list[dict[str, str]],
    fact_vuln: list[dict],
    fact_proyecto_mes: list[dict],
    fact_sistema_ia: list[dict],
    fact_solicitud_titular: list[dict],
) -> list[dict]:
    filas = []
    celulas = [f"C{i:02d}" for i in range(1, 13)]

    def add(mes: int, ind: str, cel: str, num: float | None, den: float | None, est_rep: str = "Reportado", nota: str = ""):
        filas.append({
            "mes": mes,
            "id_indicador": ind,
            "id_celula": cel,
            "numerador": num,
            "denominador": den,
            "estado_reporte": est_rep,
            "nota": nota,
        })

    # KPI-01: operación meses 1..12 desde fact_proyecto_mes / PORTAFOLIO
    term_por_mes = defaultdict(int)
    for r in fact_proyecto_mes:
        if r["estado"] == "Terminado":
            term_por_mes[r["mes"]] += 1
    for m in range(1, 13):
        add(m, "KPI-01", "OPE", term_por_mes[m], 25)

    # KPI-02: meses 9 y 12, base promedio de COSTO_NUBE meses 7..9 (índices 6..8)
    base_nube = sum(COSTO_NUBE[6:9]) / 3.0
    for m in (9, 12):
        add(m, "KPI-02", "OPE", round(COSTO_NUBE[m - 1] - base_nube, 4), round(base_nube, 4))

    # KPI-03: semestral (meses 6 y 12), 0/1
    for m in (6, 12):
        add(m, "KPI-03", "OPE", 0, 1, nota="P3.1 y P3.3 inician en el mes 13")

    # KPI-04: línea base mes 3; meses 1-2 antes de línea base; C11 mes 8 sin reporte; 9/12 mes 12; retroceso
    for m in (1, 2):
        add(m, "KPI-04", "OPE", None, None, "Antes de la línea base")
    activos_kpi04 = {
        3: 6, 4: 7, 5: 7, 6: 8, 7: 8, 8: 7, 9: 7, 10: 8, 11: 9, 12: 9,
    }
    # Para que mes 8 (sin C11) tenga 7/11 y mes 9 baje a 7/12 (retroceso frente a 63.6% -> 58.3%),
    # y mes 12 termine en 9/12 (75.0% -> Intermedio)
    cel_ordenadas = ["C01", "C02", "C04", "C05", "C06", "C07", "C08", "C10", "C12", "C03", "C09", "C11"]
    for m in range(3, 13):
        activos = set(cel_ordenadas[: activos_kpi04[m]])
        for c in celulas:
            if m == 8 and c == "C11":
                add(m, "KPI-04", c, None, None, "Sin reporte", "Célula no envió reporte en el corte de mayo")
            else:
                add(m, "KPI-04", c, 1 if c in activos else 0, 1)

    # KPI-05: vulnerabilidades críticas desde mes 3 (meses 1-2 no se escriben; sin fila si 0 críticas)
    vul_cm = defaultdict(list)
    for v in fact_vuln:
        if v["severidad"] == "Crítica" and v["mes"] >= 3:
            vul_cm[(v["mes"], v["id_celula"])].append(v["horas_remediacion"])
    for m in range(3, 13):
        for c in celulas:
            hs = vul_cm.get((m, c))
            if hs:
                add(m, "KPI-05", c, round(sum(hs), 2), len(hs))

    # KPI-06: línea base mes 6; meses 1-5 antes de línea base; serie irregular con retroceso
    for m in range(1, 6):
        add(m, "KPI-06", "OPE", None, None, "Antes de la línea base")
    concil_vals = {6: 640, 7: 710, 8: 730, 9: 690, 10: 760, 11: 800, 12: 830}
    for m, horas in concil_vals.items():
        add(m, "KPI-06", "OPE", horas, 1000)

    # KPI-07: mes 5, 0 no conformidades mayores
    add(5, "KPI-07", "OPE", 0, 1, nota="Auditoría supuesta en el mes 5 (PUB-002)")

    # KPI-08: cobertura inventario de IA desde fact_sistema_ia en meses 3, 6, 9, 12
    for m in (3, 6, 9, 12):
        for c in celulas:
            ident = [s for s in fact_sistema_ia if s["id_celula"] == c and s["mes_identificado"] <= m]
            if ident:
                reg = sum(1 for s in ident if s["mes_registrado"] is not None and s["mes_registrado"] <= m)
                add(m, "KPI-08", c, reg, len(ident))

    # KPI-09: personal certificado >6 meses, trimestral; mes 12 desde sintetico_personas, anteriores bajan irregular
    pers_por_cel = defaultdict(list)
    for p in personas:
        pers_por_cel[p["celula"]].append(p)
    for c in celulas:
        ps = pers_por_cel[c]
        mas6 = [p for p in ps if float(p["antiguedad_meses"]) > 6]
        cert12 = sum(int(float(p["certificaciones"])) >= 1 for p in mas6)
        den = len(mas6)
        cert9 = max(0, cert12 - rng.choice([0, 1]))
        cert6 = max(0, cert9 - rng.choice([0, 1, 2]))
        cert3 = max(0, cert6 - rng.choice([0, 1, 2]))
        for m, num in ((3, cert3), (6, cert6), (9, cert9), (12, cert12)):
            add(m, "KPI-09", c, num, den)

    # KPI-10: rotación entre células, semestral (6 y 12); mes 12 desde sintetico_personas
    for c in celulas:
        ps = pers_por_cel[c]
        rot12 = sum(p["rotado_ultimo_anio"] == "Sí" for p in ps)
        rot6 = max(0, rot12 - rng.choice([1, 2]))
        for m, num in ((6, rot6), (12, rot12)):
            add(m, "KPI-10", c, num, len(ps))

    # KPI-11: ambientes con IaC / 48 ambientes, trimestral (9 y 12)
    add(9, "KPI-11", "OPE", 15, 48)
    add(12, "KPI-11", "OPE", 16, 48)

    # KPI-13: una fila en mes 12 no aplica al corte
    add(12, "KPI-13", "OPE", None, None, "No aplica al corte", "P4.1 inicia en el mes 13")

    # KPI-14: sesiones con acta / 4 por trimestre, un trimestre con 3/4
    for m, num in ((3, 3), (6, 4), (9, 4), (12, 4)):
        add(m, "KPI-14", "OPE", num, 4)

    # DAT-01: mensual desde fact_solicitud_titular
    sol_por_mes = defaultdict(list)
    for s in fact_solicitud_titular:
        sol_por_mes[s["mes"]].append(s)
    for m in range(1, 13):
        ss = sol_por_mes[m]
        add(m, "DAT-01", "OPE", sum(1 for x in ss if x["en_plazo"] == "Sí"), len(ss))

    # DAT-02: trimestral, activos clasificados / inventariados (meta 60 -> Bajo <= 42 %)
    for m, num in ((3, 18), (6, 26), (9, 34), (12, 40)):
        add(m, "DAT-02", "OPE", num, 120)

    # DAT-03: trimestral meses 6, 9, 12 (meta 80 -> Bueno >= 76 %)
    for m, num in ((6, 11), (9, 17), (12, 20)):
        add(m, "DAT-03", "OPE", num, 25)

    # IA-01 y IA-02: desde fact_sistema_ia en meses 6, 9, 12
    for m in (6, 9, 12):
        for c in celulas:
            reg = [s for s in fact_sistema_ia if s["id_celula"] == c and s["mes_registrado"] is not None and s["mes_registrado"] <= m]
            if reg:
                n_eval = sum(1 for s in reg if s["mes_evaluacion_riesgo"] is not None and s["mes_evaluacion_riesgo"] <= m)
                n_sup = sum(1 for s in reg if s["supervision_humana"] == "Sí")
                add(m, "IA-01", c, n_eval, len(reg))
                add(m, "IA-02", c, n_sup, len(reg))

    return filas


def _construir_decisiones() -> list[dict]:
    filas = []
    for i, (mes, cel, foco, just, dec, resp, inst, id_ind, id_proy) in enumerate(DECISIONES_DEF):
        d_base = fecha_mes(mes)
        f_dec = date(d_base.year, d_base.month, min(26, 12 + (i % 5) * 3))
        filas.append({
            "fecha": f_dec,
            "ciclo": f"{d_base.year:04d}-{d_base.month:02d}",
            "celula": cel,
            "foco": foco,
            "justificacion": just,
            "decision": dec,
            "responsable": resp,
            "instancia": inst,
            "mes": mes,
            "id_indicador": id_ind,
            "id_proyecto": id_proy,
        })
    return filas


def construir_modelo(carpeta_sinteticos: Path, semilla: int = 38500) -> dict[str, list[dict]]:
    rng = random.Random(semilla)
    carpeta_sinteticos = Path(carpeta_sinteticos)
    personas = _leer_csv(carpeta_sinteticos, "sintetico_personas.csv")
    vulns_raw = _leer_csv(carpeta_sinteticos, "sintetico_vulnerabilidades.csv")

    modelo = _construir_dimensiones()

    fact_proyecto_mes = _construir_proyectos_mes(modelo["dim_proyecto"])

    fact_vulnerabilidad = []
    for v in vulns_raw:
        m = mes_de_fecha(v["fecha_deteccion"])
        if 1 <= m <= 12:
            fact_vulnerabilidad.append({
                "mes": m,
                "fecha_deteccion": date.fromisoformat(v["fecha_deteccion"][:10]),
                "id_celula": v["celula"],
                "severidad": v["severidad"],
                "origen": v["origen"],
                "horas_deteccion": float(v["horas_deteccion"]),
                "horas_remediacion": float(v["horas_remediacion"]),
            })

    fact_sistema_ia = _construir_sistemas_ia(rng)
    fact_solicitud_titular = _construir_solicitudes_titular(rng)
    fact_medicion = _construir_mediciones(
        rng, personas, fact_vulnerabilidad, fact_proyecto_mes, fact_sistema_ia, fact_solicitud_titular
    )
    fact_decision = _construir_decisiones()

    modelo["fact_medicion"] = fact_medicion
    modelo["fact_proyecto_mes"] = fact_proyecto_mes
    modelo["fact_vulnerabilidad"] = fact_vulnerabilidad
    modelo["fact_sistema_ia"] = fact_sistema_ia
    modelo["fact_solicitud_titular"] = fact_solicitud_titular
    modelo["fact_decision"] = fact_decision
    return modelo


def control_corte(modelo: dict, corte: int) -> list[dict]:
    salida = []
    for ind in modelo["dim_indicador"]:
        iid = ind["id_indicador"]
        escala = ind["escala"]
        sentido = ind["sentido"]
        meta = ind["meta_mes12"] if corte <= 12 else ind["meta_mes24"]

        con_dato = [
            f
            for f in modelo["fact_medicion"]
            if f["id_indicador"] == iid
            and f["mes"] <= corte
            and f["estado_reporte"] == "Reportado"
            and f["denominador"] is not None
            and f["denominador"] != 0
        ]
        mes_ult = max((f["mes"] for f in con_dato), default=None)
        if mes_ult is None:
            valor = None
            valor_calc = None
        else:
            del_mes = [f for f in con_dato if f["mes"] == mes_ult]
            num = sum(f["numerador"] for f in del_mes)
            den = sum(f["denominador"] for f in del_mes)
            valor_calc = num / den * escala
            valor = round(valor_calc, 1)

        cumpl = cumplimiento(valor_calc, meta, sentido)
        salida.append({
            "id_indicador": iid,
            "nombre": ind["nombre"],
            "valor": valor,
            "meta": meta,
            "cumplimiento": cumpl,
            "estado": estado(cumpl),
            "mes_ultimo_reporte": mes_ult,
        })
    return salida


def escribir_xlsx(modelo: dict, ruta: Path) -> None:
    ruta = Path(ruta)
    ruta.parent.mkdir(parents=True, exist_ok=True)
    wb = openpyxl.Workbook()
    wb.remove(wb.active)

    for tabla, filas in modelo.items():
        ws = wb.create_sheet(tabla)
        if not filas:
            continue
        headers = list(filas[0].keys())
        ws.append(headers)
        for c in ws[1]:
            c.font = Font(bold=True)
        for fila in filas:
            ws.append([fila[h] for h in headers])
        for idx, h in enumerate(headers, start=1):
            col_letra = openpyxl.utils.get_column_letter(idx)
            ws.column_dimensions[col_letra].width = max(12, min(42, len(h) + 4))

    wb.save(ruta)


def escribir_control_csv(filas: list[dict], ruta: Path) -> None:
    ruta = Path(ruta)
    ruta.parent.mkdir(parents=True, exist_ok=True)
    campos = ["id_indicador", "nombre", "valor", "meta", "cumplimiento", "estado", "mes_ultimo_reporte"]
    with ruta.open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=campos)
        w.writeheader()
        w.writerows(filas)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("carpeta_sinteticos")
    ap.add_argument("carpeta_salida")
    args = ap.parse_args()

    carpeta_in = Path(args.carpeta_sinteticos)
    carpeta_out = Path(args.carpeta_salida)
    modelo = construir_modelo(carpeta_in, semilla=38500)
    escribir_xlsx(modelo, carpeta_out / "modelo_gobierno_ti.xlsx")
    escribir_control_csv(control_corte(modelo, 12), carpeta_out / "control_corte_mes12.csv")
    print(f"ok: {len(modelo)} hojas en modelo_gobierno_ti.xlsx y {len(modelo['dim_indicador'])} filas en control_corte_mes12.csv")


if __name__ == "__main__":
    main()
