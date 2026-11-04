# Guion: DOFA

**Expone:** Luis Alberto De Avila Mosquera. **Se muestra:** [foda-perficient.drawio](foda-perficient.drawio) (la matriz) y, si preguntan por cálculos, [Matrices_DOFA_Porter_Perficient_Colombia.xlsx](Matrices_DOFA_Porter_Perficient_Colombia.xlsx) (hojas 1 a 4). El texto completo está en [Analisis_DOFA_Porter_Perficient_Colombia.docx](Analisis_DOFA_Porter_Perficient_Colombia.docx) y el respaldo de cada factor, en [dofa-final-perficient-colombia.md](dofa-final-perficient-colombia.md).

Abreviaturas: BRE = brecha (PETI §8), P = proyecto (§9), KPI = indicador (§10), R = riesgo (§11). PUB = fuente pública, PRV-001 = la cuenta de cliente analizada (no es política de Perficient) e INT-001 = análisis del equipo. Todos son IDs del registro de evidencias.

## En 30 segundos

> La DOFA es el diagnóstico de TI que pide la Actividad 6 de la guía del MinTIC. Tiene 6 fortalezas, 7 debilidades, 6 oportunidades y 7 amenazas, y cada factor tiene su evidencia. La tensión central es F2 contra D1: la compañía se presenta como "AI-native", pero no puede demostrar cómo controla la IA que usa. La amenaza más urgente es A1, el certificado ISO 27001, que vencía al inicio del plan. Del cruce salen 13 estrategias, y entre todas cubren los 25 proyectos del PETI. La MEFI da 2,27 y la MEFE 1,70, las dos por debajo de 2,5.

## Decisiones y su porqué

| Decisión | Por qué | Referencia |
|---|---|---|
| Una sola DOFA, con el dominio de TI entre corchetes | La guía *recomienda* una DOFA por dominio, pero no la exige. Una sola se lee completa, y los 7 dominios quedan cubiertos | Guía MGGTI.GE.ES.03, Actividad 6, p. 30 |
| Solo entra un factor si cumple 3 reglas: tiene evidencia, TI puede actuar sobre él y ayuda a cubrir los dominios | Por eso no están la tasa de cambio ni las tarifas: un plan de TI no las resuelve | Registro de evidencias; PETI §6.1 |
| Interno o externo según una pregunta: ¿Perficient lo controla? | Por eso las alianzas son F3 (tenerlas) y O4 (lo que ofrece el socio), y el certificado es F1 (el SGSI) y A1 (su vencimiento) | Criterio del material de clase |
| Los factores van por prioridad dentro de cada cuadrante | D1 va primero porque choca con F2. A1 va primero porque es la única amenaza con fecha | PETI §5.1 (motivadores) |
| Una ausencia se escribe como "no se encontró en la evidencia revisada" | No se puede probar con un documento que algo no existe. Se declara el alcance de lo que se revisó | INT-001 |
| Importancia de 1 a 5, MEFI y MEFE | El enunciado de la entrega ajustada preguntaba si la DOFA guía decisiones. Con pesos y un cruce puntuado, sí las guía | Plantillas del curso (EFI, EFE, 2a, 2d) |
| Corregimos la escala de la plantilla EFI | El .xls del curso tenía invertidos el 1 y el 2. Usamos la escala de Fred David: 1 = debilidad mayor, 2 = debilidad menor | Hoja "0 Guía" del libro de matrices |

## Factor por factor

| Factor | Qué dice | Evidencia | En el PETI |
|---|---|---|---|
| F1 | SGSI certificado ISO/IEC 27001:2022 | PUB-002 | BRE-006, P1.1. Sobre el SGSI se monta el sistema de gestión de IA (P1.2) |
| F2 | Posicionamiento "AI-native" y alianzas de IA (Lovable, Gradial) | PUB-003, PUB-009, PUB-010 | §5.1. Le da a TI el mandato para gobernar la IA (OETI01) |
| F3 | Alianzas con Microsoft, Databricks y Snowflake | PUB-005 a PUB-008 | P1.7, P3.5. Límite: no prueba que la operación colombiana use esas plataformas |
| F4 | Pruebas de seguridad continuas y análisis de dependencias | PRV-001 | Proceso PM02 (§5.3). Es la base de P2.3 |
| F5 | Roles definidos, Scrum y ambientes separados | PRV-001 | §5.3. Hay a quién asignar la RACI (P2.8) |
| F6 | Formación en línea y certificaciones patrocinadas | PRV-001 | P1.5, P1.7 |
| D1 | IA sin sistema de gestión, sin inventario y sin permisos para agentes | INT-001, PRV-001 | BRE-001, BRE-002, BRE-008; P1.2 a P1.4; KPI-08 |
| D2 | Sin comité de TI, RACI, matriz de riesgos ni presupuesto | INT-001 | BRE-011, P2.8, KPI-14. La guía pide una instancia que apruebe el PETI (Actividad 16) |
| D3 | Transferencias internacionales de datos sin registro; sin concepto legal tras la privatización | INT-001, PUB-004 | BRE-016, P1.9, R04 |
| D4 | Sin misión, visión, catálogo ni tablero de TI | INT-001 | BRE-015, P2.8, P4.3 |
| D5 | Los hallazgos de seguridad y las horas se pasan a mano | PRV-001 | BRE-003, BRE-012; P2.2, P2.4; KPI-05, KPI-06 |
| D6 | Sin infraestructura como código ni control de costos de nube | INT-001 | BRE-007, BRE-013; P2.6, P2.7; R07 |
| D7 | Adopción de IA sin medir y canal de licencias no estandarizado | PRV-001, INT-001 | BRE-005, P1.6, KPI-04 |
| O1 | Clientes que piden IA gobernada | **Hipótesis** (INT-001) | OC02, OETI01 |
| O2 | ISO/IEC 42001 y NIST AI RMF | Fuente [3] | BRE-001; P1.2, P4.2 |
| O3 | Informe SOC 2 tipo II con controles de IA | Fuente [9] (AICPA) | BRE-014, P4.1 |
| O4 | Formación y certificaciones de los socios | PUB-005 a PUB-008 | P1.7, P3.4, P3.5 |
| O5 | DevSecOps, infraestructura como código y observabilidad | PETI §6.3 | P2.3, P2.5, P2.6 |
| O6 | COBIT 2019 (APO06, presupuesto) | Referencias del PETI | P2.8 |
| A1 | Vencimiento del certificado ISO sin evidencia de recertificación | PUB-002, fuente [1] | BRE-006, P1.1, R02 |
| A2 | Fuga de código o datos e inyección de instrucciones por IA | Fuentes [4] (Samsung) y [5] (OWASP LLM) | R01, R05; BRE-008; P1.2, P1.4, P1.5 |
| A3 | Sanciones por la Ley 1581 (la SIC abrió 101 investigaciones en 2025) | Fuente [6]; PUB-013, PUB-014 | BRE-016, P1.9, R04 |
| A4 | Softtek certificó ISO/IEC 42001 en noviembre de 2025 | Fuente [2] | BRE-001, P1.2 |
| A5 | Vulnerabilidades heredadas de dependencias de código abierto | Fuente [7] (OSSRA 2026) | R03; P2.2, P2.3 |
| A6 | Rotación de personal hacia empleadores del exterior (+49 % en 2025) | Fuente [8] | R06; P1.7, P2.1 |
| A7 | El cliente no autoriza cambios en su infraestructura | PRV-001 | R07, R08; P2.6, P2.7 |

## El cruce (13 estrategias)

| Tipo (nombre del enunciado y del material de clase) | Estrategias | Proyectos |
|---|---|---|
| FO, ofensivas (atacar, maxi-maxi) | F1+O2+O3, F2+O1, F3+F6+O4, F3+O4 | P1.2, P4.1, P4.2, P1.8, P3.1, P3.3, P1.7, P3.4, P3.5 |
| FA, defensivas (defender, maxi-mini) | F1+A1, F4+A5, F6+A6 | P1.1, P2.2, P2.3, P1.7, P2.1 |
| DO, adaptativas (movilizar, mini-maxi) | D1+O2, D2+D4+O6, D5+D6+O5 | P1.3, P3.2, P2.8, P4.3, P2.4 a P2.7 |
| DA, de supervivencia (reforzar, mini-mini) | D1+A2, D3+A3, D7+A2 | P1.4, P1.5, P1.9, P1.6 |

Hay tres cruces que conviene saber explicar:
- **F1 + O2 + O3:** ISO/IEC 42001 tiene la misma estructura que ISO/IEC 27001, así que el sistema de gestión de IA se monta sobre el SGSI que ya existe, y después el informe SOC 2 lo muestra a los clientes.
- **F1 + A1:** como el SGSI ya existe, el trabajo es mantenerlo y no construirlo. Por eso P1.1 es corto y arranca en el mes 0.
- **D7 + A2:** sin un canal claro para pedir licencias, la gente usa herramientas no autorizadas, y así se filtra el código.

## Cifras de las matrices

MEFI 2,27 y MEFE 1,70, las dos por debajo de 2,5. Las estrategias con más puntaje son FA1 y DA1 (10), seguidas de FO1 y DO1 (9).

## Preguntas difíciles

**¿A1 sigue siendo amenaza si la fecha ya pasó?** La DOFA es del 8 de octubre. La fecha publicada, "10/11/2026" (PUB-002), es ambigua: puede ser el 11 de octubre o el 10 de noviembre. A-Lign escribe mes/día/año, así que tomamos la lectura más temprana. Al 21 de octubre no había evidencia pública de la recertificación. Es justo el ejemplo de por qué la DOFA se revisa cada trimestre.

**¿F4, F5 y F6 son de Perficient si salen de una sola cuenta?** No las presentamos como política de Perficient: están escritas como "en la cuenta analizada (PRV-001)".

**¿Dónde está el dato de O1?** No lo hay. Es una hipótesis (INT-001), y la señal indirecta es que Softtek invirtió en certificar ISO/IEC 42001.

**¿Por qué A2, A3 y A5 no salen de Porter?** Porter mira la competencia. Lo tecnológico y lo regulatorio sale de las tendencias (§6.3) y del marco normativo (§3).

**Las fuentes [1] a [9], ¿están en el registro de evidencias?** Todavía no. Se citan con URL y fecha de consulta en el documento, y hay que registrarlas como PUB- antes de llevarlas al PETI.

**¿Por qué no hicieron PEYEA ni BCG?** Piden estados financieros y ventas por unidad de negocio, y Perficient es privada desde el 2 de octubre de 2024 (PUB-001).

## Lo que no se debe decir

- "Perficient no tiene gobierno de IA." Se dice: "en la evidencia revisada no se encontró".
- "Certificación SOC 2." SOC 2 es un informe de atestación.
- Que las estrategias ya están en marcha. Son propuestas.
