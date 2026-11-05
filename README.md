# PetiBenditos

Plan Estratégico de Tecnologías de la Información (PETI) 2026-2028 de **Perficient Inc.** para su operación nearshore de Latinoamérica. Es un trabajo académico de Gobierno de TI que aplica la metodología del MinTIC de Colombia (Guía MGGTI.GE.ES.03 v3.0, plantilla PETI y herramientas de construcción) a una empresa privada.

> **Estado documental:** PETI regional en borrador de trabajo (v2.1, septiembre de 2026); PETI Colombia v1.0 (septiembre de 2026) con DOFA, Porter y entregas del curso de octubre de 2026. La versión publicable solo puede usar evidencia clasificada como pública y validada en el [registro de evidencias](docs/registro-de-evidencias.md).

## Entregables del Primer Parcial

| Documento | Descripción |
|---|---|
| [PETI_Perficient_2026-2028_v2.1.docx](docs/PETI_Perficient_2026-2028_v2.1.docx) | **Entregable 1 (PETI vigente)** en Word, con los estilos de la plantilla del MinTIC. Al abrirlo, actualizar el índice (clic derecho > Actualizar campo) |
| [perficient_peti_v2_2026_2028.md](docs/perficient_peti_v2_2026_2028.md) | Fuente en Markdown del v2.1: 16 numerales según la plantilla, 18 brechas, 30 proyectos en 4 fases, 16 indicadores con hoja de vida, 11 riesgos |
| [Informe_Ejecutivo_Lineamientos_IA_USC.docx](docs/Informe_Ejecutivo_Lineamientos_IA_USC.docx) | **Entregable 3 (Informe Ejecutivo IA USC)** en Word formal, basado en la Circular Normativa DGI No. 001 de 2025 |
| [informe_ejecutivo_lineamientos_ia_usc.md](docs/informe_ejecutivo_lineamientos_ia_usc.md) | Fuente en Markdown del Informe Ejecutivo de Lineamientos de IA para la USC |
| [PETI_Perficient_Colombia_2026-2028_v1.0.docx](docs/PETI_Perficient_Colombia_2026-2028_v1.0.docx) | Versión simplificada enfocada en la operación de Colombia (fuente: [perficient_peti_colombia_2026_2028.md](docs/perficient_peti_colombia_2026_2028.md)): 16 brechas, 25 proyectos, 13 indicadores, Ley 1581 como obligación directa |
| [perficient_peti_plan_estrategico_2026_2028.md](docs/perficient_peti_plan_estrategico_2026_2028.md) | Versión 1.1 (histórica), estructurada sobre el PETI de MinCiencias antes de incorporar la guía y los anexos del MinTIC |
| [registro-de-evidencias.md](docs/registro-de-evidencias.md) | Fuentes con ID (`PUB-001` a `PUB-025`, `INT-`, `PRV-`), clasificación, alcance, reglas de uso y pendientes de validación |

Para regenerar el Word después de editar el Markdown:

```
python .claude/skills/guia-peti/scripts/md_a_docx.py docs/perficient_peti_v2_2026_2028.md docs/PETI_Perficient_2026-2028_v2.1.docx
```

## Entregas del curso sobre el PETI Colombia

| Documento | Descripción |
|---|---|
| [dofa-final-perficient-colombia.md](docs/dofa-final-perficient-colombia.md) | DOFA final (8 de octubre de 2026): 6 fortalezas, 7 debilidades, 6 oportunidades, 7 amenazas y 13 estrategias FO, FA, DO y DA que cubren los 25 proyectos |
| [porter-5-fuerzas-perficient-colombia.md](docs/porter-5-fuerzas-perficient-colombia.md) | Diagnóstico de las cinco fuerzas (13 de octubre de 2026), con su versión en Word ([Porter_5_fuerzas_Perficient_Colombia.docx](docs/Porter_5_fuerzas_Perficient_Colombia.docx)) y el diagrama editable ([.drawio](docs/porter-5-fuerzas-perficient-colombia.drawio)) |
| [entregas-2026-10-21/](docs/entregas-2026-10-21/README.md) | Entregas del 21 de octubre: DOFA y Porter ajustada (análisis y libro de matrices), modelo de negocio Canvas, estrategia de TI y cadena de valor |
| [entregas-2026-10-22/](docs/entregas-2026-10-22/README.md) | Entrega del 22 de octubre: diagnóstico de gestión y gobierno de TI mediante BSC (40 enunciados, radar y causas críticas) |
| [entregas-2026-10-29/](docs/entregas-2026-10-29/README.md) | Mapa estratégico de TI (BSC de TI) en draw.io: cuatro perspectivas, 14 objetivos, KPI, proyectos y relaciones causa-efecto. Incluye [segundo-parcial/](docs/entregas-2026-10-29/segundo-parcial/README.md): copia de los 7 trabajos del segundo parcial con un guion de exposición por trabajo, el reparto entre integrantes y las inconsistencias conocidas |
| [entregas-2026-11-04/](docs/entregas-2026-11-04/README.md) | Herramienta de medición de madurez digital del MinTIC diligenciada (nivel 2, "Iniciando") con su mapa de calor de procesos por áreas y el análisis de resultados; diagnóstico de madurez digital en línea de CEIPA (nivel básico, 2 de 5) con su guía de respuestas y el análisis del resultado; dashboard de CIO del PETI en Grafana con datos sintéticos de MOSTLY AI, publicado como instantánea pública ([dashboard/](docs/entregas-2026-11-04/dashboard/README.md)) |
| [justificacion-dofa-porter.md](docs/justificacion-dofa-porter.md) | Guía de estudio para defender la DOFA, Porter y las respuestas de la entrega ajustada. No se entrega |
| [preparacion-sustentacion-peti-colombia.md](docs/preparacion-sustentacion-peti-colombia.md) | Guía de estudio para la sustentación del PETI Colombia, numeral por numeral. No se entrega |
| `docs/Cuadro de Mando Integral Balanced Scorecard -BSC.pdf` | Material de clase (unidad 2): DOFA, cinco fuerzas, cadena de valor y modelo de negocio Canvas |

## Scripts

| Script | Qué genera |
|---|---|
| `scripts/generar_informe_uso_ia.py` | Informe de uso de IA con la firma del líder de equipo (la firma y el informe quedan fuera de Git) |
| `scripts/md_a_docx_simple.py` | Word con estilos neutros a partir de Markdown (tablas e imágenes), para entregas del curso (el PETI usa `md_a_docx.py`, con la plantilla del MinTIC) |
| `scripts/generar_madurez_digital.py` | Herramienta de madurez digital del MinTIC diligenciada; usa `scripts/excel_com_madurez.ps1` (Excel) y `scripts/vba_vecinos.py`, que ejecuta en Python la macro de priorización original |
| `scripts/llenar_encuesta_ceipa.js` | Se pega en la consola del navegador para marcar las 33 respuestas del diagnóstico de madurez digital de CEIPA |
| `scripts/priorizar_mapa_de_calor.py` | Priorización de un mapa de calor escrito en Markdown, sin Excel (se usó para la validación simulada) |
| `scripts/dashboard_semilla.py`, `dashboard_sintetizar.py`, `dashboard_construir.py`, `dashboard_comparar.py`, `dashboard_capturas.py` | Dashboard de CIO del PETI: tablas semilla, datos sintéticos con MOSTLY AI (Python 3.12 aparte), indicadores y tablero de Grafana, comparación semilla/sintético y capturas con Edge |
| `scripts/generar_matrices_dofa_porter.py` | Libro de matrices de la entrega DOFA y Porter |
| `scripts/generar_canvas_modelo_negocio.py` | Lienzo Canvas del modelo de negocio del área de TI |
| `scripts/generar_diagnostico_bsc.py` | Formato del docente del diagnóstico BSC, diligenciado y con radar; usa `scripts/word_com_bsc.ps1` (Word) |
| `scripts/generar_mapa_estrategico_bsc.py` | Mapa estratégico de TI (BSC de TI) en formato draw.io |

## Norma y referencias

| Rol | Documento |
|---|---|
| Metodología | `docs/MGGTI.GE.ES.01 - Guia de construccion PETI - Gobierno Digital-v. 3.0.pdf` (el código interno del documento es MGGTI.GE.ES.03) |
| Estructura | `docs/Anexo 2. Plantilla PETI.docx` |
| Formatos por actividad | `docs/Anexo 1. Herramientas_para_la_construccion_del_PETI.xlsx` |
| Referente del profesor | `docs/Plan-Estratégico-de-Tecnologías-de-la-Información_2025-V02.pdf` (PETI de MinCiencias 2023-2026) |
| Referente del profesor | `docs/articles-274095_recurso_1.pdf` (PETI del MinTIC) |

## Insumos de investigación

`docs/perficient_*.md`: resúmenes sobre la empresa (oferta, alianzas, seguridad, marcos de gobierno, reporte financiero histórico, propuesta de arquitectura). Sus citas numéricas `[n]` no tienen bibliografía; sirven para saber qué buscar, no como fuente de un hecho del PETI.

## Manejo de información

- Los insumos de entrevistas y de arquitectura de cliente son **restringidos**: permanecen locales, excluidos de Git, y no se listan ni se enlazan desde la documentación.
- Anonimizar los nombres no basta para publicar una arquitectura: las combinaciones de tecnologías, flujos y comportamientos también pueden reidentificar una cuenta.
- Antes de compartir el PETI, cada afirmación de la situación actual se valida por su ID de evidencia, su alcance, su propietario y su fecha de verificación.

## Trabajo con Claude Code

`.claude/` contiene el contexto del proyecto y las herramientas de apoyo:

- Skills: `guia-peti` (norma del MinTIC y scripts de extracción y de exportación a Word), `redaccion-peti` (estilo), `evidencias-peti`, `marcos-referencia`, `trazabilidad-peti` (con script de verificación), `/auditar-peti` y `/commit`.
- Agentes: `auditor-conformidad`, `auditor-evidencias`, `verificador-fuentes`.
