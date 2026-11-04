# Entrega del 22 de octubre de 2026

Entrega del curso Gobierno y Servicios de TI (Universidad Santiago de Cali, docente Jair Sanclemente Castro): diagnóstico estratégico enfocado en la gestión y gobierno de TI mediante BSC. Equipo Firmes por la Gobernanza. Se basa en el PETI Colombia v1.0 ([perficient_peti_colombia_2026_2028.md](../perficient_peti_colombia_2026_2028.md)), en las entregas del [21 de octubre](../entregas-2026-10-21/README.md) y en el [registro de evidencias](../registro-de-evidencias.md).

| Archivo | Qué es |
|---|---|
| [Diagnostico_BSC_Perficient_Colombia.docx](Diagnostico_BSC_Perficient_Colombia.docx) | **Lo que se sube.** El formato del docente diligenciado: 40 puntajes con su sustento, totales, tabla final con nivel, radar nativo de Word (editable) y análisis |
| [diagnostico-bsc.md](diagnostico-bsc.md) | Fuente: criterio de calificación, tabla de los 40 puntajes y análisis del punto 5 |
| [formato-docente/](formato-docente/) | Formato original del docente (.doc), copiado de `D:\Descargas` |

## Resultado

| Elemento | Puntaje | Nivel |
|---|---|---|
| 1. Enfoque estratégico | 57 / 100 | En construcción |
| 2. Traslado hacia el BSC | 46 / 100 | En construcción |
| 3. Sincronización y despliegue | 36 / 100 | Bloqueador |
| 4. Cultura de ejecución | 43 / 100 | En construcción |
| Total | 182 / 400 (45,5 %) | En construcción |

- La estrategia se conoce en el nivel corporativo, se debilita al convertirla en indicadores y metas y se rompe al bajar a los procesos. Coincide con la MEFI de 2,27 del 21 de octubre.
- La cultura de ejecución supera a la sincronización: en la cuenta analizada se ejecuta con disciplina, pero nada conecta esa ejecución con la estrategia (presupuesto, indicadores por proceso, cascada).
- Ocho causas críticas (puntaje de 3 o menos): 12, 16, 22, 23, 24, 28, 29 y 39. Cuatro no tienen proyecto en el PETI: 12, 22, 24 y 39.
- Se propone ubicar las 13 metas del PETI en las cuatro perspectivas del BSC (la guía del MinTIC lo permite en la Actividad 8). La perspectiva financiera solo tiene KPI-02.

La rúbrica de 0 a 10 y los niveles por elemento (bloqueador, en construcción, funcional, impulsor) son criterio del equipo; el formato no trae ninguno. Los puntajes son valoración del equipo (INT-001), no una encuesta al personal de Perficient.

## Cómo regenerar

```
python scripts/generar_diagnostico_bsc.py "docs/entregas-2026-10-22/formato-docente/DIAGNOSTICO BSC GOBIERNO TI GySTI.doc" docs/entregas-2026-10-22/diagnostico-bsc.md docs/entregas-2026-10-22/Diagnostico_BSC_Perficient_Colombia.docx
```

Necesita Word: `scripts/word_com_bsc.ps1` convierte el .doc y dibuja el radar. Los totales se calculan desde la tabla de puntajes; si cambias un puntaje, revisa que el análisis mencione los totales nuevos (el script se detiene si no los encuentra). Regenerar borra lo que se haya editado a mano en el Word, como los nombres de los integrantes.

Si Word queda abierto en segundo plano tras un error, ciérralo antes de volver a ejecutar: un archivo `~$` o una entrada de recuperación de documentos hace que Word abra un diálogo invisible y la automatización se quede esperando.

## Pendientes

- Escribir los nombres de los integrantes en "Evaluadores" (hoy dice `[integrantes]`).
- Los cinco cambios propuestos al PETI Colombia (perspectivas BSC en §7, fuente de datos en §10, alcance de P2.8 y P1.1, recomendación a Talento humano) no se aplicaron: requieren la versión 1.1 del PETI con su entrada en el control de cambios.
- Siguen abiertos los pendientes del 21 de octubre, en especial el estado del certificado ISO/IEC 27001 (PUB-002).
