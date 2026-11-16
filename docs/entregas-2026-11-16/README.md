# Autoevaluación de la madurez del gobierno de TI

Entrega del curso Gobierno y Servicios de TI (Universidad Santiago de Cali, docente Jair Sanclemente Castro): "Cargar resultados de la evaluación de la madurez de la gobernanza de TI", con el formato *IT Governance Self-Assessment* de Enterprise Information Services (EIS). Abre el 12 y cierra el 18 de noviembre de 2026 a las 23:59. Equipo Firmes por la Gobernanza. La carpeta lleva la fecha en que se hizo (16 de noviembre de 2026). Se basa en el PETI Colombia v1.0 ([perficient_peti_colombia_2026_2028.md](../perficient_peti_colombia_2026_2028.md)), el diagnóstico BSC del [22 de octubre](../entregas-2026-10-22/README.md), el modelo de madurez del [4 de noviembre](../entregas-2026-11-04/README.md) y el [registro de evidencias](../registro-de-evidencias.md).

| Archivo | Qué es |
|---|---|
| [Autoevaluacion_Gobierno_TI_Perficient_Colombia.xlsx](Autoevaluacion_Gobierno_TI_Perficient_Colombia.xlsx) | **Lo que se sube.** El formato del docente diligenciado: 31 respuestas (Yes, Partial o No) con su sustento en "Comments" y el nivel en la hoja Results |
| [Analisis_Autoevaluacion_Gobierno_TI_Perficient_Colombia.docx](Analisis_Autoevaluacion_Gobierno_TI_Perficient_Colombia.docx) | Análisis en español: cómo calcula la herramienta, criterio de respuesta, preguntas traducidas con su respuesta, resultado, comparación con los diagnósticos anteriores y proyección con el PETI. Sirve de anexo o para sustentar |
| [autoevaluacion-gobierno-ti.md](autoevaluacion-gobierno-ti.md) | Fuente de los dos archivos anteriores |
| `resultados.png` | Vista de la hoja Results llena, exportada por el script; va dentro del Word |
| [formato-docente/](formato-docente/) | Formato original, copiado de `D:\Descargas` |

## Resultado

| Sección | Puntos | Máximo | Porcentaje |
|---|---|---|---|
| 1. Estructuras organizacionales y de gobierno | 4 | 12 | 33,3 % |
| 2. Apoyo de la dirección | 4 | 10 | 40,0 % |
| 3. Planeación estratégica y operativa | 5 | 16 | 31,3 % |
| 4. Medición de la prestación del servicio | 2 | 10 | 20,0 % |
| 5. Organización de TI y gestión de riesgos | 6 | 14 | 42,9 % |
| Total | 21 | 62 | 33,9 %: **nivel 1, Inicial** (de 0 a 5) |

- 1 "Yes", 19 "Partial" y 11 "No". Los "No" se concentran en la instancia de gobierno (comité, seguimiento con la dirección, rol del responsable de TI) y en la medición (indicadores, costos, evaluación de inversiones).
- Es el resultado más bajo de los cuatro diagnósticos del curso (BSC 45,5 %; MinTIC nivel 2 de 4; CEIPA nivel 2 de 5), y es coherente: esta herramienta mide solo el gobierno, que fue lo más débil en todos.
- Si se ejecutan las fases 1 y 2 del PETI como están escritas, la proyección llega a 36 puntos, justo el mínimo del nivel 3. Nueve de los 15 puntos que se ganan dependen de P2.8.

Las respuestas son valoración del equipo (INT-001) con la regla de los diagnósticos anteriores: lo que no se puede demostrar no recibe "Yes". Los comentarios usan los mismos IDs de evidencia y las mismas categorías de herramientas del PETI; no nombran a la cuenta analizada.

## Cómo regenerar

```
python scripts/generar_autoevaluacion_gobierno_ti.py "docs/entregas-2026-11-16/formato-docente/04 - EIS - IT Governance Self-Assessment.xlsx" docs/entregas-2026-11-16/autoevaluacion-gobierno-ti.md docs/entregas-2026-11-16/Autoevaluacion_Gobierno_TI_Perficient_Colombia.xlsx
python scripts/md_a_docx_simple.py docs/entregas-2026-11-16/autoevaluacion-gobierno-ti.md docs/entregas-2026-11-16/Analisis_Autoevaluacion_Gobierno_TI_Perficient_Colombia.docx "Autoevaluación de la madurez del gobierno de TI — Perficient, operación en Colombia — Trabajo académico, Equipo Firmes por la Gobernanza"
```

Necesita Excel. El script llena el libro por COM y no con openpyxl, que borra las extensiones de formato condicional de la plantilla. Lee las respuestas de la tabla de la fuente, deja que Excel recalcule la hoja oculta Validation y se detiene si los puntos por sección no coinciden con la tabla "Resultado" de la fuente. Si cambias una respuesta, actualiza esa tabla, el texto del resultado y la proyección.

Las hojas Instructions, Assessment y Results están protegidas con contraseña. Se puede escribir en las celdas de respuesta y cambiar el alto de las filas, pero no el formato; por eso la agencia va corta ("Perficient Inc. - Operación en Colombia") y la fecha queda en el formato de la plantilla ("November 16, 2026").

## Pendientes

- Confirmar con el docente si basta el .xlsx o se sube también el Word del análisis.
- La plantilla está en inglés y los comentarios en español. Si el docente quiere todo en un idioma, se ajusta la columna "Comments" en la fuente y se regenera.
- Estado del certificado ISO/IEC 27001 (PUB-002): al 16 de noviembre de 2026 las dos lecturas de la fecha publicada ya pasaron y la página respondió HTTP 429. Si venció sin recertificación, las respuestas 4.5 y 5.2 bajan a "No" (19 puntos, sigue en nivel 1).
- Los tres cambios propuestos al PETI Colombia (adelantar P2.8 a la fase 1, evaluación posterior de proyectos y lecciones aprendidas, indicador de proveedores y meta de nivel 3 al año 1) se suman a los del diagnóstico BSC y del modelo de madurez; todos esperan la versión 1.1 del PETI.

## Segunda actividad: flujo automatizado de gobierno de TI con ISO/IEC 38500:2024 (en curso)

Tarea "Cargar flujo automatizado de Gobierno de TI - ISO 38500 2024" (cierre: 18 de noviembre de 2026, 23:59). Está en [flujo-iso38500/](flujo-iso38500/): un flujo de n8n que cada mes evalúa las doce células con cuatro indicadores del PETI, avisa a los líderes de las células en amarillo, pide aprobación al Comité por correo para las células en rojo y registra historial y decisiones en Google Sheets. Plan y avance: [docs/superpowers/plans/2026-11-16-flujo-gobierno-iso38500.md](../superpowers/plans/2026-11-16-flujo-gobierno-iso38500.md).

| Archivo | Qué es |
|---|---|
| `flujo-iso38500/flujo-gobierno-celulas.json` | El flujo para importar en n8n, con marcadores en lugar del ID de la hoja y de las credenciales (`scripts/flujo_gobierno_construir.py`) |
| `flujo-iso38500/hoja-gobierno-celulas.xlsx` | La hoja de Google en Excel, con correos de ejemplo (`scripts/flujo_gobierno_datos.py`) |
| `flujo-iso38500/flujo-gobierno-iso38500.md` | Borrador del documento de la entrega; falta el resultado de la ejecución y las capturas |

Pendiente: conectar Google, importar y ejecutar el flujo, tomar las capturas y generar el Word.
