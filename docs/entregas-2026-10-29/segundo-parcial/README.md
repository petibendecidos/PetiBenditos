# Segundo parcial: 29 de octubre de 2026

Copia de los 7 trabajos que se presentan hoy en el segundo parcial de Gobierno y Servicios de TI (docente Jair Sanclemente Castro). Equipo Firmes por la Gobernanza. Cada carpeta tiene el archivo que se muestra y un `guion-*.md` para exponer: por qué se tomó cada decisión y de qué parte del [PETI Colombia v1.0](../../perficient_peti_colombia_2026_2028.md) sale cada elemento. Los guiones no se entregan.

Los originales siguen en `docs/entregas-2026-10-21/`, `docs/entregas-2026-10-22/`, `docs/entregas-2026-10-29/` y en `docs/` (DOFA y Porter). Si se corrige algo, se corrige allá y se vuelve a copiar.

## Orden y reparto

El orden sigue la nota del parcial: primero el diagnóstico, después la estrategia y al final el plan y la gestión. El reparto es el mismo de la matriz de evaluación del equipo.

| # | Bloque de la nota | Trabajo | Expone | Archivo que se muestra | Guion |
|---|---|---|---|---|---|
| 0 | — | Apertura: el hilo que une todo y el cierre | Juan Mateo Salas Arturo (PM) | — | Abajo |
| 1 | Diagnóstico TI | DOFA | Luis Alberto De Avila Mosquera | [foda-perficient.drawio](1_DOFA/foda-perficient.drawio) y [matrices](1_DOFA/Matrices_DOFA_Porter_Perficient_Colombia.xlsx) | [guion-dofa.md](1_DOFA/guion-dofa.md) |
| 2 | Diagnóstico TI | Porter | Luis Alberto De Avila Mosquera | [porter-5-fuerzas….drawio](2_Porter/porter-5-fuerzas-perficient-colombia.drawio) y [docx](2_Porter/Porter_5_fuerzas_Perficient_Colombia.docx) | [guion-porter.md](2_Porter/guion-porter.md) |
| 3 | Diagnóstico TI | Modelo de negocio (Canvas) | Nicolás Chávez Oliveros | [Canvas .pptx](3_Modelo_de_negocio/Modelo_Negocio_TI_Canvas_Perficient_Colombia.pptx) | [guion-modelo-de-negocio.md](3_Modelo_de_negocio/guion-modelo-de-negocio.md) |
| 4 | Diagnóstico TI | Cadena de valor | Nicolás Chávez Oliveros | [Cadena .pptx](4_Cadena_de_valor/Cadena_de_valor_Perficient_Colombia.pptx) | [guion-cadena-de-valor.md](4_Cadena_de_valor/guion-cadena-de-valor.md) |
| 5 | Estrategia | Estrategia de TI | Juan Esteban Aldana | [Estrategia .docx](5_Estrategia_TI/Estrategia_TI_Perficient_Colombia.docx) | [guion-estrategia-ti.md](5_Estrategia_TI/guion-estrategia-ti.md) |
| 6 | Plan y gestión | Diagnóstico BSC | Juan Pablo Sotelo Mejía | [Diagnóstico .docx](6_Diagnostico_BSC/Diagnostico_BSC_Perficient_Colombia.docx) | [guion-diagnostico-bsc.md](6_Diagnostico_BSC/guion-diagnostico-bsc.md) |
| 7 | Plan y gestión | Mapa estratégico BSC | Juan Pablo Sotelo Mejía | [Mapa .png](7_Mapa_estrategico_BSC/Mapa_estrategico_TI_BSC_Perficient_Colombia.png) | [guion-mapa-estrategico.md](7_Mapa_estrategico_BSC/guion-mapa-estrategico.md) |

Juan Mateo responde las preguntas que crucen varios trabajos. Las más probables son las inconsistencias de la última sección.

## Guion de apertura y cierre (Juan Mateo)

**Apertura, unos 45 segundos.**
> Trabajamos el PETI 2026-2028 de la operación de Perficient en Colombia con la metodología del MinTIC, como si Perficient fuera la entidad que formula su plan. Es un trabajo académico: no es un documento oficial de Perficient. Los siete trabajos siguen la misma cadena. El diagnóstico (DOFA, Porter, modelo de negocio y cadena de valor) dice dónde está TI. La estrategia dice a dónde va: cuatro objetivos de TI. El diagnóstico BSC y el mapa estratégico dicen cómo se va a medir que llegó. Todo se apoya en el mismo registro de evidencias: lo que es público tiene su fuente, lo que viene de la cuenta de cliente que analizamos se dice como tal, y lo que es propuesta se dice como propuesta.

**Cierre, unos 30 segundos.**
> La conclusión de los siete trabajos es la misma: la operación no puede competir por precio. Tiene que demostrar controles certificados, IA auditable y una entrega medible. Hoy tiene la base (un SGSI certificado, roles claros y alianzas), pero no el sistema que conecte la ejecución con la estrategia: no hay gobierno de IA, ni presupuesto, ni indicadores por proceso. El PETI lo cierra con 25 proyectos en cuatro fases, y el mapa muestra cómo se mide.

## El hilo entre trabajos (por si preguntan cómo se conectan)

| De | A | Qué pasa |
|---|---|---|
| Porter | DOFA | Explica 7 factores externos (O1, O3, O4, A1, A4, A6, A7) |
| DOFA | Estrategia | Las 13 estrategias del cruce se agrupan en los 9 programas |
| Porter | Canvas | La propuesta de valor responde al poder de los compradores |
| Cadena de valor | Canvas | Las actividades de TI (registro de tiempos, ALM, pruebas de seguridad) son la "línea de producción" |
| Estrategia | Mapa | Los 4 OETI son las 4 prioridades del mapa, con sus 13 metas |
| Diagnóstico BSC | Mapa | El enunciado 16 (sin mapa estratégico, puntaje 3) pidió el mapa; los cambios 1 y 2 piden llevarlo al PETI |

## Inconsistencias entre trabajos (mejor decirlas antes)

| Inconsistencia | Dónde | Qué responder |
|---|---|---|
| La fecha del certificado ISO (11 de octubre o 10 de noviembre de 2026) ya pasó o está por pasar, sin evidencia de recertificación | DOFA (A1), Estrategia (programa a), Mapa (CN1) | La fecha publicada es ambigua (PUB-002). Tomamos la más temprana, y por eso es la amenaza número uno |
| Compradores: 4 en el docx de Porter y 3,6 en la matriz | Porter | El docx es una nota global; la matriz promedia los determinantes (plantilla 3b). Vale la matriz |
| Las metas están en perspectivas distintas | Diagnóstico BSC y Mapa | El diagnóstico usó Kaplan y Norton; el mapa usa el BSC de TI. Vale el mapa |
| P3.5 aparece en OETI03 en el PETI y la Estrategia, y en IF3 (OETI01) en el mapa | Estrategia y Mapa | Se ubicó por su propósito. Se corrige en la versión 1.1 |
| La bibliografía de la Estrategia cita el PETI "versión 2.1" | Estrategia | Es la versión regional; el PETI Colombia es la 1.0 |
| "Retail" en la cadena de valor no tiene fuente | Cadena de valor | Pendiente de respaldar o retirar |

## Lo que nadie debe decir

- "Perficient hace…" sobre algo que solo se vio en la cuenta analizada. Se dice: "en la cuenta analizada (PRV-001)", y nada más: ni el cliente, ni las herramientas por marca, ni el sector.
- "Certificación SOC 2." SOC 2 es un informe de atestación.
- Que algo del PETI ya está en marcha. Todo es propuesta, pendiente del Comité Directivo.
