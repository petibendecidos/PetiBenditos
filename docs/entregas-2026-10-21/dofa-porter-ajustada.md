# Diagnóstico DOFA y Porter ajustado: Perficient, operación en Colombia

Equipo Firmes por la Gobernanza · Gobierno y Servicios de TI · 21 de octubre de 2026

Este documento ajusta la DOFA final (8 de octubre de 2026) y el diagnóstico de las cinco fuerzas de Porter (13 de octubre de 2026) del PETI 2026-2028 de la operación de Perficient en Colombia. Responde las tres preguntas de la entrega: si la DOFA guía decisiones o solo documenta un momento, cuál de las cinco fuerzas es hoy el mayor desafío para el área de TI y si esa área es rentable o destruye dinero.

Lo acompaña el libro `Matrices_DOFA_Porter_Perficient_Colombia.xlsx`, que consolida las dos plantillas del curso (Matrices de gerencia estratégica y Plantillas de herramientas de diagnóstico). Allí están, con fórmulas, la DOFA, la MEFI, la MEFE, la DOFA cruzada, las cinco fuerzas por determinantes, el perfil competitivo y el seguimiento. Las cifras de este documento salen de ese libro.

Es un trabajo académico. Las estrategias, acciones y proyectos son propuestas del equipo, no decisiones de Perficient. PUB-, PRV- e INT- remiten al registro de evidencias del proyecto; F, D, O y A, a los factores de la DOFA final; P, BRE, KPI y R, al portafolio, brechas, indicadores y riesgos del PETI Colombia.

## 1. ¿La DOFA guía decisiones estratégicas o solo documenta un momento?

**Respuesta corta: en este PETI la DOFA guía decisiones, pero solo porque se le agregaron tres cosas que una DOFA sola no tiene: un valor para cada factor, un cruce que produce estrategias con acciones y una regla para actualizarla.** Sin eso sería una foto del 8 de octubre de 2026.

Una matriz DOFA, por sí misma, describe la situación en una fecha. El material de clase lo advierte: se enfoca en los factores actuales, no toma en cuenta el futuro y debe actualizarse con regularidad. La prueba está en nuestra propia matriz. El 8 de octubre la amenaza A1 decía que el certificado ISO/IEC 27001 vencía el 11 de octubre de 2026. Hoy, 21 de octubre, esa fecha ya pasó y sigue sin haber evidencia pública de la renovación (PUB-002). Si nadie revisa la matriz, A1 queda escrita como un riesgo futuro cuando ya es un hecho que hay que confirmar.

Lo que convierte la DOFA en una herramienta de decisión es lo que se hace después:

| Paso | Qué se hizo | Decisión que produjo |
|---|---|---|
| 1. Valorar cada factor | Cada factor recibió una importancia de 1 a 5 según su impacto en la operación y su urgencia (sección 2) | Qué factores pesan más: F1, D1, A1 y A2 tienen importancia 5 |
| 2. Cruzar factores | Se combinaron fortalezas, debilidades, oportunidades y amenazas en 13 estrategias de los cuatro tipos (sección 3) | Qué hacer con cada factor: atacar, defender, corregir o sobrevivir |
| 3. Bajar a acciones | Cada estrategia tiene acciones concretas, un proyecto del PETI, una meta y un indicador | Quién hace qué y cómo se mide |
| 4. Ordenar | El puntaje de cada estrategia fija su prioridad (sección 4) | Qué arranca primero: la recertificación ISO y los controles sobre la IA, en el mes 0 y la fase 1 |
| 5. Revisar | La matriz se revisa cada trimestre en el Comité Directivo del PETI y cuando cambia un factor de importancia 5 (sección 5) | La DOFA se mantiene al día mientras dura el plan |

El resultado es verificable: las 13 estrategias cubren los 25 proyectos del portafolio y ningún proyecto queda sin origen en la DOFA. Si se quita la DOFA, el portafolio pierde su justificación.

## 2. Valoración de los factores

Importancia de 1 (baja) a 5 (crítica). Combina el impacto del factor sobre la operación colombiana y la urgencia dentro del horizonte del plan (octubre de 2026 a septiembre de 2028). Es una valoración del equipo (INT-001) con la evidencia citada en la DOFA final.

| Factor | Descripción | Importancia | Por qué esa importancia |
|---|---|:---:|---|
| F1 | SGSI certificado en ISO/IEC 27001:2022 (PUB-002) | 5 | Es la credencial que los clientes regulados exigen y la base para un sistema de gestión de IA |
| F2 | Posicionamiento "AI-native" y alianzas de IA (PUB-003, PUB-009, PUB-010) | 4 | Da el mandato para gobernar la IA, pero todavía es una declaración |
| F3 | Alianzas con Microsoft, Databricks y Snowflake (PUB-005 a PUB-008) | 3 | Da acceso a plataformas y formación; no prueba su uso en Colombia |
| F4 | Pruebas de seguridad continuas en la cuenta analizada (PRV-001) | 3 | Base del pipeline seguro; observada en una sola cuenta |
| F5 | Roles, Scrum y ambientes separados en la cuenta analizada (PRV-001) | 2 | Facilita asignar responsabilidades; no genera ventaja por sí sola |
| F6 | Formación y patrocinio de certificaciones en la cuenta analizada (PRV-001) | 3 | Mecanismo existente para el plan de certificaciones |
| D1 | IA sin sistema de gestión, inventario ni permisos para agentes | 5 | Contradice F2 y es la debilidad que más expone a la operación |
| D2 | Sin comité, RACI, matriz de riesgos ni presupuesto de TI | 4 | Sin ellos nadie aprueba ni mide el plan |
| D3 | Transferencias internacionales de datos sin registro por proyecto | 4 | Exposición legal directa (Ley 1581) |
| D4 | Sin misión, visión, catálogo ni tablero de TI | 3 | Se corrige con el propio PETI |
| D5 | Hallazgos de seguridad y horas pasados a mano (PRV-001) | 3 | Retrasa la corrección y produce errores de conciliación |
| D6 | Sin infraestructura como código ni control de costos de nube | 2 | Costo creciente, pero depende de la autorización del cliente |
| D7 | Adopción de IA no medida y licencias sin canal único | 3 | Empuja al uso de herramientas no aprobadas |
| O1 | Clientes que piden IA gobernada y auditable | 4 | Es la demanda que sostiene la apuesta "AI-native" |
| O2 | ISO/IEC 42001 y NIST AI RMF | 4 | Marcos listos para ordenar y demostrar el gobierno de la IA |
| O3 | Informe SOC 2 tipo II con controles de IA | 4 | Es lo que los clientes piden a sus proveedores de servicios |
| O4 | Formación y certificaciones de los socios | 3 | Reduce el costo del plan de certificaciones |
| O5 | DevSecOps, infraestructura como código y observabilidad | 3 | Prácticas maduras que atacan D5 y D6 |
| O6 | COBIT 2019 para el gobierno y el presupuesto de TI | 2 | Útil, pero no urgente |
| A1 | Vencimiento del certificado ISO sin evidencia de recertificación | 5 | La fecha más temprana posible ya pasó; perderlo deja a la operación fuera de clientes regulados |
| A2 | Fuga de código o datos e inyección de instrucciones por IA | 5 | Impacto crítico y probabilidad creciente con la adopción de IA |
| A3 | Sanciones por la Ley 1581 y leyes de datos de la región | 4 | La SIC abrió 101 investigaciones en 2025, frente a 55 en 2023 |
| A4 | Competidores con gobierno de IA certificado (Softtek, ISO/IEC 42001) | 4 | Un rival directo ya puede demostrar lo que Perficient no |
| A5 | Vulnerabilidades heredadas de dependencias | 3 | Frecuentes, pero ya hay detección (F4) |
| A6 | Rotación del talento hacia empleadores del exterior | 4 | El talento es el insumo principal de la operación |
| A7 | El cliente no autoriza cambios en su infraestructura; sobrecosto de nube | 2 | Retrasa proyectos; no los impide |

### 2.1 Qué dicen la MEFI y la MEFE

Con esas importancias se armaron las matrices de evaluación de factores internos (MEFI) y externos (MEFE). El peso de cada factor es su importancia dividida por la suma de importancias, así que siempre suma 1. La calificación va de 1 a 4. En la MEFI mide si el factor es debilidad mayor (1), debilidad menor (2), fortaleza menor (3) o fortaleza mayor (4). En la MEFE mide qué tan bien responde hoy la operación al factor, de deficiente (1) a superior (4). El promedio de referencia es 2,5.

| Matriz | Total ponderado | Lectura |
|---|:---:|---|
| MEFI | 2,27 | Por debajo del promedio. Las debilidades de gobierno, IA y datos (D1, D2, D3 son debilidades mayores) pesan más que las fortalezas de seguridad y alianzas |
| MEFE | 1,70 | Muy por debajo del promedio. La operación no está aprovechando las oportunidades de gobierno de IA (O2 y O6 con respuesta deficiente) ni protegiéndose de las amenazas más pesadas (A1, A2 y A4 con respuesta deficiente) |

Los dos totales bajo 2,5 explican por qué las primeras estrategias del plan son defensivas y de supervivencia: antes de crecer, la operación tiene que corregir su respuesta a A1 y A2.

Dos ajustes frente a las plantillas del curso, para que el resultado sea interpretable: en la MEFI del archivo de matrices la escala tenía invertidos el 1 y el 2 (ponía "debilidad mayor" en 2); aquí se usa la escala estándar de Fred David. En la MEFE de ese archivo la calificación medía la importancia del factor, que ya está en el peso; aquí mide la respuesta de la organización.

## 3. Estrategias por tipo y sus acciones

Cada estrategia se califica con un puntaje: la importancia promedio de sus factores internos más la importancia promedio de sus factores externos (de 2 a 10). El puntaje fija el orden de la sección 4.

El material de clase "Estrategias FA, FO, DA y DO" nombra cada tipo por lo que busca. Se usan esos nombres junto con los del enunciado de la entrega:

| Cruce | Nombre en el enunciado | Nombre en el material | Lógica |
|---|---|---|---|
| FO | Ofensivas | Para atacar | Maxi-maxi: maximizar fortalezas y oportunidades |
| DO | Adaptativas | Para movilizar | Mini-maxi: minimizar debilidades aprovechando oportunidades |
| FA | Defensivas | Para defender | Maxi-mini: usar las fortalezas para reducir las amenazas |
| DA | De supervivencia | Para reforzar | Mini-mini: reducir debilidades y evitar amenazas |

La última lámina del material cambia algunas etiquetas (llama "defensivos" a los DO y "reorientación" a los FA). Se siguen las definiciones de las láminas 7 a 14, que coinciden con el enunciado.

### 3.1 Estrategias ofensivas (FO): para atacar

Son las estrategias de crecimiento: usan lo que la operación ya tiene para tomar lo que el mercado ofrece.

| ID | Cruce | Estrategia | Acciones | Proyecto y meta | Puntaje |
|---|---|---|---|---|:---:|
| FO1 | F1 + O2 + O3 | Extender el SGSI certificado a un sistema de gestión de IA y mostrar sus controles en un informe SOC 2 | 1. Reutilizar políticas, auditoría interna y revisión por la dirección del SGSI para la norma ISO/IEC 42001. 2. Aprobar el manual de IA responsable. 3. Auditar internamente el sistema de gestión de IA. 4. Incluir los controles de IA en el alcance del informe SOC 2 tipo II | P1.2, P4.2, P4.1. Manual aprobado en el mes 6; informe sin salvedades en el mes 24 (KPI-08, KPI-13) | 9 |
| FO2 | F2 + O1 | Crear un centro de excelencia de IA en Colombia y llevar casos de RAG y agentes a producción | 1. Aprobar la carta del centro de excelencia. 2. Hacer pruebas de concepto con clientes. 3. Llevar casos a producción solo después de que existan los controles de P1.2 | P1.8, P3.1, P3.3. Carta en el mes 4; 5 casos en producción en el mes 24 (KPI-03) | 8 |
| FO3 | F3 + F6 + O4 | Plan de certificaciones por rol con los programas de los socios | 1. Definir el currículo por rol (nube, IA, datos). 2. Usar los cupos y rutas de formación de los socios. 3. Hacer seguimiento trimestral por Line Manager | P1.7, P3.4. 70 % del personal técnico certificado en el mes 12 y 90 % en el mes 24 (KPI-09) | 6 |
| FO4 | F3 + O4 | Construir la plataforma y el catálogo de datos sobre la tecnología de los socios | 1. Elegir la plataforma entre las de los socios. 2. Publicar un catálogo único de datos. 3. Registrar el dueño de cada conjunto de datos | P3.5. Plataforma en operación en el mes 18 (KPI-01) | 6 |

### 3.2 Estrategias defensivas (FA): para defender

Son estrategias reactivas: usan los puntos fuertes para proteger a la operación de lo que viene de afuera.

| ID | Cruce | Estrategia | Acciones | Proyecto y meta | Puntaje |
|---|---|---|---|---|:---:|
| FA1 | F1 + A1 | Confirmar el estado del certificado ISO/IEC 27001 y cerrar la recertificación | 1. Pedir a A-Lign, esta semana, la confirmación escrita de la fecha y del estado del certificado. 2. Si no está renovado, programar la auditoría de recertificación. 3. Avisar a los clientes regulados con el certificado vigente o con la fecha de la auditoría | P1.1. Certificado vigente con 0 no conformidades mayores (KPI-07) | 10 |
| FA2 | F4 + A5 | Integrar las pruebas de seguridad al pipeline de CI/CD | 1. Pasar automáticamente los hallazgos de seguridad a la plataforma ALM. 2. Bloquear en el pipeline las dependencias con vulnerabilidades críticas. 3. Medir el tiempo de remediación | P2.2, P2.3. Remediación de críticas en menos de 72 h en el mes 12 y de 24 h en el mes 24 (KPI-05) | 6 |
| FA3 | F6 + A6 | Retener talento con certificaciones visibles y conservar el conocimiento | 1. Publicar el plan de certificaciones como ruta de carrera. 2. Homologar las plantillas de la ALM para que el conocimiento quede documentado. 3. Rotar personas entre células | P1.7, P2.1. Rotación planificada del 100 % al mes 24 (KPI-10) | 7 |

### 3.3 Estrategias adaptativas (DO): para movilizar

Son estrategias de reorientación: el entorno ofrece algo que permite corregir lo que falta adentro.

| ID | Cruce | Estrategia | Acciones | Proyecto y meta | Puntaje |
|---|---|---|---|---|:---:|
| DO1 | D1 + O2 | Levantar el inventario de IA según ISO/IEC 42001 | 1. Levantar por célula qué modelos, proveedores y datos se usan. 2. Asignar un responsable por sistema. 3. Evaluar automáticamente la calidad de los modelos en uso | P1.3, P3.2. 90 % de los sistemas inventariados en el año 1 y 100 % en el año 2 (KPI-08) | 9 |
| DO2 | D2 + D4 + O6 | Formalizar comités, RACI, presupuesto y estrategia de TI con COBIT 2019 | 1. Constituir el Comité Directivo del PETI con acta. 2. Aprobar la RACI y la matriz de riesgos. 3. Adoptar la guía de presupuesto de TI (COBIT APO06). 4. Hacer el balance del plan en la fase 4 | P2.8, P4.3. 90 % de las sesiones con acta (KPI-14) | 5,5 |
| DO3 | D5 + D6 + O5 | Automatizar la conciliación, estandarizar la observabilidad, usar infraestructura como código y controlar el costo de nube | 1. Conciliar automáticamente horas y tareas. 2. Definir objetivos de servicio y tableros de observabilidad. 3. Llevar los ambientes administrados a infraestructura como código, con acuerdo previo del cliente. 4. Publicar un tablero de costos de nube | P2.4 a P2.7. 95 % de horas conciliadas, 100 % de ambientes con IaC y −15 % de costo de nube en el mes 24 (KPI-06, KPI-11, KPI-02) | 5,5 |

### 3.4 Estrategias de supervivencia (DA): para reforzar

Es el cuadrante más expuesto: una debilidad interna coincide con una amenaza externa. Aquí no se busca crecer, sino evitar el daño mientras se corrige la debilidad.

| ID | Cruce | Estrategia | Acciones | Proyecto y meta | Puntaje |
|---|---|---|---|---|:---:|
| DA1 | D1 + A2 | Definir permisos como código para los agentes y capacitar al personal en IA y datos | 1. Limitar lo que cada agente de IA puede ejecutar y registrar sus acciones. 2. Capacitar a todo el personal en seguridad, IA y protección de datos. 3. Mientras no exista el sistema de gestión de IA, usar solo herramientas aprobadas | P1.4, P1.5. 100 % del personal capacitado en el mes 8 | 10 |
| DA2 | D3 + A3 | Pedir un concepto legal y llevar un registro de transferencias internacionales por proyecto | 1. Pedir a Legal el concepto sobre la Ley 1581 y las obligaciones de control que siguen tras la privatización. 2. Registrar por proyecto qué datos personales salen del país y con qué autorización | P1.9. Concepto emitido en el mes 3 | 8 |
| DA3 | D7 + A2 | Crear un procedimiento único para pedir y aprobar licencias de IA | 1. Publicar el procedimiento de solicitud, justificación ante el cliente y aprobación. 2. Medir cuántas células usan IA con licencia aprobada | P1.6. Procedimiento publicado en el mes 3; 85 % de células con IA y licencia en el mes 12 (KPI-04) | 8 |

## 4. Orden de ejecución

El puntaje define qué estrategia se atiende primero. Cuando dos estrategias empatan, va primero la que tiene una fecha externa o es requisito de otra.

| Orden | Estrategia | Tipo | Puntaje | Arranque | Por qué en ese lugar |
|:---:|---|---|:---:|---|---|
| 1 | FA1 Recertificación ISO/IEC 27001 | Defensiva | 10 | Mes 0 (ya) | Tiene fecha externa, y esa fecha ya pasó |
| 2 | DA1 Permisos para agentes y capacitación | Supervivencia | 10 | Meses 1 a 8 | Reduce el riesgo de fuga (R01) mientras no hay sistema de gestión de IA |
| 3 | DO1 Inventario de IA | Adaptativa | 9 | Meses 1 a 4 | Es requisito de FO1 y de DA1: no se gobierna lo que no se conoce |
| 4 | FO1 Sistema de gestión de IA y SOC 2 | Ofensiva | 9 | Meses 1 a 24 | Responde a A4; empieza en la fase 1 y cierra con el informe SOC 2 |
| 5 | DA2 Concepto legal y registro de transferencias | Supervivencia | 8 | Meses 1 a 3 | Define qué obligaciones aplican antes de fijar controles |
| 6 | DA3 Procedimiento de licencias de IA | Supervivencia | 8 | Meses 1 a 3 | Proyecto corto que corta el uso de herramientas no aprobadas |
| 7 | FO2 Centro de excelencia y casos de IA | Ofensiva | 8 | Meses 3 a 18 | Los casos en producción esperan los controles de FO1 |
| 8 | FA3 Retención y documentación | Defensiva | 7 | Meses 1 a 10 | Protege el insumo principal (talento) |
| 9 | FO3 Plan de certificaciones | Ofensiva | 6 | Meses 1 a 18 | Comparte acciones con FA3 |
| 10 | FA2 Pruebas de seguridad en el pipeline | Defensiva | 6 | Meses 8 a 12 | Necesita las plantillas homologadas (P2.1) |
| 11 | FO4 Plataforma de datos | Ofensiva | 6 | Meses 13 a 18 | Inversión alta; espera a que el gobierno esté formalizado |
| 12 | DO2 Gobierno de TI con COBIT | Adaptativa | 5,5 | Meses 7 a 9 | El Comité Directivo se constituye antes, con el PETI; aquí se formaliza el resto |
| 13 | DO3 Automatización, IaC y costos de nube | Adaptativa | 5,5 | Meses 7 a 12 | Depende de la autorización de cada cliente (A7) |

La lectura del orden es clara: **las primeras seis estrategias son defensivas, de supervivencia o habilitantes**. Primero se protege lo que ya existe (la certificación) y se controla el riesgo de la IA; después se crece con IA y datos. Es la secuencia de las cuatro fases del PETI.

## 5. Cómo se mantiene viva la DOFA

| Regla | Responsable propuesto | Frecuencia |
|---|---|---|
| Revisar la matriz completa, las importancias, las calificaciones y el orden de las estrategias | Comité Directivo del PETI | Trimestral |
| Revisar de inmediato cuando cambia un factor de importancia 5 (F1, D1, A1, A2) | CTO | Cuando ocurra |
| Pasar un factor de cuadrante cuando un proyecto lo cierra (por ejemplo, D1 deja de ser debilidad cuando P1.2 y P1.3 terminan) | Arquitectura | Al cierre de cada proyecto |
| Dejar constancia de cada cambio en el control de cambios del PETI | CTO | En cada revisión |

**Ajuste que hay que hacer hoy:** A1 debe pasar de "el certificado vence el 11 de octubre de 2026" a "la fecha más temprana posible de vencimiento (11 de octubre de 2026) ya pasó y no hay evidencia pública de la recertificación". Si A-Lign confirma que el certificado está vigente, A1 sale de las amenazas y F1 se refuerza. Si confirma que venció, A1 pasa a ser una debilidad crítica y FA1 se vuelve la única prioridad del mes.

## 6. Porter: las cinco fuerzas, ajustadas

La industria analizada es la de servicios de ingeniería de software, datos e IA que se prestan desde Colombia a clientes de Norteamérica. Siguiendo la plantilla de cinco fuerzas del curso, cada fuerza se calculó ahora como el promedio de sus determinantes, cada uno calificado de 1 (casi no presiona) a 5 (presiona mucho) con la evidencia del diagnóstico del 13 de octubre. El nivel de cada fuerza no cambia frente a ese diagnóstico.

| Fuerza | Promedio de determinantes | Nivel | Cómo le llega al área de TI |
|---|:---:|:---:|---|
| Rivalidad entre competidores | 4,4 | Muy alta | Indirectamente: los rivales (Globant, Softtek) compiten con credenciales que TI tiene que producir |
| Poder de los proveedores | 4,0 | Alta | Directamente en el talento; parcialmente en las plataformas de nube y de IA |
| Poder de los compradores | 3,6 | Alta | Directamente: el cliente fija las condiciones de seguridad, es dueño de la infraestructura y pide pasar al precio el ahorro de la IA |
| Amenaza de sustitutos | 3,3 | Media | En las herramientas de IA que reemplazan horas de trabajo |
| Amenaza de nuevos entrantes | 3,0 | Media | Poco: la barrera son las certificaciones que TI mantiene |

El poder de los compradores sale en 3,6 y no más alto porque dos determinantes lo frenan: ningún cliente concentra los ingresos y cambiar de proveedor en medio de un contrato es costoso. Los otros tres determinantes (presión de precio, exigencia de controles y tipo de comprador) están en 4 y 5, y los tres recaen en TI.

**Perfil competitivo.** La matriz de perfil competitivo del libro de matrices compara a la operación con Globant y Softtek en seis factores críticos de éxito. Perficient obtiene 2,60, Globant 2,95 y Softtek 3,20. Perficient iguala o supera en escala y alianzas, pero queda en 1 sobre 4 en gobierno de IA certificado, donde Softtek tiene 4. Las calificaciones de los competidores son valoración del equipo y la hoja marca qué falta comprobar.

### 6.1 ¿Cuál de las cinco fuerzas es hoy el mayor desafío estratégico para el área de TI, y por qué?

**El poder de los compradores.** La rivalidad es la fuerza más intensa de la industria, pero no es la que más exige al área de TI. La rivalidad la enfrenta el negocio con precio, oferta y ventas. Al área de TI le llega convertida en tres exigencias concretas que el cliente le pone, y las tres caen sobre TI:

1. **El cliente exige controles demostrables.** Los clientes regulados piden informes SOC 2 a sus proveedores para evaluar el riesgo de tercerizar, y piden certificaciones vigentes. La certificación ISO/IEC 27001 de Perficient no tiene evidencia pública de renovación después de su fecha más temprana de vencimiento (A1), no hay evidencia pública del alcance de un informe SOC 2 y la IA que se usa no tiene sistema de gestión (D1). Un rival directo, Softtek, ya certificó ISO/IEC 42001 (A4). Así es como la rivalidad llega a TI: el cliente compara proveedores por lo que cada uno puede demostrar, y demostrarlo es trabajo de TI.
2. **El cliente es dueño de la infraestructura.** En la cuenta analizada, la infraestructura opera en nube pública bajo responsabilidad compartida con el cliente, y los cambios requieren su autorización (PRV-001; A7, R08). TI no puede imponer infraestructura como código, observabilidad ni control de costos: tiene que proponerlos y negociarlos cuenta por cuenta.
3. **El cliente quiere el ahorro de la IA en el precio.** ISG reporta que los precios contratados de servicios de TI caen más rápido que nunca y atribuye parte a la productividad de la IA. Si la operación usa IA, el cliente espera pagar menos horas. TI tiene que demostrar que la IA aumenta la productividad sin aumentar el riesgo, y hoy no mide ninguna de las dos cosas (D7; no hay indicador de productividad de la entrega).

Por eso no se elige la fuerza con el promedio más alto. La rivalidad (4,4) y los proveedores (4,0) presionan más a la industria, pero la pregunta es por el área de TI, y la fuerza que más trabajo le pone a TI es la de los compradores. Las otras fuerzas pesan menos para TI. El poder de los proveedores (talento) es alto, pero lo gestionan en conjunto Talento humano y los Line Managers, y el PETI ya tiene respuesta (P1.7, P3.4, P2.1). Los sustitutos y los nuevos entrantes son de intensidad media.

**Qué hace TI frente a esta fuerza (todo propuesto en el PETI):**

| Exigencia del comprador | Respuesta | Proyecto | Indicador |
|---|---|---|---|
| Controles certificados | Recertificar ISO/IEC 27001 y montar el sistema de gestión de IA | P1.1, P1.2, P1.3 | KPI-07, KPI-08 |
| Controles demostrados por un tercero | Informe SOC 2 tipo II con controles de IA | P4.1 | KPI-13 |
| Infraestructura del cliente | Presentar los estándares como propuesta y pedir acuerdo previo | P2.6, P2.7 | KPI-11, KPI-02 |
| Ahorro de la IA en el precio | Medir la adopción de IA y la productividad de la entrega | P1.6, P2.3 | KPI-04 y un indicador nuevo de productividad (sección 6.2) |

### 6.2 ¿Es rentable el área de TI o destruye dinero? ¿Por qué?

**Respuesta: el área de TI es la que hace posible el ingreso, pero hoy no puede demostrar que es rentable, y hay cuatro puntos donde pierde o pone en riesgo dinero.** No es posible dar un número porque Perficient es privada desde octubre de 2024 y no publica estados financieros de la operación colombiana (PUB-001), y porque TI no tiene presupuesto propio ni indicadores de costo y valor (D2, D4). Que no se pueda medir ya es un hallazgo.

**Por qué genera valor.** En una firma de servicios, TI no es un área de apoyo lejana del ingreso: es la línea de producción. La plataforma ALM, los pipelines y los ambientes son donde se construye lo que se le factura al cliente, y el sistema de registro de tiempos es la base de la facturación (proceso PA02, con cobertura total). Además, las credenciales que TI mantiene, como el SGSI certificado, son la condición para que un cliente regulado contrate. Sin TI no hay horas que facturar ni contratos que ganar.

**Dónde pierde o pone en riesgo dinero:**

| Punto | Qué pasa | Efecto en dinero | Respuesta del PETI |
|---|---|---|---|
| Horas conciliadas a mano (D5) | En la cuenta analizada, horas y tareas se concilian a mano entre herramientas (PRV-001) | Errores de conciliación: horas trabajadas que no se facturan o que el cliente disputa | P2.4; KPI-06 (95 % conciliado) |
| Nube sin control de costos (D6) | No hay tablero ni alertas de costo de nube | Sobrecosto que nadie ve hasta la factura (R07) | P2.7; KPI-02 (−15 % al mes 24) |
| Credencial en riesgo (A1) | No hay evidencia pública de la recertificación ISO | Perder contratos con clientes regulados, cuyo valor supera con creces el costo de recertificar | P1.1; KPI-07 |
| IA sin controles (D1, A2) | Uso de IA sin inventario ni permisos | Una fuga de código o datos del cliente cuesta el contrato y puede generar sanciones (R01, R04) | P1.2 a P1.5 |

**Veredicto del equipo:** el área de TI es rentable en potencia y hoy se gestiona a ciegas. No destruye dinero por existir. Lo pone en riesgo por lo que no controla: horas sin conciliar, nube sin tablero, una credencial sin renovación confirmada e IA sin controles. El portafolio del PETI cuesta, en órdenes de magnitud, entre USD 1,4 y 6,65 millones en dos años. Se justifica si evita perder clientes regulados y recupera las horas y el gasto de nube que hoy se pierden. Para saberlo hay que medir.

**Cómo se demostraría (propuesta).** Desde la perspectiva financiera de un cuadro de mando integral, bastan cuatro mediciones:

| Medición | Fórmula | Fuente |
|---|---|---|
| Costo de TI por hora facturada | Gasto total de TI de la operación / horas facturadas | Guía de presupuesto (P2.8) y registro de tiempos |
| Horas recuperadas por conciliación | Horas facturadas después de P2.4 − horas facturadas antes, a igual volumen | KPI-06 |
| Ahorro de nube | Costo base − costo del periodo | KPI-02 |
| Productividad de la entrega | Tiempo desde que un cambio se aprueba hasta que llega a producción | Pipelines de P2.3; ocuparía el número KPI-12, hoy libre |

Si después de un año el costo de TI por hora facturada baja, o se mantiene mientras suben las horas y los casos de IA en producción (KPI-03), TI es rentable. Si sube sin que suban las horas ni los casos, TI está destruyendo dinero y el Comité Directivo debe repriorizar el portafolio.

## 7. Límites

- Las importancias, calificaciones y puntajes son valoraciones del equipo (INT-001), no el resultado de una encuesta.
- F4, F5, F6, D5, D7 y A7 vienen de una sola cuenta de cliente (PRV-001). Describen cómo se trabaja ahí, no una política de Perficient.
- La conclusión sobre la rentabilidad es cualitativa: no hay cifras públicas de ingresos ni de costos de la operación colombiana.
- Las fuentes externas son las de la DOFA final y del diagnóstico de Porter (consultadas el 8 y el 13 de octubre de 2026). Todavía no están en el registro de evidencias.
