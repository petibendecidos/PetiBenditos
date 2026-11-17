# Qué muestra el dashboard

El dashboard "Gobierno de datos, IA y TI (ISO/IEC 38500:2024)" es un informe de Power BI para el Comité Directivo del PETI. Responde una pregunta por página: cómo van los indicadores, qué proyectos y riesgos piden una decisión, y si la TI, los datos y la IA están en meta.

> **Estado de esta sección.** El diseño, los indicadores y las reglas de cálculo están cerrados. El informe se está construyendo en Power BI Desktop. Las capturas y las cifras finales se agregan en [Evidencias del dashboard](evidencias.md) cuando el informe esté terminado.

## Para quién es y qué decide

| Usuario | Qué hace con el dashboard |
|---|---|
| Comité Directivo del PETI (trimestral) | Revisa el resumen por principio de la ISO, aprueba ajustes al portafolio y acepta o no el riesgo residual |
| Comité Táctico de TI (mensual) | Sigue los indicadores de TI, datos e IA por célula y prepara las decisiones que suben al Comité Directivo |

Las dos instancias son propuestas del PETI (§12).

## Cómo entra la ISO/IEC 38500:2024

* **Cada indicador tiene un principio** (§5.2 a §5.12), **una tarea del modelo** (involucrar a las partes interesadas, evaluar, dirigir o monitorear) y **un elemento del marco** (§7.2). La matriz principal agrupa los indicadores por principio.
* **Los 11 principios aparecen aunque alguno no tenga indicador.** Propósito (5.2) y Liderazgo (5.8) quedan vacíos a propósito: el tablero no los mide; se revisan en el comité y en la autoevaluación de gobierno de TI. Es un hallazgo, no un error.
* **Las decisiones se registran** con tema, justificación, responsable y fecha, como pide la guía de gobierno de TI de EIS. Son las mismas columnas de la bitácora del [flujo automatizado](../flujo/README.md).

## Qué cambió frente al tablero de Grafana del 4 de noviembre

| Problema del tablero anterior | Qué se hace ahora |
|---|---|
| 22 paneles en una sola página, todos con el mismo peso | 5 páginas de 5 a 7 visuales, una por pregunta del Comité |
| Bloques de color saturados y sin significado | Rojo solo para lo que está mal; verde, amarillo y gris como punto con su palabra; un color fijo por dominio |
| Series rectas y metas planas, que se veían inventadas | Ruido, meses sin reporte, frecuencias reales (trimestral, semestral, anual) y retrocesos |
| Paneles de tickets y tiempos de atención: gestión, no gobierno | Solo indicadores del PETI y cinco complementarios de datos e IA, cada uno con su principio y tarea de la norma |
| La instantánea no conservaba filtros | Filtros sincronizados, mes de corte movible, detalle por indicador y tendencia al pasar el cursor |
| Metas del mes 12 supuestas | Metas del año 1 tomadas del PETI (§7) |

## Cómo se usa

| Control | Qué hace |
|---|---|
| Mes de corte | Muestra lo que veía el Comité en ese mes (de octubre de 2026 a septiembre de 2027). Está en todas las páginas |
| Célula | Filtra los indicadores que se miden por célula. Los de toda la operación no cambian y lo dicen con la marca "toda la operación" |
| Dominio | TI, datos o IA |
| Clic derecho en un indicador → Obtener detalles | Abre su hoja de vida: fórmula, meta, frecuencia, responsable, principio, tarea, tendencia y decisiones ligadas |
| Pasar el cursor sobre un indicador | Muestra su tendencia mensual |
| Quitar filtros | Vuelve a la vista inicial |

## Qué se entrega

El archivo de Power BI (`.pbix`), su exportación en PDF, un documento Word y un video corto del recorrido. Todo queda en el repositorio del proyecto, carpeta `docs/entregas-2026-11-16/dashboard-iso38500/`; el video, fuera de Git si pesa más de 20 MB.
