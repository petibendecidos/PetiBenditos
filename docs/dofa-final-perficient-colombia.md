# Análisis DOFA: Perficient, operación en Colombia (PETI 2026-2028)

Equipo de Arquitectura y Gobernanza de TI — Perficient LATAM · 8 de octubre de 2026

> **Nota del 21 de octubre de 2026.** La fecha de A1 (11 de octubre de 2026, lectura más temprana del certificado) ya pasó y no se encontró evidencia pública de la recertificación. Esta matriz se conserva como quedó el 8 de octubre. La versión ajustada, con la importancia de cada factor, la MEFI, la MEFE, los nombres de los tipos de estrategia según el material de clase y el orden de ejecución, está en `docs/entregas-2026-10-21/`.

| | 🟢 **FAVORABLE** | 🔴 **DESFAVORABLE** |
|:---:|---|---|
| **ANÁLISIS INTERNO** | 🟩 **FORTALEZAS** | 🟥 **DEBILIDADES** |
| | 🟩 **F1** [Seguridad] SGSI certificado en ISO/IEC 27001:2022, certificado ISMS-PE-101123 de A-Lign (PUB-002) | 🟥 **D1** [Seguridad, información] Uso de IA sin sistema de gestión, sin inventario y sin permisos para agentes (INT-001; PRV-001) |
| | 🟩 **F2** [Estrategia] Posicionamiento declarado "AI-native" (PUB-003) y alianzas de IA con Lovable y Gradial (PUB-009, PUB-010) | 🟥 **D2** [Gobierno] Sin comité de TI, RACI, matriz de riesgos ni presupuesto de TI (INT-001) |
| | 🟩 **F3** [Información, uso y apropiación] Alianzas con Microsoft, Databricks y Snowflake (PUB-005 a PUB-008) | 🟥 **D3** [Seguridad, gobierno] Transferencias internacionales de datos sin registro por proyecto; obligaciones posteriores a la privatización sin concepto legal (INT-001; PUB-004) |
| | 🟩 **F4** [Seguridad, sistemas] Pruebas de seguridad continuas y análisis de dependencias en la cuenta analizada (PRV-001) | 🟥 **D4** [Estrategia] Sin misión, visión, catálogo de servicios ni tablero de TI (INT-001) |
| | 🟩 **F5** [Gobierno, infraestructura] Roles definidos, Scrum y ambientes separados en la cuenta analizada (PRV-001) | 🟥 **D5** [Sistemas de información] Hallazgos de seguridad y horas se pasan a mano entre herramientas (PRV-001) |
| | 🟩 **F6** [Uso y apropiación] Formación en línea, patrocinio de certificaciones y capacitaciones obligatorias en la cuenta analizada (PRV-001) | 🟥 **D6** [Infraestructura] Sin infraestructura como código ni control de costos de nube (INT-001) |
| |  | 🟥 **D7** [Uso y apropiación] Adopción de IA no medida y canal de licencias no estandarizado (PRV-001; INT-001) |
| **ANÁLISIS EXTERNO** | 🟦 **OPORTUNIDADES** | 🟧 **AMENAZAS** |
| | 🟦 **O1** Clientes que piden IA gobernada y auditable (INT-001; [2]) | 🟧 **A1** El certificado ISO vence el 11 de octubre de 2026 y no hay evidencia pública de su recertificación (PUB-002; [1]; R02) |
| | 🟦 **O2** ISO/IEC 42001 y NIST AI RMF para ordenar y demostrar el gobierno de la IA ([3]) | 🟧 **A2** Fuga de código o datos e inyección de instrucciones por herramientas de IA ([4], [5]; R01, R05) |
| | 🟦 **O3** Informe SOC 2 tipo II con controles de IA, que los clientes piden a sus proveedores de servicios ([9]) | 🟧 **A3** Sanción por incumplir la Ley 1581 y leyes de datos más exigentes en la región ([6]; PUB-013, PUB-014; R04) |
| | 🟦 **O4** Plataformas, formación y certificaciones de los socios (PUB-005 a PUB-008) | 🟧 **A4** Competidores nearshore que ya certificaron su gobierno de IA: Softtek, ISO/IEC 42001 desde noviembre de 2025 ([2]) |
| | 🟦 **O5** Prácticas maduras de DevSecOps, infraestructura como código y observabilidad | 🟧 **A5** Vulnerabilidades heredadas de dependencias de código abierto ([7]; R03) |
| | 🟦 **O6** COBIT 2019 como referencia para el gobierno y el presupuesto de TI | 🟧 **A6** Rotación de personal hacia empleadores del exterior ([8]; R06) |
| |  | 🟧 **A7** El cliente no autoriza cambios en su infraestructura; sobrecosto de nube (PRV-001; R07, R08) |

*Entre corchetes, el dominio de gestión de TI. PUB-, PRV- e INT- remiten al registro de evidencias del proyecto; R01-R08, a la matriz de riesgos del PETI Colombia (§11); [1] a [9], a las fuentes externas listadas al final. Dentro de cada cuadrante los factores van en orden de prioridad.*

---

## De dónde salen los datos y por qué estos

### Cómo se construyó

La DOFA responde a la Actividad 6 de la Guía MGGTI.GE.ES.03 v3.0 del MinTIC ("Analizar y diagnosticar la gestión de TI"), que pide fortalezas y debilidades de origen interno, oportunidades y amenazas de origen externo, y un análisis por dominio de gestión de TI. Por eso cada factor interno lleva entre corchetes uno de los siete dominios del MRAE: estrategia, gobierno, información, sistemas de información, infraestructura, uso y apropiación, y seguridad.

Los datos vienen de cuatro fuentes:

| Fuente | Qué aporta | Cómo se cita |
|---|---|---|
| PETI Colombia v1.0 | Diagnóstico por dominio (§6.1), motivadores (§5.1), procesos (§5.3), brechas (§8), proyectos (§9) y riesgos (§11) | Numeral, `BRE-`, `P`, `R` |
| Registro de evidencias del proyecto | Fuentes públicas ya verificadas sobre Perficient y sobre las leyes de datos de la región | `PUB-001` a `PUB-015` |
| Entrevistas de una cuenta de cliente, anonimizadas | Cómo se trabaja en la práctica: roles, herramientas, flujos manuales | `PRV-001`, siempre como "observado en la cuenta analizada" |
| Investigación pública del 8 de octubre de 2026 | Datos del entorno para respaldar oportunidades y amenazas | `[1]` a `[9]` |

Un factor entró a la DOFA solo si cumplía tres condiciones:

1. **Tiene respaldo.** Una fuente pública, la observación de la cuenta o el diagnóstico del PETI. Lo que es lectura del equipo se marca como `INT-001`.
2. **TI puede actuar sobre él.** Cada factor se conecta con una brecha, un riesgo o un proyecto del PETI. Por eso se dejaron por fuera la tasa de cambio, la presión sobre las tarifas y otros factores de negocio que un plan de TI no resuelve.
3. **Los siete dominios quedan cubiertos.** Ninguno queda sin al menos una fortaleza o una debilidad.

La versión final salió de comparar tres enfoques: uno corporativo y de mercado, uno por dominio de TI y uno de riesgo y cumplimiento. Del primero se tomó el contexto de negocio (F2, F3, A4). Del segundo, la cobertura de los dominios (D1 a D7). Del tercero, el orden por urgencia (A1, D3, A3).

### Respaldo de las fortalezas

| Factor | De dónde sale y qué prueba | En el PETI Colombia | Por qué se incluye |
|---|---|---|---|
| F1 | La declaración de seguridad de Perficient publica la certificación ISO/IEC 27001:2022, con el certificado ISMS-PE-101123 emitido por A-Lign (PUB-002). | §6.1 Seguridad; §5.1 motivadores; BRE-006; P1.1 | Es el control que los clientes ya exigen y la base para montar un sistema de gestión de IA. ISO/IEC 42001 usa la misma estructura de las normas de sistemas de gestión, así que se puede construir sobre el SGSI existente y no empezar de cero. |
| F2 | Perficient anunció el 26 de marzo de 2026 la evolución de su marca hacia servicios "AI-native" (PUB-003). En 2026 anunció alianzas con Lovable, como su primer socio de implementación empresarial (PUB-009), y con Gradial (PUB-010). | §1 Introducción; §5.1 motivadores | Muestra que la dirección ya decidió apostar por la IA. Es una fortaleza porque le da a TI un mandato claro para gobernarla. |
| F3 | Perficient es parte del Microsoft AI Business Solutions Inner Circle 2025-2026 (PUB-005), tiene especializaciones Brickbuilder de Databricks (PUB-006, PUB-007) y es Premier Partner de Snowflake desde junio de 2025 (PUB-008). | §5.1 motivadores; §6.1 Información; P1.7, P3.5 | Da acceso a plataformas de datos, a formación y a certificaciones sin tener que construirlas. Límite: las fuentes no prueban que la operación colombiana use esas plataformas. |
| F4 | En la cuenta analizada se usa un servicio externo de pruebas de seguridad continuas y análisis de composición de software (PRV-001). | §5.3 proceso PM02; §6.1 Sistemas de información | Es la base del pipeline DevSecOps que el plan propone (P2.3). Límite: es una sola cuenta, no una política de Perficient. |
| F5 | En la cuenta analizada cada proyecto tiene Product Manager, Line Manager y Technical Lead, se trabaja con Scrum, y los ambientes de desarrollo, pruebas y producción están separados (PRV-001). | §5.3 estructura; §6.1 Gobierno e Infraestructura | Hay roles a quienes asignar responsabilidades (RACI) y una separación de ambientes que cumple un control básico de ISO/IEC 27001. |
| F6 | En la cuenta analizada hay formación en línea, patrocinio de certificaciones aprobado por el Line Manager y capacitaciones obligatorias (PRV-001). | §6.1 Uso y apropiación; P1.5, P1.7 | El plan de certificaciones (P1.7) y la capacitación en IA (P1.5) se apoyan en un mecanismo que ya existe. |

### Respaldo de las debilidades

| Factor | De dónde sale y qué prueba | En el PETI Colombia | Por qué se incluye |
|---|---|---|---|
| D1 | En la evidencia revisada no se encontró un sistema de gestión de IA, un inventario de modelos ni controles sobre agentes (INT-001). En la cuenta analizada sí hay lineamientos de uso de IA (PRV-001). | §6.1 Seguridad e Información; BRE-001, BRE-002, BRE-008; P1.2 a P1.4 | Va primero porque contrasta con F2: la compañía se presenta como "AI-native", pero no puede demostrar cómo controla la IA que usa. |
| D2 | No se encontró un comité de TI con actas, una matriz RACI, una matriz de riesgos ni una guía de presupuesto de TI (INT-001). | §6.1 Gobierno; BRE-011; P2.8 | Sin estas instancias nadie aprueba, mide ni prioriza el plan. La guía del MinTIC exige una instancia que apruebe el PETI (Actividad 16). |
| D3 | Perficient dejó de reportar a la SEC con el Form 15-12G del 15 de octubre de 2024 (PUB-004). No se encontró un concepto legal sobre las obligaciones que siguen vigentes ni un registro de transferencias internacionales de datos por proyecto (INT-001). | §3 Marco normativo; BRE-016; P1.9; R04 | La operación colombiana trata datos de clientes del exterior, y la Ley 1581 regula las transferencias internacionales. Sin registro no se puede demostrar que se cumple. |
| D4 | No se encontraron misión, visión, catálogo de servicios ni tablero de indicadores de TI para la operación (INT-001). | §6.1 Estrategia; BRE-015; P2.8, P4.3 | Es el punto de partida de la estrategia de TI (Actividad 8 de la guía). |
| D5 | En la cuenta analizada, los hallazgos de seguridad y la conciliación de horas se pasan a mano entre herramientas (PRV-001). | §6.1 Sistemas de información; BRE-003, BRE-012; P2.2, P2.4 | El trabajo manual retrasa la corrección de vulnerabilidades y produce errores de conciliación. |
| D6 | No se encontró infraestructura como código ni tableros o alertas de costo de nube (INT-001). | §6.1 Infraestructura; BRE-007, BRE-013; P2.6, P2.7 | Sin infraestructura como código los ambientes no se pueden reproducir, y sin tablero de costos no se puede controlar el gasto (R07). |
| D7 | En la cuenta analizada el canal para pedir licencias de IA no está estandarizado, y no se mide cuántas células usan IA (PRV-001; INT-001). | §6.1 Uso y apropiación; BRE-005; P1.6; KPI-04 | Si no se mide la adopción, no se puede saber si la apuesta de F2 llega a los equipos. |

### Respaldo de las oportunidades

| Factor | De dónde sale y qué prueba | En el PETI Colombia | Por qué se incluye |
|---|---|---|---|
| O1 | Es una hipótesis del equipo (INT-001) con señales indirectas: firmas que compiten en el mismo mercado nearshore ya certifican su gobierno de IA para mostrárselo a sus clientes. Softtek obtuvo ISO/IEC 42001 en noviembre de 2025 [2]. | §5.1 motivadores; OC02; OETI01 | Si los competidores invierten en demostrar gobierno de IA, es porque sus clientes lo valoran. Límite: no hay una encuesta pública de clientes de Perficient que lo confirme. |
| O2 | ISO/IEC 42001:2023 se publicó el 18 de diciembre de 2023 y especifica los requisitos de un sistema de gestión de IA para quien provee o usa productos y servicios con IA [3]. NIST AI RMF 1.0 (enero de 2023) es un marco de adopción voluntaria. | §3 Marco normativo; BRE-001; P1.2, P4.2 | Son marcos ya publicados y reconocidos, así que no hay que inventar un modelo propio. ISO/IEC 42001 se puede certificar; NIST AI RMF se adopta. |
| O3 | El AICPA define SOC 2 como un examen de los controles de una organización de servicios en seguridad, disponibilidad, integridad del procesamiento, confidencialidad o privacidad. Lo piden sus clientes y socios para evaluar el riesgo de tercerizar [9]. | §3 Marco normativo; §6.1 Seguridad; BRE-014; P4.1 | Perficient es una organización de servicios con clientes regulados en Norteamérica. Un informe SOC 2 tipo II que incluya controles de IA responde a lo que esos clientes ya piden. Es un informe de atestación, no una certificación. |
| O4 | Las mismas fuentes de F3 (PUB-005 a PUB-008). | P1.7, P3.4, P3.5 | Las alianzas son una fortaleza interna. La oportunidad externa son los programas de formación y certificación que los socios ofrecen. |
| O5 | La matriz de tendencias del PETI (§6.3) cruza DevSecOps, infraestructura como código y observabilidad con los procesos PM01 y PM02. | §6.3 Tendencias; P2.3, P2.5, P2.6 | Son prácticas maduras, con herramientas disponibles, que atacan directamente D5 y D6. |
| O6 | COBIT 2019 (ISACA, 2018) está en las referencias del PETI y su objetivo APO06 cubre el presupuesto y los costos de TI. | §7 Situación objetivo (gobierno); P2.8 | Da una estructura conocida para cerrar D2 sin diseñar el gobierno desde cero. |

### Respaldo de las amenazas

| Factor | De dónde sale y qué prueba | En el PETI Colombia | Por qué se incluye |
|---|---|---|---|
| A1 | Perficient publica la fecha del certificado como "10/11/2026" (PUB-002). A-LIGN, el organismo que lo emitió, escribe sus fechas como mes/día/año; en otro certificado suyo se lee "Issue Date: 7/26/2019" [1]. Con esa lectura, el certificado vence el 11 de octubre de 2026. No se encontró evidencia pública de un certificado renovado. | §5.1 motivadores; BRE-006; P1.1; R02 | Es la amenaza más urgente: vence en el primer mes del plan y la certificación es una condición que imponen los clientes. |
| A2 | En abril de 2023, ingenieros de Samsung subieron código fuente interno a ChatGPT y la empresa prohibió las herramientas de IA generativa [4]. El OWASP Top 10 para aplicaciones con LLM 2025 pone la inyección de instrucciones en primer lugar (LLM01) e incluye la divulgación de información sensible (LLM02) y la autonomía excesiva de los agentes (LLM06) [5]. | R01, R05; BRE-008; P1.2, P1.4, P1.5 | La operación colombiana trabaja con código y datos de clientes y usa asistentes de IA (D1, D7). El caso de Samsung muestra que el riesgo ya se materializó en otras empresas. |
| A3 | La Superintendencia de Industria y Comercio inició 101 investigaciones por protección de datos en 2025, frente a 83 en 2024 y 55 en 2023, e impuso multas por COP 5.157 millones en lo corrido de 2025 [6]. México tiene una LFPDPPP nueva, vigente desde marzo de 2025 (PUB-014), y Chile tiene la Ley 21.719, con entrada en vigencia en discusión (PUB-013). | §3 Marco normativo; BRE-016; P1.9; R04 | La vigilancia de la Superintendencia crece año a año, y los proyectos que comparten datos con otros países de la región quedan sujetos a leyes nuevas. |
| A4 | Softtek, que se presenta como la firma que originó el modelo nearshore, obtuvo ISO/IEC 42001 con Applus+ Laboratories el 6 de noviembre de 2025 y dice ser la primera empresa de tecnología de Latinoamérica en lograrlo [2]. | Se relaciona con BRE-001 y P1.2 | Es una amenaza competitiva concreta: un rival directo ya puede demostrar ante los clientes lo que Perficient todavía no (D1). |
| A5 | El informe OSSRA 2026 de Black Duck encontró al menos una vulnerabilidad en el 87 % de las bases de código auditadas, vulnerabilidades de alto riesgo en el 78 % y componentes con cuatro o más años de atraso en el 92 % [7]. | R03; BRE-003, BRE-007; P2.2, P2.3 | La operación construye software para clientes con dependencias de código abierto. F4 detecta los problemas, pero la corrección depende de cerrar D5. |
| A6 | Según un informe de Deel citado por ENTER.CO, la contratación de talento colombiano por empresas extranjeras creció 49 % en 2025, y los desarrolladores de software están entre los perfiles más buscados [8]. | R06; OC04; P1.7, P2.1 | El talento que Perficient forma en Colombia tiene cada vez más ofertas directas del exterior. Las certificaciones (F6) y la documentación (P2.1) reducen la pérdida de conocimiento cuando alguien se va. |
| A7 | En la cuenta analizada la infraestructura opera en nube pública bajo responsabilidad compartida con el cliente (PRV-001). | R07, R08; P2.6, P2.7 | Varias mejoras del plan (infraestructura como código, control de costos) requieren permiso del cliente. Si no lo da, el proyecto se retrasa. |

## Cruce de estrategias (FO, FA, DO, DA)

El cruce combina los factores de la DOFA para decidir qué hacer con ellos:

| Tipo | Qué combina | Pregunta que responde |
|---|---|---|
| 🟩🟦 **FO** | Fortalezas + oportunidades | ¿Qué tenemos que nos permite aprovechar lo que ofrece el entorno? |
| 🟩🟧 **FA** | Fortalezas + amenazas | ¿Qué tenemos que nos sirve para frenar lo que nos amenaza? |
| 🟥🟦 **DO** | Debilidades + oportunidades | ¿Qué ofrece el entorno para corregir lo que nos falta? |
| 🟥🟧 **DA** | Debilidades + amenazas | ¿Dónde coinciden una debilidad y una amenaza, y cómo se reduce ese riesgo? |

Todas las estrategias son **propuestas** del equipo. Ninguna abre un proyecto nuevo: cada una lleva a brechas (§8) y proyectos (§9) que ya están en el PETI Colombia. Las 13 estrategias cubren los 25 proyectos del portafolio, así que todos los proyectos tienen origen en la DOFA.

### Proyectos del PETI Colombia (recordatorio)

El número del proyecto indica la fase: P1 es la fase 1 (meses 1 a 6, de octubre de 2026 a marzo de 2027), P2 la fase 2 (meses 7 a 12), P3 la fase 3 (meses 13 a 18) y P4 la fase 4 (meses 19 a 24, hasta septiembre de 2028). El mes 0 es septiembre de 2026. Los responsables son roles propuestos.

| Proyecto | Nombre | Meses | Responsable propuesto |
|---|---|---|---|
| P1.1 | Recertificación de ISO/IEC 27001:2022 | 0-5 | CISO |
| P1.2 | Sistema de gestión de IA | 1-6 | CISO, con CTO |
| P1.3 | Inventario de sistemas de IA | 1-4 | Arquitectura |
| P1.4 | Permisos como código para agentes de IA | 4-6 | DevSecOps |
| P1.5 | Capacitación en seguridad, IA y protección de datos | 1-8 | Talento humano, con CISO |
| P1.6 | Procedimiento de licencias de IA | 1-3 | PM y Line Manager, con CTO |
| P1.7 | Plan de certificaciones por rol | 1-5 | Talento humano, con CTO |
| P1.8 | Centro de excelencia de IA en Colombia | 3-6 | CTO |
| P1.9 | Concepto legal y registro de obligaciones (Ley 1581, SOX residual) | 1-3 | CTO, con Legal |
| P2.1 | Plantillas ALM homologadas | 7-10 | Technical Leads |
| P2.2 | Integración de pruebas de seguridad con la ALM | 9-11 | DevSecOps |
| P2.3 | Pipeline de CI/CD estandarizado | 8-12 | DevSecOps |
| P2.4 | Conciliación de tiempos con la ALM | 9-12 | Operaciones |
| P2.5 | Observabilidad estandarizada | 7-10 | SRE |
| P2.6 | Infraestructura como código | 7-12 | Arquitectura de nube |
| P2.7 | Tablero de costos de nube | 7-9 | FinOps |
| P2.8 | Formalización del gobierno y la estrategia de TI | 7-9 | CTO |
| P3.1 | RAG en producción para clientes | 13-18 | CoE de IA |
| P3.2 | Evaluación automática de modelos de lenguaje | 13-16 | CoE de IA |
| P3.3 | Agente conversacional en producción | 13-18 | CoE de IA y PM |
| P3.4 | Cierre del plan de certificaciones | 13-18 | Talento humano |
| P3.5 | Plataforma y catálogo de datos | 13-18 | Arquitectura de datos |
| P4.1 | Informe SOC 2 tipo II con controles de IA | 13-24 | CISO |
| P4.2 | Auditoría interna del sistema de gestión de IA | 19-21 | CISO y CoE de IA |
| P4.3 | Balance del PETI y arquitectura 2028-2030 | 21-24 | CTO |

### 🟩🟦 Estrategias FO: usar fortalezas para aprovechar oportunidades

| Cruce | Estrategia propuesta | Brechas | Proyectos | Por qué |
|---|---|---|---|---|
| F1 + O2 + O3 | Extender el SGSI certificado a un sistema de gestión de IA y llevar sus controles al informe SOC 2 | BRE-001 Sistema de gestión de IA; BRE-014 Informe SOC 2 con controles de IA | P1.2 Sistema de gestión de IA; P4.1 Informe SOC 2 tipo II con controles de IA; P4.2 Auditoría interna del sistema de gestión de IA | ISO/IEC 42001 tiene la misma estructura que ISO/IEC 27001, así que se reutilizan las políticas, la auditoría interna y la revisión por la dirección del SGSI que ya está certificado (F1). Después, el informe SOC 2 (O3) puede mostrar esos controles a los clientes. También responde a D1 y a A4: Perficient alcanza a los competidores que ya certificaron su gobierno de IA. |
| F2 + O1 | Crear un centro de excelencia de IA en Colombia y llevar casos de RAG y agentes a producción | BRE-001 Sistema de gestión de IA; BRE-005 Procedimiento de licencias de IA | P1.8 Centro de excelencia de IA en Colombia; P3.1 RAG en producción para clientes; P3.3 Agente conversacional en producción | La dirección ya se comprometió con ser "AI-native" (F2) y los clientes buscan IA que se pueda auditar (O1). El centro de excelencia se crea en la fase 1 y los casos en producción llegan en la fase 3, después de que el sistema de gestión de IA (P1.2) ya tenga controles. |
| F3 + F6 + O4 | Plan de certificaciones por rol, articulado con los socios | BRE-009 Formación en IA | P1.7 Plan de certificaciones por rol; P3.4 Cierre del plan de certificaciones | Las alianzas (F3) exigen personal certificado, los socios ofrecen formación (O4) y la cuenta ya tiene patrocinio de certificaciones (F6). Se ordena por rol lo que hoy depende de cada Line Manager. |
| F3 + O4 | Construir la plataforma y el catálogo de datos sobre las tecnologías de los socios | BRE-010 Plataforma de datos | P3.5 Plataforma y catálogo de datos | Perficient tiene alianzas con Databricks y Snowflake (F3), pero el diagnóstico no encontró una plataforma de datos unificada (§6.1). Usar la tecnología y el soporte de un socio cuesta menos que construir una plataforma propia. |

### 🟩🟧 Estrategias FA: usar fortalezas para frenar amenazas

| Cruce | Estrategia propuesta | Brechas | Proyectos | Por qué |
|---|---|---|---|---|
| F1 + A1 | Confirmar con A-Lign el estado del certificado y cerrar la recertificación | BRE-006 Recertificación ISO/IEC 27001 | P1.1 Recertificación de ISO/IEC 27001:2022 | Es la estrategia más urgente: el certificado vence el 11 de octubre de 2026 (A1). Como el SGSI ya existe (F1), se trata de mantenerlo, no de construirlo. Por eso P1.1 arranca en el mes 0, antes que el resto del plan. |
| F4 + A5 | Integrar las pruebas de seguridad al pipeline de CI/CD | BRE-003 Integración de hallazgos de seguridad con la ALM; BRE-007 Infraestructura como código | P2.2 Integración de pruebas de seguridad con la ALM; P2.3 Pipeline de CI/CD estandarizado | La cuenta ya hace pruebas continuas y análisis de dependencias (F4), pero los hallazgos se pasan a mano. Con la integración, una dependencia vulnerable (A5) se detecta y bloquea dentro del pipeline, en vez de esperar a que alguien la registre. |
| F6 + A6 | Usar las certificaciones y la documentación para retener talento y conservar el conocimiento | BRE-004 Plantillas ALM; BRE-009 Formación en IA | P1.7 Plan de certificaciones por rol; P2.1 Plantillas ALM homologadas | Las empresas del exterior contratan cada vez más talento colombiano (A6). Un plan de certificaciones visible (F6) es un motivo para quedarse, y las plantillas homologadas hacen que el conocimiento quede documentado cuando alguien se va. |

### 🟥🟦 Estrategias DO: corregir debilidades con oportunidades

| Cruce | Estrategia propuesta | Brechas | Proyectos | Por qué |
|---|---|---|---|---|
| D1 + O2 | Levantar el inventario de IA según ISO/IEC 42001 | BRE-002 Inventario de sistemas de IA | P1.3 Inventario de sistemas de IA; P3.2 Evaluación automática de modelos de lenguaje | No se puede gobernar lo que no se conoce. ISO/IEC 42001 (O2) pide definir el alcance del sistema de gestión, y para eso hay que saber qué modelos, proveedores y datos se usan (D1). La evaluación automática mide después la calidad de esos modelos. |
| D2 + D4 + O6 | Formalizar los comités, la RACI, el presupuesto y la estrategia de TI con COBIT 2019 | BRE-011 Comités y gobierno de TI; BRE-015 Estrategia de TI documentada | P2.8 Formalización del gobierno y la estrategia de TI; P4.3 Balance del PETI y arquitectura 2028-2030 | COBIT 2019 (O6) ya define objetivos para el gobierno y el presupuesto de TI (APO06), así que no hay que diseñarlos desde cero. Responde a las dos debilidades de gobierno (D2) y de estrategia (D4). El balance de la fase 4 cierra el ciclo y prepara el siguiente plan. |
| D5 + D6 + O5 | Automatizar la conciliación, estandarizar la observabilidad, usar infraestructura como código y controlar el costo de nube | BRE-007 Infraestructura como código; BRE-012 Conciliación de tiempos; BRE-013 Observabilidad y control de costos de nube | P2.4 Conciliación de tiempos con la ALM; P2.5 Observabilidad estandarizada; P2.6 Infraestructura como código; P2.7 Tablero de costos de nube | Son prácticas maduras con herramientas disponibles (O5) que atacan los flujos manuales (D5) y la falta de control de la infraestructura (D6). También reducen el sobrecosto de nube (A7). |

### 🟥🟧 Estrategias DA: reducir debilidades frente a amenazas

| Cruce | Estrategia propuesta | Brechas | Proyectos | Por qué |
|---|---|---|---|---|
| D1 + A2 | Definir permisos como código para los agentes y capacitar al personal en IA y datos | BRE-008 Permisos de agentes de IA; BRE-009 Formación en IA | P1.4 Permisos como código para agentes de IA; P1.5 Capacitación en seguridad, IA y protección de datos | El OWASP Top 10 para aplicaciones con IA incluye la autonomía excesiva de los agentes (LLM06), y los permisos limitan lo que un agente puede ejecutar. El caso de Samsung fue un error humano, y la capacitación ataca esa causa. Juntas reducen el riesgo de fuga (R01) mientras no exista sistema de gestión de IA (D1). |
| D3 + A3 | Pedir un concepto legal y llevar un registro de transferencias internacionales por proyecto | BRE-016 Cumplimiento de la Ley 1581 en proyectos | P1.9 Concepto legal y registro de obligaciones (Ley 1581, SOX residual) | La Superintendencia abre cada año más investigaciones (A3), y hoy no se puede demostrar qué datos salen del país en cada proyecto (D3). Se hace en los meses 1 a 3 porque los demás controles dependen de saber qué obligaciones aplican. |
| D7 + A2 | Crear un procedimiento único para pedir y aprobar licencias de IA | BRE-005 Procedimiento de licencias de IA | P1.6 Procedimiento de licencias de IA | Si no hay un canal claro para pedir herramientas aprobadas (D7), el personal termina usando herramientas no autorizadas, que es como se filtran código y datos (A2). Es el proyecto más corto de la fase 1 (meses 1 a 3). |

### Límites de esta DOFA

- O1 es una hipótesis con señales indirectas, no un dato medido con clientes de Perficient.
- F4, F5, F6, D5, D7 y A7 vienen de una sola cuenta de cliente (PRV-001). Describen cómo se trabaja ahí, no una política de Perficient para toda la operación.
- No se puede saber con fuentes públicas si la recertificación ISO ya se emitió (A1).
- Las fuentes [1] a [9] se consultaron el 8 de octubre de 2026 y todavía no están en el registro de evidencias. Para citarlas en el PETI hay que registrarlas antes como filas `PUB-`.

### Fuentes externas

1. A-LIGN Compliance and Security. (2019). *Certificate of registration: Alkemics SAS, ISO/IEC 27001* [Certificado; se usa solo para establecer el formato de fecha del organismo]. https://www.salsify.com/hubfs/Security/Certificat-Alkemics-ISO-27001.pdf
2. Softtek. (2025, 6 de noviembre). *Softtek, first technology company in Latin America to earn ISO 42001 artificial intelligence certification*. https://www.softtek.com/news-releases/softtek-first-technology-company-in-latin-america-to-earn-iso-42001-artificial-intelligence-certification
3. International Electrotechnical Commission. (2023, 18 de diciembre). *ISO/IEC 42001:2023 Information technology — Artificial intelligence — Management system*. https://webstore.iec.ch/publication/90574
4. Forbes Australia. (2023, 2 de mayo). *Samsung bans ChatGPT among employees after sensitive code leak*. https://www.forbes.com.au/news/innovation/samsung-bans-chatgpt-among-employees-after-sensitive-code-leak/
5. OWASP Foundation. (2024). *OWASP Top 10 for LLM Applications 2025*. https://genai.owasp.org/llm-top-10/
6. Superintendencia de Industria y Comercio. (2025, 14 de agosto). *Por violación a las normas de protección de datos personales, la Superintendencia de Industria y Comercio ha iniciado 101 investigaciones*. https://sedeelectronica.sic.gov.co/noticias/por-violacion-las-normas-de-proteccion-de-datos-personales-la-superintendencia-de-industria-y-comercio-ha-iniciado-101-investigaciones-e
7. Black Duck. (2026, 25 de febrero). *Open source trends: 2026 OSSRA report*. https://www.blackduck.com/blog/open-source-trends-ossra-report.html
8. ENTER.CO. (2026, 18 de marzo). *Empresas extranjeras están contratando más colombianos: estas son las áreas clave*. https://www.enter.co/?p=582237
9. AICPA & CIMA. (s. f.). *SOC 2: Reporting on an examination of controls at a service organization relevant to security, availability, processing integrity, confidentiality, or privacy*. https://www.aicpa-cima.com/cpe-learning/publication/soc-2-reporting-on-an-examination-of-controls-at-a-service-organization-relevant-to-security-availability-processing-integrity-confidentiality-or-privacy
