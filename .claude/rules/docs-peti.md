---
paths:
  - "docs/**"
  - "README.md"
---

# Reglas para docs/ y README.md

- **Solo lectura**: la guía (`MGGTI…pdf`), `Anexo 1…xlsx`, `Anexo 2…docx` y los dos PETI de referencia (`Plan-Estratégico…pdf`, `articles-274095…pdf`). No se editan, renombran ni convierten en el mismo sitio.
- **Restringidos**: `docs/informacion_jd-v2.md`, `docs/arquitectura-sistema-anonimizado.md`, `docs/evidencia-privada/`, `docs/privado/`. Se leen para entender el AS-IS; no se copian a ningún archivo versionado, ni se listan ni enlazan desde el README o el PETI. Borradores que necesiten ese detalle van a `docs/privado/`.
- **Insumos `docs/perficient_*.md`**: sus citas `[n]` no tienen bibliografía. No se usan como fuente de un hecho del PETI; se usan para saber qué buscar (skill `evidencias-peti`). No se reescriben para "arreglar" sus citas sin pedirlo.
- **PETI** (`docs/perficient_peti_v2_2026_2028.md`, regional v2.1, y `docs/perficient_peti_colombia_2026_2028.md`, Colombia v1.0; `docs/perficient_peti_plan_estrategico_2026_2028.md` es la v1.1 histórica y no se edita):
  - Antes de escribir un numeral, carga `guia-peti` y `redaccion-peti`.
  - Todo hecho nuevo lleva ID de `docs/registro-de-evidencias.md`; si no hay, `[EVIDENCIA: …]`.
  - Todo cambio de contenido actualiza el control de cambios (§16 en la v2.1, §15 en Colombia) y la versión del encabezado. Cambios de formato puro (tildes, una tabla mal alineada) no suben versión, pero se agrupan en una entrada al cerrar la sesión.
  - Tras tocar §7 a §11 (objetivos, brechas, portafolio, indicadores, riesgos), ejecuta el script de `trazabilidad-peti` (con la ruta del PETI Colombia como primer argumento si es ese el que cambió).
  - No renumeres IDs ni cambies títulos de numerales sin pedirlo: el índice usa anclas por título.
- **Registro de evidencias**: una fila por fuente abierta. No se borran filas; si una fuente deja de ser válida, se marca en "Alcance / limitación" y se registra la sustituta.
- **README**: si cambian las cifras del PETI (brechas, proyectos, fases) o la lista de documentos clave, se actualiza en el mismo cambio. No lista archivos restringidos.
- **Auditorías**: los informes van a `docs/auditoria/` solo tras la revisión de reidentificación.
- **Entregas del curso** (`docs/entregas-*/`, DOFA, Porter): cada carpeta de entrega lleva un `README.md` con qué se subió, de dónde sale y qué queda pendiente. Se generan con `scripts/` y sin la plantilla del MinTIC. Las mismas reglas de evidencia y reidentificación aplican.
