# Mapa estratégico de TI (BSC de TI)

Entrega del curso Gobierno y Servicios de TI (Universidad Santiago de Cali, docente Jair Sanclemente Castro). Equipo Firmes por la Gobernanza. La carpeta lleva la fecha en que se hizo (29 de octubre de 2026); la fecha de cierre de la tarea no está registrada.

El enunciado no trae instrucciones escritas. Se trabajó con dos imágenes que entregó el docente: el BSC de TI con sus cuatro perspectivas y sus preguntas (contribución al negocio, usuario, interna, innovación) y "8 pasos para crear un mapa estratégico" de BSC Designer. Las últimas diapositivas de la unidad ([Cuadro de Mando Integral Balanced Scorecard -BSC.pdf](../Cuadro%20de%20Mando%20Integral%20Balanced%20Scorecard%20-BSC.pdf), páginas 19 y 20) solo muestran el título "BSC..." y el diagrama clásico de Kaplan y Norton.

| Archivo | Qué es |
|---|---|
| [Mapa_estrategico_TI_BSC_Perficient_Colombia.drawio](Mapa_estrategico_TI_BSC_Perficient_Colombia.drawio) | **Lo que se sube.** Se abre y edita en draw.io (app.diagrams.net) |
| [Mapa_estrategico_TI_BSC_Perficient_Colombia.png](Mapa_estrategico_TI_BSC_Perficient_Colombia.png) | Vista previa renderizada con el visor de draw.io, por si la plataforma pide imagen |
| [sustentacion-mapa-estrategico.md](sustentacion-mapa-estrategico.md) | Guía para exponer: por qué se tomó cada decisión y de qué parte del PETI sale cada elemento. No se entrega |
| [segundo-parcial/](segundo-parcial/README.md) | Copia de los 7 trabajos del segundo parcial (DOFA, Porter, Canvas, cadena de valor, estrategia, diagnóstico BSC y mapa), cada uno con su guion de exposición, más el reparto entre integrantes |

## Cómo se aplicaron los 8 pasos

| Paso | En el mapa | Fuente |
|---|---|---|
| 1. Misión, visión, valores | Misión y visión de TI del PETI; cuatro valores de TI | PETI §7. Los valores los propone el equipo: el PETI no los define |
| 2. Cuatro perspectivas | Las del BSC de TI, cada una con su pregunta y su equivalente en el BSC de Kaplan y Norton | Imagen del docente |
| 3. Prioridades estratégicas | OETI01 a OETI04, un color cada una | PETI §7 |
| 4. Objetivos | 14 objetivos (CN1-CN4, US1-US3, PI1-PI4, IF1-IF3), cada uno con los objetivos corporativos que apoya | Ubicación del diagnóstico BSC del 22 de octubre, ajustada a las perspectivas de TI |
| 5. Razonamiento | 13 flechas causa-efecto numeradas y explicadas en el panel derecho | Dependencias del PETI §9 y criterio del equipo |
| 6. Métricas | Los 13 KPI del PETI con metas de año 1 y año 2, marcados como resultado o actuación; tres métricas propuestas sin KPI | PETI §7 y §10 |
| 7. Iniciativas | Los 25 proyectos del portafolio, cada uno en un solo objetivo | PETI §9 |
| 8. Cascada | Corporativo → TI Colombia → Comité Táctico → célula | PETI §5.2 y §12 |

Los códigos CN, US, PI e IF son del mapa; no son IDs del PETI y no se agregaron al documento.

## Cómo regenerar

```
python scripts/generar_mapa_estrategico_bsc.py docs/entregas-2026-10-29/Mapa_estrategico_TI_BSC_Perficient_Colombia.drawio
```

Regenerar borra lo que se haya movido o editado a mano en draw.io. El PNG no se regenera solo: se exporta desde draw.io (Archivo → Exportar como → PNG) o con el visor de draw.io en un navegador.

## Pendientes

- Confirmar con el docente si el mapa se entrega en .drawio, en imagen o en PDF.
- Agregar los nombres de los integrantes si la plataforma los pide en el archivo.
- Tres métricas son propuestas y no existen en el PETI (costo de TI por hora facturada, índice de satisfacción con los servicios de TI, pruebas de concepto evaluadas por el CoE). US3 e IF2 no tienen proyecto. Para llevar el mapa y las perspectivas al PETI Colombia hace falta una versión 1.1 con su entrada en el control de cambios (cambio 1 del diagnóstico BSC).
