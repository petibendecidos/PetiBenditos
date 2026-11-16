# Flujo de gobierno de TI por célula (ISO/IEC 38500:2024) — plan de implementación

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Entregar la tarea "Cargar flujo automatizado de Gobierno de TI - ISO 38500 2024" (cierre: 18 de noviembre de 2026, 23:59) con un flujo de n8n que corre cada mes, evalúa cada célula de la operación colombiana con las metas del PETI, pide decisiones al Comité cuando hay rojo y deja registro en Google Sheets y por Gmail.

**Architecture:** n8n 2.47.7 corre en local (`npx`, Node 24.12.0) con los datos en `D:\dev\n8n`. Una hoja de Google con seis pestañas es la fuente y el registro. La lógica de evaluación es un módulo JS probado con `node:test` que un script de Python incrusta en el JSON del flujo; el JSON versionado lleva marcadores en lugar de IDs y correos.

**Tech Stack:** n8n 2.47.7 (nodos Schedule Trigger, Manual Trigger, Google Sheets, Code, Switch, Gmail con *Send and Wait for Approval*, IF), Node 24 `node:test`, Python 3.14 con `openpyxl` y `pytest`, Google Cloud (proyecto `peti-514922`, cliente OAuth web ya creado).

**Spec:** el diseño se acordó en la conversación del 16 de noviembre de 2026 y está resumido en "Diseño" abajo. Insumos: `D:\Descargas\ISO-IEC-38500-2024.pdf` (vista previa de iTeh, 10 páginas: índice y §1 a §4.2), `ISO-38500-y-la-IA-Jorge-Garibay.pdf` (Pink Elephant, nombres en español de los 11 principios y del marco), `381911_ITG10.pdf` (capítulo de curso: modelo EDM y 6 principios de la versión 2008 con criterios de evaluación), `01 - EIS - IT Governance Guide - 2024.pdf` (Oregon EIS: comité, bitácora de decisiones, cadencia mensual).

## Diseño

```
Disparo mensual (día 1, 07:00, America/Bogota) ─┐
Disparo manual (demostración) ──────────────────┤
  → Leer Config → Leer Células → Leer Umbrales → Leer Mediciones   (Google Sheets)
  → Evaluar células (Code: un ítem por célula, semáforo con los rangos del PETI §10)
  → Registrar historial (Sheets, agregar o actualizar por clave ciclo|célula), cuya salida va a dos ramas:
      a) Según estado (Switch):
           Bueno / Sin datos → nada más
           Intermedio → Avisar a líderes (Gmail, un correo por célula al correo_lider)
           Bajo → Agrupar rojos (Code, un solo ítem) → Aprobación del Comité (Gmail, enviar y esperar,
                  aprobar / escalar, límite 3 días) → Preparar decisión (Code) → Registrar decisión (Sheets "Decisiones")
      b) Armar informe (Code, una vez para todos: ranking y cambio frente al mes anterior) → Enviar informe (Gmail al Comité)
```

Los 16 nodos, con estos nombres exactos: `Disparo mensual`, `Disparo manual`, `Leer Config`, `Leer Células`, `Leer Umbrales`, `Leer Mediciones`, `Evaluar células`, `Registrar historial`, `Según estado`, `Avisar a líderes`, `Agrupar rojos`, `Aprobación del Comité`, `Preparar decisión`, `Registrar decisión`, `Armar informe`, `Enviar informe`.

| Parte del flujo | Tarea ISO/IEC 38500:2024 (§6.2) | Principio (§5) | Elemento del marco (§7.2) |
|---|---|---|---|
| Disparos y lecturas | Monitorear | Supervisión (5.5); Datos y decisiones (5.9) | Desempeño |
| Evaluar células | Evaluar | Viabilidad y desempeño en el tiempo (5.12); Generación de valor (5.3) | Desempeño |
| Avisar a líderes | Dirigir | Liderazgo (5.8); Rendición de cuentas (5.6) | Delegación |
| Aprobación del Comité y decisión | Dirigir | Gobierno del riesgo (5.10); Rendición de cuentas (5.6) | Dirección; Rendición de cuentas |
| Historial y Decisiones | Monitorear | Rendición de cuentas (5.6) | Rendición de cuentas |
| Informe al Comité | Involucrar a las partes interesadas | Participación de las partes interesadas (5.7); Estrategia (5.4) | Política |

Indicadores por célula, calculados de los datos sintéticos del 4 de noviembre (`docs/entregas-2026-11-04/dashboard/datos/sintetico_*.csv`, 12 células C01 a C12, mes 1 = octubre de 2026 a mes 12 = septiembre de 2027):

| kpi | Cálculo por célula y mes | Meta | Menor es mejor | Proyecto que corrige |
|---|---|---|---|---|
| KPI-05 | Promedio de `horas_remediacion` de severidad `Critica` detectadas en el mes | 72 | sí | P2.2, P2.3 |
| ANS | % de tickets con `dentro_ans = Si` en el mes (meta supuesta, INT-001) | 90 | no | P2.5 |
| KPI-09 | % de personas con `antiguedad_meses > 6` y `certificaciones >= 1` (foto, igual todos los meses) | 70 | no | P1.7 |
| KPI-10 | % de personas con `rotado_ultimo_anio = Si` (foto) | 50 | no | P2.1 (R06) |

Cumplimiento y estado, iguales a `scripts/dashboard_construir.py` (`cumpl`, `estado`): mayor es mejor → `min(100, 100·valor/meta)`; menor es mejor → `100` si `valor <= meta`, si no `100·meta/valor`; redondeo a 1 decimal. Estado: `>= 95` Bueno, `> 70` Intermedio, si no Bajo. Estado de la célula: el peor de sus indicadores con dato; `Sin datos` si ninguno tiene dato.

Correos: Comité (aprobación e informe) = la cuenta Gmail que autoriza n8n; líderes de célula y copia del informe = el correo Hotmail. **Solo se escriben en la hoja de Google y en `D:\dev\n8n\peti\`, nunca en el repositorio.**

## Global Constraints

- n8n `2.47.7` exacto (`npx n8n@2.47.7`), Node `24.12.0`, carpeta de usuario `N8N_USER_FOLDER=D:\dev\n8n`, `GENERIC_TIMEZONE=America/Bogota`, puerto `5678`.
- Ningún archivo versionado contiene correos reales, el `client_secret`, el ID de la hoja ni IDs de credenciales. Marcadores: `__SPREADSHEET_ID__`, `__CREDENCIAL_SHEETS__`, `__CREDENCIAL_GMAIL__`; correos de ejemplo `comite@ejemplo.com`, `lider@ejemplo.com`.
- El archivo `D:\Descargas\client_secret_*.json` no se copia al repositorio ni se imprime; el usuario pega ID y secreto en n8n.
- Pantalla de consentimiento en modo **Testing** con la cuenta Gmail como usuario de prueba: el token vence a los 7 días (suficiente para la entrega; documentarlo).
- El botón de aprobación apunta a `http://localhost:5678`: se aprueba desde el navegador de este equipo.
- Textos del flujo, de la hoja y del Word en español, con las reglas de `redaccion-peti` (fechas "18 de noviembre de 2026", coma decimal en el Word). Antes de escribir el Word se cargan `redaccion-peti`, `evidencias-peti` y `marcos-referencia`.
- La ISO completa no está disponible: del §5 en adelante solo se citan **nombres** (índice de la vista previa) y la descripción de Garibay como fuente secundaria.
- Commits solo con autorización del usuario y con la skill `/commit` (sin `Co-Authored-By`, sin push).

## Review Focus

- Célula sin mediciones en el mes de corte → estado `Sin datos`, se registra en Historial, no se avisa ni se escala (prueba en Task 3).
- Mes sin vulnerabilidades críticas en una célula → KPI-05 sin dato (no 0 h, no Bueno), el estado sale de los demás indicadores (prueba en Task 3).
- Ninguna célula en rojo → no se manda correo de aprobación vacío; el informe sí sale (prueba en Task 3 para `agruparRojos` y verificación en Task 6).
- Re-ejecutar el mismo mes → Historial no duplica filas (agregar o actualizar por `clave`; verificación en Task 6).
- Correos de ejemplo todavía en la hoja → el flujo se detiene con el mensaje "Reemplaza los correos de ejemplo en las pestañas Config y Celulas" (prueba en Task 3).

---

### Task 1: Referencia de la ISO/IEC 38500 y registro de fuentes

**Files:**
- Create: `.claude/skills/marcos-referencia/iso-38500.md`
- Modify: `.claude/skills/marcos-referencia/SKILL.md` (fila nueva en la tabla de marcos internacionales y en la `description`)
- Modify: `docs/registro-de-evidencias.md` (filas PUB-026 a PUB-029, versión del encabezado a 1.3)

**Interfaces:**
- Produces: `iso-38500.md` con tres tablas que usa el Word de Task 6: (1) 11 principios 2024 con número de sección, nombre en inglés y en español y descripción de Garibay; (2) tareas del modelo (Engage, Evaluate, Direct, Monitor) y 6 elementos del marco (Direction, Capability, Policy, Delegation, Performance, Accountability); (3) correspondencia con los 6 principios de 2008 (ITG10) y con la guía EIS (comité, bitácora de decisiones con foco, justificación, responsable y fecha; cadencia mensual o trimestral). IDs PUB-026 (vista previa ISO), PUB-027 (guía EIS 2024), PUB-028 (ITG10), PUB-029 (Garibay).

- [x] **Step 1:** Escribir `iso-38500.md` desde el texto de los cuatro PDF (extraer con `pdftotext -layout` a una carpeta temporal). Cada dato lleva su ID; lo que solo dice Garibay se marca "fuente secundaria". Incluir "Cuidado al citarlo": vista previa hasta §4.2; la 2024 reemplaza los 6 principios de 2008 por 11 alineados con ISO 37000; no es certificable.
- [x] **Step 2:** Agregar la fila ISO/IEC 38500:2024 a la tabla de `SKILL.md` con enlace a `iso-38500.md`, y "ISO/IEC 38500" a la `description`.
- [x] **Step 3:** Agregar PUB-026 a PUB-029 al registro con el formato de las filas existentes (clasificación Público; para PUB-028 decir que es material de curso sin autor identificado y que describe la versión 2008).
- [x] **Step 4: Verificar** (16-nov: 5 coincidencias y 11 principios)

Run: `grep -c "PUB-02[6-9]" docs/registro-de-evidencias.md; grep -c "5\.1[0-2]\|5\.[2-9]" .claude/skills/marcos-referencia/iso-38500.md`
Expected: el primero `>= 4`; el segundo `>= 11`.

- [ ] **Step 5: Commit** (con autorización) — `docs: agregar referencia de ISO/IEC 38500:2024 y sus fuentes`

### Task 2: Skill `flujos-n8n` y n8n corriendo en local

**Files:**
- Create: `.claude/skills/flujos-n8n/SKILL.md`
- Create: `scripts/n8n/iniciar_n8n.ps1`

**Interfaces:**
- Produces: `iniciar_n8n.ps1` (sin parámetros) que fija `N8N_USER_FOLDER=D:\dev\n8n`, `GENERIC_TIMEZONE=America/Bogota`, `N8N_PORT=5678` y ejecuta `npx --yes n8n@2.47.7`. La skill documenta: arranque, creación del dueño local, credenciales de Google (pasos de Task 5), convenciones de marcadores, `export:workflow`/`import:workflow` (rutas con `/` en Windows), aprobaciones solo desde localhost, vencimiento de 7 días en modo Testing y cómo reconectar.

- [ ] **Step 1:** (16-nov: script escrito, sintaxis válida; falta ejecutarlo) Escribir `iniciar_n8n.ps1` y ejecutarlo en segundo plano (la primera descarga tarda varios minutos).
- [ ] **Step 2: Verificar que responde**

Run: `curl -s -o /dev/null -w "%{http_code}" http://localhost:5678/healthz`
Expected: `200`

- [ ] **Step 3: Punto de control con el usuario:** abre `http://localhost:5678` y crea la cuenta de dueño local (correo y contraseña solo de esta instancia).
- [ ] **Step 4:** Crear en la interfaz un flujo de prueba con un nodo de cada tipo del diseño (Schedule Trigger, Manual Trigger, Google Sheets, Code, Switch, Gmail en *Send and Wait for Approval*, IF), exportarlo con `npx n8n@2.47.7 export:workflow --all --output=D:/dev/n8n/peti/tipos.json` y anotar en la skill el `type`, `typeVersion` y nombres de parámetros de cada nodo. Task 4 usa esos valores; no se adivinan.
- [x] **Step 5:** (16-nov; la sección "Nodos confirmados" queda para el Step 4) Escribir `SKILL.md` (≤ 120 líneas, `description` que empiece por "Usar cuando").
- [ ] **Step 6: Commit** (con autorización) — `chore: agregar skill y arranque local de n8n`

### Task 3: Lógica de evaluación (módulo JS)

**Files:**
- Create: `scripts/n8n/evaluar_celulas.js`
- Test: `scripts/n8n/evaluar_celulas.test.js`

**Interfaces:**
- Produces (CommonJS, sin dependencias, `module.exports`):
  - `cumplimiento(valor: number|null, meta: number, menorEsMejor: boolean) -> number|null`
  - `estadoDe(cumpl: number|null) -> "Bueno"|"Intermedio"|"Bajo"|null`
  - `validarCorreos(config: object, celulas: object[]) -> void` (lanza `Error("Reemplaza los correos de ejemplo en las pestañas Config y Celulas")` si algún correo termina en `@ejemplo.com` o está vacío)
  - `evaluarCelulas({config, celulas, umbrales, mediciones}) -> object[]`: un objeto por célula con `ciclo` (`"2027-09"` para mes 12), `clave` (`"2027-09|C05"`), `celula`, `correo_lider`, `estado`, `indicadores: [{kpi, valor, meta, cumplimiento, estado, proyecto}]`, `cambio` (estado del mes anterior o `null`).
  - `agruparRojos(evaluadas: object[]) -> object[]`: `[]` si no hay `Bajo`; si hay, un solo objeto `{ciclo, celulas: [...], asunto, cuerpoHtml}`.
  - `armarInforme(evaluadas: object[]) -> {asunto, cuerpoHtml}`: tabla ordenada de peor a mejor y conteo por estado.
- Formas de entrada (filas de Sheets): `config` `{mes_corte, correo_comite, correo_copia}`; `celulas` `{celula, nombre, correo_lider}`; `umbrales` `{kpi, nombre, meta, menor_es_mejor ("Si"/"No"), unidad, proyecto}`; `mediciones` `{mes, etiqueta, celula, kpi, valor, n}` con `valor` vacío cuando no hay dato.

- [ ] **Step 1: Escribir las pruebas** (`node:test` + `assert`):
  - `cumplimiento(181, 72, true) === 39.8`; `cumplimiento(60, 72, true) === 100`; `cumplimiento(63, 90, false) === 70`; `cumplimiento(null, 72, true) === null`.
  - `estadoDe(95) === "Bueno"`; `estadoDe(70.1) === "Intermedio"`; `estadoDe(70) === "Bajo"`.
  - Célula con KPI-05 vacío y el resto ≥ meta → estado `Bueno` y KPI-05 con `estado === null`.
  - Célula sin filas en el mes de corte → `estado === "Sin datos"`.
  - Célula con un KPI en Bajo y otro en Bueno → `estado === "Bajo"`; `clave === "2027-09|C05"` con `mes_corte = 12`.
  - `agruparRojos` sin rojos → `[]`; con dos rojos → un objeto con `celulas.length === 2`.
  - `validarCorreos` con `comite@ejemplo.com` → lanza el mensaje exacto.
- [ ] **Step 2: Correr y ver que fallan** — Run: `node --test scripts/n8n/` → Expected: FAIL (módulo no existe).
- [ ] **Step 3: Implementar** las funciones en `evaluar_celulas.js`. `ciclo`: mes 1 = `2026-10`.
- [ ] **Step 4: Correr y ver que pasan** — Run: `node --test scripts/n8n/` → Expected: todas PASS.
- [ ] **Step 5: Commit** (con autorización) — `feat: agregar evaluación por célula para el flujo de gobierno`

### Task 4: Datos de la hoja y constructor del flujo

**Files:**
- Create: `scripts/flujo_gobierno_datos.py`
- Create: `scripts/flujo_gobierno_construir.py`
- Test: `scripts/tests/test_flujo_gobierno.py`
- Create (generados): `docs/entregas-2026-11-16/flujo-iso38500/hoja-gobierno-celulas.xlsx`, `docs/entregas-2026-11-16/flujo-iso38500/flujo-gobierno-celulas.json`

**Interfaces:**
- Consumes: `evaluar_celulas.js` (Task 3) y los `type`/`typeVersion`/parámetros anotados en la skill (Task 2, Step 4).
- Produces:
  - `python scripts/flujo_gobierno_datos.py <carpeta_datos> <salida.xlsx> [--correo-comite X --correo-lider Y --correo-copia Z]` → pestañas `Config`, `Celulas`, `Umbrales`, `Mediciones`, `Historial` (solo encabezados: `clave, ciclo, celula, estado, KPI-05, ANS, KPI-09, KPI-10, fecha_ejecucion`), `Decisiones` (solo encabezados: `fecha, ciclo, celula, foco, justificacion, decision, responsable`). Sin argumentos usa los correos de ejemplo; `Config.mes_corte = 12`.
  - `python scripts/flujo_gobierno_construir.py <salida.json> [--spreadsheet-id X --credencial-sheets Y --credencial-gmail Z]` → JSON de n8n con los nodos del diseño (nombres en español exactamente como en el diagrama) y el código de `evaluar_celulas.js` incrustado en cada nodo Code seguido de la llamada correspondiente. Sin argumentos deja los marcadores.

- [ ] **Step 1: Escribir las pruebas** (`pytest`):
  - `test_mediciones`: 12 células × 12 meses × 4 kpi = 576 filas; C05 mes 12 KPI-05 igual al promedio calculado a mano desde `sintetico_vulnerabilidades.csv`.
  - `test_correos_de_ejemplo`: sin argumentos, ningún correo distinto de `@ejemplo.com` en el libro.
  - `test_flujo_estructura`: toda conexión apunta a un nodo existente; existen los 16 nombres de la lista del diseño; ningún `@` fuera de los marcadores de ejemplo; contiene `__SPREADSHEET_ID__` y `__CREDENCIAL_GMAIL__`; el nodo de aprobación tiene límite de espera de 3 días.
  - `test_flujo_con_ids`: con argumentos, no queda ningún marcador.
- [ ] **Step 2: Correr y ver que fallan** — Run: `python -m pytest scripts/tests/test_flujo_gobierno.py -q` → Expected: FAIL.
- [ ] **Step 3: Implementar** los dos scripts. El Historial se escribe con la operación de agregar o actualizar de Sheets, columna de coincidencia `clave`. El nodo Code de evaluación llama primero a `validarCorreos`.
- [ ] **Step 4: Correr y ver que pasan** — Run: `python -m pytest scripts/tests/test_flujo_gobierno.py -q` → Expected: todas PASS.
- [ ] **Step 5:** Generar el libro y el JSON versionados (con marcadores) y la copia privada con correos reales en `D:\dev\n8n\peti\hoja-gobierno-celulas.xlsx`.
- [ ] **Step 6: Commit** (con autorización) — `feat: agregar datos y constructor del flujo de gobierno por célula`

### Task 5: Conexión con Google (punto de control con el usuario)

**Files:** ninguno versionado. Notas operativas en la skill de Task 2 si algo cambia.

- [ ] **Step 1 (usuario, Google Cloud Console, proyecto `peti-514922`):** activar Gmail API, Google Sheets API y Google Drive API; en la pantalla de consentimiento (Audience) dejar el estado **Testing** y agregar la cuenta Gmail como usuario de prueba. La URI de redirección ya está bien en el cliente.
- [ ] **Step 2 (usuario, n8n):** crear las credenciales "Google Sheets PETI" (Google Sheets OAuth2 API) y "Gmail PETI" (Gmail OAuth2 API) con el ID y el secreto del archivo de `D:\Descargas`, e iniciar sesión con la cuenta Gmail. Aceptar el aviso de app no verificada.
- [ ] **Step 3 (usuario, Drive):** subir `D:\dev\n8n\peti\hoja-gobierno-celulas.xlsx`, abrirlo con Hojas de cálculo de Google y guardarlo como hoja de Google. Pasar la URL.
- [ ] **Step 4: Verificar** — Run: `npx n8n@2.47.7 export:credentials --all --output=D:/dev/n8n/peti/credenciales.json` y leer solo `id` y `name` → Expected: aparecen las dos credenciales. Anotar los IDs y el ID de la hoja (de la URL) en `D:\dev\n8n\peti\ids.txt`.

### Task 6: Importar, ejecutar, evidenciar y documentar

**Files:**
- Create: `docs/entregas-2026-11-16/flujo-iso38500/flujo-gobierno-iso38500.md` → `Flujo_Gobierno_TI_ISO38500_Perficient_Colombia.docx`
- Create: `docs/entregas-2026-11-16/flujo-iso38500/README.md`, `docs/entregas-2026-11-16/flujo-iso38500/capturas/`
- Modify: `docs/entregas-2026-11-16/README.md`, `README.md`, `.claude/CLAUDE.md`

**Interfaces:**
- Consumes: JSON con IDs (Task 4 con los valores de Task 5), `iso-38500.md` (Task 1).

- [ ] **Step 1:** `python scripts/flujo_gobierno_construir.py D:/dev/n8n/peti/flujo-con-ids.json --spreadsheet-id … --credencial-sheets … --credencial-gmail …` y `npx n8n@2.47.7 import:workflow --input=D:/dev/n8n/peti/flujo-con-ids.json` (si falla, importar desde la interfaz: *Import from File*). Reiniciar n8n si la interfaz no lo muestra.
- [ ] **Step 2:** Ejecutar con el disparo manual. Aprobar desde el navegador de este equipo el correo que llega a la cuenta Gmail.
- [ ] **Step 3: Verificar**
  - Historial: 12 filas con `ciclo = 2027-09`.
  - Decisiones: una fila por célula en Bajo, con `decision` = "Aprobado plan correctivo" o "Escalado al Comité Directivo".
  - Hotmail: un aviso por célula en Intermedio y copia del informe. Gmail: aprobación e informe.
  - Volver a ejecutar: Historial sigue con 12 filas para `2027-09`.
- [ ] **Step 4:** Activar el flujo (disparo mensual) y tomar con el usuario las capturas: lienzo con la ejecución en verde, correo de aprobación, informe, pestañas Historial y Decisiones. Guardar en `capturas/` (sin correos visibles o recortados).
- [ ] **Step 5:** Escribir `flujo-gobierno-iso38500.md` (qué hace, por qué es distinto del ejemplo del profesor, tabla de correspondencia con la ISO, indicadores y reglas, decisiones registradas, cómo importarlo, límites: datos sintéticos, ISO en vista previa, token de 7 días, aprobación en localhost) y generar el Word con `scripts/md_a_docx_simple.py`. README de la carpeta con qué se sube (JSON + Word + capturas), cómo regenerar y pendientes; actualizar el README del 16 de noviembre, el README raíz y `CLAUDE.md`.
- [ ] **Step 6: Verificar que no se filtró nada**

Run: `grep -rnE "[A-Za-z0-9._%+-]+@(gmail|hotmail)\.com|client_secret\"|apps\.googleusercontent\.com" docs/ scripts/ .claude/ ; git status --short`
Expected: sin coincidencias; en `git status` no aparece nada de `D:\dev\n8n`.

- [ ] **Step 7: Commit** (con autorización) — `docs: agregar entrega del flujo de gobierno de TI con ISO/IEC 38500`

## Sin subagente nuevo

No se crea un subagente. El trabajo es secuencial, depende de pasos del usuario (dueño de n8n, consentimiento de Google, aprobación por correo) y comparte estado local (n8n en ejecución, IDs). Un subagente empezaría sin ese contexto. La revisión final la cubren los agentes existentes `auditor-evidencias` (fuentes y filtración de datos) y la verificación del Step 6.
