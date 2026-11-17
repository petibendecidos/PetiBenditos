# Indicadores y reglas

## Cuatro indicadores por célula

| Indicador | Cómo se calcula por célula y por mes | Meta | Proyecto del PETI que lo corrige |
|---|---|---|---|
| KPI-05 Remediación de vulnerabilidades críticas | Promedio de horas entre la detección y el cierre de las vulnerabilidades críticas detectadas en el mes | 72 h o menos | P2.2, P2.3 |
| ANS de soporte | Porcentaje de tickets resueltos dentro del acuerdo de nivel de servicio | 90 % (supuesto del equipo) | P2.5 |
| KPI-09 Personal técnico certificado | Personas con más de 6 meses y al menos una certificación, sobre las personas con más de 6 meses | 70 % | P1.7 |
| KPI-10 Rotación entre células | Personas rotadas en el último año, sobre el total de la célula | 50 % (meta intermedia supuesta) | P2.1 (riesgo R06) |

KPI-05, KPI-09 y KPI-10 son indicadores del PETI (§10). El ANS de soporte es complementario. KPI-09 y KPI-10 salen de una foto del personal y valen lo mismo todos los meses.

## Del valor al estado

**Cumplimiento** (un decimal, con tope de 100 %):

* Si mayor es mejor: valor / meta × 100.
* Si menor es mejor (KPI-05): 100 si el valor está en la meta o por debajo; si no, meta / valor × 100.

**Estado del indicador**, con los rangos del PETI (§10):

| Cumplimiento | Estado |
|---|---|
| 95 % o más | Bueno |
| Más de 70 % y menos de 95 % | Intermedio |
| 70 % o menos | Bajo |

**Estado de la célula:** el de su peor indicador.

## Casos especiales

| Caso | Qué hace el flujo |
|---|---|
| Una célula no tuvo vulnerabilidades críticas en el mes | KPI-05 queda sin dato y no cuenta como bueno; el estado sale de los otros indicadores |
| Una célula no tiene ninguna medición en el mes | Queda "Sin datos": se registra en el historial, pero no genera avisos ni aprobaciones |
| No hay células en rojo | No se manda la solicitud de aprobación; el informe sí sale |
| El flujo vuelve a correr sobre el mismo mes | El historial actualiza la fila de cada célula; la bitácora sí agrega las decisiones nuevas |
| El Comité no responde en tres días | La decisión queda como "Sin respuesta en el plazo" |
| La hoja todavía tiene los correos de ejemplo | El flujo se detiene con el mensaje "Reemplaza los correos de ejemplo en las pestañas Config y Celulas" |

Las reglas de cumplimiento y estado son las mismas del dashboard de CIO del 4 de noviembre y del dashboard de Power BI. Todos los casos de esta tabla tienen una prueba automática.

## La hoja de Google

| Pestaña | Contenido | Quién la escribe |
|---|---|---|
| Config | Mes de corte, correo del Comité, correo de copia | El equipo |
| Celulas | Célula, nombre, correo de los líderes | El equipo |
| Umbrales | Indicador, nombre, meta, si menor es mejor, unidad, proyecto | El equipo |
| Mediciones | Mes, etiqueta, célula, indicador, valor, tamaño de la muestra | Las herramientas de la operación (aquí, datos sintéticos) |
| Historial | Clave, ciclo, célula, estado, valor de cada indicador, fecha de ejecución | El flujo |
| Decisiones | Fecha, ciclo, célula, tema, justificación, decisión, responsable | El flujo |

Para cambiar una meta basta con editar la pestaña Umbrales. El flujo no tiene metas escritas en el código.
