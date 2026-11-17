# Análisis del diagnóstico BSC con una herramienta de analítica de datos

Tarea "Cargar ajuste nuevo proceso de análisis del diagnóstico gestión y gobierno TI alineado al BSC mediante herramienta de analítica de datos" del curso Gobierno y Servicios de TI (Universidad Santiago de Cali, docente Jair Sanclemente Castro). Abre el 12 y cierra el 18 de noviembre de 2026 a las 23:59. Equipo Firmes por la Gobernanza. Se hizo el 16 de noviembre de 2026.

La tarea retoma el formato del diagnóstico BSC del [22 de octubre](../../entregas-2026-10-22/README.md) (los mismos 40 enunciados y los mismos puntajes) y cambia la forma de analizarlo: el formulario pasa a ser un conjunto de datos que se analiza en Excel con una tabla estructurada, fórmulas, tablas dinámicas y segmentaciones. No se volvió a calificar: en el último mes no hay evidencia nueva sobre la operación que justifique cambiar un puntaje.

| Archivo | Qué es |
|---|---|
| [Analisis_BSC_Perficient_Colombia.xlsx](Analisis_BSC_Perficient_Colombia.xlsx) | **Lo que se sube.** La herramienta: hojas Inicio, Tablero (6 segmentaciones, 7 tablas dinámicas, tarjetas y 5 gráficos), Resumen (fórmulas y radar actual frente al mes 24), Prioridades (FILTER y SORTBY), Datos (40 registros), Parámetros (umbral de causa crítica, rúbrica y niveles) y Pivotes |
| [Analisis_Diagnostico_BSC_Perficient_Colombia.docx](Analisis_Diagnostico_BSC_Perficient_Colombia.docx) | **También se sube.** El análisis en 5 páginas: qué cambia en el proceso, tablero, resultados por elemento, perspectiva, ámbito, cobertura y respaldo, prioridades con análisis de sensibilidad y límites |
| [analisis-bsc.md](analisis-bsc.md) | Fuente del Word |
| [clasificacion-bsc.md](clasificacion-bsc.md) | Fuente de la hoja Datos: tema, perspectiva BSC, objetivo de COBIT 2019, respuesta y cobertura del PETI y puntaje al mes 24 de cada enunciado, con la razón |
| `tablero.png`, `resumen.png`, `prioridades.png` | Imágenes que exporta el script y van dentro del Word |

## Resultado

| Lectura | Resultado |
|---|---|
| Total | 182 de 400 (45,5 %), en construcción; 230 (57,5 %) al mes 24 si se ejecuta el PETI |
| Elemento crítico | Sincronización y despliegue: 36, bloqueador; 49 al mes 24 |
| Perspectiva BSC más baja | Financiera 3,5 (2 enunciados) y procesos internos 3,7 (9 enunciados, 4 causas críticas); procesos sigue última al mes 24 (4,6) |
| Gobierno frente a gestión | Los 6 enunciados de gobierno (EDM) promedian 3,8; los 34 de gestión, 4,7 |
| Cobertura del PETI | 10 cubiertos, 17 en parte, 6 sin respuesta (3, 12, 13, 22, 24, 27), 7 fuera del alcance de TI |
| Respaldo | Solo 11 de 40 puntajes citan fuente pública; 13 se apoyan solo en la cuenta analizada |
| Sensibilidad | Si las recomendaciones llevan a 6 los enunciados 12, 13, 16, 22, 24 y 27, el total llega a 244 (61 %), nivel funcional |

## Cómo regenerar

```
python scripts/generar_analisis_bsc.py docs/entregas-2026-10-22/Diagnostico_BSC_Perficient_Colombia.docx docs/entregas-2026-10-22/diagnostico-bsc.md docs/entregas-2026-11-16/analisis-bsc/clasificacion-bsc.md docs/entregas-2026-11-16/analisis-bsc/Analisis_BSC_Perficient_Colombia.xlsx
python scripts/md_a_docx_simple.py docs/entregas-2026-11-16/analisis-bsc/analisis-bsc.md docs/entregas-2026-11-16/analisis-bsc/Analisis_Diagnostico_BSC_Perficient_Colombia.docx "Análisis del diagnóstico BSC de gestión y gobierno de TI — Perficient, operación en Colombia — Trabajo académico, Equipo Firmes por la Gobernanza"
```

Necesita Excel. El libro se arma por COM porque openpyxl no crea tablas dinámicas ni segmentaciones. Los puntajes y el sustento se leen del diagnóstico del 22 de octubre (una sola fuente) y el texto de los enunciados, del Word diligenciado. El script se detiene si los totales por elemento no son 57, 46, 36 y 43 o si el libro no reproduce las cifras que calcula en Python. Si cambias la clasificación o una proyección, revisa las cifras del Word y de este README: el script las imprime al final.

Tres trampas de Excel por COM que el script ya resuelve:

- Con Excel oculto, inmovilizar paneles antes de escribir fórmulas que se desbordan (FILTER, SORTBY, incluso SEQUENCE) cierra Excel ("Error en la llamada a procedimiento remoto"). Los paneles se inmovilizan al final.
- pywin32 llama a Excel con la configuración regional del usuario: `NumberFormat` y las fórmulas de formato condicional se leen en español (en "0.0" el punto es separador de miles). El script toma el separador decimal de Excel y usa fórmulas de formato condicional sin funciones.
- Un texto como "1-2" se convierte en fecha al escribirlo; las bandas se llaman "1 a 2", "3 a 4", etc.

## Decisiones que se tomaron sin consultar

- Los puntajes no se recalificaron. La tarea pide un nuevo proceso de análisis, no un nuevo diagnóstico, y las entregas posteriores (mapa estratégico, flujo, dashboard) son trabajos del equipo, no cambios en la operación de Perficient.
- La proyección al mes 24 es criterio del equipo enunciado por enunciado, con la misma rúbrica. Sirve para medir el efecto del PETI; no es una meta.
- Se agregó la categoría "Sistema de gestión" a las cuatro perspectivas para los 13 enunciados que tratan del propio ciclo de planeación y seguimiento; meterlos a la fuerza en una perspectiva habría deformado los promedios.

## Pendientes

- Los cuatro cambios recomendados al PETI Colombia (evaluación de proveedores en P1.1, caracterización de procesos en P2.8, perspectivas BSC y mapa estratégico en §7, benchmarking en P4.3) repiten en parte los del 22 de octubre y se suman a los de las demás entregas; todos esperan la versión 1.1 del PETI.
