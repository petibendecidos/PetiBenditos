# Dashboard de gobierno de datos, IA y TI en Power BI (ISO/IEC 38500:2024) — plan de implementación

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Para Lucho:** las tareas 1, 2 y 7 son de código y texto (puedes pedírselas a Claude Code en el repo). Las tareas 3 a 6 son tuyas, en Power BI Desktop, a mano: eso es justamente lo que pidió el profesor ("se veía muy IA"). Marca cada casilla al terminarla y haz commit del plan para que Mateo vea el avance.

**Goal:** Entregar la tarea "Cargar dashboard interactivo estratégico de métricas de Gobierno de TI - ISO 38500 2024. Métricas de Gobierno de Datos, IA y TI" (cierre: **miércoles 18 de noviembre de 2026, 23:59**; meta interna: subir a las 20:00) con un informe de Power BI de 5 páginas más una hoja de vida por indicador, filtros y detalle, armado sobre un modelo en estrella con datos sintéticos.

**Architecture:** Un script de Python genera un libro de Excel con 14 tablas (modelo en estrella) a partir de los CSV sintéticos del 4 de noviembre y de reglas del escenario, y un CSV de control con el valor y el estado de cada indicador al mes 12. Power BI importa el libro, aplica un tema JSON versionado y calcula todo con medidas DAX que siguen las mismas reglas del script. El CSV de control sirve para comprobar que Power BI y el script dan las mismas cifras.

**Tech Stack:** Python 3.14 con `openpyxl` y `pytest` (sin pandas ni numpy: numpy provoca segfault en este equipo), Power BI Desktop (versión de Microsoft Store disponible el 17 de noviembre de 2026), Recortes de Windows para el video, `scripts/md_a_docx_simple.py` para el Word.

**Spec:** el diseño se acordó en la conversación del 16 de noviembre de 2026 y está en "Diseño" abajo. Insumos: [iso-38500.md](../../../.claude/skills/marcos-referencia/iso-38500.md) (principios, modelo, marco, cuidado al citar), [PETI Colombia](../../perficient_peti_colombia_2026_2028.md) §7 (metas METI), §9 (portafolio), §10 (indicadores), §11 (riesgos), los datos sintéticos de [entregas-2026-11-04/dashboard/datos](../../entregas-2026-11-04/dashboard/datos/), la [autoevaluación EIS del 16 de noviembre](../../entregas-2026-11-16/README.md) y el [plan del flujo n8n](2026-11-16-flujo-gobierno-iso38500.md) (misma semana, mismos datos y misma bitácora de decisiones).

## Diseño

### Por qué cambia frente al tablero de Grafana del 4 de noviembre

| Problema del tablero anterior | Qué se hace ahora |
|---|---|
| 22 paneles en una sola página, todos con el mismo peso | 5 páginas de 5 a 7 visuales, una por pregunta del Comité |
| Bloques de semáforo saturados, degradados, morados y lilas sin significado | Rojo solo para lo que está mal; verde, amarillo y gris solo como punto con texto; un color fijo por dominio |
| Series rectas (KPI-04, KPI-06) y metas planas: se ven inventadas | Ruido, un mes sin reporte, frecuencias reales (trimestral, semestral, anual) y retrocesos |
| Panel de tickets y MTTR por prioridad: es gestión, no gobierno | Solo indicadores del PETI y cinco complementarios de datos e IA, todos con principio y tarea de la ISO 38500 |
| La instantánea de Grafana no conserva filtros | Filtros sincronizados, mes de corte movible, detalle por indicador y tooltip de tendencia |
| Metas del mes 12 con asterisco (supuestas) | Metas del año 1 tomadas del PETI §7 (METI). Cambian tres estados frente al 4 de noviembre; se explica en el Word |

### Cómo se lee la ISO/IEC 38500:2024 en el tablero

- Cada indicador tiene un **principio** (§5.2 a §5.12), una **tarea del modelo** (involucrar a las partes interesadas, evaluar, dirigir, monitorear; §6.2) y un **elemento del marco** (§7.2). De §5 en adelante solo se citan los nombres (PUB-026); las descripciones son de Garibay (PUB-029, fuente secundaria).
- La página 1 muestra los 11 principios aunque alguno no tenga indicador: Propósito (5.2) y Liderazgo (5.8) quedan vacíos a propósito. Eso dice que el tablero no los mide y que se revisan en el comité y en la autoevaluación EIS. Es un hallazgo, no un error.
- La bitácora de decisiones sigue la guía EIS (PUB-027): foco, justificación, responsable y fecha. Usa las mismas columnas que la pestaña "Decisiones" del flujo n8n, así que las dos entregas se conectan.

### Páginas

| # | Página | Tarea ISO | Pregunta que responde |
|---|---|---|---|
| 1 | Resumen para el Comité | Evaluar | ¿Cómo van los indicadores por principio y qué se decidió? |
| 2 | Dirigir: portafolio y riesgos | Dirigir | ¿Qué proyectos van atrasados y qué riesgos subieron? |
| 3 | Monitorear: TI | Monitorear | ¿Seguridad, cumplimiento, nube y talento están en meta? |
| 4 | Gobierno de datos | Monitorear / Involucrar | ¿Se atiende a los titulares y se controlan los datos? |
| 5 | Gobierno de IA | Evaluar / Monitorear | ¿Qué IA se usa, con qué riesgo y con qué supervisión? |
| — | Hoja de vida del indicador (oculta, detalle) | — | Ficha del Anexo 1 y tendencia de un indicador |
| — | Tendencia (oculta, tooltip) | — | Mini serie al pasar el cursor |

### Indicadores (filas de `dim_indicador`)

Metas del año 1 = PETI §7 (METI). Las de origen "Complementario" son supuestos del equipo (INT-001) y no están en el PETI. Meses = meses en que hay medición (mes 1 = octubre de 2026; corte = mes 12, septiembre de 2027).

| id | Nombre corto | Dominio | Principio | Tarea | Elemento | Sentido | Meta 12 | Meta 24 | Nivel | Meses | Escala | Proyecto |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| KPI-01 | Ejecución acumulada del PETI | TI | 5.5 | Monitorear | Desempeño | mayor | 55 | 95 | Operación | 1-12 | 100 | Todo el portafolio |
| KPI-02 | Variación del costo de nube | TI | 5.3 | Evaluar | Desempeño | mayor | −5 | −15 | Operación | 9, 12 | 100 | P2.7 |
| KPI-03 | Casos de IA en producción | IA | 5.3 | Evaluar | Capacidad | mayor | 1 | 5 | Operación | 6, 12 | 1 | P3.1, P3.3 |
| KPI-04 | Adopción de IA en células | IA | 5.4 | Dirigir | Capacidad | mayor | 85 | 95 | Célula | 3-12 | 100 | P1.6, P1.8 |
| KPI-05 | Remediación de vulnerabilidades críticas (h) | TI | 5.10 | Monitorear | Desempeño | menor | 72 | 24 | Célula | 3-12 | 1 | P2.2, P2.3 |
| KPI-06 | Conciliación de horas y tareas | TI | 5.9 | Monitorear | Desempeño | mayor | 90 | 95 | Operación | 6-12 | 100 | P2.4 |
| KPI-07 | No conformidades mayores ISO/IEC 27001 | TI | 5.12 | Monitorear | Rendición de cuentas | menor | 0 | 0 | Operación | 5 | 1 | P1.1 |
| KPI-08 | Cobertura del inventario de IA | IA | 5.10 | Evaluar | Política | mayor | 90 | 100 | Célula | 3, 6, 9, 12 | 100 | P1.3 |
| KPI-09 | Personal técnico certificado | TI | 5.4 | Dirigir | Capacidad | mayor | 70 | 90 | Célula | 3, 6, 9, 12 | 100 | P1.7 |
| KPI-10 | Rotación entre células | TI | 5.10 | Dirigir | Capacidad | mayor | 50 | 100 | Célula | 6, 12 | 100 | P2.1 (R06) |
| KPI-11 | Ambientes con infraestructura como código | TI | 5.12 | Dirigir | Capacidad | mayor | 60 | 100 | Operación | 9, 12 | 100 | P2.6 |
| KPI-13 | Informe SOC 2 sin salvedades | TI | 5.7 | Involucrar | Rendición de cuentas | mayor | (vacía) | 1 | Operación | 12 (sin dato) | 1 | P4.1 |
| KPI-14 | Sesiones de comité con acta | TI | 5.6 | Monitorear | Rendición de cuentas | mayor | 90 | 90 | Operación | 3, 6, 9, 12 | 100 | P2.8 |
| DAT-01 | Solicitudes de titulares respondidas en plazo | Datos | 5.11 | Involucrar | Rendición de cuentas | mayor | 95 | 98 | Operación | 1-12 | 100 | P1.9 |
| DAT-02 | Activos de datos clasificados | Datos | 5.9 | Dirigir | Política | mayor | 60 | 90 | Operación | 3, 6, 9, 12 | 100 | P3.5 |
| DAT-03 | Proyectos con transferencias internacionales registradas | Datos | 5.11 | Monitorear | Rendición de cuentas | mayor | 80 | 100 | Operación | 6, 9, 12 | 100 | P1.9 |
| IA-01 | Sistemas de IA con evaluación de riesgo | IA | 5.10 | Evaluar | Política | mayor | 80 | 100 | Célula | 6, 9, 12 | 100 | P1.2 |
| IA-02 | Sistemas de IA con supervisión humana definida | IA | 5.6 | Dirigir | Delegación | mayor | 90 | 100 | Célula | 6, 9, 12 | 100 | P1.2, P1.4 |

Fórmula, línea base, frecuencia y responsable de los KPI se copian del PETI §10. Para los complementarios:
- DAT-01: solicitudes respondidas dentro del plazo / solicitudes recibidas × 100, mensual, responsable Legal con CISO.
- DAT-02: activos clasificados / activos inventariados × 100, trimestral, responsable Arquitectura de datos.
- DAT-03: proyectos con transferencia registrada / proyectos que tratan datos personales × 100, trimestral, responsable CTO con Legal.
- IA-01: sistemas registrados con evaluación de riesgo / sistemas registrados × 100, trimestral, responsable CISO.
- IA-02: sistemas registrados con responsable de supervisión humana / sistemas registrados × 100, trimestral, responsable CoE de IA.

### Reglas de cálculo (iguales en Python y en DAX)

- Valor = Σ numerador / Σ denominador × escala. Sumar numeradores y denominadores, nunca promediar porcentajes, permite agregar meses y células sin error.
- **Valor al corte** = valor del último mes con dato ≤ mes de corte. Un indicador trimestral se muestra con su último reporte y la fecha de ese reporte.
- Meta del periodo = `meta_mes12` si el mes es ≤ 12; si no, `meta_mes24`.
- **Cumplimiento** (1 decimal):
  - Sin valor o sin meta: vacío.
  - Sentido "menor": 100 si valor ≤ meta; 0 si meta = 0 y valor > 0; si no, 100·meta/valor.
  - Sentido "mayor": max(0, min(100, 100·valor/meta)). Sirve también para KPI-02, donde valor y meta son negativos; si el costo sube, da 0.
- **Estado** (rangos del PETI §10): vacío → "No evaluado"; ≥ 95 → "Bueno"; > 70 → "Intermedio"; si no, "Bajo".
- Indicador de nivel "Operación": el filtro de célula no lo cambia. Se muestra con la marca "toda la operación".

### Estados esperados al mes 12 (los fija la prueba de Task 1)

| Bueno | Intermedio | Bajo | No evaluado |
|---|---|---|---|
| KPI-07, KPI-08, KPI-09, KPI-14, DAT-03, IA-02 | KPI-01, KPI-02, KPI-04, KPI-06, DAT-01, IA-01 | KPI-03, KPI-05, KPI-10, KPI-11, DAT-02 | KPI-13 |

Frente al 4 de noviembre cambian KPI-02 (Bueno → Intermedio, meta −5 % del METI11 en lugar de −3 %), KPI-03 (Bueno → Bajo, el METI03 pide 1 caso en el año 1 pero P3.1 y P3.3 empiezan en el mes 13: es una inconsistencia del PETI y se dice), KPI-13 (Bueno → No evaluado, no tiene meta al año 1) y KPI-05 (181 h → 217,9 h, porque ahora es el valor del mes y no el promedio del trimestre).

## Global Constraints

- Carpeta de la entrega: `docs/entregas-2026-11-16/dashboard-iso38500/` (misma semana que el flujo n8n y la autoevaluación).
- Python sin pandas ni numpy; semilla fija `38500`; mismas entradas → mismo libro byte a byte en contenido.
- Mes 1 = octubre de 2026; mes 12 = septiembre de 2027 (corte por defecto); `dim_fecha` va del mes 1 al 24. Etiquetas "oct 2026". Nunca `dd/mm/aaaa`.
- Células `C01` a `C12` y `OPE` (toda la operación). Líneas de servicio: C01-C03 "Desarrollo de software", C04-C06 "Datos e IA", C07-C09 "Nube y DevOps", C10-C12 "Calidad y pruebas". Nada de nombres de clientes, proveedores, ciudades ni herramientas reales. No se usa nada de `docs/privado/`, `docs/evidencia-privada/` ni de los archivos restringidos.
- Colores (tema y reglas de formato): fondo `#fcfcfb`; texto `#0b0b0b` y secundario `#52514e`; dominios TI `#2a78d6`, Datos `#eb6834`, IA `#1baf7a`; estados Bueno `#0ca30c`, Intermedio `#fab219`, Bajo `#d03b3b`, No evaluado `#8a8985`; rampa azul para magnitudes `#cde2fb`, `#86b6ef`, `#3987e5`, `#1c5cab`. El rojo se usa solo para "Bajo" y "Atrasado".
- Fuente Segoe UI (la de Power BI). Lienzo de 1280 × 720.
- ISO 38500: solo nombres del §5 en adelante (PUB-026) y descripciones de Garibay como fuente secundaria (PUB-029). Son cuatro tareas del modelo, no tres. Nunca "cumple la ISO 38500" ni "certificación".
- Plazos de respuesta a titulares (10 días hábiles para consultas y 15 para reclamos): supuesto del escenario hasta verificar los artículos de la Ley 1581 (la skill `marcos-referencia` los marca `[VERIFICAR]`).
- KPI-07 supone la auditoría de recertificación en el mes 5, sin evidencia pública (PUB-002). Va en la nota de `fuente_dato`.
- Textos del informe y del Word en español, con las reglas de `redaccion-peti`. Antes de escribir el Word se cargan `redaccion-peti`, `evidencias-peti` y `marcos-referencia`.
- Nada se publica (Publicar en la web, YouTube, Drive público) sin el visto bueno de Mateo y sin pasar `auditor-evidencias`.
- Commits solo con la skill `/commit`.

## Review Focus

- Filtro de célula puesto y un indicador de nivel "Operación" (KPI-01): sigue mostrando su valor con la marca "toda la operación"; no queda en blanco ni pasa a "No evaluado". Verificación en Task 3, Step 7.
- Indicador sin medición en el mes de corte (KPI-02 con corte en el mes 11): muestra el valor del mes 9 y "último reporte: jun 2027"; no queda vacío. Prueba `test_valor_al_corte_usa_ultimo_reporte` en Task 1 y verificación en Task 3.
- Corte antes de la línea base (KPI-06 con corte en el mes 4): "No evaluado", nunca 0 % ni "Bajo". Prueba `test_antes_de_linea_base` en Task 1.
- Mes sin reporte de una célula (C11, KPI-04, mes 8): la operación usa 11 células ese mes y la serie de C11 muestra un hueco, no una caída a 0. Prueba `test_mes_sin_reporte` en Task 1.
- Abrir el `.pbix` en otro equipo: los datos se ven porque están importados. Si alguien pulsa "Actualizar", falla la ruta; se arregla en Transformar datos → Configuración de origen de datos → Cambiar origen. Lo dice el README (Task 7) y Mateo lo prueba (Task 6, Step 6).

---

### Task 1: Generador del modelo de datos

**Files:**
- Create: `scripts/powerbi_iso38500_datos.py`
- Test: `scripts/tests/test_powerbi_iso38500.py` (el test agrega `scripts/` a `sys.path` e importa el módulo como `gen`)
- Create (generados): `docs/entregas-2026-11-16/dashboard-iso38500/datos/modelo_gobierno_ti.xlsx`, `docs/entregas-2026-11-16/dashboard-iso38500/datos/control_corte_mes12.csv`

**Interfaces:**
- Consumes: `docs/entregas-2026-11-04/dashboard/datos/sintetico_vulnerabilidades.csv`, `sintetico_personas.csv` (valores en ASCII: `Si`, `Critica`; se ponen tildes al escribir). Las constantes `PORTAFOLIO`, `INICIO` y `COSTO_NUBE` de `scripts/dashboard_construir.py`, importadas, no copiadas (el módulo tiene guardia `__main__`).
- Produces:
  - `cumplimiento(valor: float|None, meta: float|None, sentido: str) -> float|None`
  - `estado(cumpl: float|None) -> str` (`"Bueno"|"Intermedio"|"Bajo"|"No evaluado"`)
  - `construir_modelo(carpeta_sinteticos: Path, semilla: int = 38500) -> dict[str, list[dict]]`, con una clave por tabla (nombres abajo)
  - `control_corte(modelo: dict, corte: int) -> list[dict]` con `id_indicador, nombre, valor, meta, cumplimiento, estado, mes_ultimo_reporte`; aplica "Reglas de cálculo" y el nivel "Operación"
  - `escribir_xlsx(modelo: dict, ruta: Path) -> None`: una hoja por tabla con el mismo nombre; números como número, no como texto
  - CLI: `python scripts/powerbi_iso38500_datos.py <carpeta_sinteticos> <carpeta_salida>` escribe el libro y `control_corte_mes12.csv` (UTF-8 con BOM, coma como separador)

Tablas y columnas (nombres exactos; Task 3 y las medidas dependen de ellos):

| Tabla | Columnas |
|---|---|
| `dim_fecha` | `mes` (1-24), `fecha` (primer día del mes), `etiqueta` ("oct 2026"), `anio`, `trimestre` ("T1" a "T8" del PETI), `fase` (1: meses 1-6, 2: 7-12, 3: 13-18, 4: 19-24) |
| `dim_corte` | `mes` (1-12), `etiqueta`. Tabla sin relaciones para el filtro "Mes de corte" |
| `dim_principio` | `seccion` ("5.2"…"5.12"), `orden` (1-11), `nombre_es`, `nombre_en`, `descripcion` (Garibay), `fuente` ("PUB-026 nombre; PUB-029 descripción"). Valores de la tabla de principios de `iso-38500.md` |
| `dim_tarea` | `id_tarea` (1-4), `tarea` ("Involucrar a las partes interesadas", "Evaluar", "Dirigir", "Monitorear"), `seccion` ("6.2.1"…"6.2.4") |
| `dim_indicador` | `id_indicador`, `nombre`, `dominio`, `origen` ("PETI §10"/"Complementario"), `objetivo` (OETI o "—"), `meta_id` (METI o "—"), `seccion_principio`, `id_tarea`, `elemento_marco`, `formula`, `unidad` ("%", "h", "número", "sí/no"), `sentido`, `escala`, `linea_base`, `meta_mes12` (vacía en KPI-13), `meta_mes24`, `frecuencia`, `responsable`, `nivel`, `proyecto_corrige`, `fuente_dato` |
| `dim_celula` | `id_celula` (C01-C12, OPE), `nombre` ("Célula 01"…, "Toda la operación"), `linea` (OPE: "Toda la operación") |
| `dim_proyecto` | `id_proyecto`, `nombre`, `fase`, `objetivo`, `brecha`, `id_indicador` (el primero si hay varios), `responsable`, `mes_inicio`, `mes_fin_plan`, `mes_fin_real` (vacío si sigue abierto) |
| `dim_riesgo` | `id_riesgo`, `riesgo`, `probabilidad`, `impacto`, `nivel`, `tratamiento`, `proyectos` (PETI §11), `nivel_corte`, `motivo_cambio` |
| `fact_medicion` | `mes`, `id_indicador`, `id_celula`, `numerador`, `denominador`, `estado_reporte` ("Reportado"/"Sin reporte"/"Antes de la línea base"/"No aplica al corte"), `nota` |
| `fact_proyecto_mes` | `mes` (1-12), `id_proyecto`, `avance_plan`, `avance_real` (0-100), `estado` ("Por iniciar"/"En ejecución"/"Atrasado"/"Terminado") |
| `fact_vulnerabilidad` | `mes`, `fecha_deteccion`, `id_celula`, `severidad` (con tilde), `origen`, `horas_deteccion`, `horas_remediacion` (solo meses 1-12) |
| `fact_sistema_ia` | `id_sistema` ("IA-S01"…), `id_celula`, `tipo` ("Asistente de código"/"Búsqueda con documentos (RAG)"/"Agente"/"Clasificación o predicción"), `origen` ("Servicio externo"/"API de terceros"/"Desarrollo propio"), `mes_identificado`, `mes_registrado`, `mes_evaluacion_riesgo`, `supervision_humana` ("Sí"/"No"), `usa_datos_personales`, `nivel_riesgo` ("Alto"/"Medio"/"Bajo"), `estado` ("Piloto"/"Uso interno"/"Producción") |
| `fact_solicitud_titular` | `id_solicitud`, `mes`, `fecha_recibida`, `tipo` ("Consulta"/"Reclamo"), `plazo_dias_habiles` (10/15), `dias_habiles_respuesta`, `en_plazo` ("Sí"/"No") |
| `fact_decision` | `fecha`, `ciclo` ("2027-09"), `celula` (id o "OPE"), `foco` ("Priorización"/"Riesgo"/"Desempeño"/"Estrategia"), `justificacion`, `decision`, `responsable` (rol), `instancia` ("Comité Directivo"/"Comité Táctico"), `mes`, `id_indicador`, `id_proyecto`. Las 7 primeras son las de la pestaña "Decisiones" del flujo n8n |

Reglas del escenario:
- **KPI-01** sale de `PORTAFOLIO`: terminados acumulados / 25 (13 al mes 12).
- **KPI-05** sale de `fact_vulnerabilidad`: por célula y mes, severidad "Crítica", numerador = Σ horas de remediación, denominador = número de vulnerabilidades. Los meses 1 y 2 no se escriben (línea base en el mes 3). Un mes sin críticas no lleva fila.
- **KPI-09 y KPI-10** salen de `sintetico_personas.csv` por célula al mes 12, con las fórmulas de `dashboard_construir.py` (líneas 126-128). Los meses anteriores bajan de forma irregular.
- **KPI-04**: una fila por célula y mes (1/1 o 0/1); 9 de 12 al mes 12; al menos una célula retrocede un mes. C11 en el mes 8: "Sin reporte", con numerador y denominador vacíos.
- **KPI-08, IA-01 e IA-02** se calculan de `fact_sistema_ia` (40 a 60 sistemas). Así el detalle de la página 5 cuadra con las tarjetas.
- **DAT-01** se calcula de `fact_solicitud_titular` (3 a 10 por mes).
- **KPI-02**: base = promedio de los costos de los meses 7-9 de `COSTO_NUBE`; numerador = costo del mes − base; denominador = base. **KPI-11**: numerador/48 ambientes. **KPI-14**: sesiones con acta / 4 por trimestre; un trimestre con 3/4.
- **KPI-03**: numerador 0, denominador 1. **KPI-07**: mes 5, 0/1. **KPI-13**: una fila en el mes 12 con "No aplica al corte" y la nota "P4.1 inicia en el mes 13".
- **Proyectos**: estado en el mes m: "Terminado" si `mes_fin_real` ≤ m; "Por iniciar" si m < `mes_inicio`; "Atrasado" si m ≥ `mes_fin_plan` sin terminar o si `avance_real` < `avance_plan` − 15; si no, "En ejecución". Al mes 12: 13 terminados, 4 atrasados (P1.8, P2.2, P2.3, P2.6), 8 por iniciar.
- **Riesgos** (`nivel_corte`, supuesto del escenario):
  - R01 Alto → Medio (P1.2, P1.4 y P1.5 cerrados).
  - R02 Alto → Bajo (recertificación supuesta del mes 5; ver PUB-002).
  - R03 sigue Alto (KPI-05 en Bajo).
  - R06 Medio → Alto (KPI-10 en Bajo).
  - Los demás sin cambio.
- **Decisiones**: 12 a 16 filas escritas a mano como constantes, entre el mes 3 y el 12, de una o dos frases cada una (≤ 160 caracteres), en lenguaje de acta y sin adjetivos. Ejemplos de tono:
  - "Se aplaza P2.6 un trimestre; DevSecOps se concentra en P2.3 por R03."
  - "Se exige plan de remediación a C05 y C09: críticas sobre 200 h en dos meses seguidos."
  - "No se aprueba licencia de IA para C11 hasta registrar sus sistemas en el inventario."
  - "El informe SOC 2 se mantiene en la fase 4; no se adelanta."

- [ ] **Step 1: Escribir las pruebas** (`pytest`):
  - `test_cumplimiento`: `(181, 72, "menor") == 39.8`; `(60, 72, "menor") == 100`; `(0, 0, "menor") == 100`; `(1, 0, "menor") == 0`; `(-4.4, -5, "mayor") == 88.0`; `(2, -5, "mayor") == 0`; `(None, 72, "menor") is None`; `(5, None, "mayor") is None`.
  - `test_estado`: `95 → "Bueno"`, `94.9 → "Intermedio"`, `70.1 → "Intermedio"`, `70 → "Bajo"`, `None → "No evaluado"`.
  - `test_estados_mes12`: `control_corte(modelo, 12)` da exactamente la tabla "Estados esperados al mes 12".
  - `test_valores_de_referencia`: al mes 12, KPI-01 = 52.0, KPI-05 = 217.9, KPI-09 = 66.7 y KPI-10 = 33.2 (tolerancia 0.05).
  - `test_kpi05_por_celula`: KPI-05 de C05 al mes 12 es igual al promedio de `horas_remediacion` de las críticas de C05 detectadas en septiembre de 2027 en el CSV, calculado dentro del test.
  - `test_valor_al_corte_usa_ultimo_reporte`: con corte 11, KPI-02 tiene `mes_ultimo_reporte == 9`; con corte 12, KPI-07 tiene `mes_ultimo_reporte == 5` y estado "Bueno".
  - `test_antes_de_linea_base`: con corte 4, KPI-06 queda en "No evaluado" y su valor es `None`.
  - `test_mes_sin_reporte`: la fila (8, KPI-04, C11) existe con `estado_reporte == "Sin reporte"`; la suma de denominadores de KPI-04 en el mes 8 es 11.
  - `test_series_no_rectas`: en la serie de operación de KPI-04 y de KPI-06 hay al menos un mes que baja frente al anterior, y las diferencias entre meses no son todas iguales.
  - `test_integridad`: toda clave foránea existe en su dimensión; `dim_principio` tiene 11 filas; 5.2 y 5.8 no tienen indicador; todo `seccion_principio` e `id_tarea` de `dim_indicador` existe.
  - `test_proyectos_mes12`: conteo por estado al mes 12 = {Terminado: 13, Atrasado: 4, Por iniciar: 8}.
  - `test_decisiones`: entre 12 y 16 filas; `foco` dentro de los 4 valores; textos ≤ 160 caracteres; ningún texto de ninguna tabla contiene "@".
  - `test_determinista`: dos llamadas a `construir_modelo` con la misma semilla dan dicts iguales.
- [ ] **Step 2: Correr y ver que fallan** — Run: `python -m pytest scripts/tests/test_powerbi_iso38500.py -q` → Expected: FAIL (`ModuleNotFoundError`).
- [ ] **Step 3: Implementar** `scripts/powerbi_iso38500_datos.py` con las interfaces y reglas de arriba. Usa `random.Random(semilla)`, nunca el `random` global. Si un estado del mes 12 no cae donde pide la tabla, ajusta la regla del escenario, no la prueba.
- [ ] **Step 4: Correr y ver que pasan** — Run: `python -m pytest scripts/tests/test_powerbi_iso38500.py -q` → Expected: todas PASS.
- [ ] **Step 5: Generar** — Run: `python scripts/powerbi_iso38500_datos.py docs/entregas-2026-11-04/dashboard/datos docs/entregas-2026-11-16/dashboard-iso38500/datos` → Expected: el libro con 14 hojas y el CSV de control con 18 filas.
- [ ] **Step 6: Commit** — `/commit` (`feat: agregar generador del modelo de datos del dashboard ISO 38500`).

### Task 2: Tema de Power BI y medidas DAX

**Files:**
- Create: `docs/entregas-2026-11-16/dashboard-iso38500/powerbi/tema-gobierno-ti.json`
- Create: `docs/entregas-2026-11-16/dashboard-iso38500/powerbi/medidas.dax`
- Test: `scripts/tests/test_powerbi_iso38500.py` (agregar `test_tema`)

**Interfaces:**
- Consumes: nombres de tablas y columnas de Task 1.
- Produces: el tema (Task 4 lo importa) y las medidas, cada una en un bloque `Nombre = expresión` separado por una línea en blanco y precedido de un comentario `//` de una línea con qué hace (Task 3 las pega una por una).

Tema: `name` "Gobierno TI PETI"; `dataColors` empieza con `#2a78d6`, `#eb6834`, `#1baf7a`, `#52514e`; `background` `#fcfcfb`; `foreground` `#0b0b0b`; `good` `#0ca30c`; `neutral` `#fab219`; `bad` `#d03b3b`. En `visualStyles` (`"*"`): sin borde, sin sombra, sin fondo de visual (transparente sobre la página), título en Segoe UI Semibold 11 de color `#0b0b0b`, ejes y etiquetas en `#52514e`, líneas de cuadrícula `#e6e5e1`.

Medidas (nombres exactos):

| Medida | Qué devuelve |
|---|---|
| `Corte` | `SELECTEDVALUE(dim_corte[mes], 12)` |
| `Es de operación` | TRUE si `SELECTEDVALUE(dim_indicador[nivel]) = "Operación"` |
| `Valor` | Σ numerador / Σ denominador × escala; si `Es de operación`, quita el filtro de `dim_celula` |
| `Mes último reporte` | Mayor `fact_medicion[mes]` ≤ `Corte` con denominador no vacío, sin filtro de `dim_fecha` y con la misma regla de célula |
| `Valor al corte` | `[Valor]` en el `Mes último reporte`, quitando el filtro de `dim_fecha` |
| `Meta al corte` | `meta_mes12` si `Corte` ≤ 12, si no `meta_mes24` |
| `Cumplimiento` | Regla de "Reglas de cálculo", redondeada a 1 decimal (usar `ISBLANK`, no `= BLANK()`, porque 0 es un valor válido) |
| `Estado` | "Bueno"/"Intermedio"/"Bajo"/"No evaluado" |
| `Estado orden` | 1 Bueno, 2 Intermedio, 3 Bajo, 4 No evaluado (para íconos y orden) |
| `Color estado` | Hex del estado (Global Constraints) |
| `Valor texto` | Valor al corte con unidad ("52 %", "217,9 h", "0", "—") y " · toda la operación" si es de operación y hay filtro de célula |
| `Último reporte texto` | "último reporte: jun 2027" |
| `Valor (serie)` | `[Valor]` si `MAX(dim_fecha[mes])` ≤ `Corte`; si no, vacío |
| `Meta (serie)` | Meta del mes del eje, solo hasta `Corte` |
| `Indicadores Bueno` / `Indicadores Intermedio` / `Indicadores Bajo` | Conteo de `VALUES(dim_indicador[id_indicador])` con ese `Estado` |
| `Proyectos al corte` | Filas de `fact_proyecto_mes` con `mes = Corte` (se usa con `estado` en el eje o como filtro) |
| `Terminados plan (acum)` / `Terminados real (acum)` | Proyectos con `mes_fin_plan` / `mes_fin_real` ≤ mes del eje, solo hasta `Corte` |
| `Color proyecto` | Por iniciar: sin color; En ejecución `#86b6ef`; Terminado `#1c5cab`; Atrasado `#d03b3b` |
| `Vulnerabilidades` | Filas de `fact_vulnerabilidad` hasta `Corte` |
| `Sistemas identificados` / `Sistemas registrados` / `Con evaluación de riesgo` / `Con supervisión humana` | Conteos de `fact_sistema_ia` hasta `Corte` (por `mes_identificado`, `mes_registrado`, `mes_evaluacion_riesgo`) |
| `Solicitudes` / `Solicitudes fuera de plazo` | Conteos de `fact_solicitud_titular` hasta `Corte` |
| `Decisiones hasta el corte` | Filas de `fact_decision` con `mes` ≤ `Corte` (filtro de visual = 1) |

Patrón de `Valor al corte` (el resto sigue el mismo estilo):

```dax
Valor al corte =
VAR m = [Mes último reporte]
RETURN IF ( NOT ISBLANK ( m ), CALCULATE ( [Valor], REMOVEFILTERS ( dim_fecha ), dim_fecha[mes] = m ) )
```

- [ ] **Step 1: Escribir la prueba** `test_tema`: el JSON carga; `dataColors[:3] == ["#2a78d6", "#eb6834", "#1baf7a"]`; `good`, `neutral` y `bad` son los de Global Constraints. Y `test_medidas_declaradas`: cada nombre de la tabla de medidas aparece en `medidas.dax` como `^Nombre =`.
- [ ] **Step 2: Correr y ver que fallan** — Run: `python -m pytest scripts/tests/test_powerbi_iso38500.py -q -k "tema or medidas"` → Expected: FAIL.
- [ ] **Step 3: Escribir** el tema y `medidas.dax`.
- [ ] **Step 4: Correr y ver que pasan** — mismo comando → Expected: PASS.
- [ ] **Step 5: Commit** — `/commit` (`feat: agregar tema y medidas del dashboard ISO 38500`).

### Task 3: Modelo en Power BI (Lucho, a mano, unos 60 minutos)

**Files:** Create `docs/entregas-2026-11-16/dashboard-iso38500/Dashboard_Gobierno_TI_ISO38500_Perficient_Colombia.pbix`

**Interfaces:**
- Consumes: el libro y el CSV de control de Task 1 y `medidas.dax` de Task 2.

- [ ] **Step 1:** Instalar Power BI Desktop desde Microsoft Store. Antes de cargar nada, ir a Archivo → Opciones y configuración → Opciones:
  - En "Archivo actual → Carga de datos", desmarcar "Detectar automáticamente nuevas relaciones" y "Fecha y hora automáticas".
  - En "Archivo actual → Configuración regional", poner "Español (Colombia)".
- [ ] **Step 2:** Inicio → Obtener datos → Excel → `modelo_gobierno_ti.xlsx`. Marcar las 14 hojas → Transformar datos. Revisar los tipos:
  - `mes` y los `id_tarea`: número entero.
  - `numerador`, `denominador`, metas y horas: número decimal.
  - `fecha`: fecha.
  - Lo demás: texto.

  Cerrar y aplicar. Se usa xlsx y no CSV porque con configuración es-CO un CSV con punto decimal se lee mal.
- [ ] **Step 3:** En la vista de modelo, crear estas relaciones (todas de varios a uno, dirección de filtro única):

  | Desde | Hacia |
  |---|---|
  | `fact_medicion[mes]` | `dim_fecha[mes]` |
  | `fact_medicion[id_indicador]` | `dim_indicador[id_indicador]` |
  | `fact_medicion[id_celula]` | `dim_celula[id_celula]` |
  | `dim_indicador[seccion_principio]` | `dim_principio[seccion]` |
  | `dim_indicador[id_tarea]` | `dim_tarea[id_tarea]` |
  | `fact_proyecto_mes[mes]` | `dim_fecha[mes]` |
  | `fact_proyecto_mes[id_proyecto]` | `dim_proyecto[id_proyecto]` |
  | `fact_vulnerabilidad[mes]` | `dim_fecha[mes]` |
  | `fact_vulnerabilidad[id_celula]` | `dim_celula[id_celula]` |
  | `fact_sistema_ia[id_celula]` | `dim_celula[id_celula]` |
  | `fact_solicitud_titular[mes]` | `dim_fecha[mes]` |
  | `fact_decision[mes]` | `dim_fecha[mes]` |
  | `fact_decision[celula]` | `dim_celula[id_celula]` |
  | `fact_decision[id_indicador]` | `dim_indicador[id_indicador]` |

  **No** relacionar `fact_decision[id_proyecto]` ni `dim_proyecto[id_indicador]`: crean dos caminos hacia `dim_indicador`. `dim_corte` y `dim_riesgo` quedan sueltas.
- [ ] **Step 4:** Configurar columnas:
  - Ordenar por columna: `dim_fecha[etiqueta]` por `mes`, `dim_corte[etiqueta]` por `mes`, `dim_principio[nombre_es]` por `orden`, `dim_tarea[tarea]` por `id_tarea`.
  - Ocultar en la vista de informe las columnas clave de las tablas `fact_`.
  - Marcar `dim_fecha` como tabla de fechas, con la columna `fecha`.
- [ ] **Step 5:** Crear una tabla vacía "Medidas" (Inicio → Especificar datos, sin filas) y pegar en ella cada medida de `medidas.dax`. Darles formato: `Valor al corte` y `Cumplimiento` con 1 decimal; los conteos, enteros.
- [ ] **Step 6: Verificar el cuadre.** Crear en una página de borrador una tabla con `dim_indicador[id_indicador]`, `Valor al corte`, `Meta al corte`, `Cumplimiento`, `Estado` y `Mes último reporte`, sin filtros. → Expected: las 18 filas iguales a `control_corte_mes12.csv`. Si una no cuadra, la medida está mal, no el CSV.
- [ ] **Step 7: Verificar los casos de Review Focus** en la misma tabla, con un filtro de `dim_celula` y otro de `dim_corte`:
  - Célula = C05: KPI-01 sigue en 52 % y aparece "toda la operación".
  - Corte = sep 2027 → jul 2027 (mes 10): KPI-02 muestra el valor del mes 9.
  - Corte = ene 2027 (mes 4): KPI-06 queda "No evaluado".

  Borrar la página de borrador.
- [ ] **Step 8:** Guardar el `.pbix` y hacer commit (`/commit`, `feat: agregar modelo de Power BI del dashboard ISO 38500`).

### Task 4: Páginas 1 y 2 (Lucho, unas 2,5 horas)

**Interfaces:**
- Consumes: medidas de Task 2; tema de Task 2 (Vista → Temas → Buscar temas → `tema-gobierno-ti.json`).

Plantilla de todas las páginas, que se hace en la página 1 y se duplica:
- Banda superior de 64 px con el título de la página (Segoe UI Semibold 20) y debajo, en gris, "Perficient · operación en Colombia · PETI 2026-2028 · datos sintéticos".
- A la derecha, el filtro "Mes de corte" (desplegable, selección única, `dim_corte[etiqueta]`, valor predeterminado sep 2027) y el navegador de páginas (Insertar → Botones → Navegador → Navegador de páginas, sin las páginas ocultas).
- Márgenes de 24 px, separación de 16 px. Los visuales de una misma fila tienen la misma altura.

- [ ] **Step 1: Página 1 "Resumen para el Comité"**:
  1. Filtros "Dominio" (botones con `dim_indicador[dominio]`) y "Célula" (desplegable con `dim_celula[nombre]`).
  2. Cuatro tarjetas (visual "Tarjeta" nuevo). Cada una lleva `Valor texto`, `Meta al corte` como etiqueta de referencia y `Último reporte texto`, filtrada por indicador: KPI-01, KPI-05, KPI-08 y DAT-01. El estado va como punto de color con su palabra, no como fondo.
  3. Matriz "Indicadores por principio de la ISO/IEC 38500". Filas: `dim_principio[nombre_es]` > `dim_indicador[id_indicador]` y `nombre`. Valores: `Valor texto`, `Meta al corte`, `Cumplimiento`, `Estado`. Formato condicional de íconos en `Estado`, según `Estado orden`: círculo con el color del estado. "Mostrar elementos sin datos" activado en las filas, para que se vean Propósito y Liderazgo vacíos.
  4. Matriz pequeña "Dónde mide el tablero": filas `dim_tarea[tarea]`, columnas `dim_indicador[dominio]`, valor el conteo de indicadores.
  5. Tabla "Últimas decisiones": `fecha`, `instancia`, `foco`, `decision`, `responsable`. Filtros del visual: `Decisiones hasta el corte` = 1 y las 5 más recientes por `fecha`.
- [ ] **Step 2: Página 2 "Dirigir: portafolio y riesgos"**:
  1. Filtros "Fase" (`dim_proyecto[fase]`) y "Objetivo" (`dim_proyecto[objetivo]`).
  2. Cuatro números en una fila: `Proyectos al corte` por estado (Terminado, En ejecución, Atrasado, Por iniciar). Solo "Atrasado" lleva el punto rojo.
  3. Gráfico de líneas "Proyectos terminados, plan y real". Eje `dim_fecha[etiqueta]`; líneas `Terminados plan (acum)` (gris `#52514e`, punteada) y `Terminados real (acum)` (azul `#2a78d6`, 2 px). Etiqueta de datos solo en el último punto.
  4. Matriz "Cronograma". Filas: `dim_proyecto[id_proyecto]` y `nombre`. Columnas: `dim_fecha[etiqueta]` (meses 1-12). Valor: una medida que devuelve " ". Color de fondo por valor de campo = `Color proyecto`. Leyenda en un cuadro de texto debajo.
  5. Tabla "Riesgos": `id_riesgo`, `riesgo`, `nivel`, `nivel_corte`, `motivo_cambio`, `proyectos`. Formato condicional del texto de `nivel_corte`: "Alto" en `#d03b3b`.
- [ ] **Step 3: Verificar** con el corte en sep 2027: página 1 con 6 Bueno, 6 Intermedio, 5 Bajo y 1 No evaluado; página 2 con 13 terminados, 4 atrasados, 0 en ejecución y 8 por iniciar. Mover el corte a mar 2027 y comprobar que todo cambia y que las líneas se cortan en mar 2027.
- [ ] **Step 4:** Guardar y commit (`/commit`, `feat: agregar páginas de resumen y portafolio del dashboard`).

### Task 5: Páginas 3 a 5, detalle y tooltip (Lucho, unas 3 horas)

- [ ] **Step 1: Página 3 "Monitorear: TI"** (duplicar la plantilla):
  1. Tarjetas KPI-05, KPI-07, KPI-11 y KPI-02.
  2. Líneas "Remediación de vulnerabilidades críticas (horas)": `Valor (serie)` y `Meta (serie)` filtradas a KPI-05; la meta gris punteada.
  3. Barras horizontales "Horas de remediación por célula, último mes": `Valor al corte` de KPI-05 por `dim_celula[nombre]`, de mayor a menor, con línea constante en 72 (panel Análisis).
  4. Columnas apiladas "Vulnerabilidades detectadas por mes": `Vulnerabilidades` por `dim_fecha[etiqueta]` y `severidad`, con la rampa azul (Baja `#cde2fb` … Crítica `#1c5cab`) y separación de 2 px entre segmentos.
  5. Barras "Personal certificado por línea de servicio": KPI-09 por `dim_celula[linea]`.
- [ ] **Step 2: Página 4 "Gobierno de datos"**:
  1. Tarjetas DAT-01, DAT-02 y DAT-03.
  2. Líneas de DAT-01 con su meta.
  3. Columnas agrupadas "Solicitudes de titulares por mes": Consulta `#eb6834`, Reclamo `#52514e`.
  4. Tabla "Solicitudes respondidas fuera de plazo": `fecha_recibida`, `tipo`, `plazo_dias_habiles`, `dias_habiles_respuesta`.
  5. Cuadro de texto de una línea: "Plazos de respuesta: supuesto del escenario (10 días hábiles para consultas, 15 para reclamos), pendiente de verificar en la Ley 1581 de 2012."
- [ ] **Step 3: Página 5 "Gobierno de IA"**:
  1. Tarjetas KPI-08, IA-01, IA-02, KPI-04 y KPI-03.
  2. Barras horizontales "Del uso a la supervisión": `Sistemas identificados`, `Sistemas registrados`, `Con evaluación de riesgo` y `Con supervisión humana`, en ese orden y en un solo color (`#1baf7a`). No usar el visual de embudo.
  3. Matriz "Sistemas por tipo y nivel de riesgo", con fondo de rampa azul según el conteo.
  4. Líneas de KPI-04 por mes, con su meta.
  5. Tabla "Sistemas sin evaluación de riesgo": `id_sistema`, célula, `tipo`, `nivel_riesgo`, `usa_datos_personales`.
- [ ] **Step 4: Página "Hoja de vida del indicador"** (oculta). En Información de página → Obtener detalles, agregar `dim_indicador[id_indicador]`.
  - Tarjeta de varias filas con los campos de la hoja de vida del Anexo 1: nombre, dominio, objetivo, meta_id, fórmula, unidad, línea base, metas, frecuencia, responsable, `dim_principio[nombre_es]`, `dim_tarea[tarea]`, `elemento_marco`, `proyecto_corrige`, `fuente_dato`.
  - Líneas `Valor (serie)` y `Meta (serie)`.
  - Tabla por célula si `nivel` = "Célula".
  - Tabla de decisiones ligadas al indicador.
  - Comprobar que aparece el botón Atrás.
- [ ] **Step 5: Página "Tendencia"** (oculta). Tamaño Información sobre herramientas, "Permitir uso como información sobre herramientas", con `dim_indicador[id_indicador]` en los campos. Una línea `Valor (serie)` con la meta. Asignarla como tooltip de la matriz de la página 1 y de las tarjetas.
- [ ] **Step 6: Interacciones:**
  - Vista → Sincronizar segmentaciones: "Mes de corte" en todas las páginas; "Célula" en las páginas 1, 3 y 5.
  - Marcador "Sin filtros" y botón "Quitar filtros" en la banda superior.
  - En la página 1, Formato → Editar interacciones: la tabla de decisiones no filtra a la matriz.
- [ ] **Step 7: Verificar:**
  - Clic derecho en KPI-05 de la página 1 → Obtener detalles → Hoja de vida muestra KPI-05 con su tendencia.
  - Con Célula = C05, las páginas 3 y 5 cambian y la página 4 no (sus indicadores son de operación).
  - Las tarjetas de la página 5 cuadran con las barras "Del uso a la supervisión".
- [ ] **Step 8:** Guardar y commit (`/commit`, `feat: agregar páginas de TI, datos, IA y detalle del dashboard`).

### Task 6: Revisión visual, exportación y video (Lucho, con Mateo, unas 1,5 horas)

- [ ] **Step 1: Lista "que no parezca IA"**. Revisar página por página y corregir:
  - Como máximo 7 visuales por página. Sin velocímetros, donas, embudos, degradados, sombras ni ejes dobles.
  - Rojo solo en "Bajo", "Atrasado" y riesgo "Alto". El color de un dominio es el mismo en todas las páginas.
  - Títulos de visual cortos y en minúscula normal, con la unidad en el título. Sin emojis ni palabras como "insights", "inteligente" o "360°".
  - Sin etiquetas de datos en cada punto: solo en el último punto o en el total.
  - Fechas como "sep 2027" y porcentajes como "52 %".
  - Bordes alineados en la cuadrícula; filas con la misma altura.
  - Ningún texto generado que "interprete" los datos. La única interpretación está en la bitácora de decisiones y en el Word.
- [ ] **Step 2: Accesibilidad:** texto alternativo en cada visual (qué muestra, en una frase) y orden de tabulación de izquierda a derecha y de arriba abajo.
- [ ] **Step 3: Capturas** de las páginas 1 a 5 y de la hoja de vida de KPI-05 (Archivo → Exportar → PDF, más recortes PNG). Van a `capturas/`. Exportar el PDF completo como `Dashboard_Gobierno_TI_ISO38500_Perficient_Colombia.pdf`.
- [ ] **Step 4: Video** de 2 a 3 minutos con Recortes (Win+Mayús+R), sin audio o con la voz de Lucho:
  1. Página 1 con corte en sep 2027.
  2. Mover el corte a mar 2027 ("lo que veía el Comité en marzo").
  3. Filtrar C05.
  4. Detalle de KPI-05.
  5. Tooltip.
  6. Página 5.

  Guardar como `video-recorrido.mp4` **fuera de Git** si pesa más de 20 MB.
- [ ] **Step 5 (opcional, con permiso de Mateo):** si la cuenta de la USC deja publicar en el servicio de Power BI, Publicar → Mi área de trabajo → Archivo → Insertar informe → Publicar en la web. Antes, correr `auditor-evidencias` sobre la carpeta. Si el administrador lo bloquea, no insistir: se entrega el `.pbix`, el PDF y el video.
- [ ] **Step 6: Mateo abre el `.pbix`** en su equipo, sin actualizar. Expected: se ven todas las páginas con datos.

### Task 7: Documento de entrega, README y guía de exposición

**Files:**
- Create: `docs/entregas-2026-11-16/dashboard-iso38500/dashboard-gobierno-iso38500.md` → `Dashboard_Gobierno_TI_ISO38500_Perficient_Colombia.docx`
- Create: `docs/entregas-2026-11-16/dashboard-iso38500/README.md`, `docs/entregas-2026-11-16/dashboard-iso38500/guia-exposicion-dashboard-iso38500.md`
- Modify: `docs/entregas-2026-11-16/README.md` (índice), `README.md` (estructura), `.claude/CLAUDE.md` (fila de entregas: mencionar el dashboard en Power BI del 16-18 de noviembre)

- [ ] **Step 1:** Cargar `redaccion-peti`, `evidencias-peti` y `marcos-referencia`. Escribir `dashboard-gobierno-iso38500.md` con estas secciones:
  1. Para quién es y qué decide: el Comité Directivo del PETI (§12).
  2. Por qué Power BI y qué cambió frente al 4 de noviembre, con la tabla de "Diseño".
  3. Cómo entra la ISO/IEC 38500:2024: principios, tareas y elementos, con PUB-026 a PUB-029 y la advertencia de la vista previa.
  4. Modelo de datos: captura de la vista de modelo y una tabla de las 14 tablas.
  5. Indicadores: la tabla de `dim_indicador` sin columnas técnicas.
  6. Cómo usarlo: filtros, mes de corte, detalle y tooltip.
  7. Lectura al corte de septiembre de 2027: 5 a 8 frases sobre lo que se ve, incluida la inconsistencia de KPI-03 en el PETI.
  8. Datos sintéticos y límites: supuestos de KPI-07, de los plazos de la Ley 1581 y de los complementarios.
  9. Capturas.

  Generar el Word: `python scripts/md_a_docx_simple.py docs/entregas-2026-11-16/dashboard-iso38500/dashboard-gobierno-iso38500.md docs/entregas-2026-11-16/dashboard-iso38500/Dashboard_Gobierno_TI_ISO38500_Perficient_Colombia.docx "Dashboard de gobierno de datos, IA y TI (ISO/IEC 38500:2024) — Trabajo académico, Equipo Firmes por la Gobernanza"`.
- [ ] **Step 2:** README de la carpeta (formato de `docs/entregas-2026-11-04/dashboard/README.md`). Debe decir:
  - Qué se sube: `.pbix`, PDF, Word y video.
  - Cómo regenerar los datos y cómo cambiar la ruta del origen en Power BI (Review Focus 5).
  - Decisiones.
  - Pendientes: verificar los plazos de la Ley 1581, la inconsistencia de METI03 para la versión 1.1 del PETI y la evidencia de la recertificación (PUB-002).
- [ ] **Step 3:** Guía de exposición, que no se entrega. Incluye:
  - Recorrido de 5 minutos en el orden del video.
  - Por qué cada decisión, con referencia al PETI y a `iso-38500.md`.
  - Preguntas difíciles con su respuesta:
    - ¿Por qué Propósito y Liderazgo están vacíos?
    - ¿Por qué KPI-03 sale en rojo si sus proyectos no han empezado?
    - ¿De dónde salen los datos?
    - ¿Cumple Perficient la ISO 38500? No es certificable; se usa como referencia.
    - ¿Qué cambió frente al tablero de Grafana?
- [ ] **Step 4: Verificar que no se filtró nada.**

  Run: `grep -rnE "@[a-z0-9.-]+\.(com|co)|PRV-00[12]" docs/entregas-2026-11-16/dashboard-iso38500/ scripts/powerbi_iso38500_datos.py; python -m pytest scripts/tests/test_powerbi_iso38500.py -q`

  Expected: sin coincidencias (PRV solo puede aparecer como ID, sin detalle) y todas las pruebas PASS. Después, pedir a Claude que corra el agente `auditor-evidencias` sobre la carpeta.
- [ ] **Step 5: Commit** — `/commit` (`docs: agregar entrega del dashboard de gobierno de TI en Power BI`).
- [ ] **Step 6: Subir a la plataforma antes de las 20:00 del 18 de noviembre**: Word, PDF, `.pbix` y video (o el enlace, si se publicó con permiso).

## Cronograma

| Cuándo | Qué | Quién |
|---|---|---|
| Martes 17, mañana | Tasks 1 y 2 | Lucho con Claude Code |
| Martes 17, tarde | Task 3 y página 1 de Task 4 | Lucho |
| Miércoles 18, mañana | Página 2 y Task 5 | Lucho |
| Miércoles 18, 14:00-18:00 | Task 6 (Mateo revisa y abre el `.pbix`) y Task 7 | Lucho y Mateo |
| Miércoles 18, 20:00 | Entrega | Lucho |

Si falta tiempo, se recorta en este orden: video con voz (va sin voz), página "Tendencia" (tooltip), marcador "Sin filtros" y, como último recurso, se unen las páginas 4 y 5 en "Datos e IA". La página 1, la hoja de vida y el filtro de mes de corte no se recortan: son la parte interactiva que pide la tarea.
