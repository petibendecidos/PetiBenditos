# Diagnóstico BSC de gestión y gobierno de TI: Perficient, operación en Colombia

Fuente del formato diligenciado `Diagnostico_BSC_Perficient_Colombia.docx`. El script `scripts/generar_diagnostico_bsc.py` toma de aquí tres bloques: lo que va antes del formulario, las calificaciones (una fila por enunciado) y el resultado del punto 5. Lo que está fuera de esos bloques no se copia al Word.

<!-- antes -->

## Organización evaluada y criterio de calificación

**Organización:** Perficient Inc., operación en Colombia. **Rol de quien evalúa:** equipo de arquitectura y gobernanza de TI del PETI 2026-2028 (trabajo académico). **Evaluadores:** Equipo Firmes por la Gobernanza [integrantes]. **Fecha:** 22 de octubre de 2026.

El formato pide la opinión de quien diligencia. Aquí la opinión de cada enunciado se apoya en lo que el equipo puede demostrar: el PETI Colombia v1.0, la DOFA y el análisis de Porter ajustados del 21 de octubre de 2026 y el registro de evidencias del proyecto. Los códigos PUB- son fuentes públicas; PRV-001 son entrevistas de una cuenta de cliente, que describen esa cuenta y no una política de Perficient; INT-001 es análisis del equipo. Lo que no se puede demostrar no recibe puntaje alto, aunque sea probable en una empresa del tamaño de Perficient.

Para que los 40 puntajes sean comparables se usó esta regla:

| Puntaje | Criterio |
|---|---|
| 0 | No existe y no hay ningún indicio |
| 1-2 | Indicios aislados, sin documento |
| 3-4 | Existe en parte o de manera informal, o solo se observó en la cuenta analizada |
| 5-6 | Está definido o documentado, pero no aprobado, no medido o en uso parcial |
| 7-8 | Documentado y en uso, con brechas menores |
| 9-10 | Documentado, medido y mejorado de forma sistemática |

En el formato, los enunciados de cultura de ejecución vuelven a numerarse del 1 al 10. En el análisis se citan como 31 a 40.

<!-- fin-antes -->

## Calificaciones

<!-- calificaciones -->

| N.º | Puntaje | Sustento |
|---|---|---|
| 1 | 8 | Perficient declara foco por industria: salud y ciencias de la vida, servicios financieros, manufactura y automotriz (PUB-025, PUB-007). La operación colombiana atiende clientes de Norteamérica (PETI §1). |
| 2 | 7 | Las especializaciones por industria y por producto con socios (PUB-006, PUB-007) muestran conocimiento de las necesidades. Los clientes regulados piden controles certificados e IA gobernada (INT-001). No hay un documento por segmento para Colombia. |
| 3 | 5 | Hay mediciones externas: 4,7 de 5 en 33 reseñas de Clutch (PUB-023) y Major Player en IDC MarketScape (PUB-011). No se encontró una medición propia de satisfacción; el perfil competitivo del 21 de octubre es valoración del equipo. |
| 4 | 4 | Porter y el perfil competitivo frente a Globant y Softtek se hicieron una vez, para este trabajo. No hay evidencia de un monitoreo periódico de competidores. |
| 5 | 6 | En la cuenta analizada hay formación en línea, patrocinio de certificaciones y rotación entre células (PRV-001); hay formación interna en datos (PUB-022). No se encontró encuesta de clima ni plan basado en necesidades. |
| 6 | 5 | El accionista es EQT desde el 2 de octubre de 2024 (PUB-001); sus expectativas no son públicas. El PETI pide validar con Legal y Finanzas las obligaciones tras la privatización (P1.9). |
| 7 | 5 | El PETI analiza tendencias tecnológicas (§6.3), una sola vez. No cubre tendencias económicas, sociales ni políticas, ni hay una herramienta de vigilancia periódica. |
| 8 | 6 | Los retos están en los motivadores del PETI (§5.1): marca "AI-native" (PUB-003), privatización (PUB-001), recertificación ISO (PUB-002) y Ley 1581. Están escritos, pero el PETI no está aprobado. |
| 9 | 6 | Propuesta declarada: consultoría "AI-native" (PUB-003) y entrega nearshore en husos horarios cercanos. Los competidores directos dicen algo parecido y la diferencia no se mide (Porter: rivalidad 4,4 de 5). |
| 10 | 5 | El modelo de negocio está graficado en el Canvas del equipo (21 de octubre). No hay evidencia de que la operación lo tenga graficado y comunicado a su personal. |
| 11 | 4 | En la cuenta analizada la plataforma ALM registra sprints, tareas y tiempos, y el registro de tiempos cubre el proceso PA02 (PRV-001; PETI §5.3). No hay indicadores de proceso, y PE01 y PV01 no tienen soporte de TI. |
| 12 | 3 | Hay un servicio externo de pruebas de seguridad, y la nube la administra el cliente o un proveedor (PRV-001). No se encontró evaluación del desempeño de proveedores; los niveles de socio (PUB-005 a PUB-008) los otorga el socio. |
| 13 | 4 | Hay referencias externas sueltas (IDC, PUB-011; Clutch, PUB-023) y el perfil competitivo del equipo. No hay benchmarking sistemático de indicadores. |
| 14 | 6 | La DOFA está documentada y ponderada (MEFI 2,27; MEFE 1,70; INT-001), pero se construyó con fuentes públicas y entrevistas, no con datos de desempeño de procesos ni de proveedores (11 y 12), que no existen. |
| 15 | 4 | No se registró la misión, la visión ni los valores corporativos de Perficient. La misión y la visión de TI de la operación son una propuesta del PETI (§7). |
| 16 | 3 | No hay mapa estratégico. El PETI enlaza objetivos corporativos (OC01 a OC04) con objetivos de TI, pero no los ubica en perspectivas BSC ni muestra relaciones de causa y efecto. |
| 17 | 5 | El PETI define 13 indicadores con fórmula, frecuencia y responsable (§10), sin fuente de datos, y seis tienen la línea base "por medir". Son propuestos: hoy no hay tablero de indicadores de TI (§6.1). |
| 18 | 6 | Las 13 metas tienen valor al año 1 y al año 2 (§7, METI01 a METI13). Faltan la aprobación y la línea base de seis indicadores. |
| 19 | 6 | Hay 25 proyectos, cada uno con objetivo, brecha e indicador (§9). Ninguno tiene patrocinador ni caso de negocio aprobado. |
| 20 | 5 | Hay meses, fases, costos en órdenes de magnitud y responsables (§9), pero los responsables son roles propuestos y el costo es un rango. El Comité Directivo debía constituirse en octubre de 2026 y no hay evidencia del acta. |
| 21 | 5 | Los procesos están en el mapa del PETI (§5.3, ocho procesos) y en la cadena de valor del 21 de octubre. Los hizo el equipo; no son documentos de procesos de la operación. |
| 22 | 3 | No hay caracterización de procesos (entradas, proveedores, actividades, salidas y clientes). En la cuenta analizada se conocen flujos sueltos, como el paso de hallazgos de seguridad a tickets (PRV-001). |
| 23 | 3 | Los procesos misionales no tienen indicadores de eficiencia, calidad ni impacto. El PETI propone KPI-05 (remediación) y KPI-06 (conciliación de horas), con línea base por medir. |
| 24 | 3 | Los objetivos, metas, indicadores e iniciativas del PETI se organizan por objetivo de TI, no por proceso. Ningún proceso tiene su conjunto completo. |
| 25 | 4 | El PETI fija una regla de prioridad (riesgo crítico y plazos externos primero, §9) y la DOFA cruzada ordena las estrategias. Como no hay objetivos de proceso, no hay qué priorizar frente a los de la organización. |
| 26 | 4 | En la cuenta analizada la reunión diaria y la rotación entre células coordinan el trabajo (PRV-001), pero los hallazgos de seguridad y las horas se pasan a mano entre herramientas (§6.1). |
| 27 | 4 | Las licencias y los cambios de infraestructura dependen de la aprobación del cliente (PRV-001; riesgo R08). Las alianzas exigen personal certificado, pero no hay plan de certificaciones por rol (BRE-009). |
| 28 | 2 | No hay guía de presupuesto de TI (§6.1, BRE-011). Las licencias se justifican caso por caso ante el cliente (PRV-001) y los costos del PETI son rangos sin aprobar (INT-001). |
| 29 | 3 | No hay despliegue en cascada. El único vínculo observado es que el Line Manager autoriza certificaciones según su beneficio para la organización y el proyecto (PRV-001). |
| 30 | 5 | El trabajo diario sigue el backlog del cliente en sprints (PRV-001), que es el objetivo de entrega (OC01). No se conecta con los objetivos de TI ni con los demás objetivos corporativos. |
| 31 | 4 | Los sprints dan un ritmo de seguimiento en la cuenta analizada (PRV-001). No hay calendario de medición de indicadores; el PETI propone frecuencias y un comité trimestral (§10, §12). |
| 32 | 5 | El SGSI certificado (PUB-002) exige revisión por la dirección, auditoría interna y acciones correctivas en seguridad (ISO/IEC 27001, cláusulas 9 y 10). Fuera de seguridad no se encontró un ciclo equivalente. |
| 33 | 4 | Existen plataforma ALM, registro de tiempos y observabilidad (PRV-001), pero no se integran: la conciliación de horas es manual y no hay tablero (§6.1; BRE-012, BRE-013). |
| 34 | 4 | El Line Manager se ocupa del desarrollo profesional (PRV-001). No se encontró un sistema de metas personales con seguimiento. |
| 35 | 5 | En la cuenta analizada los hallazgos de seguridad se priorizan y se corrigen (PRV-001), y el SGSI exige acciones correctivas. En estrategia y procesos no hay metas contra las cuales corregir. |
| 36 | 6 | El Line Manager, el Technical Lead y la reunión diaria dan seguimiento y retroalimentación regulares en la cuenta analizada (PRV-001). No se sabe si ocurre igual en otras cuentas. |
| 37 | 5 | Los roles y niveles están definidos (PM, Line Manager, Technical Lead; senior, intermedio y junior; PETI §5.3). Falta el currículo de certificaciones por rol (BRE-009, P1.7). |
| 38 | 4 | Las certificaciones se aprueban por su beneficio para la organización y el proyecto, y hay formación en IA por perfil (PRV-001). No hay evidencia sobre selección, carrera ni remuneración. |
| 39 | 1 | Sin un BSC no puede haber vínculo entre la evaluación del desempeño, la compensación y el BSC. No se encontró evidencia de cómo se evalúa y remunera al personal. |
| 40 | 5 | La dirección comunica en público la evolución "AI-native" (PUB-003) y las alianzas (PUB-005 a PUB-010). No hay evidencia de que la estrategia se comunique y refuerce dentro de la operación colombiana; el PETI propone hacerlo en noviembre de 2026 (§12). |

<!-- fin-calificaciones -->

## Resultado

<!-- resultado -->

La tabla anterior suma los puntajes de cada cuestionario: enfoque estratégico 57, traslado hacia el BSC 46, sincronización y despliegue 36 y cultura de ejecución 43, para un total de 182 sobre 400 (45,5 %). Cada elemento suma hasta 100 puntos. Los niveles de la columna agregada son un criterio del equipo para leer el gráfico; el formato no trae uno.

Niveles: 0 a 39, bloqueador (el elemento impide ejecutar la estrategia); 40 a 59, en construcción (existe por partes, sin conexión); 60 a 79, funcional (opera con brechas puntuales); 80 a 100, impulsor (sostiene la ejecución).

[[GRAFICO]]

### Qué muestra el gráfico

Leído en el sentido de las agujas del reloj, que es el orden del método, el área se encoge: la estrategia se conoce en el nivel corporativo (57), pierde fuerza cuando hay que convertirla en objetivos, indicadores y metas (46) y se rompe al bajar a los procesos (36). Ningún elemento llega a 60. Es el mismo mensaje de la DOFA del 21 de octubre, donde la MEFI quedó en 2,27, bajo el promedio de 2,5: las debilidades internas pesan más que las fortalezas.

La cultura de ejecución (43) queda por encima de la sincronización (36), y eso dice algo. En la cuenta analizada la gente trabaja con disciplina: sprints, reunión diaria, roles claros, un Line Manager que acompaña y un SGSI certificado que obliga a corregir hallazgos (PRV-001, PUB-002). Lo que falta no es la voluntad de ejecutar sino el sistema que conecte esa ejecución con la estrategia: presupuesto, indicadores por proceso y objetivos en cascada.

El punto de partida, entonces, es una operación que sabe hacia dónde va la compañía y entrega bien a sus clientes, pero que no puede mostrar con datos cómo su trabajo diario sirve a esa estrategia.

### Elemento que causa los problemas y sus causas críticas

El elemento crítico es **sincronización y despliegue**, el único en nivel bloqueador. Las causas son los ocho enunciados con 3 puntos o menos:

| Enunciado | Puntaje | Causa | Respuesta del PETI Colombia |
|---|---|---|---|
| 39. Desempeño y compensación conectados con el BSC | 1 | No existe un BSC con el cual conectarlos | Ninguna; es un tema de Talento humano, fuera del alcance de TI |
| 28. Presupuesto ligado a objetivos | 2 | No hay guía de presupuesto de TI | P2.8 (BRE-011) |
| 12. Datos de proveedores y socios | 3 | No se mide el servicio de pruebas de seguridad ni el de nube | Ninguna. Puede entrar en P1.1, porque ISO/IEC 27001 pide controlar a los proveedores (Anexo A, 5.19 a 5.22) |
| 16. Mapa estratégico | 3 | Los objetivos no están en perspectivas BSC | P2.8 (BRE-015); ver la tabla siguiente |
| 22. Relación cliente-proveedor de los procesos | 3 | No hay caracterización de procesos | Ninguna |
| 23. Indicadores de procesos clave | 3 | Solo dos procesos tienen indicador propuesto | KPI-05 y KPI-06 (P2.2, P2.4) |
| 24. Objetivos, metas e indicadores por proceso | 3 | El PETI se organiza por objetivo de TI, no por proceso | Ninguna |
| 29. Despliegue en cascada | 3 | No hay comités ni objetivos por nivel | Comités por célula (§12) y P2.8 |

Cuatro de las ocho causas no tienen hoy un proyecto en el PETI (12, 22, 24 y 39). Son la principal lección del diagnóstico para la siguiente versión del plan.

### Los objetivos del PETI en las cuatro perspectivas del BSC (propuesta)

La guía del MinTIC permite construir los objetivos de TI con las cuatro perspectivas del BSC (Actividad 8). El PETI Colombia no lo hizo. Esta es la ubicación que propone el equipo para sus metas actuales:

| Perspectiva | Metas e indicadores del PETI | Qué falta |
|---|---|---|
| Financiera | METI11 Variación del costo de nube (KPI-02) | Costo de TI por hora facturada, propuesto en el análisis de Porter del 21 de octubre |
| Cliente | METI03 Casos de IA en producción (KPI-03); METI04 No conformidades ISO (KPI-07); METI05 Informe SOC 2 sin salvedades (KPI-13) | Una medición de satisfacción propia (enunciado 3) |
| Procesos internos | METI01 Inventario de IA (KPI-08); METI02 Adopción de IA (KPI-04); METI06 Remediación de vulnerabilidades (KPI-05); METI07 Ejecución del PETI (KPI-01); METI08 Comités con acta (KPI-14); METI09 Conciliación de horas (KPI-06); METI10 Infraestructura como código (KPI-11) | Indicadores para PM03 (analítica) y PA03 (licencias) |
| Aprendizaje y crecimiento | METI12 Personal certificado (KPI-09); METI13 Rotación entre células (KPI-10) | — |

La relación de causa y efecto se lee de abajo hacia arriba: personal certificado y rotado (aprendizaje) permite gobernar la IA, estandarizar la entrega y conciliar las horas (procesos); eso sostiene la certificación, el informe SOC 2 y los casos de IA que piden los clientes (cliente); y eso protege el ingreso y baja el costo (financiera). La perspectiva financiera es la más débil: tiene un solo indicador.

### Cambios que se proponen al PETI Colombia

No se aplicaron. Requieren una versión 1.1 del PETI con su entrada en el control de cambios.

1. Agregar a §7 la perspectiva BSC de cada meta y un mapa estratégico (enunciado 16).
2. Agregar a §10 la fuente de datos de cada indicador (enunciado 17) y el costo de TI por hora facturada en la perspectiva financiera.
3. Ampliar P2.8 para que caracterice los procesos misionales y les asigne objetivos e indicadores (enunciados 22 a 24).
4. Incluir en P1.1 la evaluación periódica de los proveedores de pruebas de seguridad y de nube (enunciado 12).
5. Recomendar a Talento humano que la evaluación del desempeño incluya metas del PETI cuando exista el tablero (enunciado 39).

### Límites

- Los puntajes son valoración del equipo (INT-001), no una encuesta al personal de Perficient. En una aplicación real cada directivo y líder llenaría el formato y se promediarían las respuestas.
- Lo que viene de PRV-001 describe una cuenta de cliente, no la operación completa ni una política de Perficient.
- Los enunciados sobre accionistas, valores corporativos, compensación y procesos de recursos humanos se calificaron sin evidencia interna. Un puntaje bajo ahí significa "no demostrable", no "inexistente".

<!-- fin-resultado -->
