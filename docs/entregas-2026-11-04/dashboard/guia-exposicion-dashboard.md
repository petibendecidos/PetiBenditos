# Guía del dashboard de CIO del PETI: qué se hizo y cómo exponerlo

Para quien exponga el dashboard del 4 de noviembre de 2026. No se entrega; sirve para entender el trabajo y defenderlo sin leer.

## En una frase

Se hizo un dashboard de CIO en Grafana que muestra cómo iría el PETI Colombia a mitad del plan (mes 12, septiembre de 2027), con datos sintéticos generados por MOSTLY AI; se publicó como un enlace público que se abre sin cuenta ni contraseña.

## 1. Dónde está cada cosa

| Qué | Dónde |
|---|---|
| **El dashboard (lo que se muestra)** | https://snapshots.raintank.io/dashboard/snapshot/XuadxcseLJupiHbunv3ZXRV9u23xjfag |
| Informe que se subió a la tarea | `docs/entregas-2026-11-04/dashboard/Dashboard_CIO_PETI_Perficient_Colombia.docx` (7 páginas, con el enlace y las capturas) |
| Fuente del informe | `docs/entregas-2026-11-04/dashboard/dashboard-cio-peti.md` |
| Índice de la carpeta | `docs/entregas-2026-11-04/dashboard/README.md` |
| Capturas (por si no hay internet) | `docs/entregas-2026-11-04/dashboard/capturas/`: `dashboard_completo.png` y una por fila (`seccion_1.png` a `seccion_5.png`) |
| Datos | `docs/entregas-2026-11-04/dashboard/datos/`: `semilla_*.csv` (inventados por reglas), `sintetico_*.csv` (generados por MOSTLY AI, los que usa el tablero), `series_mensuales.csv` e `indicadores_mes12.csv` (indicadores calculados) |
| Tablero de Grafana | `docs/entregas-2026-11-04/dashboard/grafana/`: `snapshot.json` (lo que se publicó) y `dashboard.json` (versión editable para importar en otro Grafana) |
| Scripts | `scripts/dashboard_semilla.py`, `dashboard_sintetizar.py`, `dashboard_construir.py`, `dashboard_comparar.py`, `dashboard_capturas.py` |
| PETI del que salen los indicadores | `docs/perficient_peti_colombia_2026_2028.md` (§9 portafolio, §10 indicadores, §11 riesgos, §12 gobierno) |

Para exponer no hace falta descargar nada: basta un navegador con internet y el enlace.

## 2. Qué pedía la tarea y qué se entregó

La tarea pedía cargar un dashboard y "un enlace y/o credenciales de la herramienta usada para el análisis de datos", usando datos sintéticos. El profesor dejó cuatro lecturas (CaixaBank Tech, Universitat Carlemany, ManageEngine y CAST) y una lista de plataformas: Tableau, n8n, Zapier, UiPath, Looker Studio, Datapad, Grafana y MOSTLY AI. No dio un método ni criterios de calificación.

Se entregó el enlace del dashboard (no necesita credenciales) y el Word con la justificación.

## 3. Qué se hizo, en orden

1. **Se leyeron las cuatro referencias** y se sacó de cada una lo que servía (sección 4).
2. **Se decidió el tipo de dashboard:** uno estratégico de CIO para el Comité Directivo del PETI, con tres capas (descriptiva, predictiva y prescriptiva sencilla).
3. **Se escogieron las plataformas:** Grafana para el tablero y MOSTLY AI para los datos, porque fueron las únicas de la lista que funcionaban sin crear cuentas y daban un enlace abierto.
4. **Se generaron tablas semilla** con un script: 1734 tickets de mesa de servicio, 2531 vulnerabilidades y 220 personas, todo inventado por reglas, con una mejora mes a mes por efecto de los proyectos del PETI.
5. **MOSTLY AI aprendió de cada tabla semilla y generó una tabla sintética** del mismo tamaño, en el computador, sin cuenta (modo local del SDK de código abierto). Tardó entre 75 y 145 segundos por tabla.
6. **Se compararon semilla y sintético** para ver si los datos sintéticos conservaban lo importante. Casi todo se conservó, con una excepción que hay que contar (sección 8).
7. **Se calcularon los indicadores del mes 12**, el semáforo y las proyecciones al mes 24 con un script en Python.
8. **Se armó el tablero en Grafana** (versión OSS 13.3.0 descargada en zip, sin instalar) con 5 filas y 20 paneles.
9. **Se publicó la instantánea** en snapshots.raintank.io, el servicio de Grafana Labs para compartir tableros. Antes se revisó que no llevara nada de la información restringida de la cuenta analizada.
10. **Se escribió el informe** y se tomaron las capturas.

## 4. De dónde sale cada cosa

| Elemento del tablero | Origen |
|---|---|
| Los 13 indicadores, sus fórmulas y sus metas (mes 12 y mes 24) | PETI Colombia, §10. KPI-12 no existe en esta versión del PETI |
| Rangos del semáforo (bueno ≥ 95 % de la meta, intermedio 71–94 %, bajo ≤ 70 %) | PETI Colombia, §10, primer párrafo |
| Los 25 proyectos, su fase y su mes de fin planeado | PETI Colombia, §9 |
| Qué proyecto corrige cada indicador ("Acción recomendada") | PETI Colombia, §9 (columna de indicador de cada proyecto); para KPI-10, el riesgo R06 del §11 |
| Usuario del tablero: Comité Directivo del PETI | PETI Colombia, §12: recibe el informe de indicadores cada trimestre |
| Tickets, vulnerabilidades y personas | Tablas semilla inventadas por reglas y luego sintetizadas con MOSTLY AI |
| Avance del portafolio, adopción de IA, conciliación de horas, inventario de IA, IaC, costo de nube | Series de un escenario escritas a mano en `scripts/dashboard_construir.py` (no salen de registros detallados) |
| Qué proyectos van atrasados (P1.8, P2.2, P2.3, P2.6) | Supuesto del escenario |
| Metas intermedias con asterisco (KPI-02, 03, 10, 11) | El PETI solo da meta al mes 24; la del mes 12 es interpolación lineal, decisión del equipo |
| Proyección al mes 24 | Regresión lineal sobre los últimos meses de cada serie |
| KPI-07 en 0 | Supuesto: la auditoría de recertificación ISO/IEC 27001 (P1.1) se hizo en el mes 5 sin no conformidades mayores |
| Clasificación descriptivo / predictivo / prescriptivo | Lectura de CaixaBank Tech |
| Contenido de un dashboard de CIO (finanzas, seguridad, desempeño del servicio, satisfacción) | Lectura de ManageEngine |
| Métricas que anticipan, no solo las que reaccionan; unir TI con negocio | Lectura de CAST |
| Que se entienda sin explicación y se adapte al usuario | Lectura de Universitat Carlemany (no trae método, solo características) |

## 5. Por qué se tomó cada decisión

| Decisión | Por qué | Qué se descartó |
|---|---|---|
| Dashboard estratégico de CIO sobre el PETI | El curso trabaja el PETI de Perficient desde septiembre y sus 13 indicadores ya existen; ManageEngine y CAST hablan justamente del dashboard del CIO | Un dashboard operativo genérico de mesa de servicio, sin relación con el PETI |
| Usuario: Comité Directivo del PETI | Es la instancia que el PETI pone a revisar indicadores cada trimestre | El CTO solo, o todo el personal |
| Corte al mes 12 | Es la mitad del plan y el PETI fija metas al mes 12 para casi todos los indicadores; al mes 2 (hoy) casi todo estaría "por medir" | Mostrar el mes actual |
| Tres capas (descriptiva, predictiva, prescriptiva) | CaixaBank dice que el tipo se escoge según la decisión. El comité tiene que saber cómo va (descriptivo), si llega (predictivo) y qué proyecto empujar (prescriptivo) | Solo descriptivo, que no ayuda a decidir |
| Prescriptivo por regla y no con aprendizaje automático | La relación indicador–proyecto ya está aprobada en el portafolio del PETI; un modelo no la mejoraría con datos inventados | Un modelo de recomendación |
| Grafana | Corre en el computador sin instalar ni crear cuenta, el tablero se define con un archivo y se publica como enlace público sin credenciales | Tableau Public, Looker Studio, Datapad: exigen cuenta (Looker además obliga a armarlo a mano) |
| MOSTLY AI en modo local | La tarea pide datos sintéticos y está en la lista del profesor; el SDK de código abierto no pide cuenta y los datos no salen del equipo | La plataforma web de MOSTLY AI (pide cuenta) |
| Tablas semilla + sintetización | MOSTLY AI necesita una tabla de la cual aprender; los datos reales de Perficient no son públicos. En la vida real se entrenaría con las exportaciones reales de la ALM y la mesa de servicio, y así se puede compartir el tablero sin exponer personas ni clientes | Inventar directamente los indicadores, sin datos sintéticos |
| Instantánea pública en vez de dar usuario y contraseña | El profesor la abre sin nada; no depende de que un computador del equipo esté encendido | Grafana local con credenciales (solo funciona en el computador del equipo) |
| n8n no se usó | El tiempo no daba; se deja como mejora: refrescar los datos y avisar cuando un indicador pase a "bajo" | Zapier y UiPath: exigen cuenta |

## 6. Cómo mostrarlo

### Antes de empezar

- Abre el enlace en el navegador y presiona **F11** (pantalla completa). Espera unos segundos a que carguen todos los gráficos; si alguno queda vacío, recarga con F5.
- Ten el Word abierto en otra pestaña por si falla el internet: las capturas están ahí.
- Trucos dentro del tablero: pasar el mouse por un gráfico muestra los valores; la "i" junto al título explica el panel; en el menú de cada panel (tres puntos) está **View**, que lo amplía.

### Recorrido sugerido (5 a 7 minutos)

| Fila | Qué señalar | Qué decir |
|---|---|---|
| Resumen ejecutivo | Medidor de KPI-01 (52 %), tarjetas 7 / 3 / 3, anillo del portafolio | "A mitad del plan van 13 de 25 proyectos terminados, 52 % contra una meta de 55 %. De 13 indicadores, 7 están bien, 3 en intermedio y 3 en bajo. Hay 4 proyectos atrasados y 8 que arrancan en la fase 3." |
| Semáforo (tabla) | Columnas Estado, Proyección mes 24 y Acción recomendada | "Esta tabla es el corazón: valor, meta, cumplimiento con los rangos del PETI, proyección al mes 24 y el proyecto que hay que mover. Los tres en bajo son KPI-05, KPI-10 y KPI-11." |
| Avance del portafolio | Línea real (azul) bajo el plan (gris); proyección (naranja) | "La capa predictiva: si seguimos al ritmo de los últimos meses, ¿llegamos? La tendencia dice que sí, pero es optimista, porque los proyectos de la fase 3 son más grandes." |
| Seguridad y cumplimiento | KPI-05 con la meta en rojo punteado | "Remediar una vulnerabilidad crítica toma 181 horas contra una meta de 72. Va bajando, pero al mes 24 llegaría a 102 horas cuando la meta es 24. Depende de P2.2 y P2.3, que están atrasados." |
| Servicio y operación | ANS, primer contacto, satisfacción; adopción de IA | "La mesa de servicio mejora en el año: ANS de 87 % a 93 %, primer contacto de 56 % a 72 %. La adopción de IA llega a 78 % contra 85 %, porque el centro de excelencia de IA (P1.8) está atrasado." |
| Costo y talento | Costo de nube, certificación por rol, KPI-10 y KPI-11 | "El costo de nube bajó 4,4 %. La rotación entre células (33 %) y la infraestructura como código (33 %) están en bajo frente a la meta intermedia de 50 %." |
| Cierre | Volver a la tabla | "La recomendación al comité es recuperar P2.2, P2.3 y P2.6 antes de abrir la fase 3 en el mes 13, porque los proyectos de esa fase se despliegan sobre el pipeline y los ambientes que esos tres dejan." |

Después, si hay tiempo, explicar los datos: "Nada de esto es real. Generamos tablas semilla por reglas, MOSTLY AI aprendió de ellas y produjo tablas sintéticas del mismo tamaño, y el tablero usa las sintéticas."

### Si quieren ver Grafana "por dentro"

Solo funciona en el computador de Juan Mateo, que tiene Grafana descargado. Allí se abre `http://localhost:3300/d/peti-colombia-cio` (usuario `admin`) y se pueden editar los paneles. Para la exposición basta el enlace público.

## 7. Preguntas que pueden hacer

| Pregunta | Respuesta |
|---|---|
| ¿Estos datos son reales? | No. Son sintéticos y el escenario es simulado. El PETI arrancó en octubre de 2026 y sus líneas base todavía se están midiendo; además, los datos operativos de Perficient no son públicos. |
| ¿Qué hizo exactamente MOSTLY AI? | Entrenó un modelo generativo por tabla con las tablas semilla y produjo tablas nuevas con las mismas columnas y el mismo comportamiento estadístico, sin copiar filas. Corrió en el computador con su SDK de código abierto, sin cuenta. |
| ¿Entonces para qué sintetizar si la semilla ya era inventada? | Para mostrar el flujo que se usaría con datos reales: se entrena con las exportaciones reales y se comparte la versión sintética, que no expone personas ni clientes. La semilla hace el papel de esos datos reales. |
| ¿Cómo saben que los datos sintéticos sirven? | Se compararon métricas de la semilla y del sintético (tabla en el Word): promedios y proporciones casi iguales, salvo las horas de remediación de las críticas. |
| ¿Qué tipo de dashboard es? | Estratégico, para el Comité Directivo. Según la clasificación de CaixaBank combina descriptivo, predictivo (tendencia al mes 24) y prescriptivo sencillo (acción recomendada). |
| ¿Por qué Grafana y no Tableau o Looker Studio? | Grafana corre sin cuenta y publica un enlace sin credenciales. Tableau Public y Looker Studio exigen cuenta, y Looker obliga a armar el informe a mano. |
| ¿Por qué no usaron n8n, Zapier o UiPath? | Son herramientas de automatización. Zapier y UiPath exigen cuenta; n8n quedó como mejora para refrescar los datos y enviar alertas. |
| ¿De dónde salen las metas? | Del §10 del PETI Colombia. Las que tienen asterisco son interpolación lineal de la meta del mes 24, porque el PETI no fija meta al mes 12 para esos indicadores. |
| ¿Por qué "En ejecución" está en 0? | En el mes 12 terminan las fases 1 y 2: sus proyectos o ya se cerraron (13) o están atrasados (4). La fase 3 arranca en el mes 13 (8 proyectos por iniciar). |
| ¿Cómo se calcula la proyección? | Regresión lineal sobre los últimos meses de cada serie, prolongada hasta el mes 24. Es sencilla a propósito; para KPI-01 es optimista. |
| ¿La "acción recomendada" la decide un algoritmo? | No. Es una regla: cada indicador apunta al proyecto que lo mueve según el portafolio del PETI. |
| ¿KPI-07 en 0 quiere decir que Perficient se recertificó? | No. Es un supuesto del escenario; no hay evidencia pública de la recertificación ISO/IEC 27001. |
| ¿Cuántos empleados tiene Perficient en Colombia? | El tablero no lo dice: las 220 personas y las 12 células son del escenario, no cifras de Perficient. |

## 8. Lo que conviene decir antes de que lo pregunten

- **KPI-05 empeoró por la sintetización.** MOSTLY AI casi duplicó las horas para remediar una vulnerabilidad crítica (126 horas en la semilla, 228 en el sintético), porque mezcló en parte las críticas con las medias y bajas, que tardan mucho más. Con la semilla, KPI-05 daría unas 98 horas (intermedio); con el sintético da 181 (bajo). Se intentó corregir: con más tiempo de entrenamiento no cambió; con cuatro veces más filas la diferencia bajó de casi cuatro veces a menos de dos. Se dejó así y se documentó, porque es una lección real: antes de decidir con datos sintéticos hay que revisar su calidad, sobre todo en indicadores que dependen de la relación entre dos columnas.
- **Todo es escenario.** Los atrasos de P1.8, P2.2, P2.3 y P2.6 son supuestos para que el tablero tenga algo que recomendar.
- **La lectura de Carlemany no trae método.** Por eso el informe propone un método de siete pasos armado con las otras lecturas.
- **El enlace es público.** Lo puede abrir cualquiera que lo tenga. Solo lleva indicadores del PETI y datos inventados; nada de la información restringida de la cuenta analizada.

## 9. Si algo falla

| Problema | Qué hacer |
|---|---|
| El enlace no abre o no hay internet | Mostrar las capturas del Word o de la carpeta `capturas/` |
| Un gráfico sale vacío | Recargar con F5 y esperar unos segundos |
| Piden cambiar algo en vivo | La instantánea no se edita. Los cambios se hacen en los scripts y se publica una instantánea nueva (eso lo hace Juan Mateo; el enlace cambia) |
