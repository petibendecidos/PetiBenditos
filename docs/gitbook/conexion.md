# Cómo se conectan el flujo y el dashboard

Las dos herramientas cubren partes distintas del mismo ciclo de gobierno. **El flujo actúa:** evalúa cada mes, pide decisiones y las registra. **El dashboard muestra:** deja ver al Comité el estado de todos los indicadores, el portafolio, los riesgos y las decisiones tomadas.

| | Flujo automatizado | Dashboard |
|---|---|---|
| Herramienta | n8n, Gmail y Google Sheets | Power BI |
| Frecuencia | Cada mes, solo | Cuando el Comité lo abre, con el mes de corte que elija |
| Alcance | 4 indicadores por célula | 18 indicadores de TI, datos e IA, por célula y de toda la operación |
| Tareas de la norma | Evaluar, dirigir, monitorear, involucrar a las partes interesadas | Evaluar, dirigir, monitorear, involucrar a las partes interesadas |
| Produce | Historial por célula y bitácora de decisiones | Lectura para el Comité; no produce datos |

## Lo que comparten

* **Las mismas metas y reglas.** Cumplimiento y estado se calculan igual en los dos, con los rangos del PETI (§10): 95 % o más, bueno; más de 70 %, intermedio; 70 % o menos, bajo. KPI-05, KPI-09 y KPI-10 tienen la misma meta en los dos.
* **La misma bitácora de decisiones.** El flujo escribe fecha, ciclo, célula, tema, justificación, decisión y responsable. El dashboard muestra decisiones con esas mismas columnas, más la instancia que decidió y el indicador al que se refieren.
* **Los mismos datos sintéticos.** Los dos parten de las tablas sintéticas del 4 de noviembre: doce células, doce meses, vulnerabilidades, tickets y personal.

## Lo que no comparten

* El flujo usa el **ANS de soporte**, que no está en el dashboard. El dashboard deja fuera la gestión de tickets porque es operación, no gobierno; el flujo lo usa como alerta temprana por célula.
* El dashboard tiene indicadores que **no se miden por célula** (ejecución del PETI, costo de nube, ISO/IEC 27001, gobierno de datos), y el flujo no los evalúa.

## El ciclo completo

```
Mediciones del mes ─► FLUJO: evalúa cada célula ─► avisa / pide decisión ─► Historial y Decisiones (Google Sheets)
                                                                                      │
                                                                                      ▼
                         Comité ◄── DASHBOARD: estado de los 18 indicadores, portafolio, riesgos y decisiones
                           │
                           └─► ajusta metas en la pestaña Umbrales y prioridades del portafolio
```

## Siguiente paso propuesto

Hoy el dashboard lee su propio libro de datos. El siguiente paso sería que lea directamente las pestañas Historial y Decisiones que escribe el flujo, con el conector de Google Sheets de Power BI. Así, las decisiones que el Comité toma por correo aparecerían en el dashboard sin pasos manuales.
