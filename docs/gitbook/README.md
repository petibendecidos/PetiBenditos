# Gobierno de TI con ISO/IEC 38500:2024: flujo automatizado y dashboard

Documentación de dos herramientas de gobierno de TI construidas para la operación de Perficient en Colombia, dentro del Plan Estratégico de Tecnologías de la Información (PETI) 2026-2028:

* **Un flujo automatizado en n8n** que cada mes evalúa las doce células de entrega contra las metas del PETI, avisa a los líderes cuando un indicador se aleja de la meta, pide una decisión al Comité por correo cuando el caso es grave y deja registro de todo en Google Sheets.
* **Un dashboard en Power BI** para el Comité, con las métricas de gobierno de TI, de datos y de IA, organizadas según los principios y las tareas de la ISO/IEC 38500:2024.

> **Trabajo académico.** Curso Gobierno y Servicios de TI, Universidad Santiago de Cali, docente Jair Sanclemente Castro. Equipo Firmes por la Gobernanza, noviembre de 2026. No es un documento oficial de Perficient. Los datos de las dos herramientas son **sintéticos**: simulan doce meses de operación, de octubre de 2026 a septiembre de 2027.

## Para quién es

| Lector | Qué le sirve |
|---|---|
| Comité Directivo y Comité Táctico de TI (instancias propuestas en el PETI) | Qué decisiones pide el flujo, cómo leer el dashboard y qué significa cada estado |
| Equipo que opera las herramientas | Arquitectura del flujo, instalación, credenciales y problemas conocidos |
| Docente y evaluadores | Correspondencia con la ISO/IEC 38500:2024, evidencias de ejecución y límites |

## Cómo está organizada

| Sección | Contenido |
|---|---|
| [ISO/IEC 38500:2024 en una página](iso-38500.md) | Principios, modelo y marco de la norma, y cómo se usan aquí |
| [Flujo automatizado](flujo/README.md) | Qué hace, nodos, indicadores, evidencias de ejecución, instalación y operación |
| [Dashboard](dashboard/README.md) | Páginas, indicadores, reglas de cálculo y evidencias |
| [Cómo se conectan](conexion.md) | Qué produce el flujo y qué muestra el dashboard |
| [Fuentes y límites](fuentes-y-limites.md) | De dónde sale cada dato y qué no se puede afirmar |

## Las dos herramientas en el modelo de la norma

La ISO/IEC 38500:2024 organiza el gobierno de TI en cuatro tareas: **involucrar a las partes interesadas, evaluar, dirigir y monitorear**. Cada herramienta cubre una parte:

| Tarea | Flujo automatizado | Dashboard |
|---|---|---|
| Evaluar | Compara cada célula con las metas y le asigna un estado | Página 1 (resumen por principio) y página 5 (gobierno de IA) |
| Dirigir | Avisa a los líderes y pide la decisión del Comité | Página 2 (portafolio y riesgos) |
| Monitorear | Guarda el historial y la bitácora de decisiones cada mes | Páginas 3 y 4 (TI y gobierno de datos) |
| Involucrar a las partes interesadas | Manda el informe mensual al Comité | Indicadores de titulares de datos y de informe a clientes |
