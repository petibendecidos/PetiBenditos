# Guion: diagnóstico BSC

**Expone:** Juan Pablo Sotelo Mejía. **Se muestra:** [Diagnostico_BSC_Perficient_Colombia.docx](Diagnostico_BSC_Perficient_Colombia.docx), el formato del docente diligenciado con el radar. La fuente con los 40 sustentos está en [diagnostico-bsc.md](../../../entregas-2026-10-22/diagnostico-bsc.md).

Abreviaturas: BRE = brecha (§8), P = proyecto (§9), KPI = indicador (§10). PUB = fuente pública, PRV-001 = la cuenta analizada e INT-001 = análisis del equipo.

## En 30 segundos

> Calificamos los 40 enunciados del formato, de 0 a 10, con un criterio fijo y la evidencia de cada uno. Total: 182 de 400, el 45,5 %, en nivel "en construcción". El radar se encoge en el orden del método: la estrategia se conoce arriba (57), se debilita al convertirla en indicadores (46) y se rompe al bajar a los procesos (36). Sincronización y despliegue es el único elemento en nivel bloqueador. La ejecución diaria es disciplinada (43), pero nada la conecta con la estrategia. Cuatro de las ocho causas críticas no tienen proyecto en el PETI. Ese es el hallazgo principal.

## Decisiones y su porqué

| Decisión | Por qué | Referencia |
|---|---|---|
| Rúbrica de 0 a 10 hecha por el equipo | El formato no trae criterio. Sin una regla, 40 puntajes no se pueden comparar | Diagnóstico, "criterio de calificación" |
| "Solo se observó en la cuenta analizada" vale como máximo 3-4 | Una cuenta no es la operación completa | Regla de evidencia (PRV-001) |
| Lo que no se puede demostrar no recibe puntaje alto | Aunque sea probable en una empresa del tamaño de Perficient. Un puntaje bajo significa "no demostrable", no "inexistente" | INT-001 |
| Niveles por elemento: bloqueador, en construcción, funcional e impulsor | Para leer el radar. El formato no trae niveles | Criterio del equipo |
| Proponer cambios al PETI sin aplicarlos | Aplicarlos exige la versión 1.1 con su entrada en el control de cambios (§15) | Regla del PETI |

## Resultado

| Elemento | Puntaje | Nivel |
|---|---|---|
| 1. Enfoque estratégico (enunciados 1-10) | 57 | En construcción |
| 2. Traslado hacia el BSC (11-20) | 46 | En construcción |
| 3. Sincronización y despliegue (21-30) | 36 | **Bloqueador** |
| 4. Cultura de ejecución (31-40) | 43 | En construcción |
| Total | 182 / 400 (45,5 %) | En construcción |

Coincide con la MEFI (2,27) de la DOFA: las debilidades internas pesan más.

## Las 8 causas críticas (puntaje de 3 o menos)

| Enunciado | Puntaje | Por qué | Respuesta del PETI |
|---|---|---|---|
| 39. Desempeño y compensación ligados al BSC | 1 | No hay un BSC con el cual ligarlos | Ninguna (es tema de Talento humano) |
| 28. Presupuesto ligado a objetivos | 2 | No hay guía de presupuesto de TI | P2.8 (BRE-011) |
| 12. Datos de proveedores | 3 | No se evalúa el servicio de pruebas de seguridad ni el de nube | Ninguna. Podría entrar en P1.1 (ISO 27001, Anexo A, 5.19 a 5.22) |
| 16. Mapa estratégico | 3 | Los objetivos no estaban en perspectivas BSC | P2.8 (BRE-015). El mapa estratégico de hoy lo atiende, aunque todavía no está dentro del PETI |
| 22. Cliente-proveedor de los procesos | 3 | No hay caracterización de procesos | Ninguna |
| 23. Indicadores de procesos | 3 | Solo dos procesos tienen indicador propuesto | KPI-05 y KPI-06 (P2.2, P2.4) |
| 24. Objetivos por proceso | 3 | El PETI se organiza por objetivo de TI, no por proceso | Ninguna |
| 29. Despliegue en cascada | 3 | No hay comités ni objetivos por nivel | §12 (comités) y P2.8 |

Sin proyecto quedan los enunciados 12, 22, 24 y 39.

## Los 5 cambios que proponemos al PETI

1. En §7, poner la perspectiva BSC de cada meta y un mapa estratégico (enunciado 16). Es la entrega siguiente.
2. En §10, poner la fuente de datos de cada indicador y agregar el costo de TI por hora facturada (enunciado 17).
3. Ampliar P2.8 para que caracterice los procesos y les dé objetivos e indicadores (enunciados 22 a 24).
4. Incluir en P1.1 la evaluación de los proveedores de pruebas de seguridad y de nube (enunciado 12).
5. Recomendar a Talento humano que la evaluación del desempeño incluya metas del PETI (enunciado 39).

## Preguntas difíciles

**¿Por qué no hicieron una encuesta?** En una aplicación real, cada directivo y cada líder llenaría el formato y se promediarían las respuestas. No tenemos acceso a ellos, así que es la valoración del equipo con evidencia (INT-001), y lo decimos.

**¿Por qué el enunciado 1 tiene 8 si todo lo demás está bajo?** Perficient declara en público su foco por industria (PUB-025, PUB-007). Es lo más demostrable que hay.

**¿Por qué la cultura de ejecución (43) supera a la sincronización (36)?** En la cuenta analizada se trabaja con sprints, reunión diaria y roles claros (PRV-001). Hay disciplina, pero no hay un sistema que la conecte con la estrategia.

**La ubicación de las metas aquí no coincide con el mapa estratégico.** Aquí usamos las perspectivas de Kaplan y Norton (financiera, cliente, procesos, aprendizaje). En el mapa usamos las del BSC de TI (contribución al negocio, usuario, interna, innovación). Por eso KPI-04 pasa de procesos a usuario y KPI-01 pasa a contribución al negocio. El mapa es la versión que vale.
