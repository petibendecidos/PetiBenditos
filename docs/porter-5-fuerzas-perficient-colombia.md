# Diagnóstico de las 5 fuerzas de Porter: Perficient, operación en Colombia (PETI 2026-2028)

Equipo de Arquitectura y Gobernanza de TI — Perficient LATAM · 13 de octubre de 2026

**Industria analizada:** servicios de ingeniería de software, datos e IA que se prestan desde Colombia a clientes de Norteamérica bajo el modelo nearshore. Es el mercado en el que compite la operación colombiana de Perficient, no el de la consultoría global de la compañía.

| Fuerza | Intensidad | Tendencia | Qué la explica |
|---|:---:|:---:|---|
| **Rivalidad entre competidores** | Muy alta (5/5) | En aumento | Firmas globales con miles de empleados en Colombia y precios a la baja en contratos de servicios [1], [2], [3], [7] |
| **Poder de los compradores** | Alta (4/5) | En aumento | Grandes empresas de EE. UU. que piden trasladar al precio el ahorro de la IA y exigen controles demostrables [1], [7], [13] |
| **Poder de los proveedores** | Alta (4/5) | En aumento | El talento es el insumo principal y lo disputan empleadores del exterior; las plataformas de nube y de IA están concentradas [9], [10], [11], [12] |
| **Amenaza de sustitutos** | Media (3/5) | En aumento | Centros de capacidad propios de los clientes, contratación directa de talento colombiano y herramientas de IA que reducen horas [8], [9] |
| **Amenaza de nuevos entrantes** | Media (3/5) | Estable | Las barreras formales son bajas, pero los clientes regulados exigen certificaciones, alianzas y trayectoria [1], [6] |

*Escala de 1 (muy baja) a 5 (muy alta): cuánto limita cada fuerza la capacidad de la operación para sostener precios y márgenes. La tendencia es la esperada para el horizonte del PETI (octubre de 2026 a septiembre de 2028). Los números entre corchetes remiten a las fuentes listadas al final; PUB- y PRV- remiten al registro de evidencias del proyecto.*

**Lectura general.** Es una industria de rentabilidad presionada: hay muchos competidores con capacidad parecida, los clientes tienen poder para bajar precios y el insumo crítico, el talento, se encarece. En ese escenario la operación colombiana no puede diferenciarse por costo. Puede hacerlo por lo que el cliente regulado no encuentra en cualquier proveedor: controles certificados, un uso de la IA que se pueda auditar y una entrega que se mida. Las tres cosas dependen de TI, y por eso este diagnóstico alimenta el PETI.

---

## De dónde salen los datos y por qué estos

### Cómo se construyó

El modelo de las cinco fuerzas no es una actividad de la Guía MGGTI.GE.ES.03 v3.0 del MinTIC; la guía pide el análisis del entorno (Actividad 4) y la DOFA (Actividad 6). Se aplica porque lo pide el curso, con las definiciones del material de clase [14]:

| Fuerza | Qué estima, según el material de clase |
|---|---|
| Poder de los proveedores | Qué tan fácil les resulta a los proveedores subir los precios |
| Poder de los compradores | Qué tan fácil les resulta a los compradores bajar los costos |
| Rivalidad competitiva | Número de competidores y sus capacidades |
| Amenaza de sustitución | Si el cliente puede pasarse con facilidad a otro producto cuando suben los precios |
| Amenaza de nuevos participantes | Si las empresas existentes tienen barreras frente a quien llega atraído por la rentabilidad |

En el PETI, el análisis cumple dos funciones. Explica de dónde vienen varias oportunidades y amenazas de la DOFA, y muestra en cuáles fuerzas puede actuar TI. Cada fuerza se calificó revisando sus determinantes uno por uno (concentración, costos de cambio, barreras, diferenciación) y marcando si la evidencia la sube o la baja.

Las reglas para incluir un dato fueron las mismas de la DOFA:

1. **Tiene respaldo.** Fuente pública abierta en esta sesión, observación de la cuenta (PRV-001) o diagnóstico del PETI. Lo que es lectura del equipo se marca como `INT-001`.
2. **Describe a la industria en Colombia o al cliente de Norteamérica.** Las cifras globales se usan solo si no hay una local y se dice que son globales.
3. **Se dice qué no prueba.** Varias cifras son de 2023 a 2025; se aclara cuando una fuente no describe la situación actual.

Una advertencia sobre la fuente [1]: es el último informe anual (10-K) que Perficient presentó ante la SEC, para el año 2023. La compañía es privada desde el 2 de octubre de 2024 (PUB-001), así que el 10-K se usa solo como descripción de su mercado y de sus clientes en 2023, no como dato vigente.

### Rivalidad entre competidores: muy alta (5/5)

| Determinante | Evidencia | Efecto |
|---|---|---|
| Número y tamaño de los rivales | El 10-K 2023 nombra como competidores a firmas globales (Accenture, Deloitte Consulting, EPAM Systems, Globant y Endava), a proveedores offshore (Infosys, Cognizant y Wipro), a firmas locales y boutique y a los equipos de servicios de los fabricantes de software [1] | Sube |
| Rivales con escala en Colombia | Globant tiene más de 6.000 empleados en Colombia, con oficinas en Bogotá, Medellín, Cali y Barranquilla; es su país con más personal en América Latina [2]. Softtek abrió en 2021 un centro en Bogotá con una inversión anunciada de USD 60 millones y más de 1.000 cargos nuevos [3] | Sube |
| Diferenciación de los rivales en gobierno de IA | Softtek obtuvo ISO/IEC 42001 el 6 de noviembre de 2025 y se presenta como la primera empresa de tecnología de Latinoamérica en lograrlo [4] | Sube |
| Tamaño del mercado local | El sector de software y TI de Colombia vendió COP 44,2 billones en 2024, con 6.805 empresas activas; las exportaciones llegaron a USD 1.758 millones, 16 % más que en 2023 [5] | Mixto: el mercado crece, pero lo reparten muchas empresas |
| Precios | ISG reporta que los precios contratados de servicios administrados de TI bajan a un ritmo sin precedentes: la mejora de precio a los dos años de contrato se duplicó frente al promedio histórico, que era de entre 10 % y 20 %. Atribuye parte a la IA y parte a que hay "cientos" de proveedores que ofertan para ganar [7] | Sube |

La rivalidad es la fuerza más intensa. La operación colombiana compite por los mismos clientes y por el mismo talento con firmas que ya tienen miles de personas en las mismas ciudades. La diferencia de precio entre ellas es pequeña, y la de capacidad técnica también. Lo que sí distingue a un proveedor ante un cliente regulado es lo que puede demostrar: Softtek ya puede mostrar un sistema de gestión de IA certificado y Perficient todavía no (DOFA, A4 y D1).

### Amenaza de nuevos entrantes: media (3/5)

| Determinante | Evidencia | Efecto |
|---|---|---|
| Barreras formales | El 10-K 2023 describe el mercado como competitivo y "con bajas barreras de entrada" [1] | Sube |
| Llegada de inversión extranjera | ProColombia acompañó 178 proyectos de inversión extranjera directa en 2025; cerca del 11 % fueron de software y servicios de TI, el segundo sector después de las energías renovables. Estados Unidos originó cerca del 24 % de los proyectos [6] | Sube |
| Exigencias del cliente regulado | Los clientes piden informes SOC 2 a sus proveedores de servicios para evaluar el riesgo de tercerizar [13]. Perficient tiene ISO/IEC 27001:2022 (PUB-002) y alianzas de nivel alto con Microsoft, Databricks y Snowflake (PUB-005 a PUB-008). Un entrante tarda años en reunir estas credenciales | Baja |
| Relación con los clientes actuales | En 2023, el 92 % de los ingresos por servicios de Perficient vino de clientes que ya lo eran el año anterior [1] | Baja |

Para montar una empresa de desarrollo en Colombia hace falta poco capital, y cada año llegan nuevas. Lo que frena a un entrante en el segmento de Perficient no es el capital sino la confianza: certificaciones vigentes, informes de atestación, niveles de socio y casos previos con clientes de la misma industria. Por eso la fuerza es media y no alta. Esa barrera solo protege mientras las credenciales estén vigentes: si el certificado ISO/IEC 27001 vence sin renovarse (DOFA, A1), la barrera baja justo cuando empieza el plan.

### Amenaza de sustitutos: media (3/5), en aumento

| Sustituto | Evidencia | Efecto |
|---|---|---|
| Centros de capacidad propios del cliente (GCC) | Everest Group cuenta más de 6.350 centros de capacidad global en ubicaciones offshore y nearshore, con nuevas aperturas creciendo cerca del 7 % anual, y señala que su mandato pasa del ahorro de costos a funciones de mayor valor [8] | Sube |
| Contratación directa del talento colombiano | Según Deel, citado por ENTER.CO, la contratación de colombianos por empresas extranjeras creció 49 % en 2025, con los desarrolladores de software entre los perfiles más buscados [9] | Sube |
| Herramientas de IA que reemplazan horas de trabajo | ISG vincula parte de la caída de precios a la productividad que trae la IA, aunque aclara que todavía no se sabe cuánto se debe a la IA y cuánto a otras fuerzas del mercado [7] | Sube, sin magnitud medida |
| Costo de cambio para el cliente | Montar un centro propio exige saber operar en la región y conseguir talento; el resumen de Everest menciona esas mismas dificultades para las empresas que lo intentan [8] | Baja |

Un sustituto aquí no es otro proveedor, sino otra forma de conseguir el mismo resultado sin contratar servicios: abrir un centro propio, contratar directamente a los ingenieros o reemplazar parte del trabajo con herramientas de IA. Ninguno sustituye por completo un proyecto nearshore en el horizonte de dos años, pero los tres crecen. La IA es el más incierto: puede reducir las horas que el cliente compra o volverse el servicio que compra, según quién demuestre primero que la controla.

### Poder de los compradores: alto (4/5)

| Determinante | Evidencia | Efecto |
|---|---|---|
| Quién compra | En 2023, cerca del 96 % de los ingresos de Perficient vino de clientes de Estados Unidos [1] | Sube: grandes empresas con áreas de compras profesionales |
| Concentración de clientes | El cliente más grande representó cerca del 7 % de los ingresos en 2023, frente a 5 % en 2022 y 4 % en 2021 [1] | Baja: ningún cliente domina, aunque la concentración creció |
| Presión de precio | Los precios contratados caen más rápido que el promedio histórico y los proveedores asumen más riesgo mientras el cliente espera el beneficio de la IA [7] | Sube |
| Exigencia de controles | Los clientes piden SOC 2 para evaluar el riesgo de tercerizar [13]. En la cuenta analizada, la infraestructura opera en nube pública bajo responsabilidad compartida con el cliente y los cambios requieren su autorización (PRV-001) | Sube |
| Costo de cambio | La alta retención de ingresos (92 % de clientes recurrentes) indica que cambiar de proveedor en un contrato en curso es costoso [1] | Baja |

Los compradores tienen poder porque hay muchos proveedores con oferta parecida y porque son ellos quienes fijan las condiciones de seguridad y de infraestructura. Ese poder se ejerce sobre todo al renovar o al abrir un proyecto nuevo, cuando comparan proveedores; dentro de un contrato en curso, el costo de cambio protege a Perficient. Que el cliente pida controles demostrables es a la vez una presión y una oportunidad: el proveedor que puede entregar el informe SOC 2 o el certificado ISO/IEC 42001 pasa el filtro que otros no pasan (DOFA, O1 y O3).

### Poder de los proveedores: alto (4/5)

| Proveedor | Evidencia | Poder |
|---|---|---|
| Talento técnico (el insumo principal) | La contratación de colombianos por empresas extranjeras creció 49 % en 2025 [9]. El empleo en información y telecomunicaciones pasó de 326.000 a 406.000 personas entre 2018 y 2024, pero creció solo 0,8 % en 2024 [5]. El salario mínimo de 2026 subió 23 % (Decreto 1469 de 2025), y el Consejo de Estado le devolvió plenos efectos en julio de 2026 [12] | Alto |
| Plataformas de nube | Amazon, Microsoft y Google concentraron el 63 % del gasto mundial en infraestructura de nube en el tercer trimestre de 2025 [10] | Medio-alto |
| Socios tecnológicos (programas de alianza) | El 10-K 2023 advierte que perder la relación con fabricantes como Microsoft, Adobe, Salesforce u Oracle aumentaría los costos de venta [1]. Los niveles de socio exigen personal certificado (PUB-005 a PUB-008) | Medio-alto |
| Proveedores de modelos de IA | Tres proveedores (Anthropic, OpenAI y Google) concentraban cerca del 77 % del uso empresarial de modelos de lenguaje a mediados de 2025; solo el 11 % de los equipos cambió de proveedor en el último año [11] | Medio |

El talento pesa más que los demás proveedores juntos, porque en una firma de servicios el costo principal es la nómina y el ingreso depende de las horas facturables. Las señales no son todas de escasez: el empleo del sector casi no creció en 2024 [5]. La presión viene de la competencia por perfiles específicos (IA, nube, datos) y de empleadores del exterior que pagan en dólares. El alza del salario mínimo eleva el piso salarial y los costos atados a él, pero no está medido cuánto mueve los salarios de los ingenieros. En las plataformas el poder es menor de lo que sugiere la concentración, porque Perficient tiene alianzas con varias a la vez; el riesgo está en depender de un solo proveedor de modelos de IA sin una alternativa evaluada.

## Lectura para el PETI: dónde puede actuar TI

TI no controla los precios del mercado ni las decisiones de compra de los clientes. Sí controla tres cosas que mueven las fuerzas: las credenciales que el cliente exige (suben la barrera de entrada y bajan el poder del comprador), la capacidad de demostrar productividad con IA controlada (responde a los sustitutos y a la presión de precio) y la retención del talento certificado (baja el poder del proveedor principal). La tabla conecta cada fuerza con lo que el PETI Colombia ya propone. Ninguna fila abre un proyecto nuevo.

| Fuerza | Qué puede hacer TI (propuesto) | Factores DOFA | Objetivo | Brechas | Proyectos | Indicadores |
|---|---|---|---|---|---|---|
| Rivalidad | Cerrar la diferencia con los rivales que ya certificaron su gobierno de IA | F1, D1, A4, O2 | OETI01 | BRE-001, BRE-002 | P1.2, P1.3, P4.2 | KPI-08 |
| Nuevos entrantes | Mantener vigentes las credenciales que funcionan como barrera: ISO/IEC 27001, SOC 2 y niveles de socio | F1, F3, A1, O3, O4 | OETI02, OETI04 | BRE-006, BRE-014, BRE-009 | P1.1, P4.1, P1.7, P3.4 | KPI-07, KPI-13, KPI-09 |
| Sustitutos | Ofrecer lo que un centro propio o una herramienta suelta no dan: IA en producción con controles y entrega estandarizada | F2, O1, O5 | OETI01, OETI03 | BRE-001, BRE-004, BRE-007 | P1.8, P3.1, P3.3, P2.3 | KPI-03, KPI-04 |
| Compradores | Entregar los controles que el cliente pide y hacer visible el costo y el avance de la entrega | O1, O3, A7, D5 | OETI02, OETI03 | BRE-014, BRE-012, BRE-013 | P4.1, P2.4, P2.5, P2.7 | KPI-13, KPI-06, KPI-02 |
| Proveedores (talento) | Retener talento con certificaciones visibles y conservar el conocimiento cuando alguien se va | F6, A6 | OETI04 | BRE-009, BRE-004 | P1.7, P3.4, P2.1 | KPI-09, KPI-10 |
| Proveedores (plataformas e IA) | Registrar qué proveedor de nube y de modelos usa cada sistema y qué dependencia crea | F3, D1, D6 | OETI01, OETI03 | BRE-002, BRE-013 | P1.3, P2.7 | KPI-08, KPI-02 |

### Relación con la DOFA

Las cinco fuerzas explican el origen externo de varias oportunidades y amenazas de la DOFA:

| Factor DOFA | Fuerza de la que sale |
|---|---|
| O1 Clientes que piden IA gobernada y auditable | Poder de los compradores |
| O3 Informe SOC 2 tipo II con controles de IA | Poder de los compradores y barrera de entrada |
| O4 Plataformas y certificaciones de los socios | Poder de los proveedores (plataformas) |
| A1 Vencimiento del certificado ISO | Barrera de entrada que se pierde |
| A4 Competidores con gobierno de IA certificado | Rivalidad |
| A6 Rotación de personal hacia el exterior | Poder de los proveedores (talento) y sustitutos (contratación directa) |
| A7 El cliente no autoriza cambios en su infraestructura | Poder de los compradores |

La presión de precio, que viene de los compradores y de los rivales que ofertan para ganar, aparece aquí y no en la DOFA, a propósito. Quedó fuera de la DOFA porque un plan de TI no fija tarifas. Las cinco fuerzas, en cambio, describen la industria completa, y ahí sí tiene que estar.

### Observaciones para revisar en el PETI

Son propuestas del equipo (INT-001); no se aplicaron al PETI Colombia v1.0.

1. **Falta un indicador de productividad de la entrega.** El poder de los compradores y la amenaza de la IA giran alrededor de la productividad, y el PETI no mide ninguna (KPI-01 mide la ejecución del plan, no la entrega). Se podría evaluar un indicador de tiempo de entrega o de frecuencia de despliegue de los pipelines de P2.3. El número KPI-12 está libre.
2. **La dependencia de proveedores de modelos de IA no tiene control explícito.** El inventario de P1.3 podría registrar, por sistema, el proveedor del modelo y la alternativa evaluada, y el sistema de gestión de IA de P1.2 podría incluir un criterio de continuidad del proveedor.
3. **Ubicación en el documento.** Como la guía del MinTIC no pide este análisis, puede ir como anexo o como numeral corto junto a la DOFA en §6, citado desde los motivadores (§5.1).

## Límites de este diagnóstico

- Las calificaciones de 1 a 5 son valoraciones del equipo (INT-001), hechas con la evidencia citada. No salen de una encuesta a clientes ni a competidores.
- El 10-K [1] describe a Perficient en 2023, antes de la privatización. Las cifras de clientes (96 % de EE. UU., 92 % recurrentes, 7 % el mayor) pueden haber cambiado.
- Los datos de Globant [2] son de junio de 2024 y los de Softtek en Bogotá [3], de 2021. Confirman presencia y escala, no el tamaño actual.
- Las cifras de ISG [7], Everest [8], Synergy [10] y Menlo [11] son globales o de Norteamérica, no de Colombia.
- Del informe de Everest [8] solo se leyó el resumen público. El de Menlo [11] mide uso en producción, no gasto, con una muestra de 150 responsables técnicos.
- Se descartó a propósito la cifra de déficit de 68.000 a 112.000 desarrolladores para 2025 que repiten varios medios: viene de un estudio de 2017 y no hay una medición reciente que la confirme.
- Ninguna fuente pública da el número de empleados de Perficient en Colombia ni su participación en el mercado colombiano.
- Las fuentes [1] a [3], [5] a [8] y [10] a [12] se consultaron el 13 de octubre de 2026; [4], [9] y [13] son las mismas de la DOFA, consultadas el 8 de octubre. Ninguna está todavía en el registro de evidencias: para citarlas en el PETI hay que registrarlas antes como filas `PUB-`.

## Fuentes externas

1. Perficient, Inc. (2024). *Form 10-K for the fiscal year ended December 31, 2023* [Informe anual presentado ante la SEC; describe la situación de 2023]. https://www.sec.gov/Archives/edgar/data/1085869/000108586924000040/prft-20231231.htm
2. Caparroso, J. (2024, 4 de junio). Globant ya tiene más empleados en Colombia que en cualquier otro país de Latinoamérica. *Forbes Colombia*. https://forbes.co/2024/06/04/tecnologia/globant-ya-tiene-mas-empleados-en-colombia-que-en-cualquier-otro-pais-de-latinoamerica/
3. Softtek. (2021, 4 de noviembre). *Softtek announces expansion of digital capabilities with global reach in Colombia*. https://www.softtek.com/news-releases/softtek-announces-expansion-of-digital-capabilities-with-global-reach-in-colombia
4. Softtek. (2025, 6 de noviembre). *Softtek, first technology company in Latin America to earn ISO 42001 artificial intelligence certification*. https://www.softtek.com/news-releases/softtek-first-technology-company-in-latin-america-to-earn-iso-42001-artificial-intelligence-certification
5. Lorduy, J. (2025, 6 de octubre). Industria del software colombiano alcanza ventas por 44,2 billones [Cifras del Observatorio Cenisoft presentadas por Fedesoft y datos del DANE]. *Portafolio*. https://www.portafolio.co/tecnologia/industria-del-software-colombiano-alcanza-ventas-por-44-2-billones-641497
6. Valora Analitik. (2026, 6 de enero). *ProColombia acompañó 178 proyectos de inversión extranjera directa en 2025: estos fueron los principales sectores*. https://www.valoraanalitik.com/procolombia-inversion-extranjera-2025/
7. Jones, S., y Rose, M. (2025, 31 de octubre). *Index Insider: AI isn't the only reason providers are feeling pricing pressure*. ISG. https://isg-one.com/articles/index-insider--ai-isn-t-the-only-reason-providers-are-feeling-pricing-pressure
8. Everest Group. (2026, 5 de marzo). *Global Capability Centers (GCCs) market outlook for 2026: What is next for providers* [Resumen público]. https://www.everestgrp.com/report/egr-2026-34-r-7948
9. ENTER.CO. (2026, 18 de marzo). *Empresas extranjeras están contratando más colombianos: estas son las áreas clave*. https://www.enter.co/?p=582237
10. Synergy Research Group. (2025, 19 de noviembre). *Cloud market share trends: Big three together hold 63% while Oracle and the neoclouds inch higher*. https://srgresearch.com/articles/cloud-market-share-trends-big-three-together-hold-63-while-oracle-and-the-neoclouds-inch-higher
11. Menlo Ventures. (2025, 31 de julio). *2025 mid-year LLM market update*. https://menlovc.com/insights/2025-mid-year-llm-market-update
12. Portafolio. (2026, 17 de julio). *Consejo de Estado reactiva el aumento del 23 % del salario mínimo de 2026: esto determinó*. https://www.portafolio.co/economia/gobierno/consejo-de-estado-reactiva-el-aumento-del-23-del-salario-minimo-de-2026-esto-determino-498416
13. AICPA & CIMA. (s. f.). *SOC 2: Reporting on an examination of controls at a service organization relevant to security, availability, processing integrity, confidentiality, or privacy*. https://www.aicpa-cima.com/cpe-learning/publication/soc-2-reporting-on-an-examination-of-controls-at-a-service-organization-relevant-to-security-availability-processing-integrity-confidentiality-or-privacy
14. Sanclemente Castro, J. (s. f.). *Gobierno y Servicios de TI. Unidad 2: Diagnóstico, planeación y gestión de proyectos de TI* [Material de clase, sección 2: 5 fuerzas de Porter]. Facultad de Ingeniería.
