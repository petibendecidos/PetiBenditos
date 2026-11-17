# Guía de exposición: dashboard de gobierno de datos, IA y TI (ISO/IEC 38500:2024)

Material de apoyo para defender la entrega en voz alta. No se sube a la plataforma.

## 1. Idea central en una frase

El informe en Power BI traduce los 13 indicadores del PETI Colombia y cinco indicadores complementarios de datos e IA al marco de la ISO/IEC 38500:2024, permitiendo evaluar principios, dirigir el portafolio y monitorear la operación por célula desde octubre de 2026 hasta septiembre de 2027.

## 2. Recorrido sugerido (5 minutos)

1. **Página 1 (`Resumen`, corte por defecto `sep 2027`):** mostrar las cuatro tarjetas iniciales (**6 Bueno**, **6 Intermedio**, **5 Bajo**, **KPI-01 en 52 %**). Señalar el gráfico de barras de cumplimiento y el gráfico apilado por tarea de la ISO (Involucrar, Evaluar, Dirigir, Monitorear), más la tabla de decisiones recientes que sigue la guía EIS (`PUB-027`).
2. **Filtro de tiempo (`Mes de corte`):** cambiar de `sep 2027` a `mar 2027` (mes 6) para mostrar que todo el tablero recalcula retrospectivamente; destacar que `KPI-02` usa su último reporte válido si un mes no tiene medición y que `KPI-06` antes de su línea base pasa a **No evaluado** en lugar de cero. Volver a `sep 2027`.
3. **Filtro por célula (`Célula = C05`):** mostrar cómo `KPI-05` empeora a `396,8 h` en esa célula mientras `KPI-01` se mantiene en `52 %` con la marca `toda la operación`. Quitar el filtro.
4. **Hoja de vida (`Drillthrough`):** clic derecho sobre la barra de `KPI-05` → **Obtener detalles → Hoja de vida**. Mostrar la ficha del Anexo 1, la serie mensual frente a la meta de 72 h y el desglose por célula. Volver con el botón **Volver**.
5. **Página 2 (`Portafolio`):** mostrar **13 terminados, 4 atrasados (`P1.8`, `P2.2`, `P2.3`, `P2.6`), 0 en ejecución y 8 por iniciar**; la curva acumulada plan frente a real y los riesgos `R03` y `R06` en **Alto**.
6. **Página 3 (`Operación`):** usar los botones de severidad y riesgo de IA; destacar el embudo operativo de IA (`50` identificados → `46` registrados → `32` con evaluación de riesgo → `42` con supervisión humana) y las solicitudes de titulares (`79` totales, `15` fuera de plazo).

## 3. Decisiones de diseño con sustento en el PETI y la norma

- **Cuatro tareas del modelo (no tres):** la edición 2024 (`PUB-026`, §6.2) añadió *Involucrar a las partes interesadas* a las tres tareas clásicas de 2008 (evaluar, dirigir, monitorear).
- **Vista previa de la norma:** como el equipo solo dispone de la vista previa (`PUB-026`), de §5 en adelante se utilizan únicamente los nombres oficiales y las descripciones de Garibay (`PUB-029`) como fuente secundaria.
- **Bitácora de decisiones compartida con n8n:** sigue el estándar de la guía EIS (`PUB-027`) —tema, justificación, responsable y fecha— con el mismo esquema del flujo automatizado.

## 4. Preguntas difíciles y respuestas directas

| Pregunta | Respuesta |
|---|---|
| ¿Por qué Propósito (5.2) y Liderazgo (5.8) no tienen indicadores en el tablero? | Porque el tablero mide indicadores operativos y de portafolio; propósito y liderazgo son cualitativos y se evalúan en las actas del Comité y en la autoevaluación de madurez de EIS, no con promedios artificiales. |
| ¿Por qué `KPI-03` (Casos de IA en producción) sale en rojo (`0` frente a `1`) si `P3.1` y `P3.3` empiezan en el mes 13? | Es una inconsistencia real del PETI Colombia v1.0 que el tablero hace visible: la meta `METI03` pide un caso en el año 1, pero los proyectos que lo producen están programados en fase 3 (año 2). Se deja como hallazgo para corregir en la versión 1.1 del PETI. |
| ¿De dónde salen los datos? | Son sintéticos y reproducibles (`scripts/powerbi_iso38500_datos.py`, semilla `38500`): vulnerabilidades y personas vienen de las tablas generadas con MOSTLY AI el 4 de noviembre, y las series complementarias de IA, solicitudes y decisiones siguen reglas deterministas documentadas. No hay datos reales ni de clientes. |
| ¿Perficient "cumple" o está "certificada" en la ISO/IEC 38500:2024? | No. La ISO/IEC 38500 es una norma de principios y orientación, no certificable (`PUB-026`). Se usa como marco de referencia voluntario para estructurar el gobierno y los indicadores del PETI. |
| ¿Qué cambió frente al tablero de Grafana del 4 de noviembre? | Se pasó de una instantánea estática de 22 paneles a un modelo en estrella interactivo en Power BI con mes de corte, filtros sincronizados y metas oficiales del PETI §7; por eso cambian `KPI-02` (meta −5 %), `KPI-03` (inconsistencia de `METI03`), `KPI-13` (sin meta año 1) y `KPI-05` (medición mensual de 217,9 h en lugar de promedio trimestral). |
