# Sustentación del mapa estratégico de TI

Guía para exponer el [mapa estratégico](Mapa_estrategico_TI_BSC_Perficient_Colombia.png). No se entrega. Explica por qué se tomó cada decisión y de qué parte del [PETI Colombia v1.0](../perficient_peti_colombia_2026_2028.md) sale cada elemento, con lo que dice el PETI en ese punto.

Abreviaturas: OC = objetivo corporativo (PETI §5.2), OETI = objetivo de TI (§7), METI = meta (§7), BRE = brecha (§8), P = proyecto (§9), KPI = indicador (§10), R = riesgo (§11).

## El mapa en 30 segundos

> El mapa tiene cuatro filas, que son las perspectivas del BSC de TI. Se lee de abajo hacia arriba: si certificamos y rotamos al talento (innovación), los procesos de TI mejoran (interna); con mejores procesos, las células y los clientes reciben lo que necesitan (usuario), y eso produce lo que la dirección espera de TI (contribución al negocio). Hay 14 objetivos, cada uno coloreado según el objetivo de TI del PETI al que pertenece, con su indicador, sus metas a dos años y sus proyectos. Las 13 flechas numeradas explican la relación causa-efecto entre objetivos.

## Decisiones generales

| Decisión | Por qué | Referencia |
|---|---|---|
| Usar las 4 perspectivas del **BSC de TI** y no las de Kaplan y Norton | Es el modelo que entregó el docente. Un área de TI no tiene "clientes" ni "finanzas" propias: sirve al negocio y a sus usuarios. Cada perspectiva indica a cuál de Kaplan y Norton equivale | Van Grembergen y Van Bruggen (1997); imagen del docente |
| Contribución al negocio arriba, innovación abajo | En un mapa estratégico, la fila de arriba es el resultado final y la de abajo es la base que lo hace posible | BSC Designer, paso 5 |
| Un color por objetivo de TI | Así se ve de un vistazo a qué OETI pertenece cada objetivo y que los cuatro están en el mapa | PETI §7: OETI01 a OETI04 |
| Métrica **R** (resultado) o **A** (actuación) | Las R dicen si se logró el objetivo (llegan tarde). Las A se mueven antes y avisan. Arriba predominan las R y abajo las A | Kaplan y Norton: indicadores de resultado y de actuación |
| Usar los KPI del PETI y no inventar otros | Así el mapa queda conectado con el plan. Solo hay 3 métricas nuevas, con borde punteado y la marca "Propuesta" | PETI §10 (13 KPI) |
| Poner cada proyecto en un solo objetivo | Si un proyecto aparece dos veces, no se sabe a qué objetivo rinde cuentas. Los 25 proyectos quedan repartidos sin repetir | PETI §9: 25 proyectos |
| Mostrar los vacíos en lugar de taparlos | US3 e IF2 no tienen proyecto y hay 3 métricas sin KPI. Mostrarlos es más honesto que rellenarlos, y es lo que debe corregir la versión 1.1 | Diagnóstico BSC del 22 de octubre, cambios 1 y 2 |
| Los valores los propone el equipo | El PETI tiene misión y visión, pero no valores, y el paso 1 los pide | PETI §7 (solo misión y visión) |

## Los 8 pasos

| Paso | Qué pusimos | De dónde sale |
|---|---|---|
| 1. Misión, visión y valores | La misión y la visión, copiadas tal cual del PETI. Los cuatro valores (seguridad desde el diseño, decidir con datos, cumplimiento demostrable, aprendizaje continuo) salen de lo que repiten los OETI | PETI §7. Valores: propuesta del equipo |
| 2. Perspectivas | Las 4 del BSC de TI, cada una con su pregunta | Imagen del docente |
| 3. Prioridades | Los 4 OETI | PETI §7 |
| 4. Objetivos | 14 objetivos repartidos así: 4 de contribución al negocio, 3 de usuario, 4 internos y 3 de innovación | Ubicación propuesta en el diagnóstico BSC (§ resultado), ajustada a las perspectivas de TI |
| 5. Causa-efecto | 13 flechas numeradas, explicadas en el panel derecho | Dependencias de PETI §9 y criterio del equipo |
| 6. Métricas | 13 KPI con la meta del año 1 (septiembre de 2027) y del año 2 (septiembre de 2028), más 3 propuestas | PETI §7 (METI) y §10 (KPI) |
| 7. Iniciativas | Los 25 proyectos del portafolio | PETI §9 |
| 8. Cascada | Corporativo → TI Colombia → Comité Táctico → célula | PETI §5.2 y §12 (comités trimestral, mensual y semanal) |

## Objetivo por objetivo

### Contribución al negocio: ¿cómo ve la dirección al área de TI?

**CN1. Conservar la confianza de los clientes regulados** (OETI02)
- **Por qué va aquí:** la certificación es lo que la dirección le muestra a un cliente regulado para ganarse su confianza. Es un resultado del negocio, no un proceso interno.
- **OC02:** "Mantener la confianza de clientes regulados mediante controles certificados".
- **OETI02:** "Mantener la certificación de seguridad y cumplir la Ley 1581".
- **Métricas:** METI04 / KPI-07, no conformidades mayores ISO/IEC 27001 (cuántas hay por auditoría; meta: 0; anual; responsable: CISO). METI05 / KPI-13, informe SOC 2 tipo II sin salvedades (meta: sí en el mes 24). Ambas son R porque las mide un auditor externo al final del periodo.
- **Proyectos:** P1.1, recertificación de ISO/IEC 27001:2022 (BRE-006, "la fecha publicada cae al inicio del plan"; según la ficha, sirve para "evitar que caduque la certificación que exigen los clientes"). P4.1, informe SOC 2 tipo II con controles de IA (BRE-014, "no cubre IA").
- **Riesgo:** R02, que el certificado venza sin recertificación (riesgo alto).

**CN2. Llevar la IA a producción con los clientes** (OETI01)
- **Por qué va aquí:** el esfuerzo de IA solo le sirve al negocio cuando un cliente lo usa en producción. Es lo que se factura.
- **OC01:** "Entregar servicios de ingeniería digital e IA a escala de producción".
- **OETI01:** "Gobernar el uso de la IA en la operación colombiana".
- **Métrica:** METI03 / KPI-03, casos de IA en producción con métricas (0 → 1 → 5; semestral; CoE de IA). Es R.
- **Proyectos:** P3.1, RAG en producción para clientes (BRE-001). P3.3, agente conversacional en producción (BRE-008).

**CN3. Operar con un costo de TI controlado y trazable** (OETI03)
- **Por qué va aquí:** equivale a la perspectiva financiera, y el costo es lo primero que la dirección le pide a TI.
- **OC03:** "Operar con eficiencia y trazabilidad en la entrega nearshore".
- **OETI03:** "Estandarizar la entrega de software, su gobierno y su costo".
- **Métricas:** METI11 / KPI-02, variación del costo de nube administrada ((costo del periodo − costo base) / costo base; meta: −5 % el año 1 y −15 % el año 2; la línea base está por medir con P2.7). Además, la métrica **propuesta** de costo de TI por hora facturada, porque KPI-02 es el único indicador de costo del PETI (diagnóstico BSC, cambio 2).
- **Proyecto:** P2.7, tablero de costos de nube (BRE-013, "sin tableros estándar de monitoreo ni alertas de costo").
- **Riesgo:** R07, sobrecosto de nube.

**CN4. Cumplir el plan de TI que aprobó la dirección** (OETI03)
- **Por qué va aquí:** la dirección aprueba el PETI en el Comité Directivo y espera verlo ejecutado. Apoya los cuatro OC porque el plan completo los apoya.
- **Métrica:** METI07 / KPI-01, ejecución acumulada (proyectos terminados / 25 × 100; meta: 55 % en el mes 12 y 95 % en el mes 24; trimestral; CTO).
- **Proyecto:** P4.3, balance del PETI y arquitectura 2028-2030 (BRE-015).
- **Referencia:** §12, "el plan se revisa cada trimestre".

### Usuario: ¿cómo ven los usuarios al área de TI?

Los usuarios de TI son las células de desarrollo y los clientes que reciben su trabajo.

**US1. Dar a las células acceso ordenado a la IA** (OETI01)
- **Por qué va aquí:** el usuario interno nota si puede usar IA sin trámites eternos ni riesgos. Es A porque la adopción ocurre antes que los casos en producción (CN2).
- **Métrica:** METI02 / KPI-04, células con IA activa y licencia aprobada / total de células (85 % → 95 %; mensual; la línea base se toma en el mes 3).
- **Proyecto:** P1.6, procedimiento de licencias de IA (BRE-005, "canal de solicitud no estandarizado"; según la ficha, sirve para "dar acceso ordenado a herramientas de IA").

**US2. Entregar al cliente horas conciliadas con las tareas** (OETI03)
- **Por qué va aquí:** el cliente ve a TI a través de lo que le facturan. Si las horas cuadran con las tareas, confía en la factura.
- **Métrica:** METI09 / KPI-06, horas conciliadas / horas registradas (90 % → 95 %; mensual; Operaciones).
- **Proyecto:** P2.4, conciliación de tiempos con la ALM (BRE-012, "conciliación manual").

**US3. Conocer la satisfacción de usuarios y clientes con TI** (OETI03) ⚠ propuesto
- **Por qué va aquí:** la pregunta de la perspectiva es "¿cómo nos ven?" y ningún KPI del PETI la responde de forma directa. Lo agregamos para que el vacío quede a la vista.
- **OC02:** la confianza de los clientes.
- **Métrica propuesta:** índice de satisfacción con los servicios de TI. No hay KPI ni proyecto.
- **Referencia:** en el diagnóstico BSC (enunciado 3, puntaje 5) solo hay mediciones externas, como Clutch (PUB-023) e IDC (PUB-011). No se encontró una medición propia.

### Interna: ¿cuán efectivos y eficientes son los procesos de TI?

**PI2. Cerrar a tiempo las vulnerabilidades críticas** (OETI02)
- **Por qué va aquí:** mide un proceso, el de remediación, y no un resultado. El diagnóstico BSC (enunciado 23) lo pone entre los pocos indicadores de proceso del PETI.
- **Métrica:** METI06 / KPI-05, horas promedio entre la detección y el cierre (< 72 h → < 24 h; mensual; DevSecOps).
- **Proyectos:** P2.2, integración de pruebas de seguridad con la ALM (BRE-003, "los hallazgos pasan a mano"). P2.3, pipeline de CI/CD estandarizado (BRE-003 y BRE-007).
- **Riesgo:** R03, vulnerabilidades heredadas de dependencias.

**PI1. Gobernar el uso de la IA con un sistema certificable** (OETI01)
- **Por qué va aquí:** es el proceso de control de la IA. Sale de la visión del PETI: "gestionará el uso de la IA con un sistema certificable".
- **OC01 y OC02:** permite IA en producción (OC01) con controles certificados (OC02).
- **Métrica:** METI01 / KPI-08, sistemas registrados / identificados (90 % → 100 %; trimestral; Arquitectura).
- **Proyectos:** P1.2, sistema de gestión de IA (BRE-001); P1.3, inventario de IA (BRE-002); P1.4, permisos como código para agentes (BRE-008); P3.2, evaluación automática de modelos (BRE-002); P4.2, auditoría interna del sistema de gestión de IA (BRE-001). En el PETI, los cinco tienen KPI-08.
- **Riesgos:** R01, fuga de código o datos por IA; R05, inyección de instrucciones o sesgos.

**PI3. Estandarizar los ambientes y la entrega de software** (OETI03)
- **Por qué va aquí:** es el proceso de entrega. Sale de la visión: "pipelines y ambientes estandarizados".
- **Métrica:** METI10 / KPI-11, ambientes con infraestructura como código (60 % → 100 %; trimestral; Arquitectura de nube).
- **Proyectos:** P2.1, plantillas ALM homologadas (BRE-004); P2.5, observabilidad estandarizada (BRE-013); P2.6, infraestructura como código (BRE-007).
- **Riesgo:** R08, que el cliente no autorice cambios en su infraestructura.

**PI4. Formalizar el gobierno de TI y el registro de obligaciones legales** (OETI03)
- **Por qué va aquí:** el gobierno de TI es un proceso interno. Los comités con acta son la evidencia de que funciona.
- **OC02 y OC03:** cumplir la ley ayuda a la confianza (OC02) y el gobierno de TI, a la trazabilidad (OC03).
- **Métrica:** METI08 / KPI-14, sesiones de comité con acta / sesiones programadas (90 %; CTO).
- **Proyectos:** P2.8, formalización del gobierno y la estrategia de TI (BRE-011 y BRE-015). P1.9, concepto legal y registro de obligaciones (BRE-016, "transferencias internacionales de datos sin registro por proyecto").
- **Riesgo:** R04, sanción por incumplir la Ley 1581.

### Innovación: ¿cómo está posicionada TI frente a las necesidades futuras?

**IF3. Preparar la plataforma de datos e IA que pedirán los clientes** (OETI01) ⚠ métrica propuesta
- **Por qué va aquí:** es una capacidad que se construye ahora para responder a lo que los clientes pedirán después, y eso es lo que pregunta la perspectiva.
- **Métrica propuesta:** pruebas de concepto evaluadas por el CoE. Sale de la ficha de P1.8, que habla de "pruebas de concepto y evaluación de herramientas nuevas".
- **Proyectos:** P1.8, centro de excelencia de IA en Colombia (BRE-001 y BRE-005; según la ficha, sirve para "tener un equipo de referencia en IA"). P3.5, plataforma y catálogo de datos (BRE-010, "alianzas sin plataforma unificada").

**IF1. Certificar al personal técnico en IA, nube y datos** (OETI04)
- **OC04:** "Desarrollar y retener talento certificado en Colombia".
- **OETI04:** "Desarrollar las capacidades del talento colombiano en IA, nube y datos".
- **Métrica:** METI12 / KPI-09, personal con más de 6 meses y al menos una certificación (70 % → 90 %; trimestral; Talento humano).
- **Proyectos:** P1.5, capacitación en seguridad, IA y protección de datos; P1.7, plan de certificaciones por rol; P3.4, cierre del plan de certificaciones. Los tres atienden BRE-009, "currículo no desplegado a todo el personal".

**IF2. Rotar al personal entre células** (OETI04) ⚠ sin proyecto
- **Por qué va aquí:** la rotación reparte el conocimiento y reduce la dependencia de personas clave. Es la base para estandarizar.
- **Métrica:** METI13 / KPI-10, personas rotadas / total (50 % → 100 %; semestral; Line Managers).
- **Proyecto:** el PETI no tiene un proyecto propio para esto. Lo más cercano es R06, "rotación de personal y pérdida de conocimiento", cuyo tratamiento es "rotación planificada y documentación" y lo asigna a P2.1.

## Las 13 flechas

| # | Relación | Por qué | Apoyo en el PETI |
|---|---|---|---|
| 1 | IF1 → PI1 | Quien está certificado en IA y seguridad sabe aplicar los controles | P1.5 capacita en "seguridad, IA y protección de datos" |
| 2 | IF1 → PI3 | Quien está certificado en nube sabe automatizar ambientes | P1.7, "currículo por rol (nube, IA, datos)" |
| 3 | IF2 → PI3 | Rotar lleva las mismas prácticas a todas las células | R06 se trata con rotación y con P2.1 (plantillas) |
| 4 | IF3 → US1 | El CoE prueba las herramientas antes de que lleguen a las células | Ficha de P1.8: "evaluación de herramientas nuevas"; P1.8 se mide con KPI-04 |
| 5 | PI1 → US1 | Con inventario y reglas claras, las licencias se aprueban sin frenar a nadie | P1.3 (inventario) y P1.6 (licencias), los dos de OETI01 |
| 6 | PI1 → CN1 | El sistema de gestión de IA aporta los controles de IA que incluye el SOC 2 | §9: "P4.2 precede al informe de P4.1"; P4.1 es "con controles de IA" |
| 7 | PI2 → CN1 | Las vulnerabilidades que no se cierran terminan en no conformidades | KPI-05 y KPI-07, ambos de OETI02 |
| 8 | PI3 → US2 | Sin plantillas homologadas no se pueden conciliar horas | §9: "P2.1 precede a P2.2 y P2.4" |
| 9 | PI3 → CN3 | Con infraestructura como código y observabilidad, el costo se mide por ambiente | §7, dominio de infraestructura: "IaC, observabilidad... y control de costos de nube" |
| 10 | PI4 → CN4 | El Comité Táctico revisa el portafolio cada mes y corrige los desvíos | §12, Comité Táctico: "seguimiento de proyectos, indicadores y riesgos" |
| 11 | US1 → CN2 | Las células que ya usan IA son las que llevan casos a producción | METI02 → METI03, ambas de OETI01 |
| 12 | US2 → CN3 | Las horas conciliadas muestran en qué se va el costo | OC03, "eficiencia y trazabilidad" |
| 13 | US3 → CN1 | Medir la satisfacción avisa antes de perder a un cliente | **Hipótesis del equipo**: el PETI no la respalda |

## Preguntas difíciles que pueden hacer

**¿Por qué hay métricas que no están en el PETI?** Porque el mapa mostró tres vacíos: el costo por hora facturada (CN3), la satisfacción (US3) y las pruebas de concepto (IF3). Las marcamos como propuestas para no presentarlas como si ya existieran. Entran en la versión 1.1 del PETI.

**¿Por qué US3 e IF2 no tienen proyecto?** Porque el PETI no tiene uno, y no quisimos inventarlo dentro del mapa. Es un hallazgo: el plan mide la rotación (KPI-10) pero no tiene un proyecto que la ejecute.

**En el PETI, P3.5 pertenece a OETI03, pero en el mapa está en IF3, que es de OETI01. ¿Por qué?** La ubicamos por su propósito, que es preparar la plataforma de datos que pedirán los clientes. Esa es una necesidad futura. Es una diferencia real con el PETI: hay que corregirla en la versión 1.1 o devolver P3.5 a PI3.

**En el PETI, P1.9 pertenece a OETI02, pero en el mapa está en PI4 (OETI03).** En el PETI, P1.9 se mide con KPI-14 (comités con acta), el mismo indicador de PI4. La ubicamos por su indicador y no por su OETI.

**P2.1, P2.5 y P3.5 se miden con KPI-01 en el PETI, no con KPI-11.** Es cierto. En el PETI, esos proyectos solo cuentan para la ejecución del plan (KPI-01). En el mapa, el objetivo PI3 se mide con KPI-11 porque es el indicador que dice si los ambientes están estandarizados. Al menos P2.1 y P2.5 deberían tener un indicador propio.

**La ficha de P1.1 dice que la recertificación se hace antes del 11 de octubre de 2026, y esa fecha ya pasó.** La fecha publicada del certificado es ambigua (PUB-002): puede ser el 11 de octubre o el 10 de noviembre de 2026. No encontramos evidencia pública de la recertificación. Por eso CN1 conserva la meta, pero su estado está sin confirmar.

**¿Por qué no se usó KPI-12?** El PETI Colombia no lo usa. Se dejó el hueco en la numeración para que coincida con la del PETI regional (§10).

**¿Este mapa es de Perficient?** No. Es una propuesta del equipo (INT-001) dentro de un trabajo académico y depende de que la apruebe el Comité Directivo del PETI, que todavía no está constituido (§12 y §15).

**En el diagnóstico BSC del 22 de octubre, las metas estaban en otras perspectivas.** El diagnóstico usó las perspectivas de Kaplan y Norton (financiera, cliente, procesos y aprendizaje). El mapa usa las del BSC de TI, donde el "cliente" de TI es el negocio y el usuario es la célula. Por eso KPI-03, KPI-07 y KPI-13 pasaron de cliente a contribución al negocio, KPI-04 pasó de procesos a usuario y KPI-01 pasó de procesos a contribución al negocio. El mapa es la versión que vale.

**¿Por qué el mapa no está en el PETI?** Llevarlo al PETI es el cambio 1 que propuso el diagnóstico BSC (agregar a §7 la perspectiva de cada meta y un mapa estratégico). Para eso hace falta la versión 1.1, con su entrada en el control de cambios.
