# Dashboard de CIO del PETI Colombia

Entrega del curso Gobierno y Servicios de TI (Universidad Santiago de Cali, docente Jair Sanclemente Castro), 4 de noviembre de 2026, Equipo Firmes por la Gobernanza. La tarea pide cargar el dashboard y el enlace o las credenciales de la herramienta usada para el análisis de datos, con datos sintéticos. Las referencias del profesor fueron cuatro artículos (CaixaBank Tech, Universitat Carlemany, ManageEngine y CAST) y una lista de plataformas: Tableau, n8n, Zapier, UiPath, Looker Studio, Datapad, Grafana y MOSTLY AI.

| Archivo | Qué es |
|---|---|
| **Enlace** | https://snapshots.raintank.io/dashboard/snapshot/XuadxcseLJupiHbunv3ZXRV9u23xjfag: lo que se pega en la tarea. Instantánea pública de Grafana, sin usuario ni contraseña |
| [Dashboard_CIO_PETI_Perficient_Colombia.docx](Dashboard_CIO_PETI_Perficient_Colombia.docx) | **Lo que se sube.** Tipo de dashboard y justificación, método, datos sintéticos, plataformas evaluadas, lectura y capturas |
| [dashboard-cio-peti.md](dashboard-cio-peti.md) | Fuente del Word |
| [guia-exposicion-dashboard.md](guia-exposicion-dashboard.md) | Guía para quien exponga: dónde está cada cosa, de dónde sale, por qué se decidió así, recorrido sugerido y preguntas difíciles. No se entrega |
| `capturas/` | Capturas del tablero (completo y por fila); van dentro del Word |
| `grafana/dashboard.json` | El tablero editable. Cada panel trae sus datos en CSV con la fuente TestData de Grafana; para importarlo, primero hay que crear una fuente TestData con uid `peti-testdata` |
| `grafana/snapshot.json` | La instantánea: los mismos paneles, con los datos guardados dentro. Con este archivo se publica el enlace |
| `datos/semilla_*.csv` | Tablas generadas por reglas (`scripts/dashboard_semilla.py`) |
| `datos/sintetico_*.csv` | Tablas sintéticas de MOSTLY AI (`scripts/dashboard_sintetizar.py`); son las que usa el tablero |
| `datos/series_mensuales.csv`, `datos/indicadores_mes12.csv` | Indicadores calculados (`scripts/dashboard_construir.py`) |

## Decisiones

- **Tipo:** dashboard estratégico de CIO para el Comité Directivo del PETI. Es descriptivo (semáforo de los 13 indicadores), predictivo (tendencia al mes 24) y prescriptivo sencillo (proyecto que corrige cada indicador). Toma el corte del mes 12 de un escenario simulado.
- **Plataformas:** Grafana OSS 13.3.0 para el tablero y el SDK de MOSTLY AI en modo local para los datos. Ninguna de las dos pidió crear cuenta. Tableau, Looker Studio, Datapad, Zapier y UiPath exigen cuenta; n8n quedó como mejora posible (refresco de los datos y alertas).
- **Enlace:** Grafana publica instantáneas en snapshots.raintank.io sin cuenta y sin vencimiento. La instantánea guarda los datos, así que el enlace no depende de que el equipo tenga Grafana encendido.

## Cómo se generó

```
python scripts/dashboard_semilla.py docs/entregas-2026-11-04/dashboard/datos
# Python 3.12 en un entorno aparte con `uv pip install "mostlyai[local]"` (en el Python 3.14 del equipo numpy falla)
PYTHONUTF8=1 python scripts/dashboard_sintetizar.py docs/entregas-2026-11-04/dashboard/datos 1.5
python scripts/dashboard_construir.py docs/entregas-2026-11-04/dashboard
python scripts/dashboard_comparar.py docs/entregas-2026-11-04/dashboard/datos
python scripts/dashboard_capturas.py <enlace> docs/entregas-2026-11-04/dashboard/capturas docs/entregas-2026-11-04/dashboard/grafana/dashboard.json
python scripts/md_a_docx_simple.py docs/entregas-2026-11-04/dashboard/dashboard-cio-peti.md docs/entregas-2026-11-04/dashboard/Dashboard_CIO_PETI_Perficient_Colombia.docx "Dashboard de CIO del PETI Colombia — Trabajo académico, Equipo Firmes por la Gobernanza"
```

En Windows, mostly.ai corrompe las tildes de los valores categóricos. Por eso las tablas semilla van en ASCII (`Si`, `Critica`, `C05`) y `dashboard_construir.py` pone las tildes al mostrar los datos.

## Pendientes

- El tablero no tiene datos reales. Cuando el PETI tenga mediciones, los mismos scripts sirven si se reemplazan las tablas semilla por exportaciones reales.
- KPI-07 supone que la recertificación ISO/IEC 27001 se hizo en el mes 5. No hay evidencia pública de ella (ver CLAUDE.md, PUB-002).
