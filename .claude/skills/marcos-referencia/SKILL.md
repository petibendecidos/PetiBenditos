---
name: marcos-referencia
description: Usar cuando el PETI de Perficient nombra, aplica o mapea un marco o una norma (COBIT 2019 con sus 40 objetivos, niveles de capacidad y los diagnósticos de sensibilización gerencial y de control en TI, TOGAF, ITIL 4, ISO/IEC 38500:2024 de gobierno de TI con sus principios y su modelo evaluar-dirigir-monitorear, ISO/IEC 27001:2022, ISO/IEC 42001:2023, NIST AI RMF, SOC 2, SOX, MRAE del MinTIC, Política de Gobierno Digital, Ley 1581 de 2012 u otras leyes de datos de LATAM), cuando se redacta el marco normativo (§5), la gobernanza (§17) o el mapeo de controles, cuando hay que decidir si una norma aplica a Perficient, se adapta o es solo referencia, o cuando se mapean procesos o controles (APO06, DSS01, A.8.28…).
argument-hint: "[marco o norma]"
---

# Marcos y normas del PETI

## Principio

Un marco se cita por lo que exige o aporta al plan, no por su prestigio. Cada mención responde tres preguntas: **qué es** (emisor, versión, año), **qué relación tiene con Perficient** (obligatorio, contractual, voluntario, referencia metodológica) y **dónde se usa en el PETI** (numeral, brecha, proyecto, indicador). Lo que no se ha comprobado en el texto oficial se marca `[VERIFICAR]` y no se presenta como cierto. Al verificar algo, quita la marca aquí y registra la fuente en `docs/registro-de-evidencias.md` en el mismo cambio.

## Tres tipos de relación (decídelo antes de escribir)

| Relación | Significa | Ejemplos para Perficient |
|---|---|---|
| **Obligación legal** | Aplica por ley donde opera | Protección de datos personales en cada país LATAM |
| **Compromiso voluntario o contractual** | Perficient lo adoptó o un cliente lo exige | ISO/IEC 27001 (certificado), informes SOC 2 para clientes |
| **Referencia metodológica** | Se usa como guía para construir el plan | Guía y plantilla del MinTIC, MRAE, COBIT, TOGAF, ITIL, NIST AI RMF |

La guía del MinTIC, el MRAE, MIPG, el Decreto 767 de 2022 y el Decreto 612 de 2018 obligan a **entidades públicas colombianas**. Para Perficient son referencia metodológica; el PETI lo dice en el marco normativo y en la metodología.

## Marcos internacionales

| Marco | Emisor y versión | Qué aporta al PETI | Cuidado al citarlo |
|---|---|---|---|
| COBIT 2019 | ISACA, 2018-2019 | Gobierno y gestión de TI: 40 objetivos en 5 dominios (EDM, APO, BAI, DSS, MEA); cascada de metas; factores de diseño; capacidad de 0 a 5 basada en CMMI. Ej.: APO06 *Managed Budget and Costs*, DSS01 *Managed Operations*, APO12 *Managed Risk*, EDM02 *Ensured Benefits Delivery*. Los 40 objetivos con su nombre en español y su correspondencia con brechas y proyectos del PETI, la escala de capacidad, las fuentes (PUB-030 a PUB-035) y los diagnósticos de sensibilización gerencial y de control en TI están en [cobit-2019.md](cobit-2019.md) | Se cita el objetivo por código y nombre. No es certificable para una organización. Hay formatos que mezclan códigos de COBIT 5 y 2019 (APO09 a APO12 corridos, BAI11 "problemas"): compáralos con la tabla de `cobit-2019.md`. La escala de la ISO/IEC 33000 es la de COBIT 5. |
| TOGAF | The Open Group; TOGAF Standard, 10.ª edición (2022) | Método ADM (fase preliminar, A-H y gestión de requisitos) y dominios de arquitectura: negocio, datos, aplicaciones, tecnología | El PETI añade "seguridad" como capa; TOGAF la trata como transversal. Decirlo. |
| ISO/IEC 38500:2024 | ISO/IEC, edición 3, febrero de 2024 (reemplaza la de 2015) | Gobierno de TI para el órgano de gobierno: 11 principios (§5), modelo con cuatro tareas (involucrar a las partes interesadas, evaluar, dirigir, monitorear; §6) y marco con seis elementos (§7). Detalle, fuentes y correspondencia con el PETI en [iso-38500.md](iso-38500.md) | Solo hay vista previa hasta §4.2 (PUB-026): de §5 en adelante se citan nombres y el resumen secundario de Garibay (PUB-029). No es certificable. Los 6 principios y el modelo de tres tareas son de 2008. |
| ITIL 4 | AXELOS/PeopleCert, 2019 | Sistema de valor del servicio y 34 prácticas (gestión de incidentes, de cambios, de niveles de servicio, monitoreo y eventos, mejora continua) | Es buena práctica, no norma. |
| ISO/IEC 27001:2022 | ISO/IEC | SGSI certificable. Anexo A con 93 controles en 4 temas: organizacionales (5.x), personas (6.x), físicos (7.x) y tecnológicos (8.x). Ej.: 8.15 registro de eventos, 8.25-8.29 desarrollo seguro y pruebas de seguridad | El certificado dura 3 años con auditorías de seguimiento anuales y de recertificación al final `[VERIFICAR con el certificado de A-Lign]`. La transición desde la versión 2013 terminó el 31 de octubre de 2025. |
| ISO/IEC 42001:2023 | ISO/IEC, diciembre de 2023 | Sistema de gestión de IA (AIMS) certificable, estructura de sistema de gestión (cláusulas 4-10) y anexo de controles | Número y agrupación de controles del anexo A `[VERIFICAR]`. Hoy Perficient no declara certificación: el PETI la propone. |
| NIST AI RMF 1.0 | NIST, enero de 2023 (NIST AI 100-1) | Funciones Gobernar, Mapear, Medir, Gestionar. Perfil de IA generativa NIST AI 600-1 (julio de 2024) | Voluntario; se adopta, no se certifica. |
| SOC 2 | AICPA | Informe de **atestación** sobre controles según los Trust Services Criteria: seguridad, disponibilidad, integridad del procesamiento, confidencialidad y privacidad. Tipo I (diseño en una fecha) y tipo II (eficacia operativa en un periodo) | No es certificación ni acreditación. `docs/perficient_iso27001_soc2_ciberseguridad.md` omite integridad del procesamiento. Vigencia y alcance del informe de Perficient: sin evidencia pública registrada. |
| SOX §302/§906 | Congreso de EE. UU., 2002 | Certificación de estados financieros por CEO y CFO de emisores registrados ante la SEC | Perficient dejó de cotizar el 2 de octubre de 2024 (PUB-001). Si sigue alguna obligación de reporte (por ejemplo, por deuda registrada) `[VERIFICAR con Legal/Finanzas]`. Form 15-12G del 15-oct-2024 y sin presentaciones posteriores en EDGAR (PUB-004). En el PETI: antecedente, no obligación vigente. |
| OWASP Top 10 para aplicaciones LLM | OWASP | Riesgos de aplicaciones con LLM (inyección de instrucciones, fuga de información sensible, agencia excesiva) | Útil para R04 y P1.4; citar la edición por año. |

## Marco colombiano (referencia metodológica)

| Documento | Qué es | Uso en el PETI |
|---|---|---|
| Guía MGGTI.GE.ES.03 v3.0 (nov. 2023) | Metodología de construcción del PETI | Estructura y actividades. Ver `guia-peti` |
| Plantilla PETI (Anexo 2) y herramientas (Anexo 1) | Estructura del documento y formatos | Ídem |
| MRAE v3.0 | Marco de referencia de arquitectura empresarial del Estado | Dominios de gestión de TI y lineamientos para el diagnóstico |
| Decreto 767 de 2022 | Política de Gobierno Digital | Contexto de la plantilla; no obliga a Perficient |
| Decreto 1078 de 2015, Decreto 1083 de 2015, Decreto 612 de 2018, Decreto 415 de 2016, Ley 1341 de 2009 | Normas que obligan a entidades públicas a tener PETI y área de TI | Solo como antecedente de por qué existe el PETI en Colombia |
| MSPI | Modelo de Seguridad y Privacidad de la Información del MinTIC | Instrumento sugerido por la plantilla (6.7) para calificar controles; se puede usar con los dominios de ISO 27001 |

## Protección de datos en los países de la operación (obligación legal)

| País | Norma principal | Estado |
|---|---|---|
| Colombia | Ley 1581 de 2012 y Decreto 1377 de 2013 (compilado en el Decreto 1074 de 2015); autoridad: SIC | Números y fechas verificables en el gestor normativo de Función Pública `[VERIFICAR artículos antes de citarlos]` |
| Argentina | Ley 25.326 de 2000 | Verificada, vigente (PUB-012) |
| Chile | Ley 19.628; Ley 21.719 de 2024 | Vigencia prevista 1-dic-2026 `[VERIFICAR en BCN]`; el Gobierno propuso el 1-sep-2026 aplazarla al 1-dic-2027 (PUB-013) |
| México | Nueva LFPDPPP, DOF 20-mar-2025; autoridad: Secretaría Anticorrupción y Buen Gobierno | Verificada (PUB-014) |
| Uruguay | Ley 18.331 de 2008 y modificaciones (19.670, 20.075, entre otras) | Verificada (PUB-015) |
| Clientes de EE. UU. y la UE | CCPA/CPRA y GDPR se mencionan en la capacitación de Perficient; el Reglamento (UE) 2024/1689 de IA puede aplicar a proyectos con clientes europeos | `[VERIFICAR aplicabilidad por cliente]` |

En el PETI basta una fila por país con la norma y la obligación para TI (autorización, finalidad, seguridad, transferencias internacionales, derechos del titular). No se desarrolla doctrina.

## Mapeo del PETI a los marcos (cómo hacerlo)

- Una fila por proceso o control del PETI, con el objetivo COBIT o el control ISO que le corresponde **por código y nombre**. Si no hay correspondencia clara, "—" y no un código forzado.
- El §17.3 actual solo tiene COBIT para una fila; complétalo o explica por qué el resto no aplica.
- El PETI Colombia anuncia en §3 un "mapeo (anexo)" con COBIT que no existe. La tabla de los 40 objetivos de [cobit-2019.md](cobit-2019.md) ya tiene la correspondencia con brechas y proyectos: úsala como base y deja "—" donde no hay proyecto (APO08, APO10, DSS03, DSS04).
- ISO 27001 se mapea al Anexo A de 2022 (5.x a 8.x). Un código A.12 o A.14 es de la versión 2013 y está mal.

## Señales de alerta

- "Acreditación SOC 2" o "certificación SOC 2".
- "Certificación NIST" o "cumplimiento NIST AI RMF" como si fuera auditable.
- SOX presentado como obligación vigente.
- "El PETI cumple MIPG" o "de acuerdo con el Decreto 612 Perficient debe…".
- Controles ISO 27001 con numeración de 2013.
- Un marco en el §5 que no aparece en ningún proyecto, brecha o indicador: o se usa o se retira.
