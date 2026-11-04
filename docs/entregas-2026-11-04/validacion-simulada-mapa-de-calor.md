# Validación simulada del mapa de calor: Perficient, operación en Colombia

<!--
Fuente de Validacion_Simulada_Mapa_de_Calor_Perficient_Colombia.docx. El bloque cruces-validados lo lee
scripts/priorizar_mapa_de_calor.py (con los ejes de madurez-digital.md) para correr la priorización.
-->

**Organización evaluada:** Perficient Inc., operación en Colombia. **Elaboró:** Equipo Firmes por la Gobernanza (trabajo académico). **Fecha:** 4 de noviembre de 2026. **Documento base:** análisis del modelo de madurez digital y mapa de calor de la misma fecha.

> **Esto es una simulación.** El marco del MinTIC pide que el mapa de calor lo califique un equipo con tres perfiles. El equipo académico no tiene acceso a esas personas, así que asumió cada perfil con un criterio escrito y la evidencia del proyecto (PETI Colombia v1.0, registro de evidencias, entregas de octubre). Ninguna calificación de este documento es opinión de una persona de Perficient. Sirve para probar la consistencia de la valoración del equipo y para preparar el taller real, no para reemplazarlo.

## Para qué

El marco de transformación digital (MinTIC, 2020, numeral 2.3.2) dice que el mapa de calor se construye con "un equipo de trabajo formado por 3 perfiles": quien conoce el proceso de principio a fin, quien conoce la participación del área en ese punto y quien lidera la transformación digital con una visión global. En la entrega del mapa, los 31 cruces los calificó el equipo académico con un solo criterio (INT-001), y su validación quedó como pendiente. Esta simulación responde dos preguntas: si la valoración del equipo es coherente con sus propias reglas, y si el resultado cambia cuando cada factor se mira desde tres posiciones distintas.

## Los tres perfiles simulados

| Perfil | Quién lo asume en la operación | Factor que más mira | Criterio escrito |
|---|---|---|---|
| A. Responsable del proceso | El rol que el PETI pone al frente de cada proceso: CTO (PE01), Technical Lead (PM01), DevSecOps y CISO (PM02), arquitectura de datos (PM03), Talento humano (PA01), Operaciones (PA02), PM y Line Manager (PA03), CISO (PV01) | Potencial | Potencial 3 si la iniciativa mueve directamente el indicador del proceso (KPI-05 en vulnerabilidades, KPI-06 en registro de tiempos, KPI-09 en talento, KPI-13 en auditoría). Factibilidad 2 si la iniciativa depende de un proyecto que todavía no existe (dependencias del PETI, §9) |
| B. Representante del área | Quien conoce lo que el área hace hoy y con qué gente | Factibilidad | Factibilidad 1 si el área no decide sobre el recurso (lo controla el cliente o el corporativo) o si el rol que ejecutaría es solo una propuesta y el costo es alto. Factibilidad 2 si el área ya carga otro proyecto de fase 1 en los mismos meses. Urgencia 3 si el área sufre hoy una pérdida o una obligación concreta |
| C. Líder de la transformación | CTO, con el centro de excelencia de IA propuesto (P1.8) | Urgencia | Urgencia 3 para plazos legales o de certificación y para lo que el PETI pone en fase 1; 1 para la fase 4. Sube un punto la urgencia de la IA para clientes, por la marca "AI-native" (PUB-003) y la rivalidad del sector (Porter, 4,4 de 5). Potencial 3 para lo que habilita otros proyectos o reduce un riesgo crítico (R01) |

## Regla de consolidación

Cada factor del cruce se consolida con la **mediana** de los tres perfiles, para que una sola opinión extrema no mueva el resultado. Un cruce queda en 0 cuando dos perfiles dicen que el área no participa en el proceso; si dos o más lo califican, la mediana se toma entre ellos. El valor final sale de la tabla de priorización del MinTIC.

## Calificación por cruce

Cada columna muestra factibilidad, potencial y urgencia (F-P-U). "Equipo" es la valoración inicial del equipo, antes de las correcciones que trajo esta validación; "0" es sin interacción.

| Área | Proceso | Equipo | Perfil A | Perfil B | Perfil C | Consolidado | Valor | Por qué cambia |
|---|---|---|---|---|---|---|---|---|
| A1 | PM01 | 2-3-3 | 2-3-3 | 2-3-3 | 2-3-3 | 2-3-3 | 9 → 9 | Sin cambio: los tres coinciden en que la licencia depende del cliente (R08) y en que es fase 1 |
| A1 | PM02 | 3-2-2 | 2-3-2 | 3-2-2 | 3-2-2 | 3-2-2 | 7 → 7 | A ve más potencial (KPI-05) pero también la dependencia de P2.1; la mediana no cambia |
| A1 | PM03 | 2-3-1 | 2-3-1 | 2-3-1 | 2-3-2 | 2-3-1 | 7 → 7 | Solo C sube la urgencia por la marca "AI-native" |
| A1 | PA01 | 3-1-1 | 3-2-1 | 3-1-1 | 3-1-1 | 3-1-1 | 3 → 3 | A ve la rotación como defensa ante R06; los otros no |
| A1 | PA02 | 3-2-2 | 2-3-2 | 3-2-2 | 3-2-2 | 3-2-2 | 7 → 7 | A: depende de P2.1 y de la ALM del cliente; la mediana no cambia |
| A1 | PA03 | 3-2-3 | 3-2-3 | 3-2-3 | 3-3-3 | 3-2-3 | 8 → 8 | C ve potencial alto por R01 (fuga por herramientas de IA) |
| A2 | PE01 | 2-2-1 | 2-2-1 | 2-2-1 | 2-2-1 | 2-2-1 | 4 → 4 | Sin cambio |
| A2 | PM01 | 2-3-2 | 2-3-2 | 2-3-2 | 2-3-2 | 2-3-2 | 8 → 8 | Sin cambio |
| A2 | PM02 | 2-3-2 | 2-3-3 | 2-3-2 | 2-3-2 | 2-3-2 | 8 → 8 | A sube la urgencia por R03 (nivel alto); los otros respetan la fase 2 |
| A2 | PM03 | 2-3-1 | 2-3-1 | 1-3-1 | 2-3-2 | 2-3-1 | 7 → 7 | B: costo alto y rol propuesto (BRE-010); C: la plataforma de datos sostiene la IA para clientes |
| A2 | PA02 | 2-1-2 | 2-2-2 | 2-1-2 | 2-1-2 | 2-1-2 | 2 → 2 | Sin cambio en la mediana |
| A2 | PA03 | 3-2-3 | 3-2-3 | 3-2-3 | 3-3-3 | 3-2-3 | 8 → 8 | C: el inventario habilita P1.2 y P1.4 |
| A2 | PV01 | 2-2-2 | 2-3-1 | 2-2-2 | 2-2-1 | **2-2-1** | **6 → 4** | El informe SOC 2 (P4.1) es fase 4. El equipo le dio urgencia 2 contra su propia regla |
| A3 | PM01 | 2-3-3 | 2-3-3 | 1-3-3 | 2-3-3 | 2-3-3 | 9 → 9 | B advierte que el CISO lleva P1.1 y P1.2 a la vez (meses 0 a 6); la mediana no cambia |
| A3 | PM02 | 3-2-2 | 3-3-2 | 3-2-2 | 3-2-2 | 3-2-2 | 7 → 7 | A ve potencial alto (KPI-05) |
| A3 | PM03 | 2-2-2 | 2-2-2 | 2-2-3 | 2-2-3 | **2-2-3** | **6 → 7** | El registro de transferencias de datos es P1.9, fase 1, y responde a una obligación legal (Ley 1581, R04) |
| A3 | PA01 | 3-2-3 | 3-2-3 | 3-2-3 | 3-2-3 | 3-2-3 | 8 → 8 | Sin cambio |
| A3 | PA03 | 3-2-2 | 3-2-3 | 2-2-2 | 3-2-3 | **3-2-3** | **7 → 8** | La revisión de herramientas de IA entra en P1.6, fase 1. El equipo le dio urgencia 2 contra su propia regla |
| A3 | PV01 | 3-3-3 | 3-3-3 | 3-3-3 | 3-3-3 | 3-3-3 | 9 → 9 | Sin cambio: plazo externo del certificado (PUB-002) |
| A4 | PM01 | 2-1-2 | 2-2-2 | 2-1-2 | 2-1-1 | 2-1-2 | 2 → 2 | Sin cambio en la mediana |
| A4 | PA01 | 3-2-2 | 3-3-2 | 3-2-3 | 3-3-3 | **3-3-3** | **7 → 9** | El plan de certificaciones (P1.7) es fase 1: el equipo le dio urgencia 2 contra su propia regla. Además, A y C ven más potencial porque las alianzas exigen personal certificado (PUB-005 a PUB-008) |
| A4 | PA03 | 3-1-2 | 3-1-3 | 3-1-3 | 3-1-3 | **3-1-3** | **4 → 7** | La aprobación del Line Manager es parte de P1.6, fase 1 |
| A5 | PE01 | 2-2-2 | 2-3-2 | 1-2-2 | 2-2-2 | 2-2-2 | 6 → 6 | B: el presupuesto lo decide el corporativo; A: el presupuesto es una causa crítica del BSC (enunciado 28) |
| A5 | PM01 | 2-2-2 | 2-2-2 | 1-2-2 | 2-2-2 | 2-2-2 | 6 → 6 | B: la nube la administra el cliente (PRV-001) y FinOps es un rol propuesto |
| A5 | PA02 | 2-3-2 | 2-3-2 | 2-3-3 | 2-3-2 | 2-3-2 | 8 → 8 | B ve urgencia por las horas sin conciliar (análisis DOFA del 21 de octubre) |
| A5 | PA03 | 2-2-1 | 2-2-1 | 2-2-1 | 2-1-1 | 2-2-1 | 4 → 4 | Sin cambio en la mediana |
| A6 | PE01 | 2-3-2 | 2-3-2 | 2-3-3 | 2-3-3 | **2-3-3** | **8 → 9** | B y C adelantan la urgencia: el Comité Directivo debía constituirse en octubre de 2026 (PETI §12) sin evidencia del acta, y el modelo de madurez y el BSC señalan el gobierno como la brecha más grave |
| A6 | PM01 | 2-2-3 | 2-2-3 | 2-2-3 | 2-3-3 | 2-2-3 | 7 → 7 | C ve el CoE como la "oficina de transformación digital" que pide la aclaración 7 |
| A6 | PM03 | 2-3-1 | 2-3-1 | 2-3-1 | 2-3-2 | 2-3-1 | 7 → 7 | Solo C sube la urgencia |
| A6 | PA01 | 0 | 3-2-3 | 0 | 3-2-3 | **3-2-3** | **0 → 8** | P1.7 está a cargo de "Talento humano, con CTO" (PETI §9): la Dirección de TI sí participa. El equipo dejó el cruce en gris |
| A6 | PA03 | 3-2-3 | 3-2-3 | 3-2-3 | 3-2-3 | 3-2-3 | 8 → 8 | Sin cambio |
| A6 | PV01 | 3-2-3 | 3-3-3 | 3-2-3 | 3-2-3 | 3-2-3 | 8 → 8 | A ve más potencial porque P1.9 precede a los controles de P1.2 |

Se revisaron también tres cruces en gris. En los tres, dos perfiles mantuvieron el 0: células × auditoría (A ve que las células generan evidencia para auditorías, pero no hay mejora digital propia del área), seguridad × planeación (el CISO participa en el Comité Directivo, pero esa participación no se digitaliza) y talento humano × planeación.

## Cruces consolidados

<!-- cruces-validados -->

| Área | Proceso | F | P | U | Valor | Iniciativa digital en el cruce |
|---|---|---|---|---|---|---|
| A1 | PM01 | 2 | 3 | 3 | 9 | IA en el ciclo de desarrollo con licencia aprobada y plantillas ALM homologadas (P1.6, P2.1) |
| A1 | PM02 | 3 | 2 | 2 | 7 | Hallazgos de seguridad convertidos en tickets de forma automática (P2.2) |
| A1 | PM03 | 2 | 3 | 1 | 7 | Soluciones RAG y agentes en producción para clientes (P3.1, P3.3) |
| A1 | PA01 | 3 | 1 | 1 | 3 | Rotación entre células apoyada en la plataforma de formación (KPI-10) |
| A1 | PA02 | 3 | 2 | 2 | 7 | Horas registradas desde la tarea de la ALM (P2.4) |
| A1 | PA03 | 3 | 2 | 3 | 8 | Solicitud digital de licencias de IA (P1.6) |
| A2 | PE01 | 2 | 2 | 1 | 4 | Arquitectura objetivo 2028-2030 (P4.3) |
| A2 | PM01 | 2 | 3 | 2 | 8 | Infraestructura como código, pipeline estándar y observabilidad (P2.3, P2.5, P2.6) |
| A2 | PM02 | 2 | 3 | 2 | 8 | Pruebas SAST, DAST y SCA dentro del pipeline (P2.3) |
| A2 | PM03 | 2 | 3 | 1 | 7 | Plataforma y catálogo de datos (P3.5) |
| A2 | PA02 | 2 | 1 | 2 | 2 | Integración técnica entre la ALM y el registro de tiempos (P2.4) |
| A2 | PA03 | 3 | 2 | 3 | 8 | Inventario de sistemas de IA (P1.3) |
| A2 | PV01 | 2 | 2 | 1 | 4 | Evidencia de controles generada por el pipeline para auditorías (P4.1) |
| A3 | PM01 | 2 | 3 | 3 | 9 | Sistema de gestión de IA y permisos como código para agentes (P1.2, P1.4) |
| A3 | PM02 | 3 | 2 | 2 | 7 | Tablero de tiempos de remediación de vulnerabilidades (KPI-05) |
| A3 | PM03 | 2 | 2 | 3 | 7 | Controles de protección de datos personales en analítica (BRE-016, P1.9) |
| A3 | PA01 | 3 | 2 | 3 | 8 | Capacitación en seguridad, IA y protección de datos (P1.5) |
| A3 | PA03 | 3 | 2 | 3 | 8 | Revisión de seguridad de cada herramienta de IA antes de aprobarla (P1.6) |
| A3 | PV01 | 3 | 3 | 3 | 9 | Recertificación ISO/IEC 27001 con gestión digital de evidencias del SGSI (P1.1) |
| A4 | PM01 | 2 | 1 | 2 | 2 | Documentación y rotación para no perder conocimiento (R06) |
| A4 | PA01 | 3 | 3 | 3 | 9 | Plan de certificaciones por rol con seguimiento (P1.7, P3.4) |
| A4 | PA03 | 3 | 1 | 3 | 7 | Aprobación del Line Manager en el flujo de licencias (P1.6) |
| A5 | PE01 | 2 | 2 | 2 | 6 | Guía de presupuesto de TI (P2.8) |
| A5 | PM01 | 2 | 2 | 2 | 6 | Tablero de costos de nube (P2.7) |
| A5 | PA02 | 2 | 3 | 2 | 8 | Conciliación automática de horas y tareas (P2.4) |
| A5 | PA03 | 2 | 2 | 1 | 4 | Costo de licencias por proyecto |
| A6 | PE01 | 2 | 3 | 3 | 9 | Tablero de indicadores y estrategia de TI documentada (P2.8) |
| A6 | PM01 | 2 | 2 | 3 | 7 | Centro de excelencia de IA en Colombia (P1.8) |
| A6 | PM03 | 2 | 3 | 1 | 7 | Casos de IA con clientes liderados por el CoE (P3.1 a P3.3) |
| A6 | PA01 | 3 | 2 | 3 | 8 | Plan de certificaciones alineado con las alianzas, decidido con el CTO (P1.7) |
| A6 | PA03 | 3 | 2 | 3 | 8 | Procedimiento de licencias de IA (P1.6) |
| A6 | PV01 | 3 | 2 | 3 | 8 | Concepto legal y registro de obligaciones (P1.9) |

<!-- fin-cruces-validados -->

## Mapa consolidado

En negrita, los cruces que cambiaron frente a la valoración del equipo.

| Área | PE01 | PM01 | PM02 | PM03 | PA01 | PA02 | PA03 | PV01 |
|---|---|---|---|---|---|---|---|---|
| A1 Células de entrega | 0 | 9 | 7 | 7 | 3 | 7 | 8 | 0 |
| A2 Arquitectura, nube y DevSecOps | 4 | 8 | 8 | 7 | 0 | 2 | 8 | **4** |
| A3 Seguridad de la información | 0 | 9 | 7 | **7** | 8 | 0 | **8** | 9 |
| A4 Talento humano | 0 | 2 | 0 | 0 | **9** | 0 | **7** | 0 |
| A5 Operaciones y finanzas | 6 | 6 | 0 | 0 | 0 | 8 | 4 | 0 |
| A6 Dirección de TI | **9** | 7 | 0 | 7 | **8** | 0 | 8 | 8 |

## Priorización con el mapa consolidado

Se corrió la macro `vecinos` original de la herramienta (rama de tres iniciativas, ejecutada con `scripts/vba_vecinos.py`) sobre el mapa consolidado. Ahora hay cinco cruces con 9, y la macro elige tres por el promedio de sus vecinos:

| Cruce con valor 9 | Índice | Equipo (inicial) | Entregada (con las cinco correcciones) | Validación simulada completa |
|---|---|---|---|---|
| PE01 Planeación × A6 Dirección de TI: tablero de indicadores y gobierno de TI (P2.8) | 6,50 | No era 9 (valía 8) | No es 9 (vale 8) | **1.º** |
| PM01 Entrega de software × A1 Células: IA en el ciclo de desarrollo (P1.6, P2.1) | 5,00 | 1.º (5,00) | 1.º (5,00) | **2.º** |
| PM01 Entrega de software × A3 Seguridad: sistema de gestión de IA y permisos para agentes (P1.2, P1.4) | 4,25 | 3.º (4,25) | 2.º (4,25) | **3.º** |
| PV01 Auditoría × A3 Seguridad: recertificación ISO/IEC 27001 (P1.1) | 4,00 | 2.º (4,33) | 3.º (4,00) | 4.º, fuera de los tres |
| PA01 Talento × A4 Talento humano: plan de certificaciones por rol (P1.7) | 2,00 | No era 9 (valía 7) | No es 9 (vale 8) | 5.º, fuera de los tres |

## Qué mostró la validación

**La valoración del equipo tenía cinco incoherencias con su propia regla.** El análisis dice que la urgencia se calificó por fases del PETI (fase 1, 3; fase 2, 2; fases 3 y 4, 1). Cinco cruces no la cumplían: el informe SOC 2 (fase 4, calificado 2), los controles de datos personales en analítica, la revisión de seguridad de herramientas de IA, el plan de certificaciones y la aprobación del Line Manager (los cuatro de fase 1, calificados 2). El perfil del líder de la transformación, que aplica la regla de fases al pie de la letra, las encontró todas. Este es el hallazgo más sólido de la simulación, porque no depende de opiniones: son errores de aplicación de un criterio escrito.

**Tres cambios sí son de criterio.** El primero es el cruce de la Dirección de TI con la planeación, que sube de 8 a 9 porque dos perfiles adelantan su urgencia. El PETI pone P2.8 en la fase 2, pero también dice que el Comité Directivo se constituía en octubre de 2026, y no hay evidencia del acta. El modelo de madurez (preguntas 7 y 11) y el diagnóstico BSC (sincronización y despliegue, bloqueador) apuntan a lo mismo. El segundo es el potencial del plan de certificaciones, que dos perfiles suben de 2 a 3 porque las alianzas exigen personal certificado. El tercero es un cruce que estaba en gris: el PETI asigna el plan de certificaciones a "Talento humano, con CTO", así que la Dirección de TI sí participa en ese proceso.

**El resultado cambia en un punto que importa.** Con la valoración del equipo, el mapa no mostraba caliente el gobierno de TI, y el análisis tuvo que explicar por qué P2.8 seguía siendo necesario. Con la validación simulada, el gobierno sale primero, y los dos instrumentos de la herramienta (el modelo de madurez y el mapa) quedan diciendo lo mismo. La IA en las células y el sistema de gestión de IA se mantienen entre los tres primeros con los mismos índices: esos dos resultados resisten el cambio de perspectiva.

**En la validación completa, la recertificación ISO sale de los tres primeros**, pero no porque haya perdido valor: sigue en 9. Cae porque su vecino, el informe SOC 2, bajó de 6 a 4 al corregir la urgencia. Es una limitación del algoritmo: desempata por los vecinos, no por el plazo. La recomendación del análisis no cambia: P1.1 se ejecuta primero porque su plazo es externo (PUB-002).

## Qué se corrigió en la entrega

Las cinco incoherencias se corrigieron en la herramienta y en el análisis que se entregan, porque no son opinión de nadie: son la regla del equipo bien aplicada. Solo cambió la urgencia de cada cruce.

| Cruce | Antes (F-P-U, valor) | Entregado (F-P-U, valor) |
|---|---|---|
| A2 Arquitectura × PV01 Auditoría (informe SOC 2, fase 4) | 2-2-2, 6 | 2-2-1, 4 |
| A3 Seguridad × PM03 Analítica (datos personales, P1.9) | 2-2-2, 6 | 2-2-3, 7 |
| A3 Seguridad × PA03 Licencias (revisión de herramientas de IA, P1.6) | 3-2-2, 7 | 3-2-3, 8 |
| A4 Talento humano × PA01 Talento (plan de certificaciones, P1.7) | 3-2-2, 7 | 3-2-3, 8 |
| A4 Talento humano × PA03 Licencias (aprobación del Line Manager, P1.6) | 3-1-2, 4 | 3-1-3, 7 |

Con las correcciones, los tres puntos calientes son los mismos de la valoración inicial, pero el sistema de gestión de IA pasa al segundo lugar y la recertificación ISO al tercero (índice 4,00, antes 4,33). Los tres cambios de criterio no se llevaron a la entrega: los propusieron perfiles simulados y necesitan a las personas reales.

## Recomendaciones

1. Presentar los tres cambios de criterio (gobierno de TI a 9, más potencial en el plan de certificaciones y la Dirección de TI en ese plan) como propuesta para el taller real, no como hecho.
2. Proponer en la siguiente versión del PETI adelantar a la fase 1 la parte de P2.8 que corresponde al Comité Directivo y al tablero mínimo de indicadores, con su entrada en el control de cambios (§15).
3. Mantener P1.1 como el primer proyecto en ejecución aunque ningún mapa lo ponga primero: su plazo es externo.

## Guion para el taller real

La simulación deja preparado el taller con los tres perfiles reales. Duración estimada: 90 minutos.

| Paso | Qué se hace | Material |
|---|---|---|
| 1 | Presentar ejes, factores y tabla de priorización (10 min) | Este documento y la herramienta |
| 2 | Confirmar las áreas y los cruces en gris (15 min) | Mapa de la entrega |
| 3 | Calificar primero los 7 cruces que cambiaron y los 5 con valor 9 (40 min) | Tabla "Calificación por cruce" |
| 4 | Revisar el resto solo si alguien discrepa de la valoración del equipo (15 min) | Mapa consolidado |
| 5 | Correr la priorización y comparar con esta simulación (10 min) | `scripts/priorizar_mapa_de_calor.py` |

Participantes sugeridos: un Technical Lead o PM de una célula (perfil A), el CISO o alguien de seguridad de la información (perfil B, para las áreas de mayor valor), y el CTO o quien lidere la adopción de IA en Colombia (perfil C).

## Limitaciones

- Los tres perfiles los asumió el mismo equipo que hizo la valoración original. La simulación encuentra incoherencias y cambios de perspectiva, pero no aporta información nueva sobre la operación.
- Los criterios de cada perfil son supuestos del equipo sobre cómo razonaría cada rol (INT-001). Una persona real puede pesar otros factores, como la carga de trabajo, la relación con el cliente o el presupuesto corporativo.
- La evidencia de la cuenta analizada (PRV-001) describe una cuenta y no toda la operación.
