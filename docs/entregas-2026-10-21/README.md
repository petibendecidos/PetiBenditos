# Entregas del 21 de octubre de 2026

Entregas del curso Gobierno y Servicios de TI (Universidad Santiago de Cali, docente Jair Sanclemente Castro) que cerraron el 21 de octubre de 2026 a las 23:59. Equipo Firmes por la Gobernanza. Todas se basan en el PETI Colombia v1.0 ([perficient_peti_colombia_2026_2028.md](../perficient_peti_colombia_2026_2028.md)) y en el [registro de evidencias](../registro-de-evidencias.md).

| Entrega en la plataforma | Archivos | Origen |
|---|---|---|
| Cargar resultado diagnóstico DOFA y Porter ajustada | [DOFA final](../dofa-final-perficient-colombia.md), [Porter](../Porter_5_fuerzas_Perficient_Colombia.docx), [Analisis_DOFA_Porter_Perficient_Colombia.docx](Analisis_DOFA_Porter_Perficient_Colombia.docx), [Matrices_DOFA_Porter_Perficient_Colombia.xlsx](Matrices_DOFA_Porter_Perficient_Colombia.xlsx) | DOFA y Porter: trabajo previo del equipo. Análisis y matrices: hechos para esta entrega |
| Cargar resultados modelo de negocio TI | [Modelo_Negocio_TI_Canvas_Perficient_Colombia.pptx](Modelo_Negocio_TI_Canvas_Perficient_Colombia.pptx) | Hecho para esta entrega |
| Cargar plantilla estrategia de TI | [Estrategia_TI_Perficient_Colombia.docx](Estrategia_TI_Perficient_Colombia.docx) | Borrador de un integrante sobre la plantilla *IT Strategy* de Project Management Docs, con la fecha del certificado ISO corregida en dos sitios |
| Cargar resultados cadena de valor TI | [Cadena_de_valor_Perficient_Colombia.pptx](Cadena_de_valor_Perficient_Colombia.pptx) | Borrador de un integrante, sin cambios de contenido; fechas de la nota al pie en formato largo. Sus afirmaciones públicas quedaron registradas como PUB-016 a PUB-025 |

`DOFA_Porter_Ajustada_Perficient_Colombia.docx` es una versión anterior del análisis, generada con la plantilla del MinTIC. La reemplaza `Analisis_DOFA_Porter_Perficient_Colombia.docx`; no se entrega.

## Qué contiene el análisis DOFA y Porter

Fuente: [dofa-porter-ajustada.md](dofa-porter-ajustada.md).

- **¿La DOFA guía decisiones o solo documenta un momento?** Guía decisiones porque se le agregaron importancia por factor, cruce en 13 estrategias con acciones, orden de ejecución y una regla de revisión trimestral. El ejemplo es A1: la fecha más temprana del certificado ISO (11 de octubre de 2026) pasó entre la DOFA del 8 de octubre y esta entrega.
- **Tipos de estrategia**, con los nombres del enunciado y del material "Estrategias FA, FO, DA y DO": FO ofensivas o para atacar (maxi-maxi), DO adaptativas o para movilizar (mini-maxi), FA defensivas o para defender (maxi-mini), DA de supervivencia o para reforzar (mini-mini).
- **MEFI 2,27 y MEFE 1,70**: las dos bajo el promedio de 2,5.
- **Cinco fuerzas por determinantes**: rivalidad 4,4; proveedores 4,0; compradores 3,6; sustitutos 3,3; nuevos entrantes 3,0.
- **Mayor desafío para el área de TI**: el poder de los compradores (controles demostrables, infraestructura del cliente y ahorro de la IA en el precio), aunque la rivalidad sea la fuerza más intensa de la industria.
- **¿TI es rentable o destruye dinero?** Hace posible el ingreso, pero hoy no puede demostrar que es rentable; pierde o arriesga dinero en horas sin conciliar, nube sin control, la certificación sin renovación confirmada e IA sin controles. Se proponen cuatro mediciones, entre ellas el costo de TI por hora facturada.
- **Perfil competitivo**: Perficient 2,60; Globant 2,95; Softtek 3,20. Las calificaciones de los competidores son valoración del equipo.

## Qué contiene el libro de matrices

| Hoja | Plantilla de origen | Ajuste |
|---|---|---|
| 0 Guía | — | Qué se tomó de cada plantilla y qué se dejó por fuera |
| 1 DOFA | DAFO (.xls) y 2a (.xlsx) | Factores con ID de evidencia e importancia de 1 a 5 |
| 2 MEFI | Matriz EFI (.xls) y 2e (.xlsx) | Escala de Fred David; el .xls tenía invertidos el 1 y el 2 |
| 3 MEFE | Matriz EFE (.xls) y 2f (.xlsx) | La calificación mide la respuesta de la organización, no la importancia |
| 4 DOFA cruzada | 2d (.xlsx) y material de estrategias | Puntaje calculado desde la hoja 1 |
| 5 Cinco fuerzas | 3b (.xlsx) | Determinantes con evidencia en lugar de variables genéricas |
| 6 Perfil competitivo | MPC (.xls) y 3a (.xlsx) | Escala de 1 a 4 |
| 7 Seguimiento | Evaluación de la estrategia y Plan de mejoramiento (.xls); 7e (.xlsx) | Proyectos e indicadores del PETI Colombia |

No se usaron PEYEA (no hay estados financieros públicos de la operación), la matriz cuantitativa de estrategias, BCG, ADL ni McKinsey (no hay ventas por unidad de negocio).

## Cómo regenerar

```
python scripts/md_a_docx_simple.py docs/entregas-2026-10-21/dofa-porter-ajustada.md docs/entregas-2026-10-21/Analisis_DOFA_Porter_Perficient_Colombia.docx "DOFA y Porter ajustada — Perficient, operación en Colombia — Trabajo académico, Equipo Firmes por la Gobernanza"
python scripts/generar_matrices_dofa_porter.py docs/entregas-2026-10-21/Matrices_DOFA_Porter_Perficient_Colombia.xlsx
python scripts/generar_canvas_modelo_negocio.py docs/entregas-2026-10-21/Modelo_Negocio_TI_Canvas_Perficient_Colombia.pptx
```

El libro de matrices sale sin valores calculados: se abre en Excel para que calcule. Regenerar el Word o la presentación borra cualquier cambio hecho a mano en esos archivos (por ejemplo, los nombres de los integrantes).

## Pendientes

- Los nombres de los integrantes no están en ningún archivo; se agregan a mano en la portada o en el pie.
- Confirmar con A-Lign el estado del certificado ISO/IEC 27001 y actualizar A1 en la DOFA y la ficha de P1.1 del PETI Colombia, que todavía dice "antes del 11 de octubre de 2026".
- Registrar como filas `PUB-` las fuentes externas de la DOFA ([1] a [9]) y de Porter ([1] a [14]).
- Comprobar las calificaciones de Globant y Softtek en el perfil competitivo (certificaciones vigentes, alianzas).
- Conseguir una fuente para "retail" en las ofertas por industria de la cadena de valor.
