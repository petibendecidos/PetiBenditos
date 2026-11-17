# Clasificación de los 40 enunciados del diagnóstico BSC

Fuente de la hoja Datos de `Analisis_BSC_Perficient_Colombia.xlsx`. El script `scripts/generar_analisis_bsc.py` junta esta tabla con el texto de los enunciados (formato diligenciado en `docs/entregas-2026-10-22/Diagnostico_BSC_Perficient_Colombia.docx`) y con los puntajes y el sustento (`docs/entregas-2026-10-22/diagnostico-bsc.md`). Los puntajes no se repiten aquí: tienen una sola fuente.

Columnas:

- **Tema:** nombre corto del enunciado para gráficos y tablas.
- **Perspectiva:** perspectiva del BSC a la que pertenece la capacidad que mide el enunciado. Los enunciados sobre el propio sistema de planeación y seguimiento (retos, misión, mapa, indicadores, metas, iniciativas, calendario de medición, corrección) van en "Sistema de gestión", que no es una perspectiva sino el mecanismo que las une. La alineación, el liderazgo y los sistemas de información van en aprendizaje y crecimiento, como capital organizacional y capital de información (Kaplan y Norton).
- **COBIT:** objetivo de COBIT 2019 más cercano, con los nombres de `.claude/skills/marcos-referencia/cobit-2019.md`. De él sale el ámbito: EDM es gobierno; APO, BAI, DSS y MEA son gestión.
- **Respuesta:** qué tiene hoy el PETI Colombia v1.0 para el enunciado.
- **Cobertura:** Cubierto (un proyecto o numeral lo resuelve), Cubierto en parte, Sin respuesta (es de TI y el PETI no lo trata) o Fuera del alcance de TI (lo decide el negocio o Talento humano).
- **Mes 24:** puntaje que tendría el enunciado si los 25 proyectos se ejecutan como están escritos, con la misma rúbrica del diagnóstico. Es una proyección del equipo (INT-001), no una meta aprobada.

<!-- clasificacion -->

| N.º | Tema | Perspectiva | COBIT | Respuesta | Cobertura | Mes 24 | Por qué |
|---|---|---|---|---|---|---|---|
| 1 | Segmentos de clientes objetivo | Cliente | APO02 | Los define el negocio | Fuera del alcance de TI | 8 | Sin cambio |
| 2 | Necesidades de clientes por segmento | Cliente | APO08 | Las levanta el área comercial | Fuera del alcance de TI | 7 | Sin cambio |
| 3 | Ventaja competitiva según satisfacción | Cliente | APO08 | Ninguna | Sin respuesta | 5 | Sigue sin medición propia de satisfacción |
| 4 | Monitoreo de competidores | Cliente | APO02 | Lo hace el negocio | Fuera del alcance de TI | 4 | Sin cambio |
| 5 | Necesidades de los empleados | Aprendizaje y crecimiento | APO07 | P1.5 y P1.7 | Cubierto en parte | 7 | El plan de certificaciones parte de las necesidades de cada rol; sigue sin encuesta de clima |
| 6 | Expectativas de los accionistas | Financiera | EDM05 | P1.9 | Cubierto en parte | 6 | El registro de obligaciones aclara lo que se exige tras la privatización; las expectativas de EQT siguen sin conocerse |
| 7 | Vigilancia de tendencias | Sistema de gestión | APO04 | P1.8 y revisión anual del PETI (§12) | Cubierto en parte | 6 | El CoE de IA evalúa herramientas nuevas; no cubre tendencias económicas ni sociales |
| 8 | Retos estratégicos | Sistema de gestión | APO02 | Motivadores (§5.1) y aprobación del PETI (§12) | Cubierto | 8 | Retos escritos y aprobados por el Comité Directivo |
| 9 | Propuesta de valor diferenciada | Cliente | APO02 | P3.1 y P3.3 (KPI-03) | Cubierto en parte | 7 | Los casos de IA con métricas muestran la diferencia; los competidores ofrecen algo parecido |
| 10 | Modelo de negocio comunicado | Sistema de gestión | APO02 | Lo define el negocio | Fuera del alcance de TI | 5 | Sin cambio |
| 11 | Desempeño de procesos | Procesos internos | MEA01 | P2.4 y P2.5 (KPI-05, KPI-06) | Cubierto en parte | 6 | Dos procesos con indicador medido; PE01 y PV01 siguen sin soporte de TI |
| 12 | Desempeño de proveedores y socios | Procesos internos | APO10 | Ninguna | Sin respuesta | 3 | Sin cambio |
| 13 | Benchmarking | Cliente | APO02 | Ninguna | Sin respuesta | 4 | Sin cambio |
| 14 | DOFA con datos de desempeño | Sistema de gestión | APO02 | DOFA (§6.2), revisión anual (§12), datos de P2.4 y P2.5 | Cubierto en parte | 7 | La revisión anual ya tiene datos de procesos; faltan los de proveedores y el benchmarking |
| 15 | Visión, misión y valores | Sistema de gestión | EDM01 | P2.8 (BRE-015) | Cubierto en parte | 6 | Misión y visión de TI aprobadas; los valores corporativos no dependen de TI |
| 16 | Mapa estratégico | Sistema de gestión | APO02 | P2.8 (BRE-015) | Cubierto en parte | 5 | La estrategia queda formalizada, pero el PETI no pide ubicar las metas en perspectivas |
| 17 | Indicadores con definición operativa | Sistema de gestión | MEA01 | §10 y tablero de P2.8 | Cubierto en parte | 7 | Tablero en uso y líneas base medidas |
| 18 | Metas de corto y largo plazo | Sistema de gestión | APO02 | METI01 a METI13 (§7) | Cubierto | 8 | Metas aprobadas con línea base |
| 19 | Iniciativas y proyectos | Sistema de gestión | APO05 | Portafolio de 25 proyectos (§9) | Cubierto | 8 | Portafolio aprobado y con patrocinador |
| 20 | Cronogramas con recursos y responsables | Sistema de gestión | BAI01 | Hoja de ruta (§9) y comités (§12) | Cubierto | 7 | Responsables nombrados; los costos siguen en rangos hasta cada caso de negocio |
| 21 | Procesos de la cadena de valor documentados | Procesos internos | APO01 | P2.1 | Cubierto en parte | 6 | Plantillas homologadas para la entrega; los procesos de apoyo siguen sin documento |
| 22 | Relación cliente-proveedor de los procesos | Procesos internos | APO01 | Ninguna | Sin respuesta | 3 | Sin cambio |
| 23 | Indicadores de procesos clave | Procesos internos | MEA01 | KPI-05 y KPI-06 (P2.2, P2.4) | Cubierto en parte | 5 | Dos de los ocho procesos con indicador |
| 24 | Objetivos, metas e indicadores por proceso | Procesos internos | APO01 | Ninguna | Sin respuesta | 3 | Sin cambio |
| 25 | Prioridad de procesos frente a la organización | Procesos internos | EDM02 | Regla de prioridad (§9) y Comité Directivo | Cubierto en parte | 5 | Hay quién prioriza; los procesos siguen sin objetivos propios |
| 26 | Sincronización entre procesos | Procesos internos | APO01 | P2.2 y P2.4 | Cubierto en parte | 6 | Las integraciones con la ALM quitan los traspasos manuales |
| 27 | Sincronización con proveedores y socios | Procesos internos | APO10 | Solo como riesgo (R08) | Sin respuesta | 4 | Sin cambio |
| 28 | Presupuesto ligado a objetivos | Financiera | EDM04 | P2.8 (BRE-011) y P2.7 | Cubierto | 6 | Guía de presupuesto y tablero de costos de nube; las licencias siguen sujetas al cliente |
| 29 | Despliegue en cascada | Aprendizaje y crecimiento | EDM01 | Comités por nivel (§12) y P2.8 | Cubierto en parte | 5 | Comités Directivo, Táctico y por célula con acta; sin objetivos por nivel |
| 30 | Trabajo diario alineado | Aprendizaje y crecimiento | APO01 | Comité por célula (§12) | Cubierto en parte | 6 | La célula revisa cada semana su avance frente al plan |
| 31 | Calendario de mediciones | Sistema de gestión | MEA01 | Frecuencias de §10 y KPI-14 | Cubierto | 7 | Cada indicador con frecuencia y comité que lo revisa |
| 32 | Evaluación y ajuste de metas | Sistema de gestión | MEA01 | Comité Directivo trimestral, revisión anual (§12) y P4.3 | Cubierto | 7 | Ciclo de revisión fuera de seguridad |
| 33 | Sistemas de información para el control | Aprendizaje y crecimiento | APO14 | P2.4, P2.5, P2.7 y P3.5 | Cubierto | 7 | Horas, observabilidad, costos y datos integrados en el tablero |
| 34 | Metas personales | Aprendizaje y crecimiento | APO07 | Las maneja Talento humano | Fuera del alcance de TI | 4 | Sin cambio |
| 35 | Acciones correctivas | Sistema de gestión | MEA01 | Comité Táctico mensual (§12) y SGSI | Cubierto en parte | 6 | Los desvíos de indicadores tienen instancia que decide |
| 36 | Seguimiento y retroalimentación de jefes | Aprendizaje y crecimiento | APO07 | Las maneja Talento humano | Fuera del alcance de TI | 6 | Sin cambio |
| 37 | Competencias por puesto | Aprendizaje y crecimiento | APO07 | P1.7 y P3.4 | Cubierto | 7 | Currículo de certificaciones por rol cerrado |
| 38 | Procesos de recursos humanos conectados | Aprendizaje y crecimiento | APO07 | P1.7 | Cubierto en parte | 5 | La capacitación se conecta con las alianzas; selección, carrera y remuneración no |
| 39 | Desempeño y compensación con el BSC | Aprendizaje y crecimiento | APO07 | La decide Talento humano | Fuera del alcance de TI | 1 | Sin cambio |
| 40 | Comunicación de la estrategia | Aprendizaje y crecimiento | EDM05 | Presentación e inducción del PETI (§12) | Cubierto | 7 | Presentación a todo el personal e inducción a cada ingreso |

<!-- fin-clasificacion -->
