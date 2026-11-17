# Diagnóstico de sensibilización gerencial y diagnóstico de control en TI (COBIT 2019)

Entrega del curso Gobierno y Servicios de TI (Universidad Santiago de Cali, docente Jair Sanclemente Castro): "Diagnóstico de Sensibilización Gerencial - Diagnóstico de Control en TI", con los dos formatos de COBIT 2019 que entregó el docente. Equipo Firmes por la Gobernanza. Se hizo el 16 de noviembre de 2026 y se basa en el PETI Colombia v1.0 ([perficient_peti_colombia_2026_2028.md](../../perficient_peti_colombia_2026_2028.md)), en las entregas anteriores y en el [registro de evidencias](../../registro-de-evidencias.md) (PUB-030 a PUB-035 se agregaron para esta entrega).

| Archivo | Qué es |
|---|---|
| [Diagnostico_Sensibilizacion_Gerencial_COBIT2019_Perficient_Colombia.xls](Diagnostico_Sensibilizacion_Gerencial_COBIT2019_Perficient_Colombia.xls) | **Se sube.** Formato del docente diligenciado: importancia, desempeño, quién lo hace, auditado, formalidad y responsable para los 40 objetivos; hoja "Riesgo" con importancia × desempeño en fórmulas |
| [Diagnostico_Control_TI_COBIT2019_Perficient_Colombia.xlsx](Diagnostico_Control_TI_COBIT2019_Perficient_Colombia.xlsx) | **Se sube.** Formato del docente diligenciado: nivel de capacidad de 0 a 5 y observaciones con las brechas y proyectos del PETI; hoja "Resultados" con resumen por dominio, detalle por objetivo, nivel objetivo al mes 24 y dos gráficos |
| [Analisis_Diagnosticos_COBIT2019_Perficient_Colombia.docx](Analisis_Diagnosticos_COBIT2019_Perficient_Colombia.docx) | Análisis en español: origen de las herramientas, criterio de llenado, correcciones a los formatos, resultados, cruce de los dos diagnósticos, comparación con los diagnósticos anteriores y recomendaciones para el PETI. Sirve de anexo o para sustentar |
| [diagnosticos-cobit.md](diagnosticos-cobit.md) | Fuente de los tres archivos anteriores |
| `resultados.png`, `resultados_por_proceso.png` | Gráficos de la hoja Resultados, exportados por el script; van dentro del Word |
| [formato-docente/](formato-docente/) | Formatos originales, copiados de `D:\Descargas` |

## Resultado

| Dominio | Nivel actual promedio | Nivel al mes 24 con el PETI | Objetivos de riesgo alto |
|---|---|---|---|
| EDM: Evaluar, dirigir y monitorear | 0,80 | 2,60 | 3 de 5 |
| APO: Alinear, planificar y organizar | 1,36 | 2,57 | 5 de 14 |
| BAI: Construir, adquirir e implementar | 1,36 | 2,55 | 0 de 11 |
| DSS: Entregar, dar servicio y soporte | 1,17 | 1,83 | 1 de 6 |
| MEA: Monitorear, evaluar y valorar | 1,00 | 2,75 | 2 de 4 |
| Total | **1,23 de 5** | 2,48 | **11 de 40** |

- Los 11 objetivos de riesgo alto (importancia × desempeño de 20 o más) están en nivel 0 o 1, y en los 11 el responsable es "No se sabe". En total, 24 de 40 objetivos no tienen responsable conocido.
- Solo 4 objetivos están formalizados y auditados, todos por el SGSI ISO/IEC 27001 (APO12, APO13, DSS05, MEA04). APO13 es el único en nivel 3.
- Siete de los 11 objetivos de riesgo alto dependen de P2.8, que está en la fase 2. Continuidad (DSS04), problemas (DSS03) y proveedores (APO10) no tienen proyecto en el PETI.

## Decisiones que se tomaron sin consultar

- **Se corrigió el formato de control en TI.** Traía 37 filas con códigos de COBIT 2019 y nombres de COBIT 5: APO09 a APO12 corridos, BAI11 como "problemas", MEA02 y MEA03 invertidos, y faltaban APO09 (acuerdos de servicio), APO13, APO14 y MEA04. Quedó con los 40 objetivos y una nota que explica el cambio. Si el docente quiere el formato tal como lo entregó, hay que rehacerlo con 37 filas y perder el cruce con el otro diagnóstico.
- En el formato de sensibilización se corrigieron dos erratas ("Build, Acquire and **Implement**" y "APO13 Manage**d** Security").
- Se respetó la escala de desempeño del formato (1 = muy bien, 5 = no se sabe o mal), que está invertida frente a la original de COBIT 3 (PUB-030). El análisis lo explica.
- El responsable se escribió como rol, no como nombre.
- Los nombres del formato de sensibilización quedaron en inglés y las respuestas de texto en español, como en la autoevaluación de EIS.

## Cómo regenerar

```
python scripts/generar_diagnosticos_cobit.py "docs/entregas-2026-11-16/diagnosticos-cobit/formato-docente/COBIT 2019_Management-Awareness-Diagnostic_v1.0.xls" docs/entregas-2026-11-16/diagnosticos-cobit/formato-docente/Diagnostico_Control_TI_COBIT_2019.xlsx docs/entregas-2026-11-16/diagnosticos-cobit/diagnosticos-cobit.md docs/entregas-2026-11-16/diagnosticos-cobit/Diagnostico_Sensibilizacion_Gerencial_COBIT2019_Perficient_Colombia.xls docs/entregas-2026-11-16/diagnosticos-cobit/Diagnostico_Control_TI_COBIT2019_Perficient_Colombia.xlsx
python scripts/md_a_docx_simple.py docs/entregas-2026-11-16/diagnosticos-cobit/diagnosticos-cobit.md docs/entregas-2026-11-16/diagnosticos-cobit/Analisis_Diagnosticos_COBIT2019_Perficient_Colombia.docx "Diagnósticos de sensibilización gerencial y de control en TI (COBIT 2019) — Perficient, operación en Colombia — Trabajo académico, Equipo Firmes por la Gobernanza"
```

Necesita Excel. El script lee las dos tablas de 40 objetivos de la fuente, llena los formatos por COM (para conservar el .xls y los estilos del docente), reescribe las tablas de resultado de la fuente y se detiene si los promedios que calcula Excel no coinciden con los suyos. La prosa ("Lectura", "Cruce", "Comparación", "Recomendaciones") no se recalcula: si cambias un valor, revísala.

## Estado

Lista para subir sin cambios: los dos libros y el Word del análisis. Los tres llevan solo la fecha del 16 de noviembre de 2026 y no tienen marcas de pendiente ni de verificación.

- El nivel de seguridad (APO13 en 3) se apoya en el certificado ISO/IEC 27001 publicado (PUB-002). El análisis muestra el efecto de no contar con él (promedio 1,13) como análisis de sensibilidad.
- Las siete recomendaciones para el PETI Colombia van en el análisis como resultado del diagnóstico. Aplicarlas al PETI es otro trabajo: requiere una versión 1.1 con su entrada en el control de cambios (§15).
- Los datos de COBIT 2019 de la skill (`.claude/skills/marcos-referencia/cobit-2019.md`) tienen fuente en el registro (PUB-030 a PUB-035); lo que esas fuentes no respaldan se retiró.
