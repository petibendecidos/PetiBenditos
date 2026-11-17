# Dashboard estratégico de gobierno de datos, IA y TI (ISO/IEC 38500:2024)

Entrega del curso Gobierno y Servicios de TI (Universidad Santiago de Cali, docente Jair Sanclemente Castro): "Cargar dashboard interactivo estratégico de métricas de Gobierno de TI - ISO 38500 2024. Métricas de Gobierno de Datos, IA y TI". Cierre: 18 de noviembre de 2026 a las 23:59. Equipo Firmes por la Gobernanza.

| Archivo | Qué es |
|---|---|
| [Dashboard_Gobierno_TI_ISO38500_Perficient_Colombia.pbix](Dashboard_Gobierno_TI_ISO38500_Perficient_Colombia.pbix) | **Lo que se sube.** Informe interactivo de Power BI Desktop con el modelo en estrella importado, 35 medidas DAX, 3 páginas visibles (**Resumen**, **Portafolio**, **Operación**) y 1 página oculta de detalle (**Hoja de vida**) |
| [Dashboard_Gobierno_TI_ISO38500_Perficient_Colombia.docx](Dashboard_Gobierno_TI_ISO38500_Perficient_Colombia.docx) | **Lo que se sube.** Justificación ejecutiva, correspondencia con la ISO/IEC 38500:2024, cambios frente al tablero del 4 de noviembre, catálogo de 18 indicadores, lectura al corte del mes 12 y límites |
| [dashboard-gobierno-iso38500.md](dashboard-gobierno-iso38500.md) | Fuente en Markdown del documento Word |
| [guia-exposicion-dashboard-iso38500.md](guia-exposicion-dashboard-iso38500.md) | Guía de estudio para la sustentación oral (no se entrega) |
| `capturas/` | Capturas de las tres páginas visibles (`p1-resumen.jpg`, `p2-portafolio.png`, `p3-operacion.png`); van incrustadas en el Word |
| [datos/modelo_gobierno_ti.xlsx](datos/modelo_gobierno_ti.xlsx) | Libro de 14 hojas (modelo en estrella) generado con semilla `38500` |
| [datos/control_corte_mes12.csv](datos/control_corte_mes12.csv) | Archivo de control para validar que Python y DAX arrojan exactamente las mismas cifras al mes 12 |
| [powerbi/tema-gobierno-ti.json](powerbi/tema-gobierno-ti.json) | Tema JSON aplicado al informe |
| [powerbi/medidas.dax](powerbi/medidas.dax) | Catálogo documentado de las 35 medidas DAX del modelo |

## Decisiones de diseño

- **Modelo en estrella y control numérico:** el script `scripts/powerbi_iso38500_datos.py` genera las 14 tablas y el CSV de control a partir de los CSV sintéticos del 4 de noviembre (`sintetico_vulnerabilidades.csv` y `sintetico_personas.csv`). Las 35 medidas DAX suman numeradores y denominadores antes de dividir para evitar errores de promedios ponderados y replicar al decimal el CSV de control.
- **Diseño acotado y gráfico:** frente a la primera propuesta de 5 páginas con matrices densas, se consolidó en 3 páginas visibles con botones de filtro (`Dominio`, `Tarea ISO`, `Fase`, `Objetivo`, `Severidad`, `Riesgo IA`) y gráficos limpios sin títulos ni subtítulos redundantes, manteniendo la página oculta **Hoja de vida** por obtención de detalles.
- **Metas oficiales del PETI §7:** se reemplazaron las metas supuestas del 4 de noviembre por las del año 1 del PETI Colombia v1.0, lo que explica el cambio de estado de `KPI-02`, `KPI-03`, `KPI-13` y el ajuste de `KPI-05` al valor mensual del mes 12.

## Cómo regenerar los datos y cambiar el origen

```powershell
python -m pytest scripts/tests/test_powerbi_iso38500.py -q
python scripts/powerbi_iso38500_datos.py docs/entregas-2026-11-04/dashboard/datos docs/entregas-2026-11-16/dashboard-iso38500/datos
python scripts/md_a_docx_simple.py docs/entregas-2026-11-16/dashboard-iso38500/dashboard-gobierno-iso38500.md docs/entregas-2026-11-16/dashboard-iso38500/Dashboard_Gobierno_TI_ISO38500_Perficient_Colombia.docx "Dashboard de gobierno de datos, IA y TI (ISO/IEC 38500:2024) — Trabajo académico, Equipo Firmes por la Gobernanza"
```

Los datos ya están importados en el `.pbix`: el archivo abre en cualquier equipo sin necesidad de reconfigurar rutas. Si se regenera `modelo_gobierno_ti.xlsx` en otra máquina y se desea pulsar **Actualizar**, ir a **Inicio → Transformar datos → Configuración de origen de datos → Cambiar origen** y seleccionar la ruta local del nuevo libro Excel.

## Pendientes

- Exportar el PDF desde Power BI Desktop (`Archivo → Exportar → Exportar a PDF`) si la plataforma solicita copia estática adicional al `.pbix` y al Word. El dashboard se sustenta en vivo en clase.
- Verificar los plazos legales de la Ley 1581 de 2012 usados como supuesto en `DAT-01` (10 días hábiles para consultas y 15 para reclamos).
- Corregir en la versión 1.1 del PETI la inconsistencia detectada en `KPI-03` (`METI03` exige 1 caso en el año 1, mientras `P3.1` y `P3.3` inician en el mes 13).
- Obtener evidencia pública o confirmación de la recertificación ISO/IEC 27001 (`PUB-002`, supuesta en el mes 5 para `KPI-07`).
