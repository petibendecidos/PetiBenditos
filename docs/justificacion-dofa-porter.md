# Cómo justificar la DOFA y las 5 fuerzas de Porter (PETI Perficient Colombia)

Documento de estudio para el equipo, complemento de `preparacion-sustentacion-peti-colombia.md`. Sirve para defender en voz alta la DOFA (`dofa-final-perficient-colombia.md`) y el diagnóstico de Porter (`porter-5-fuerzas-perficient-colombia.md`): por qué existen, de dónde sale cada factor, cómo se calificó, qué preguntas puede hacer el profesor y qué no se debe decir. No es parte del PETI ni se entrega.

Las páginas de la guía son las del número impreso en `MGGTI.GE.ES.01 - Guia de construccion PETI - Gobierno Digital-v. 3.0.pdf`, que se cita como **MGGTI.GE.ES.03**.

---

## 1. La idea que hay que transmitir

Los dos análisis no son adornos: son el primer eslabón de la cadena del PETI. Si el profesor solo se lleva una cosa, que sea esta:

```
Porter (la industria)  ──► Oportunidades y amenazas ─┐
                                                     ├─► Cruce FO/FA/DO/DA ─► Brechas (BRE) ─► Proyectos (P) ─► Indicadores (KPI) y riesgos (R)
Diagnóstico §6.1 (TI) ──► Fortalezas y debilidades ──┘
```

- **Porter** mira hacia afuera, a la industria completa: con quién compite la operación colombiana, quién tiene poder de negociación y qué puede reemplazarla.
- **La DOFA** junta eso con lo que se encontró adentro, en el diagnóstico de TI por dominio.
- **El cruce** convierte la DOFA en 13 estrategias, y esas 13 estrategias cubren los 25 proyectos del portafolio. Ningún proyecto queda sin origen en la DOFA.

En una frase: **Porter explica por qué el mercado le exige a Perficient controles demostrables; la DOFA muestra qué le falta a TI para darlos; el portafolio lo cierra.**

---

## 2. Guion corto (para decir sin leer)

**DOFA, unos 90 segundos.**
"La DOFA responde a la Actividad 6 de la guía del MinTIC, que pide analizar la gestión de TI con factores internos y externos. Cada fortaleza y debilidad lleva entre corchetes su dominio del MRAE, y entre los siete dominios no queda ninguno sin factor. Solo entró un factor si cumplía tres condiciones: tener respaldo con ID de evidencia, que TI pudiera actuar sobre él y que ayudara a cubrir los dominios. Por eso dejamos fuera la tasa de cambio o las tarifas: un plan de TI no las resuelve. La tensión central es F2 contra D1: la compañía se presenta como *AI-native*, pero no puede demostrar cómo controla la IA que usa. La amenaza más urgente es A1, el vencimiento del certificado ISO 27001. Con el cruce sacamos 13 estrategias, y cada una apunta a brechas y proyectos que ya están en el PETI; entre todas cubren los 25 proyectos."

**Porter, unos 90 segundos.**
"Porter no está en la guía del MinTIC; lo aplicamos porque lo pide el curso, y lo usamos como el análisis del entorno que alimenta la parte externa de la DOFA. La industria es la de servicios de software, datos e IA que se prestan desde Colombia a clientes de Norteamérica, porque ese es el alcance del PETI, no la consultora global. La fuerza más alta es la rivalidad: Globant tiene más de 6.000 personas en Colombia y Softtek ya certificó ISO 42001. Le siguen el poder de los compradores y el de los proveedores, donde el proveedor principal es el talento. La conclusión es que la operación no puede diferenciarse por precio, sino por lo que un cliente regulado no encuentra en cualquiera: controles certificados, IA auditable y entrega medida. Las tres cosas dependen de TI, y por eso cada fuerza termina conectada con objetivos, brechas, proyectos e indicadores del PETI."

---

## 3. Justificar la DOFA

### 3.1 Por qué existe

| Qué pide la norma | Dónde | Cómo lo cumple la DOFA |
|---|---|---|
| Analizar y diagnosticar la gestión de TI | Guía, Actividad 6 (pp. 29-30) | Es el cierre del diagnóstico §6.1 |
| "Se recomienda realizar una matriz DOFA por cada dominio de gestión de TI" del MRAE | Guía, Actividad 6, paso 2 (p. 30) | Cada factor interno tiene su dominio entre corchetes; los siete dominios quedan cubiertos |
| Usar la DOFA por dominio como insumo de las oportunidades de mejora | Guía, Actividad 10 (p. 35) | El cruce lleva cada estrategia a brechas (§8) y proyectos (§9) |
| Formato interno (F, D) y externo (O, A) | Anexo 1, hoja "Actividad 6" | Matriz de cuatro cuadrantes |

### 3.2 Por qué estos factores y no otros

Hay que poder decir las tres reglas de memoria:

1. **Tiene respaldo.** Una fuente pública (`PUB-`), lo observado en la cuenta analizada (`PRV-001`) o el diagnóstico del PETI. Lo que es lectura del equipo se marca `INT-001`, sin esconderlo.
2. **TI puede actuar sobre él.** Todo factor se conecta con una brecha, un proyecto o un riesgo. Por eso no están la tasa de cambio ni la presión de tarifas.
3. **Los siete dominios quedan cubiertos.** Estrategia (F2, D4), gobierno (F5, D2, D3), información (F3, D1), sistemas de información (F4, D5), infraestructura (F5, D6), uso y apropiación (F3, F6, D7), seguridad (F1, F4, D1, D3).

La versión final salió de comparar tres borradores: uno de mercado (de ahí F2, F3, A4), uno por dominio (D1 a D7) y uno de riesgo y cumplimiento (el orden de urgencia: A1, D3, A3).

### 3.3 Cómo se decidió si algo es interno o externo

La pregunta que se hace es: **¿Perficient lo controla?** Si sí, es fortaleza o debilidad; si no, es oportunidad o amenaza. Los casos que más se prestan a confusión:

| Caso | Por qué quedó donde quedó |
|---|---|
| Las alianzas aparecen dos veces (F3 y O4) | Tener la alianza es interno (F3). Lo que el socio ofrece (formación, certificaciones, plataformas) depende del socio y es externo (O4). |
| El certificado ISO es fortaleza (F1) y su vencimiento es amenaza (A1) | El SGSI certificado es una capacidad propia. Que el organismo certificador renueve, y que los clientes lo exijan, no depende solo de Perficient. |
| A7 (el cliente no autoriza cambios) viene de PRV-001 y aun así es amenaza | La decisión es del cliente, no de Perficient. Es externo aunque se haya observado dentro de la cuenta. |
| O5 y O6 son marcos y prácticas, no hechos del mercado | Son conocimiento disponible afuera (DevSecOps, IaC, COBIT 2019) que la operación puede adoptar sin inventarlo. |

### 3.4 Por qué ese orden

Dentro de cada cuadrante los factores van por prioridad.

- **D1 va primero** porque contrasta con F2: el discurso *AI-native* (PUB-003) sin sistema de gestión, inventario ni permisos para agentes es la debilidad que más expone a la compañía frente a un cliente.
- **A1 va primero** porque es la única amenaza con fecha: cae en el primer mes del plan. Por eso P1.1 arranca en el mes 0, antes que todo lo demás.
- **A3 y D3 van arriba** porque la Ley 1581 es la obligación legal directa de la operación colombiana y las investigaciones de la SIC crecen año a año (55 en 2023, 83 en 2024, 101 en 2025).

### 3.5 Cómo se "prueba" una debilidad

Es la pregunta más incómoda, porque D1, D2, D4 y D6 se apoyan en INT-001: no se encontró evidencia de que existan. Respuesta honesta: **una ausencia no se prueba con un documento; se declara con el alcance de lo que se revisó.** El PETI dice "no se encontró en la evidencia revisada", no "Perficient no tiene". La validación con la dirección de TI es el primer paso del plan, y si alguna de esas cosas existe, la brecha se cambia de "crear" a "mantener" o "modificar" sin tocar el resto del portafolio.

### 3.6 El cruce: de la DOFA a los proyectos

| Tipo | Estrategias | Proyectos que cubre |
|---|---|---|
| FO (fortalezas para aprovechar oportunidades) | 4 | P1.2, P1.7, P1.8, P3.1, P3.3, P3.4, P3.5, P4.1, P4.2 |
| FA (fortalezas para frenar amenazas) | 3 | P1.1, P1.7, P2.1, P2.2, P2.3 |
| DO (corregir debilidades con oportunidades) | 3 | P1.3, P2.4, P2.5, P2.6, P2.7, P2.8, P3.2, P4.3 |
| DA (reducir debilidades frente a amenazas) | 3 | P1.4, P1.5, P1.6, P1.9 |
| **Total** | **13** | **25 proyectos distintos** (P1.7 aparece en FO y en FA) |

Tres cruces que conviene saber explicar, porque muestran que la DOFA decide cosas:

- **F1 + O2 + O3 (FO).** ISO/IEC 42001 comparte la estructura de ISO/IEC 27001, así que el sistema de gestión de IA se monta sobre el SGSI que ya existe, y después el informe SOC 2 lo muestra a los clientes. Responde también a A4: alcanzar a Softtek.
- **F1 + A1 (FA).** Como el SGSI ya existe, el trabajo es mantenerlo, no construirlo. Por eso P1.1 es corto y va primero.
- **D7 + A2 (DA).** Si no hay un canal claro para pedir licencias de IA, la gente usa herramientas no autorizadas, y así se filtran código y datos. Es el proyecto más corto de la fase 1 (meses 1 a 3).

### 3.7 Preguntas probables sobre la DOFA

1. **P: La guía pide una DOFA por dominio. ¿Por qué hay una sola?**
   **R:** La guía lo recomienda ("se recomienda", p. 30), no lo exige. La consolidamos para que se lea completa, pero cada factor interno tiene su dominio entre corchetes y los siete quedan cubiertos. Si se exige, se separa en siete tablas sin cambiar las conclusiones.

2. **P: ¿Por qué F4, F5 y F6 son fortalezas de Perficient si salen de una sola cuenta?**
   **R:** No las presentamos como política de Perficient. Están escritas como "en la cuenta analizada (PRV-001)" y la sección de límites lo dice. Las usamos porque son el punto de partida real sobre el que se apoyan P1.7, P2.2 y P2.8, no para generalizar.

3. **P: O1 dice que los clientes piden IA gobernada. ¿Dónde está el dato?**
   **R:** Es una hipótesis del equipo (INT-001) y así está marcada. La señal indirecta es que un competidor directo invirtió en certificar ISO/IEC 42001 para mostrárselo a sus clientes. No tenemos una encuesta a clientes de Perficient.

4. **P: ¿Por qué no aparecen factores económicos, como el dólar o los precios?**
   **R:** Por la regla 2: un plan de TI no fija tarifas ni controla la tasa de cambio. La presión de precio sí aparece en Porter, que describe la industria completa. Es una exclusión hecha a propósito.

5. **P: ¿Por qué hay amenazas (A2, A3, A5) que no salen de Porter?**
   **R:** Porter mira la competencia de la industria. Lo tecnológico (fuga por IA, vulnerabilidades de dependencias) y lo regulatorio (Ley 1581) sale del análisis de tendencias (§6.3) y del marco normativo (§3). Porter explica siete factores de la DOFA, no todos.

6. **P: ¿Cada estrategia del cruce termina en algo concreto?**
   **R:** Sí. Ninguna estrategia abre un proyecto nuevo: las 13 apuntan a brechas y proyectos que ya están en §8 y §9, y entre todas cubren los 25 proyectos.

---

## 4. Justificar las 5 fuerzas de Porter

### 4.1 Por qué está, si la guía no lo pide

La guía del MinTIC pide comprender el entorno (Actividad 4, p. 28) y hacer la DOFA (Actividad 6). Porter no es una de sus 17 actividades; lo aplicamos porque lo pide el curso, con las definiciones del material de clase. En el PETI cumple dos funciones:

- explica de dónde salen siete factores externos de la DOFA (O1, O3, O4, A1, A4, A6, A7);
- muestra sobre qué fuerzas puede actuar TI, y con qué proyectos.

Como la guía no lo exige, lo razonable es ponerlo como anexo o como numeral corto junto a la DOFA en §6, citado desde los motivadores (§5.1).

### 4.2 Por qué esa industria

La industria es la de **servicios de ingeniería de software, datos e IA prestados desde Colombia a clientes de Norteamérica (nearshore)**. No es "la consultoría global", porque el alcance del PETI es la operación colombiana, y Porter analiza una industria, no una empresa. Si se tomara el mercado global, los rivales y los compradores serían otros y las conclusiones no servirían para el plan.

### 4.3 Cómo se calificó cada fuerza

La escala va de 1 (muy baja) a 5 (muy alta) y mide cuánto limita cada fuerza la capacidad de la operación para sostener precios y márgenes. Para cada fuerza se revisaron sus determinantes uno por uno y se marcó si la evidencia la sube o la baja. La nota es el balance, y es una valoración del equipo (INT-001), no una medición.

| Fuerza | Determinantes que la suben | Determinantes que la bajan | Nota | Por qué esa nota y no la vecina |
|---|---|---|:---:|---|
| Rivalidad | 4 (rivales globales, escala en Colombia, Softtek con ISO 42001, precios a la baja) y 1 mixto (mercado que crece pero muy repartido) | 0 | 5 | Es la única fuerza sin ningún determinante a favor de Perficient |
| Poder de los compradores | 3 (clientes grandes de EE. UU., presión de precio, exigencia de controles) | 2 (ningún cliente domina; costo de cambio en contratos en curso) | 4 | No llega a 5 porque el 92 % de los ingresos de 2023 vino de clientes recurrentes: cambiar de proveedor a mitad de contrato es costoso |
| Poder de los proveedores | Talento alto; nube y socios medio-alto; modelos de IA medio | Alianzas con varias plataformas a la vez | 4 | El talento pesa más que todo lo demás junto, pero en las plataformas el poder baja porque hay varias alianzas |
| Amenaza de sustitutos | 3 (centros propios del cliente, contratación directa, IA que reduce horas) | 1 (costo y dificultad de montar un centro propio) | 3 | Los tres crecen, pero ninguno reemplaza por completo un proyecto nearshore en dos años |
| Amenaza de nuevos entrantes | 2 (barreras formales bajas, llegada de inversión extranjera) | 2 (exigencias del cliente regulado, relación con clientes actuales) | 3 | Montar una empresa es barato; ganarse la confianza de un cliente regulado toma años |

### 4.4 Lo que el profesor puede cuestionar

- **El talento como proveedor.** En una firma de servicios el insumo principal es la gente y el costo principal es la nómina. La definición del material de clase ("qué tan fácil les resulta a los proveedores subir los precios") se aplica directo: si las empresas del exterior contratan más colombianos (+49 % en 2025), el ingeniero tiene con qué pedir más salario.
- **Sustitutos no es lo mismo que rivales.** Un rival es otro proveedor de servicios (Globant, Softtek). Un sustituto es otra forma de obtener el resultado sin contratar servicios: un centro propio del cliente, contratar directo al ingeniero o reemplazar horas con IA.
- **Entrantes en "media" con barreras formales bajas.** Lo que frena al entrante no es el capital sino la confianza: certificaciones vigentes, informes SOC 2, niveles de socio y casos previos. Esa barrera solo protege mientras esté vigente; si el certificado ISO vence (A1), la barrera baja justo cuando empieza el plan.
- **La IA como sustituto.** Es el más incierto: puede reducir las horas que el cliente compra o volverse el servicio que compra, según quién demuestre primero que la controla. Ese argumento une Porter con OETI01.

### 4.5 Para qué le sirve al PETI

TI no controla los precios ni las decisiones de compra del cliente. Sí controla tres cosas que mueven las fuerzas:

| Lo que TI controla | Fuerza que mueve | Proyectos |
|---|---|---|
| Las credenciales que el cliente exige (ISO 27001, SOC 2, ISO 42001, niveles de socio) | Sube la barrera de entrada y baja el poder del comprador | P1.1, P1.2, P4.1, P1.7, P3.4 |
| Demostrar productividad con IA controlada | Responde a los sustitutos y a la presión de precio | P1.8, P3.1, P3.3, P2.3 |
| Retener el talento certificado y conservar el conocimiento | Baja el poder del proveedor principal | P1.7, P3.4, P2.1 |

La tabla completa por fuerza, con objetivos, brechas e indicadores, está en el documento de Porter ("Lectura para el PETI").

### 4.6 Preguntas probables sobre Porter

1. **P: ¿Por qué usan el 10-K si Perficient ya no cotiza en bolsa?**
   **R:** Es el último informe anual que presentó ante la SEC (año 2023). Lo usamos solo para describir su mercado y sus clientes en ese año, y lo decimos. Desde el 2 de octubre de 2024 es privada (PUB-001), así que no es un dato vigente ni hay uno más reciente público.

2. **P: ¿De dónde sale que la rivalidad es 5 y no 4?**
   **R:** Es la única fuerza en la que ningún determinante juega a favor de Perficient. Es una valoración del equipo (INT-001) con la evidencia citada en cada fila, no una encuesta.

3. **P: Varias cifras son globales. ¿Sirven para Colombia?**
   **R:** Solo las usamos cuando no hay una local, y lo decimos: ISG, Everest, Synergy y Menlo son globales o de Norteamérica. Para Colombia están las cifras de Fedesoft y el DANE, ProColombia, la SIC y Deel.

4. **P: ¿Por qué no usaron la cifra del déficit de 68.000 a 112.000 desarrolladores?**
   **R:** Viene de un estudio de 2017 que varios medios repiten sin una medición nueva. La descartamos a propósito.

5. **P: ¿Cuál es la conclusión de Porter para TI, en una frase?**
   **R:** La operación no puede diferenciarse por costo; se diferencia por lo que puede demostrar: controles certificados, IA auditable y entrega medida.

---

## 5. Puntos débiles (mejor decirlos antes de que los encuentren)

| # | Punto | Dónde | Respuesta corta | Corrección posible |
|---|---|---|---|---|
| 1 | La fecha del certificado ISO: la DOFA la lee como 11 de octubre de 2026 porque A-LIGN escribe mes/día/año en otro certificado suyo. Es una inferencia, no una confirmación. Y desde el 11 de octubre de 2026, con esa lectura el certificado ya venció si no se renovó (al 21 de octubre seguía sin evidencia pública de renovación) | DOFA A1; Porter (entrantes) | Por eso es la amenaza número uno y P1.1 arranca en el mes 0. Con la lectura colombiana vencería el 10 de noviembre; en ambos casos cae al inicio del plan | Confirmar con A-LIGN o con la dirección de seguridad |
| 2 | Las fuentes externas ([1] a [9] de la DOFA y [1] a [14] de Porter) no están todavía en el registro de evidencias | Ambos documentos | Se citan con URL y fecha de consulta en cada documento | Registrarlas como filas `PUB-` antes de llevarlas al PETI |
| 3 | O1 es hipótesis | DOFA | Está marcada INT-001, con una señal indirecta (Softtek) | Ninguna sin acceso a clientes |
| 4 | Seis factores salen de una sola cuenta (F4, F5, F6, D5, D7, A7) | DOFA | Redactados como "en la cuenta analizada (PRV-001)" | Ninguna: es el alcance de la evidencia |
| 5 | Las notas de 1 a 5 son juicio del equipo | Porter | Cada nota tiene sus determinantes con fuente | Ninguna: así se hace Porter cualitativo |
| 6 | Cifras de Globant (2024) y de Softtek en Bogotá (2021) desactualizadas | Porter | Confirman presencia y escala, no tamaño actual | Buscar cifras más recientes |
| 7 | No hay número de empleados de Perficient en Colombia ni su participación de mercado | Porter | Ninguna fuente pública lo da | Pedirlo a la operación |
| 8 | La matriz DOFA usa colores y emojis (🟩 🟥 🟦 🟧) | DOFA | Son de la versión visual | Quitarlos en la versión que vaya dentro del PETI |
| 9 | Porter no está en el PETI v1.0 | — | La guía no lo pide; es un análisis del curso | Agregarlo como anexo o numeral corto en §6 |

## 6. Lo que no se debe decir

- "Perficient no tiene gobierno de IA." Se dice: "en la evidencia revisada no se encontró un sistema de gestión de IA (INT-001)".
- "Perficient trabaja con Scrum y ambientes separados." Se dice: "en la cuenta analizada (PRV-001)". Y nada que identifique al cliente: ni herramientas por marca, ni proveedor, ni sector, ni región.
- "El certificado vence el 10/11/2026." Se explica la ambigüedad y por qué se tomó la lectura más temprana.
- "Certificación SOC 2." Es un **informe de atestación**. ISO 27001 e ISO 42001 sí se certifican; NIST AI RMF se adopta.
- "Los clientes de Perficient exigen IA auditable" como hecho. Es la hipótesis O1.
- "Perficient tiene el 96 % de sus ingresos en EE. UU." en presente. Es un dato de 2023, anterior a la privatización.
- Que las estrategias del cruce ya están en marcha. Todas son **propuestas** del equipo, igual que los proyectos a los que apuntan.

## 7. Entrega ajustada del 21 de octubre: las preguntas nuevas

La entrega "DOFA y Porter ajustada" agregó tres preguntas y dos plantillas del curso. Las respuestas completas están en `docs/entregas-2026-10-21/dofa-porter-ajustada.md` y los cálculos en `Matrices_DOFA_Porter_Perficient_Colombia.xlsx` (índice en `docs/entregas-2026-10-21/README.md`).

### 7.1 Respuestas cortas (para decir sin leer)

| Pregunta | Respuesta | Si piden el porqué |
|---|---|---|
| ¿La DOFA guía decisiones o solo documenta un momento? | Guía decisiones, pero solo porque le agregamos importancia por factor, cruce en 13 estrategias con acciones, orden de ejecución y una regla de revisión trimestral | El ejemplo es nuestra propia A1: el 8 de octubre decía "vence el 11 de octubre"; el 21 de octubre esa fecha ya pasó sin evidencia de renovación. Sin revisión, la DOFA queda vieja en dos semanas |
| ¿Cuál fuerza es el mayor desafío para el área de TI? | El poder de los compradores | La rivalidad es la más intensa de la industria (4,4), pero la enfrenta el negocio con precio y ventas. A TI le llega como tres exigencias del cliente: controles demostrables (ISO, SOC 2, gobierno de IA), infraestructura que es del cliente y el ahorro de la IA trasladado al precio |
| ¿TI es rentable o destruye dinero? | Hace posible el ingreso, pero hoy no puede demostrar que es rentable | Es la línea de producción y la base de la facturación. Pierde o arriesga dinero en horas conciliadas a mano, nube sin tablero de costos, la certificación sin renovación confirmada e IA sin controles. Proponemos medir el costo de TI por hora facturada |

### 7.2 Cifras de las matrices

| Matriz | Resultado | Cómo se dice |
|---|---|---|
| MEFI | 2,27 | "Por debajo de 2,5: las debilidades de gobierno, IA y datos pesan más que las fortalezas" |
| MEFE | 1,70 | "La operación responde mal a su entorno: no aprovecha el gobierno de IA ni se protege de A1, A2 y A4" |
| Cinco fuerzas | Rivalidad 4,4; proveedores 4,0; compradores 3,6; sustitutos 3,3; entrantes 3,0 | Promedio de determinantes calificados de 1 a 5, como en la plantilla 3b del curso |
| Perfil competitivo | Perficient 2,60; Globant 2,95; Softtek 3,20 | "Perficient pierde en el factor que hoy diferencia: gobierno de IA certificado" |
| Puntaje de estrategias | FA1 y DA1 en 10; FO1 y DO1 en 9 | Importancia promedio interna más externa |

### 7.3 Nombres de los tipos de estrategia

El enunciado usa ofensivas, defensivas, adaptativas y de supervivencia. El material "Estrategias FA, FO, DA y DO" usa atacar (FO, maxi-maxi), movilizar (DO, mini-maxi), defender (FA, maxi-mini) y reforzar (DA, mini-mini). Son equivalentes. La última lámina del material cambia algunas etiquetas; seguimos las láminas 7 a 14, que coinciden con el enunciado.

### 7.4 Lo que pueden cuestionar de esta entrega

| Cuestionamiento | Respuesta |
|---|---|
| "¿Por qué el mayor desafío no es la fuerza con el promedio más alto?" | Porque la pregunta es por el área de TI, no por la industria. La rivalidad le llega a TI a través del comprador, que compara proveedores por lo que pueden demostrar |
| "¿De dónde salen las calificaciones de Globant y Softtek?" | Son valoración del equipo con la evidencia pública que hay (Softtek ISO/IEC 42001, Globant con más de 6.000 personas en Colombia). La hoja marca lo que falta comprobar |
| "¿Por qué cambiaron la escala de la plantilla de matrices?" | La MEFI del .xls ponía "debilidad mayor" en 2 y "menor" en 1; la escala de Fred David es al revés. La MEFE usaba la calificación como importancia, que ya está en el peso |
| "¿Por qué no hicieron PEYEA ni BCG?" | Piden estados financieros y ventas por unidad de negocio, y Perficient es privada desde 2024 |
| "¿Por qué la MEFE da tan baja?" | Porque califica cómo responde hoy la operación, y en las amenazas más pesadas (certificado, IA, competidor certificado) la respuesta es deficiente. Es el argumento del PETI: por eso existe el plan |
