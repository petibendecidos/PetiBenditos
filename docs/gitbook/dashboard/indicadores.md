# Indicadores y reglas de cálculo

## Los 18 indicadores

Trece son del PETI (§10) y cinco son complementarios de gobierno de datos e IA, propuestos por el equipo. Las metas del año 1 vienen de las metas del PETI (§7); las de los complementarios son supuestos del equipo.

| Indicador | Dominio | Principio (§5) | Tarea | Elemento del marco | Meta año 1 | Meta año 2 | Se mide por | Proyecto |
|---|---|---|---|---|---|---|---|---|
| KPI-01 Ejecución acumulada del PETI | TI | 5.5 Supervisión | Monitorear | Desempeño | 55 % | 95 % | Operación | Todo el portafolio |
| KPI-02 Variación del costo de nube | TI | 5.3 Generación de valor | Evaluar | Desempeño | −5 % | −15 % | Operación | P2.7 |
| KPI-03 Casos de IA en producción | IA | 5.3 Generación de valor | Evaluar | Capacidad | 1 | 5 | Operación | P3.1, P3.3 |
| KPI-04 Adopción de IA en células | IA | 5.4 Estrategia | Dirigir | Capacidad | 85 % | 95 % | Célula | P1.6, P1.8 |
| KPI-05 Remediación de vulnerabilidades críticas | TI | 5.10 Gobierno del riesgo | Monitorear | Desempeño | 72 h | 24 h | Célula | P2.2, P2.3 |
| KPI-06 Conciliación de horas y tareas | TI | 5.9 Datos y decisiones | Monitorear | Desempeño | 90 % | 95 % | Operación | P2.4 |
| KPI-07 No conformidades mayores ISO/IEC 27001 | TI | 5.12 Viabilidad y desempeño | Monitorear | Rendición de cuentas | 0 | 0 | Operación | P1.1 |
| KPI-08 Cobertura del inventario de IA | IA | 5.10 Gobierno del riesgo | Evaluar | Política | 90 % | 100 % | Célula | P1.3 |
| KPI-09 Personal técnico certificado | TI | 5.4 Estrategia | Dirigir | Capacidad | 70 % | 90 % | Célula | P1.7 |
| KPI-10 Rotación entre células | TI | 5.10 Gobierno del riesgo | Dirigir | Capacidad | 50 % | 100 % | Célula | P2.1 |
| KPI-11 Ambientes con infraestructura como código | TI | 5.12 Viabilidad y desempeño | Dirigir | Capacidad | 60 % | 100 % | Operación | P2.6 |
| KPI-13 Informe SOC 2 sin salvedades | TI | 5.7 Participación de las partes interesadas | Involucrar | Rendición de cuentas | — | Sí | Operación | P4.1 |
| KPI-14 Sesiones de comité con acta | TI | 5.6 Rendición de cuentas | Monitorear | Rendición de cuentas | 90 % | 90 % | Operación | P2.8 |
| DAT-01 Solicitudes de titulares respondidas en plazo | Datos | 5.11 Responsabilidad social | Involucrar | Rendición de cuentas | 95 % | 98 % | Operación | P1.9 |
| DAT-02 Activos de datos clasificados | Datos | 5.9 Datos y decisiones | Dirigir | Política | 60 % | 90 % | Operación | P3.5 |
| DAT-03 Proyectos con transferencias internacionales registradas | Datos | 5.11 Responsabilidad social | Monitorear | Rendición de cuentas | 80 % | 100 % | Operación | P1.9 |
| IA-01 Sistemas de IA con evaluación de riesgo | IA | 5.10 Gobierno del riesgo | Evaluar | Política | 80 % | 100 % | Célula | P1.2 |
| IA-02 Sistemas de IA con supervisión humana definida | IA | 5.6 Rendición de cuentas | Dirigir | Delegación | 90 % | 100 % | Célula | P1.2, P1.4 |

Fórmulas de los complementarios:

| Indicador | Fórmula | Frecuencia | Responsable |
|---|---|---|---|
| DAT-01 | Solicitudes respondidas dentro del plazo / solicitudes recibidas × 100 | Mensual | Legal, con el CISO |
| DAT-02 | Activos clasificados / activos inventariados × 100 | Trimestral | Arquitectura de datos |
| DAT-03 | Proyectos con transferencia registrada / proyectos que tratan datos personales × 100 | Trimestral | CTO, con Legal |
| IA-01 | Sistemas registrados con evaluación de riesgo / sistemas registrados × 100 | Trimestral | CISO |
| IA-02 | Sistemas registrados con responsable de supervisión humana / sistemas registrados × 100 | Trimestral | Centro de excelencia de IA |

Las fórmulas de los KPI son las del PETI (§10).

## Reglas de cálculo

Son las mismas en el script que genera los datos y en las medidas de Power BI. Un archivo de control con el valor y el estado de cada indicador al mes 12 permite comprobar que dan lo mismo.

* **Valor:** suma de numeradores / suma de denominadores × escala. Se suman numeradores y denominadores; nunca se promedian porcentajes.
* **Valor al corte:** el del último mes con dato hasta el mes de corte. Un indicador trimestral muestra su último reporte y la fecha de ese reporte.
* **Meta del periodo:** la del año 1 hasta el mes 12; después, la del año 2.
* **Cumplimiento** (un decimal):
  * sin valor o sin meta: vacío;
  * si menor es mejor: 100 si el valor está en la meta o por debajo; 0 si la meta es 0 y el valor es mayor; si no, meta / valor × 100;
  * si mayor es mejor: valor / meta × 100, entre 0 y 100. Sirve también para el costo de nube, donde valor y meta son negativos.
* **Estado** (rangos del PETI §10): sin cumplimiento, "No evaluado"; 95 % o más, "Bueno"; más de 70 %, "Intermedio"; si no, "Bajo".
* **Indicadores de toda la operación:** el filtro de célula no los cambia.

## Casos que el informe resuelve

| Caso | Qué muestra |
|---|---|
| Filtro de célula sobre un indicador de toda la operación | El mismo valor, con la marca "toda la operación" |
| Indicador sin medición en el mes de corte | El último reporte y su fecha, no un vacío |
| Mes de corte antes de la línea base | "No evaluado", nunca 0 % ni "Bajo" |
| Una célula sin reporte en un mes | Un hueco en su serie, no una caída a cero |
