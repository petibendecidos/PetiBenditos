---
name: redaccion-peti
description: Usar cuando se redacta, reescribe, completa, recorta o corrige cualquier texto del PETI de Perficient (introducción, alcance, motivadores, contexto, situación actual, situación objetivo, brechas, fichas de proyecto, indicadores, riesgos, comunicaciones, gobernanza), cuando el usuario pide que suene más natural, menos a IA, menos a folleto comercial o más institucional, cuando hay que quitar palabras rebuscadas o anglicismos, o cuando se prepara un resumen o presentación del PETI para el profesor.
argument-hint: "[numeral o sección] [acción: redactar|reescribir|recortar|revisar]"
---

# Redacción del PETI

## Principio

El PETI es un plan institucional de TI, no un folleto de Perficient ni un trabajo de grado. Cada oración hace una de cuatro cosas y se nota cuál: **describe un hecho con evidencia** (AS-IS), **propone** algo (TO-BE, portafolio), **define** un término o una regla, o **mide** algo (indicadores). Un hecho sin evidencia se reformula como hipótesis o se marca. Una propuesta nunca se escribe como si ya existiera.

El registro de referencia es el de los PETI de MinCiencias y MinTIC: sobrio, impersonal, con tablas donde hay datos y prosa donde hay razonamiento. El equipo que firma es de estudiantes que asumen el rol del equipo de arquitectura y gobernanza de TI; el texto debe poder defenderse en voz alta ante el profesor sin leer.

## Antes de escribir

1. Ubica el numeral y lee qué exige la norma para él con la skill `guia-peti` ([plantilla-capitulos.md](../guia-peti/plantilla-capitulos.md)).
2. Si el texto afirma algo sobre Perficient, su operación o la cuenta analizada, busca el ID en `docs/registro-de-evidencias.md`. Si no hay ID, usa la skill `evidencias-peti` o deja `[EVIDENCIA: qué se necesita]`. Nunca tomes una cifra de los `docs/perficient_*.md` sin fuente primaria: sus citas `[n]` no llevan a ninguna parte.
3. Si nombras un marco o una norma (COBIT, ISO 27001, SOC 2, Ley 1581…), comprueba con `marcos-referencia` cómo se cita y qué exige de verdad.
4. Si el texto toca brechas, proyectos, indicadores o riesgos, mantén los IDs existentes y comprueba la cadena con `trazabilidad-peti`.
5. Lee [estilo-natural.md](estilo-natural.md) y aplícalo siempre. Al entregar, recorre su lista de revisión.

## Contrato de salida

1. **El texto** listo para pegar en el Markdown del PETI, con IDs de evidencia entre paréntesis `(PUB-002)` y marcadores `[EVIDENCIA: …]` donde falte.
2. **Afirmaciones y su estado**: cada hecho del texto con su evidencia (ID), o "propuesto", o marcador.
3. **Impacto en otros numerales**: IDs creados o modificados y qué otras secciones tocan (por ejemplo, una brecha nueva exige proyecto en §13 e indicador en §14).
4. **Entrada para el control de cambios** (§16 en la v2.1, §15 en el PETI Colombia) si el texto va a reemplazar contenido.

Si el usuario pide solo el texto, entrega el texto y la lista de afirmaciones sin evidencia; no omitas esa lista.

## Reglas de fondo

| Regla | Cómo se aplica |
|---|---|
| Hecho con evidencia | "Perficient pasó a ser una compañía privada el 2 de octubre de 2024 (PUB-001)." |
| Alcance de la evidencia | Lo que viene de entrevistas o de la arquitectura de la cuenta se escribe "en la cuenta analizada se observó… (PRV-001)". Nunca "Perficient hace…" ni "en LATAM se hace…". |
| Propuesto, no hecho | TO-BE y portafolio en futuro o con "se propone": "Se propone formalizar un comité táctico mensual". Nunca "El comité táctico sesiona mensualmente". |
| Sin tono comercial | Fuera "los más altos estándares", "líder", "de clase mundial", "excelencia", "maximizar el valor", "transformar radicalmente". Un reconocimiento (Inner Circle, IDC) se nombra con su fuente y se dice qué implica para TI; no se usa como adjetivo. |
| Metas medibles | "> 85 %" solo con fórmula, línea base y fuente en el numeral de indicadores (§10). Sin línea base, la meta se marca propuesta y se dice cómo se medirá la línea base. |
| Objetivos de TI | Verbo en infinitivo, qué y no cómo, SMART, perspectiva BSC (guía, Actividad 8). |
| Brechas | Nombre corto del elemento, acción (crear, modificar, eliminar, mantener), justificación con el hallazgo del AS-IS que la origina, tiempo y costo estimados. |
| Términos de marcos | SOC 2 es un **informe de atestación**, no una certificación ni una acreditación. ISO 27001 se **certifica**. NIST AI RMF se **adopta**; no se certifica. |
| Fechas | En el texto, "2 de octubre de 2024". En tablas, `2024-10-02`. Nunca `10/11/2026` ni "2-oct-2024". |
| Cifras y porcentajes | Coma decimal y espacio antes de %: "85 %", "0,9". Rangos con "entre… y…" o guion. |
| Siglas y anglicismos | La primera vez: término en español y sigla en inglés entre paréntesis, "gestión del ciclo de vida de aplicaciones (ALM)". Nombres de producto y de marca, tal cual. "AI-Native" y "AI-First" solo como posicionamiento declarado de Perficient, entre comillas o en cursiva y con fuente. |
| Títulos | Mayúscula solo en la primera palabra y en nombres propios: "Situación actual", no "Situación Actual". No cambies títulos existentes en masa sin pedirlo: rompe los enlaces del índice. |
| Símbolos | Sin emojis ni semáforos (🔴 ✅ ⚠️) en la versión de entrega: se reemplazan por texto ("Alto", "Implementado", "Parcial"). |
| Información restringida | Nada que reidentifique la cuenta analizada. Ver `evidencias-peti`. |

## Voz por numeral

| Numeral | Voz |
|---|---|
| Introducción, objetivo, alcance | Directa: qué es el plan, para qué periodo, qué cubre y qué no. |
| Marco normativo | Tabla; cada fila dice qué exige la norma a Perficient y si aplica, se adapta o es referencia. |
| Motivadores y rupturas | Argumentativa y breve: el hecho (con ID) y su consecuencia para TI. |
| Contexto y modelo operativo | Descriptiva, cercana a la ficha de la entidad. |
| Situación actual | Cautelosa y factual. Distingue lo observado en la cuenta de lo corporativo. Si algo no existe, lo dice. |
| Situación objetivo | Propositiva, en futuro, con principios y estado deseado por dominio. |
| Brechas y oportunidades | Telegráfica en tablas; una oración de justificación por fila. |
| Portafolio | Operativa: qué, para qué, por qué, cómo, quién, cuándo, cuánto. |
| Indicadores | Fórmula primero; luego meta, frecuencia, fuente y responsable. |
| Riesgos | Causa, evento, consecuencia; control; responsable. |
| Comunicaciones y gobernanza | Instrucciones concretas: quién comunica qué, a quién, por dónde, cada cuánto. |

## Señales de alerta (detente y corrige)

- Un porcentaje, un plazo o un monto sin ID de evidencia ni marca de "propuesto".
- "Perficient tiene/usa/implementa" seguido de algo que solo aparece en PRV-001 o PRV-002.
- Adjetivos de folleto: "robusto", "de vanguardia", "integral", "holístico", "disruptivo", "sin precedentes".
- Tres párrafos o tres viñetas seguidas con la misma forma y longitud; tríadas en cada frase.
- "Acreditación SOC 2", "certificación NIST", "cumplimiento SOX" presentado como vigente.
- Una brecha que no aparece en el portafolio o un proyecto sin brecha, oportunidad ni indicador.
- Un texto que cambia contenido sin entrada en el control de cambios.

## Lo que esta skill no hace

- No inventa cifras, fechas, certificaciones ni alianzas. Un marcador es aceptable; un dato falso no.
- No decide qué norma aplica (`marcos-referencia`) ni si una fuente es válida (`evidencias-peti`).
- No reorganiza la estructura del documento sin que el usuario lo pida; propone el cambio y su impacto.
