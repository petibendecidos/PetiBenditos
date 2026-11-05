# Modelo de madurez digital y mapa de calor

Entrega del curso Gobierno y Servicios de TI (Universidad Santiago de Cali, docente Jair Sanclemente Castro): "Identificar y analizar los resultados del modelo de madurez" con la *Herramienta para la Transformación Digital de las entidades públicas* del MinTIC. Equipo Firmes por la Gobernanza. La carpeta lleva la fecha en que se hizo (4 de noviembre de 2026); la fecha de cierre de la tarea no está registrada. Se basa en el PETI Colombia v1.0 ([perficient_peti_colombia_2026_2028.md](../perficient_peti_colombia_2026_2028.md)), el diagnóstico BSC del [22 de octubre](../entregas-2026-10-22/README.md) y el [registro de evidencias](../registro-de-evidencias.md).

| Archivo | Qué es |
|---|---|
| [Herramienta_Medicion_MD_Perficient_Colombia.xlsm](Herramienta_Medicion_MD_Perficient_Colombia.xlsm) | **Lo que se sube.** La herramienta del MinTIC diligenciada: cuestionario, modelo de madurez, mapa de calor y resultados |
| [Analisis_Madurez_Digital_Perficient_Colombia.docx](Analisis_Madurez_Digital_Perficient_Colombia.docx) | **Lo que se sube.** El análisis: cómo funciona la herramienta, sustento de cada respuesta, resultado y lectura del mapa de calor |
| [madurez-digital.md](madurez-digital.md) | Fuente de los dos archivos anteriores |
| [Validacion_Simulada_Mapa_de_Calor_Perficient_Colombia.docx](Validacion_Simulada_Mapa_de_Calor_Perficient_Colombia.docx) | Validación **simulada** del mapa de calor con los tres perfiles que pide el marco, asumidos por el equipo; incluye el guion del taller real. Fuente: [validacion-simulada-mapa-de-calor.md](validacion-simulada-mapa-de-calor.md) |
| `madurez.png`, `mapa_de_calor.png`, `resultados_mapa.png` | Vistas previas de las hojas llenas, exportadas por el script; van dentro del Word |
| [formato-docente/](formato-docente/) | Herramienta original, copiada de `D:\Descargas` |

## Resultado

| Dimensión | Promedio | Nivel |
|---|---|---|
| Personas y cultura digital | 2,75 | 3 |
| Procesos | 1,67 | 2 |
| Datos digitales y analítica | 2,00 | 2 |
| Tecnología digital | 2,50 | 2 |
| Nivel de madurez digital | 2,23 | **2. Iniciando** |

Puntos calientes del mapa (opción de tres iniciativas):

1. Entrega de software × células de entrega (valor 9, índice 5,00): IA en el ciclo de desarrollo (P1.6, P2.1).
2. Entrega de software × seguridad de la información (9; 4,25): sistema de gestión de IA y permisos para agentes (P1.2, P1.4).
3. Auditoría y cumplimiento × seguridad de la información (9; 4,00): recertificación ISO/IEC 27001 (P1.1).

La brecha más grave del modelo es de gobierno (pregunta 7, esquema organizacional, y pregunta 11, datos para decidir, ambas con 1), igual que en el diagnóstico BSC. El mapa entregado no la muestra caliente porque mide dónde rinde la tecnología 4.0; el análisis explica por qué P2.8 sigue siendo necesario. Aunque la herramienta pone la recertificación ISO en tercer lugar, se recomienda ejecutarla primero por su plazo externo.

El mapa entregado ya incluye las cinco correcciones de urgencia que encontró la validación simulada. Los tres cambios de criterio de esa validación, que llevarían el gobierno de TI al primer lugar, quedaron como propuesta para el taller real.

## Cómo se diligenció

Las respuestas y los cruces son del equipo (INT-001), con la regla de calificación y el sustento por pregunta que trae el análisis. La herramienta se llenó con un script y no a mano:

```
python scripts/generar_madurez_digital.py "docs/entregas-2026-11-04/formato-docente/Herramienta_Medicion_MD_Estado_Colombia.xlsm" docs/entregas-2026-11-04/madurez-digital.md docs/entregas-2026-11-04/Herramienta_Medicion_MD_Perficient_Colombia.xlsm
python scripts/md_a_docx_simple.py docs/entregas-2026-11-04/madurez-digital.md docs/entregas-2026-11-04/Analisis_Madurez_Digital_Perficient_Colombia.docx "Modelo de madurez digital y mapa de calor — Perficient, operación en Colombia — Trabajo académico, Equipo Firmes por la Gobernanza"
```

Necesita Excel. Lo que hace y por qué:

- **Cuestionario y "Calcular Nivel de Madurez".** Escribe los 17 puntajes y repite el cálculo de la macro `CalcularndMadurez` (promedio por dimensión, menos 0,01, redondeo de VBA). La macro original no se ejecuta porque abre un cuadro de mensaje que bloquea la automatización.
- **"Crear Matriz".** Repite la macro `matriz`: nombres de procesos y áreas, celdas con la lista de 0 a 9 y los colores del formato condicional. También abre un cuadro de confirmación.
- **"Calcular priorización de Iniciativas".** La macro `vecinos` lee los botones ActiveX "1, 2 o 3 Iniciativas", que Office no carga en un libro abierto por automatización (error 438). `scripts/vba_vecinos.py` saca el código VBA original del .xlsm, traduce a Python la rama de tres iniciativas y la ejecuta con las reglas de VBA para celdas vacías. Con la rama de una iniciativa se comprobó contra un cálculo independiente en 300 matrices aleatorias, sin diferencias.
- **Fila de prueba.** La plantilla trae una fila de prueba de 2019, oculta, en la fila 21 de "Resultados Heatmap". La macro escribe debajo de la última fila con datos, así que los resultados habrían quedado ocultos. El script la borra.

Si alguien abre el libro y vuelve a pulsar "Calcular Nivel de Madurez" o "Calcular priorización", la herramienta agrega filas nuevas con fecha de ese día; no borra las existentes.

## Erratas de la herramienta

- La hoja "Formulario de Preguntas" está protegida con contraseña; las celdas de respuesta no.
- La aclaración 10 dice que "1 es inexistente", aunque la escala es de 0 a 4. Se usó 0 a 4.
- La aclaración 15 repite la escala de la pregunta 12 ("tecnologías suficientemente robustas"). Se calificó el conocimiento de las tecnologías, que es lo que pregunta.
- Las preguntas 4 y 13 hablan de la ciudadanía; para Perficient se leyeron como los clientes.

## Segunda actividad: diagnóstico de madurez digital de CEIPA

Actividad "Aplicar la herramienta de Softwhere para medir la madurez digital" en https://api.mdigital.ceipa.edu.co/, con la nota "Adjuntar resultado en archivo PDF". Está en [diagnostico-ceipa/](diagnostico-ceipa/).

| Archivo | Qué es |
|---|---|
| [Respuestas_Diagnostico_CEIPA_Perficient_Colombia.docx](diagnostico-ceipa/Respuestas_Diagnostico_CEIPA_Perficient_Colombia.docx) | Guía para diligenciar la herramienta en línea: datos de la empresa, 33 puntajes de 0 a 10 con su sustento y lectura anticipada. Fuente: [respuestas-diagnostico-ceipa.md](diagnostico-ceipa/respuestas-diagnostico-ceipa.md) |
| `Madurez Digital 2025 B.pdf` | Material de clase (CINTEL, MinTIC y Softwhere), copiado de `D:\Descargas` |
| [Resultado_Diagnostico_CEIPA_Perficient_Colombia.pdf](diagnostico-ceipa/Resultado_Diagnostico_CEIPA_Perficient_Colombia.pdf) | **Lo que se sube.** El informe que generó la herramienta el 4 de noviembre de 2026 (diligenció Nicolás Chávez Oliveros). Copiado de `D:\Descargas` |
| [Analisis_Resultado_CEIPA_Perficient_Colombia.docx](diagnostico-ceipa/Analisis_Resultado_CEIPA_Perficient_Colombia.docx) | Análisis del resultado: niveles por dimensión, comparación con la MEFI, el BSC y la herramienta del MinTIC, hoja de ruta de CEIPA frente al PETI y observaciones sobre la herramienta. No lo pide la actividad; sirve para sustentar o como anexo. Fuente: [analisis-resultado-ceipa.md](diagnostico-ceipa/analisis-resultado-ceipa.md) |

La herramienta pide datos personales de quien responde (documento, correo y teléfono) y la aceptación de la política de datos de CEIPA, así que la diligencia un integrante y no un script. Para no marcar a mano las 33 preguntas, `scripts/llenar_encuesta_ceipa.js` se pega en la consola del navegador (F12) al llegar a la encuesta: marca los puntajes de la guía y avanza página por página. Las preguntas y opciones se tomaron del código público de la página, sin enviar nada.

**Resultado:** nivel básico, "conciencia inicial" (2 de 5). Tres dimensiones quedan en básico y el portafolio digital en intermedio, con productos y servicios digitales en avanzado. Coincide con la lectura anticipada (promedio de 4,6 sobre 10; dirección y evaluación digital, la más baja, con 2,8) y con la herramienta del MinTIC (nivel 2 de 4). De las doce acciones urgentes de la hoja de ruta de CEIPA, cuatro dependen de P2.8 (fase 2), lo que refuerza la propuesta de adelantar el comité, el presupuesto y un tablero mínimo de indicadores a la fase 1. La gestión del cambio no tiene proyecto en el PETI.

## Pendientes

- Validar el mapa de calor con los tres perfiles reales que pide el marco (dueño del proceso, conocedor del área y líder de la transformación). Ya hay una validación simulada, asumida por el equipo con un criterio escrito por perfil. Encontró cinco cruces que incumplían la regla de urgencia del propio equipo; ya se corrigieron en la herramienta y en el análisis. Propone además tres cambios de criterio que llevarían el gobierno de TI (P2.8) al primer lugar; esos esperan el taller real.
- Para repetir la priorización con otro mapa, sin Excel: `python scripts/priorizar_mapa_de_calor.py "docs/entregas-2026-11-04/formato-docente/Herramienta_Medicion_MD_Estado_Colombia.xlsm" docs/entregas-2026-11-04/validacion-simulada-mapa-de-calor.md cruces-validados docs/entregas-2026-11-04/madurez-digital.md`.
- Confirmar con el docente si se sube el .xlsm, el Word o los dos.
- Para llevar el nivel 2 como línea base al PETI Colombia hace falta una versión 1.1 con su entrada en el control de cambios (§15), junto con los cambios pendientes del diagnóstico BSC y del mapa estratégico.
