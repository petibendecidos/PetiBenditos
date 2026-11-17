# Flujo automatizado de gobierno de TI con ISO/IEC 38500:2024

Entrega del curso Gobierno y Servicios de TI (Universidad Santiago de Cali, docente Jair Sanclemente Castro): "Cargar flujo automatizado de Gobierno de TI - ISO 38500 2024". Abre el 12 y cierra el 18 de noviembre de 2026 a las 23:59. Equipo Firmes por la Gobernanza. El docente dio una imagen de un flujo de n8n de ejemplo (informe semanal de redes sociales) y la vista previa de la norma; el equipo agregó tres documentos de apoyo (guía EIS 2024, capítulo ITG10 y presentación de Garibay), registrados como PUB-026 a PUB-029.

| Archivo | Qué es |
|---|---|
| [flujo-gobierno-celulas.json](flujo-gobierno-celulas.json) | **Lo que se sube.** El flujo de n8n para importar, con marcadores (`__SPREADSHEET_ID__`, `__CREDENCIAL_SHEETS__`, `__CREDENCIAL_GMAIL__`) en lugar de los IDs reales |
| [Flujo_Gobierno_TI_ISO38500_Perficient_Colombia.docx](Flujo_Gobierno_TI_ISO38500_Perficient_Colombia.docx) | **Lo que se sube.** Qué hace el flujo, por qué es distinto del ejemplo, correspondencia con la ISO/IEC 38500:2024, indicadores, resultado de la ejecución con capturas, instalación y límites |
| [flujo-gobierno-iso38500.md](flujo-gobierno-iso38500.md) | Fuente del Word |
| [hoja-gobierno-celulas.xlsx](hoja-gobierno-celulas.xlsx) | La hoja de Google en Excel (Config, Celulas, Umbrales, Mediciones, Historial, Decisiones), con correos de ejemplo |
| `capturas/` | Lienzo con la ejecución, correo de aprobación, aviso a líderes (con los correos tapados), bitácora de decisiones e historial |

## Resultado

Tres ejecuciones manuales el 16 de noviembre de 2026, las tres con éxito, sobre el ciclo 2027-09 de los datos sintéticos: 10 células en rojo (una solicitud de aprobación al Comité), 2 en amarillo (C02 y C07, un aviso a sus líderes cada una) y ninguna en verde. El Comité aprobó, escaló y volvió a aprobar; la bitácora tiene 30 decisiones y el historial sigue con 12 filas porque se actualiza por clave. El flujo quedó activo para el día 1 de cada mes a las 7:00, siempre que n8n esté encendido.

## Cómo regenerar

```
node --test scripts/n8n/*.test.js
python -m pytest scripts/tests/test_flujo_gobierno.py -q
python scripts/flujo_gobierno_datos.py docs/entregas-2026-11-04/dashboard/datos docs/entregas-2026-11-16/flujo-iso38500/hoja-gobierno-celulas.xlsx
python scripts/flujo_gobierno_construir.py docs/entregas-2026-11-16/flujo-iso38500/flujo-gobierno-celulas.json
python scripts/md_a_docx_simple.py docs/entregas-2026-11-16/flujo-iso38500/flujo-gobierno-iso38500.md docs/entregas-2026-11-16/flujo-iso38500/Flujo_Gobierno_TI_ISO38500_Perficient_Colombia.docx "Flujo automatizado de gobierno de TI con ISO/IEC 38500:2024 — Perficient, operación en Colombia — Trabajo académico, Equipo Firmes por la Gobernanza"
```

La lógica de los nodos Code vive en `scripts/n8n/evaluar_celulas.js`; el constructor la copia en el JSON. Para importar en n8n, la hoja con correos reales y el JSON con IDs reales se generan fuera del repositorio, en `D:\dev\n8n\peti\`, con los argumentos `--correo-…` y `--spreadsheet-id/--credencial-…` de los mismos scripts. Arranque de n8n, credenciales de Google y problemas conocidos: skill `flujos-n8n`.

## Pendientes

- Confirmar con el docente si se sube el JSON, el Word o los dos. El JSON no lleva credenciales: quien lo importe debe elegir sus propias credenciales y su hoja en los nodos de Google.
- La conexión con Google está en modo de prueba y vence a los siete días (hacia el 23 de noviembre de 2026); después hay que volver a iniciar sesión en las dos credenciales.
- La correspondencia con la ISO usa los nombres del índice de la norma y el resumen secundario de Garibay; falta el texto completo de los §5 a §7.
