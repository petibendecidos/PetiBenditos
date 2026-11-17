# COBIT 2019: gobierno y gestión de la información y la tecnología de la empresa

Referencia para citar COBIT 2019 en el PETI y en las entregas del curso (diagnóstico de sensibilización gerencial, diagnóstico de control en TI, mapeos de proyectos a objetivos) y para defenderlo en la sustentación. Cada dato lleva su ID del registro de evidencias. Lo que ninguna fuente registrada respalda no está en este archivo y no se cita.

## Fuentes y qué se puede citar de cada una

| ID | Fuente | Qué trae | Qué no trae |
|---|---|---|---|
| PUB-030 | ITGI, *COBIT 3rd Edition: Implementation Tool Set*, julio de 2000 (copia no oficial en standards.narod.ru) | Origen y columnas del diagnóstico de sensibilización gerencial ("IT Governance Self-Assessment") y de los formularios del diagnóstico de control en TI | COBIT 2019. Está escrito sobre los 34 procesos de COBIT 3 |
| PUB-031 | K. Harisaiprasad, *COBIT 2019 and COBIT 5 Comparison*, ISACA, 27-abr-2020 | 37 → 40 procesos; objetivos nuevos (APO14, BAI11, MEA04); seis principios del sistema de gobierno; tres del marco; desempeño basado en CMMI; 10 de los factores de diseño | El texto del marco; la lista completa de factores de diseño |
| PUB-032 | J. Souza Neto, R. Almeida y M. Mira da Silva, *Defining Target Capability Levels in COBIT 2019*, ISACA, 18-mar-2019 | Niveles de capacidad de la figura 6.2; escala de logro de actividades; regla de la guía de diseño para el nivel objetivo | Las actividades de cada objetivo |
| PUB-033 | J. Lainhart, *Introducing COBIT 2019: The Motivation for the Update*, ISACA, 29-oct-2018 | Lanzamiento en el cuarto trimestre de 2018; componentes en lugar de habilitadores | El día exacto de publicación |
| PUB-034 | M. Thomas, ISACA, 10-dic-2018; A. Rafeq y N. Elangovan, ISACA, 26-may-2021 | Los siete componentes; ejemplos de códigos EG y AG | Número total de metas |
| PUB-035 | A. Rafeq, *COBIT Design Factors*, ISACA, 4-feb-2019 | Once factores de diseño en tres grupos; dos nombres de principios | La lista nominal de los factores |

Los libros oficiales (*COBIT 2019 Framework: Introduction and Methodology*, *Governance and Management Objectives*, *Design Guide*, *Implementation Guide*) se descargan con registro en isaca.org. Esta referencia se apoya en los artículos de ISACA que los citan; si un dato no está en ellos, no se usa.

## Qué es

- Marco de ISACA para el **gobierno y la gestión de la información y la tecnología de la empresa** (I&T). Se lanzó en el cuarto trimestre de 2018 con el nombre COBIT 2019 (PUB-033); reemplaza a COBIT 5 (2012).
- **No es certificable** para una organización. Se adopta y se evalúa la capacidad de sus procesos; las personas sí se certifican (COBIT Foundation, Design and Implementation).
- Para Perficient es **referencia metodológica** (tabla de relaciones de `SKILL.md`). El PETI Colombia lo cita en §3 como "referencia de gobierno" y en §7 para la guía de presupuesto (APO06).
- Separa **gobierno** (evaluar, dirigir y monitorear; lo ejerce el órgano de gobierno) de **gestión** (planificar, construir, ejecutar y monitorear; la dirección). Es la misma distinción de la ISO/IEC 38500 ([iso-38500.md](iso-38500.md)): el dominio EDM es el modelo evaluar-dirigir-monitorear de esa norma.

## Estructura

| Elemento | Contenido | Estado |
|---|---|---|
| Principios del sistema de gobierno | Seis (PUB-031). Dos de ellos, con nombre en la fuente: sistema de gobierno dinámico y adaptado a las necesidades de la empresa (PUB-035). Se cita el número y esos dos nombres | PUB-031, PUB-035 |
| Principios del marco de gobierno | Tres: basado en un modelo conceptual, abierto y flexible, alineado con los estándares principales | PUB-031 |
| Componentes del sistema de gobierno | Siete: procesos; estructuras organizativas; información; personas, habilidades y competencias; principios, políticas y procedimientos; cultura, ética y comportamiento; servicios, infraestructura y aplicaciones. En COBIT 5 se llamaban "habilitadores" | PUB-033, PUB-034 |
| Objetivos de gobierno y gestión | 40, en cinco dominios (tabla siguiente). Cada uno tiene propósito, prácticas, actividades con nivel de capacidad, métricas y componentes | PUB-031 (40); nombres del formato del docente |
| Cascada de metas | Necesidades de las partes interesadas → metas empresariales (códigos EG, por ejemplo EG06, continuidad y disponibilidad del servicio) → metas de alineamiento (códigos AG, por ejemplo AG07, seguridad de la información y privacidad) → objetivos de gobierno y gestión. No se cita el número total de metas | PUB-034 |
| Factores de diseño | Once, en tres grupos: contextuales, estratégicos y tácticos (PUB-035). PUB-031 nombra diez: estrategia, metas empresariales, perfil de riesgo, problemas relacionados con I&T, panorama de amenazas, requisitos de cumplimiento, rol de TI, modelo de abastecimiento de TI, métodos de implementación de TI y estrategia de adopción de tecnología | PUB-031, PUB-035 |
| Áreas de enfoque | Guías temáticas que ajustan el sistema de gobierno: pymes, seguridad de la información, riesgo, DevOps, entre otras. Su lista crece con el tiempo | Fuentes secundarias |

## Los 40 objetivos y su relación con el PETI Colombia v1.0

Los nombres en inglés son los del marco (en COBIT 2019 se formulan como resultado: *Ensured…*, *Managed…*). Los nombres en español son traducción del equipo: la edición de ISACA en español puede decirlo distinto. La última columna es la correspondencia que usó el diagnóstico de control del 16 de noviembre; sirve de base para el anexo de mapeo que §3 del PETI anuncia.

| Código | Nombre (inglés) | Nombre (español) | Brechas y proyectos del PETI |
|---|---|---|---|
| EDM01 | Ensured Governance Framework Setting and Maintenance | Asegurar el establecimiento y el mantenimiento del marco de gobierno | BRE-011; P2.8 |
| EDM02 | Ensured Benefits Delivery | Asegurar la entrega de beneficios | §9 (caso de negocio); sin proyecto |
| EDM03 | Ensured Risk Optimization | Asegurar la optimización del riesgo | BRE-011; P1.2, P2.8 |
| EDM04 | Ensured Resource Optimization | Asegurar la optimización de los recursos | BRE-011, BRE-013; P2.7, P2.8 |
| EDM05 | Ensured Stakeholder Engagement | Asegurar el compromiso de las partes interesadas | §12 |
| APO01 | Managed I&T Management Framework | Gestionar el marco de gestión de I&T | P2.8 |
| APO02 | Managed Strategy | Gestionar la estrategia | BRE-015; P2.8, P4.3 |
| APO03 | Managed Enterprise Architecture | Gestionar la arquitectura empresarial | P2.1, P2.6, P4.3 |
| APO04 | Managed Innovation | Gestionar la innovación | P1.8 |
| APO05 | Managed Portfolio | Gestionar el portafolio | §9; P2.8; KPI-01 |
| APO06 | Managed Budget and Costs | Gestionar el presupuesto y los costos | BRE-011, BRE-013; P2.7, P2.8 |
| APO07 | Managed Human Resources | Gestionar los recursos humanos | BRE-009; P1.7, P3.4; KPI-09, KPI-10 |
| APO08 | Managed Relationships | Gestionar las relaciones | — |
| APO09 | Managed Service Agreements | Gestionar los acuerdos de servicio | BRE-013, BRE-015; P2.5 |
| APO10 | Managed Vendors | Gestionar los proveedores | — (propuesto: indicador de proveedores) |
| APO11 | Managed Quality | Gestionar la calidad | BRE-004; P2.1, P2.3 |
| APO12 | Managed Risk | Gestionar el riesgo | §11; P1.2, P2.8 |
| APO13 | Managed Security | Gestionar la seguridad | BRE-001, BRE-006; P1.1, P1.2 |
| APO14 | Managed Data | Gestionar los datos | BRE-002, BRE-010, BRE-016; P1.3, P1.9, P3.5 |
| BAI01 | Managed Programs | Gestionar los programas | §9 (fases) |
| BAI02 | Managed Requirements Definition | Gestionar la definición de requisitos | BRE-004; P2.1 |
| BAI03 | Managed Solutions Identification and Build | Gestionar la identificación y construcción de soluciones | BRE-003, BRE-007; P2.3 |
| BAI04 | Managed Availability and Capacity | Gestionar la disponibilidad y la capacidad | BRE-013; P2.5, P2.7 |
| BAI05 | Managed Organizational Change | Gestionar el cambio organizativo | BRE-005, BRE-009; P1.5, P1.6 |
| BAI06 | Managed IT Changes | Gestionar los cambios de TI | BRE-007; P2.3, P2.6 |
| BAI07 | Managed IT Change Acceptance and Transitioning | Gestionar la aceptación y la transición de los cambios de TI | P2.3 |
| BAI08 | Managed Knowledge | Gestionar el conocimiento | P2.1; KPI-10 |
| BAI09 | Managed Assets | Gestionar los activos | BRE-002; P1.3 |
| BAI10 | Managed Configuration | Gestionar la configuración | BRE-004, BRE-007; P2.1, P2.6 |
| BAI11 | Managed Projects | Gestionar los proyectos | BRE-012; P2.1, P2.4 |
| DSS01 | Managed Operations | Gestionar las operaciones | BRE-013; P2.5 |
| DSS02 | Managed Service Requests and Incidents | Gestionar las solicitudes y los incidentes de servicio | BRE-005; P1.6 |
| DSS03 | Managed Problems | Gestionar los problemas | — (propuesto en P2.2 o P2.5) |
| DSS04 | Managed Continuity | Gestionar la continuidad | — (propuesta: brecha y proyecto nuevos) |
| DSS05 | Managed Security Services | Gestionar los servicios de seguridad | BRE-003, BRE-008; P1.4, P2.2, P2.3 |
| DSS06 | Managed Business Process Controls | Gestionar los controles de los procesos de negocio | BRE-012; P2.4 |
| MEA01 | Managed Performance and Conformance Monitoring | Gestionar el monitoreo del desempeño y la conformidad | §10; P2.8; KPI-01, KPI-14 |
| MEA02 | Managed System of Internal Control | Gestionar el sistema de control interno | P4.2 |
| MEA03 | Managed Compliance With External Requirements | Gestionar el cumplimiento de los requisitos externos | BRE-016; P1.9 |
| MEA04 | Managed Assurance | Gestionar el aseguramiento | BRE-014; P4.1, P4.2 |

Dominios: **EDM** (Evaluate, Direct and Monitor; gobierno) y, en gestión, **APO** (Align, Plan and Organize), **BAI** (Build, Acquire and **Implement**), **DSS** (Deliver, Service and Support) y **MEA** (Monitor, Evaluate and Assess).

## Gestión del desempeño: capacidad y madurez

COBIT 2019 mide el desempeño con un esquema basado en CMMI, de 0 a 5; COBIT 5 usaba la escala de procesos de la ISO/IEC 33000 (PUB-031).

- **Capacidad**: de un proceso (un objetivo). Cada actividad del objetivo tiene asignado un nivel; el proceso alcanza un nivel cuando cumple las actividades de ese nivel.
- **Madurez**: de un área de enfoque o del conjunto de objetivos que se evalúa.

| Nivel | Descripción de la figura 6.2 (PUB-032, traducción del equipo) |
|---|---|
| 0 | Le falta capacidad básica; enfoque incompleto para cumplir el propósito de gobierno o gestión |
| 1 | Cumple más o menos su propósito con un conjunto incompleto de actividades (inicial o intuitivo) |
| 2 | Cumple su propósito con un conjunto básico, pero completo, de actividades |
| 3 | Cumple su propósito de forma mucho más organizada, con activos de la organización (proceso definido) |
| 4 | Cumple su propósito, está bien definido y su desempeño se mide cuantitativamente |
| 5 | Lo anterior, y el desempeño se mide para mejorarlo de forma continua |

Escala de logro de cada actividad (PUB-032): completo (F), más de 85 %; en gran medida (L), de 50 % a 85 %; parcial (P), de 15 % a 50 %; no logrado (N), menos de 15 %.

Nivel objetivo según la guía de diseño (§7.2.4.1, citado en PUB-032): el puntaje de importancia que dan los factores de diseño fija el nivel; 75 o más, nivel 4; 50 o más, nivel 3; 25 o más, nivel 2; el resto, nivel 1. No todo objetivo debe llegar a 5.

## Las dos herramientas del curso

El docente entregó el 16 de noviembre de 2026 dos formatos para la actividad "Diagnóstico de sensibilización gerencial - Diagnóstico de control en TI". La entrega diligenciada, el análisis y el script están en `docs/entregas-2026-11-16/diagnosticos-cobit/` y en `scripts/generar_diagnosticos_cobit.py`.

### Diagnóstico de sensibilización gerencial (*Management Awareness Diagnostic*)

- Origen: el *Implementation Tool Set* de COBIT 3 (2000), sección "IT Governance Self-Assessment" (PUB-030). Pide a la dirección, por proceso: importancia, desempeño ("la combinación de importancia y desempeño es un indicador fuerte de riesgo"), quién lo hace (TI, otra área, externo, no se sabe), quién responde, si está formalizado (contrato, SLA o procedimiento documentado) y si se audita. Riesgo alto con "No se sabe" es "el mensaje más fuerte".
- El formato del docente (`COBIT 2019_Management-Awareness-Diagnostic_v1.0.xls`) lo adapta a los 40 objetivos de 2019 e **invierte la escala de desempeño**: 1 = muy bien, 5 = no se sabe o mal. En el original era al revés. Con la escala del formato, riesgo = importancia × desempeño (1 a 25); el equipo usó alto de 20 a 25, medio de 12 a 16 y bajo de 10 o menos.
- Erratas del formato: "Build, Acquire and Operate" (es *Implement*) y "APO13 Manage Security" (es *Managed*).
- El responsable se escribe como rol, no como nombre: los nombres de la cuenta analizada son restringidos.

### Diagnóstico de control en TI (*IT Control Diagnostic*)

- Origen: en COBIT 3 eran formularios de planeación de auditoría (formulario corto y largo de la entidad, auditoría previa, evaluación de riesgos, parte responsable, contratos y SLA) (PUB-030).
- El formato del docente (`Diagnostico_Control_TI_COBIT_2019.xlsx`) pide nivel de capacidad de 0 a 5 y observaciones por objetivo, con la escala de la ISO/IEC 33000 (la de COBIT 5).
- **Errores del formato** (corregidos en la entrega): 37 filas en lugar de 40; APO09 a APO12 corridos con nombres de COBIT 5 (proveedores, calidad, riesgos, seguridad); faltan APO09 (acuerdos de servicio), APO13 y APO14; BAI11 dice "problemas" (es proyectos); MEA02 y MEA03 invertidos; falta MEA04. Su hoja "Resultados " (con espacio al final) trae un gráfico que lee `Sheet1!C12:C52`.

### Resultado del 16 de noviembre de 2026 (para no recalcularlo)

Sensibilización: importancia promedio 4,2 y desempeño 3,5; 11 objetivos de riesgo alto (EDM01, EDM02, EDM03, APO01, APO02, APO05, APO06, APO14, DSS04, MEA01, MEA03), todos sin responsable conocido; 24 de 40 con responsable "No se sabe"; solo 4 formalizados y auditados, todos por el SGSI. Control: capacidad promedio 1,23 (EDM 0,80; APO 1,36; BAI 1,36; DSS 1,17; MEA 1,00) y 2,48 al mes 24 si se ejecuta el PETI; sin proyecto: APO10, DSS03 y DSS04.

## Cómo citarlo

- Por código y nombre del objetivo: "APO06 *Managed Budget and Costs* (gestionar el presupuesto y los costos)". No por número de proceso de COBIT 5 ni de COBIT 4.1 (PO, AI, DS, ME).
- "Nivel de capacidad" para un objetivo; "nivel de madurez" para un área de enfoque o el conjunto. No se mezclan.
- En la bibliografía: ISACA. (2018). *COBIT 2019 framework: Governance and management objectives*. ISACA. Y, si se usa la escala, *COBIT 2019 framework: Introduction and methodology*.

## Señales de alerta

- "Certificación COBIT" para Perficient o para la operación.
- Códigos de COBIT 5 con nombres de 2019 o al revés: APO13 "seguridad" en 2019 es correcto; APO12 "seguridad" es de un formato corrido; BAI11 "problemas" no existe (es DSS03).
- Escala de la ISO/IEC 33000 o de la ISO/IEC 15504 presentada como la de COBIT 2019.
- "Build, Acquire and Operate" o "Construir, adquirir y operar".
- Un nivel 3 o más sin un proceso estándar que la organización documente y audite; un nivel 4 sin medición cuantitativa.
- Un objetivo de COBIT en el PETI que no aparece en ninguna brecha, proyecto ni indicador, o un mapeo que fuerza un código para que todas las filas tengan uno.
