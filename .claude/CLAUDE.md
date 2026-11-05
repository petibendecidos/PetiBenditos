# PetiBenditos: contexto permanente del proyecto

Trabajo académico de Gobierno de TI: el equipo construye el **Plan Estratégico de Tecnologías de la Información (PETI) 2026-2028 de Perficient Inc.**, enfocado en su operación nearshore de Latinoamérica, **siguiendo la metodología del MinTIC de Colombia** como si Perficient fuera la entidad que formula su plan. El documento se escribe en español, en el registro de un plan institucional, y firma como "Equipo de Arquitectura y Gobernanza de TI — Perficient LATAM".

El PETI regional **va en la versión 2.1 (borrador)**, reestructurada según la plantilla del MinTIC, pero no está terminado ni auditado. De él se derivó el **PETI Colombia v1.0**, que es la versión que usa el curso. El trabajo pendiente es auditarlo contra la norma, completarlo y dejar una versión publicable sin evidencia restringida.

## Qué es norma, qué es referencia y qué es insumo

| Rol | Archivo | Uso |
|---|---|---|
| **Norma (metodología)** | `docs/MGGTI.GE.ES.01 - Guia de construccion PETI - Gobierno Digital-v. 3.0.pdf` | Guía del MinTIC, v3.0 de noviembre de 2023. **Dentro del PDF el código es MGGTI.GE.ES.03**; el nombre del archivo dice .01. En el PETI se cita como MGGTI.GE.ES.03. Define 4 fases y 17 actividades. |
| **Norma (estructura)** | `docs/Anexo 2. Plantilla PETI.docx` | Plantilla oficial del documento PETI (cartilla MinTIC 2023). Define capítulos y contenido mínimo. |
| **Norma (herramientas)** | `docs/Anexo 1. Herramientas_para_la_construccion_del_PETI.xlsx` | Formatos por actividad: DOFA, tendencias, estrategia de TI, catálogo de brechas, catálogo de iniciativas, hoja de vida de indicadores, plan de comunicaciones. |
| Referente del profesor | `docs/Plan-Estratégico-de-Tecnologías-de-la-Información_2025-V02.pdf` | PETI 2023-2026 de MinCiencias. El PETI de Perficient copia su estructura de capítulos. |
| Referente del profesor | `docs/articles-274095_recurso_1.pdf` | PETI del MinTIC: capacidades institucionales, catálogo de hallazgos, indicadores. |
| **Entregable** | `docs/perficient_peti_v2_2026_2028.md` → `docs/PETI_Perficient_2026-2028_v2.1.docx` | PETI vigente v2.1, 16 numerales según la plantilla. Se edita el Markdown y se regenera el Word con `.claude/skills/guia-peti/scripts/md_a_docx.py`. La v1.1 (`perficient_peti_plan_estrategico_2026_2028.md`) queda como histórica. |
| **Entregable (Colombia)** | `docs/perficient_peti_colombia_2026_2028.md` → `docs/PETI_Perficient_Colombia_2026-2028_v1.0.docx` | PETI Colombia v1.0: 16 brechas, 25 proyectos, 13 indicadores. Es la base de las entregas del curso desde septiembre de 2026. El .docx lleva en la portada "Equipo Firmes por la Gobernanza", agregado a mano y ausente del Markdown: si lo regeneras, vuelve a agregarlo. |
| Entregas del curso | `docs/dofa-final-perficient-colombia.md`, `docs/porter-5-fuerzas-perficient-colombia.md`, `docs/entregas-2026-10-21/`, `docs/entregas-2026-10-22/`, `docs/entregas-2026-10-29/`, `docs/entregas-2026-11-04/` | DOFA, Porter y las entregas del 21 de octubre (análisis DOFA y Porter con libro de matrices, Canvas, estrategia de TI, cadena de valor), del 22 de octubre (diagnóstico BSC), del 29 de octubre (mapa estratégico de TI y, en `segundo-parcial/`, copia de los 7 trabajos del parcial con su guion de exposición y el reparto) y del 4 de noviembre (herramienta de madurez digital del MinTIC con mapa de calor, cuyas macros no corren por automatización y el README de la carpeta explica cómo se llenó; y, en `diagnostico-ceipa/`, el diagnóstico en línea de CEIPA, que diligencia un integrante porque pide datos personales; y, en `dashboard/`, el dashboard de CIO del PETI en Grafana con datos sintéticos, publicado como instantánea pública). Índice y pendientes en el `README.md` de cada carpeta. Se generan con `scripts/` y se escriben sin la plantilla del MinTIC. Los originales se corrigen en su carpeta y se vuelven a copiar a `segundo-parcial/`. |
| Guías de estudio | `docs/justificacion-dofa-porter.md`, `docs/preparacion-sustentacion-peti-colombia.md`, `docs/entregas-2026-10-29/sustentacion-mapa-estrategico.md`, los `guion-*.md` de `segundo-parcial/` | Para defender en voz alta; no se entregan. |
| Control de evidencia | `docs/registro-de-evidencias.md` | IDs de evidencia (`PUB-001` a `PUB-025`, `INT-`, `PRV-`), clasificación y reglas de uso. Obligatorio para la versión publicable. |
| Insumos de investigación | `docs/perficient_*.md` (salvo el PETI) | Resúmenes de investigación sobre Perficient. **Citan con números `[84]` sin bibliografía**: son pistas, no fuentes. Ninguna cifra sale de ahí sin fuente primaria registrada. |
| **Restringido (local, fuera de Git)** | `docs/informacion_jd-v2.md`, `docs/arquitectura-sistema-anonimizado.md`, `docs/evidencia-privada/`, `docs/privado/` | Entrevistas y arquitectura de una cuenta de cliente (PRV-001, PRV-002). Ver reglas abajo. |

El detalle de la norma está en la skill `guia-peti`; léela antes de escribir o auditar cualquier capítulo.

## Reglas de manejo de información (no negociables)

- Los archivos restringidos **se pueden leer** para entender el AS-IS, pero **nada que permita reidentificar al cliente** (nombres, combinaciones de proveedor + tecnología + flujo + región + rol + fechas, nombres de tablas o componentes) se copia a un archivo versionado, a un commit, a un artefacto publicado ni a la respuesta de un subagente que vaya a un archivo. En el PETI solo aparece el ID (`PRV-001`) y el alcance autorizado.
- Una práctica observada en la cuenta analizada se redacta como "observada en la cuenta analizada (PRV-001)", nunca como política de Perficient ni de toda LATAM.
- Cada hecho del AS-IS lleva ID de evidencia. Lo que no lo tiene es hipótesis y se redacta como tal o se marca `[EVIDENCIA: qué falta]`.
- Toda iniciativa TO-BE es **Propuesta** hasta que tenga patrocinador, caso de negocio y aprobación. Los responsables del portafolio son roles propuestos.
- No se publica nada (artefacto, gist, PR público) con contenido del PETI sin que el usuario lo pida y sin pasar la revisión de reidentificación de `evidencias-peti`.

## Hechos del contexto que conviene no olvidar

- **Perficient es privada desde el 2 de octubre de 2024** (adquisición de EQT, PUB-001). PRFT/NASDAQ y los 10-K de la SEC son historia; SOX no se presenta como obligación vigente sin concepto de Legal/Finanzas.
- **Certificado ISO 27001:2022 ISMS-PE-101123 (A-Lign)**: la fuente pública muestra el vencimiento como `10/11/2026` (PUB-002). En formato de EE. UU. es 11 de octubre de 2026; en formato colombiano, 10 de noviembre. Cualquiera de las dos cae en los primeros meses del PETI (inicia en octubre de 2026). No escribas la fecha sin resolver la ambigüedad y nunca uses `dd/mm/aaaa` ambiguo en el texto. Al 21 de octubre de 2026 la lectura más temprana ya pasó y no hay evidencia pública de recertificación; la DOFA (A1) y la ficha de P1.1 del PETI Colombia todavía la tratan como fecha futura.
- La guía del MinTIC es para entidades públicas y se declara a sí misma "orientación o buena práctica, no obligatoriedad" (§2.2). Para Perficient es **marco metodológico adaptado**: MIPG, FURAG, trámites, OPAs y el Comité Institucional de Gestión y Desempeño no aplican tal cual; el PETI debe decir cómo se adaptan (por ejemplo, Comité Directivo del PETI en lugar del Comité Institucional).
- El horizonte del PETI es octubre de 2026 a septiembre de 2028 (24 meses, 4 fases semestrales). El PETI se escribió en septiembre de 2026; usa la fecha real de la sesión para saber qué plazos ya pasaron.
- Curso: Gobierno y Servicios de TI, Universidad Santiago de Cali, docente Jair Sanclemente Castro. El equipo firma las entregas del curso como "Equipo Firmes por la Gobernanza"; el PETI firma como "Equipo de Arquitectura y Gobernanza de TI — Perficient LATAM".

## Convenciones del PETI

- IDs vigentes en el documento: objetivos corporativos `OC01…`; objetivos de TI `OETI01…` y metas `METI01…`; brechas `BRE-001…`; oportunidades `OPT-001…`; proyectos `P<fase>.<n>`; indicadores `KPI-01…`; riesgos `R01…`; evidencia `PUB-/INT-/PRV-`. **No renumeres IDs existentes** sin que el usuario lo pida: otros capítulos los referencian. La equivalencia con los IDs del Anexo 1 (`B001`, `IT001`, `OETI01`, `METI01`, `IND.ES.01`) está en `trazabilidad-peti`.
- Todo cambio de contenido del PETI se registra en el numeral de control de cambios (§16 en la v2.1; §15 en el PETI Colombia) con versión, fecha, numerales y descripción, y actualiza la versión del encabezado.
- El README lista la estructura del repositorio y cifras del PETI (proyectos, brechas). Si cambias esas cifras en el PETI, actualiza el README en el mismo cambio.

## Cómo trabajar

| Tarea | Usa |
|---|---|
| Entender qué exige la guía o la plantilla para un capítulo | skill `guia-peti` |
| Redactar, reescribir, recortar o "humanizar" texto del PETI | skill `redaccion-peti` (incluye `estilo-natural.md`) |
| Buscar, registrar o citar una fuente; clasificar información; revisar reidentificación | skill `evidencias-peti` |
| Citar COBIT, TOGAF, ITIL, ISO 27001/42001, NIST AI RMF, SOC 2, normas colombianas | skill `marcos-referencia` |
| Comprobar la cadena objetivo → brecha → proyecto → indicador → riesgo | skill `trazabilidad-peti` (tiene script) |
| Auditoría completa del PETI | `/auditar-peti` (orquesta los agentes) |
| Conformidad con guía, plantilla y Anexo 1 | agente `auditor-conformidad` |
| Evidencia, clasificación y reidentificación | agente `auditor-evidencias` |
| Verificar en la web afirmaciones públicas sobre Perficient y marcos | agente `verificador-fuentes` |
| Commit | `/commit` |

## Herramientas locales

- `pdftotext` está disponible (Git Bash, mingw64); `pdfinfo` y `pdftoppm` no. `python` es 3.14 con `python-docx`, `python-pptx`, `openpyxl`, `xlrd` y `PyYAML` (en el site-packages del usuario: no uses `python -I`); no importes numpy (provoca segfault en este equipo).
- Word, Excel y PowerPoint están instalados: desde PowerShell, por COM, sirven para recalcular fórmulas de un .xlsx, contar páginas de un .docx o exportar una diapositiva a PNG y revisarla.
- Para leer los anexos `.docx`/`.xlsx` y los PDF sin pelear con la codificación, usa `python .claude/skills/guia-peti/scripts/extraer_referencias.py`; escribe texto plano en una carpeta temporal.
- Las rutas con tildes (el PDF de MinCiencias) fallan en `pdftotext` directo desde Bash; el script las resuelve.
