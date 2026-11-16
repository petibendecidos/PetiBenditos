---
name: flujos-n8n
description: Usar cuando hay que crear, importar, exportar, ejecutar o depurar un flujo de n8n del curso o del PETI (por ejemplo, el flujo de gobierno de TI por célula con ISO/IEC 38500), arrancar n8n en este equipo, conectar Gmail o Google Sheets con OAuth, o cuando una credencial de Google se desconecta, una aprobación por correo no reanuda el flujo o la importación falla en Windows.
argument-hint: "[flujo o problema]"
---

# Flujos de n8n en este equipo

## Principio

El JSON del flujo se versiona; los secretos, los correos y los IDs no. n8n guarda las credenciales cifradas en su propia carpeta, fuera del repositorio, y el JSON que va a Git lleva marcadores en su lugar. Un flujo se da por terminado cuando se ejecutó de verdad y la hoja, los correos y la bitácora muestran el resultado, no cuando el JSON se importa sin errores.

## Entorno

| Elemento | Valor |
|---|---|
| Versión | n8n `2.47.7` (pide Node 24 o superior). Node `24.12.0` activo con nvm; también está la 18.20.8, que no sirve |
| Arranque | `powershell -File scripts/n8n/iniciar_n8n.ps1` (ejecutar en segundo plano; la primera vez descarga n8n y tarda varios minutos) |
| Interfaz | `http://localhost:5678`. Salud: `curl -s -o /dev/null -w "%{http_code}" http://localhost:5678/healthz` → `200` |
| Carpeta de datos | `D:\dev\n8n` (`N8N_USER_FOLDER`): base SQLite, credenciales cifradas y la clave de cifrado. **Nunca** se copia al repositorio. Si se borra, se pierden el dueño, las credenciales y los flujos |
| Trabajo local | `D:\dev\n8n\peti\`: JSON con IDs reales, hoja con correos reales, `ids.txt`. Tampoco va al repositorio |
| Zona horaria | `America/Bogota` (afecta el disparo mensual) |
| Docker | No está instalado ni hace falta |

La primera vez, n8n pide crear la cuenta de **dueño** local (correo y contraseña de esta instancia). La crea el usuario en el navegador; Claude no la conoce.

## Google (Gmail y Sheets) con OAuth

- Cliente OAuth de tipo web en el proyecto de Google Cloud `peti-514922`. URI de redirección: `http://localhost:5678/rest/oauth2-credential/callback` (ya configurada). El archivo `client_secret_*.json` queda en `D:\Descargas`: no se copia, no se imprime, no se sube. El usuario pega el ID y el secreto en n8n.
- En Google Cloud: activar Gmail API, Google Sheets API y Google Drive API; pantalla de consentimiento en estado **Testing** con la cuenta Gmail del equipo como usuario de prueba.
- En n8n: una credencial "Google Sheets PETI" (Google Sheets OAuth2 API) y otra "Gmail PETI" (Gmail OAuth2 API), cada una con el mismo ID y secreto, e iniciar sesión con la cuenta Gmail. Google muestra el aviso de "app no verificada": se acepta, porque la app es del mismo usuario.
- **En modo Testing el token vence a los 7 días.** Síntoma: el nodo falla con `invalid_grant` o la credencial aparece desconectada. Solución: abrir la credencial y volver a iniciar sesión. Pasar la app a producción con alcances de Gmail exige la verificación de Google; para el curso no vale la pena.

## Convenciones del JSON versionado

| Dato | En el repositorio | En `D:\dev\n8n\peti\` |
|---|---|---|
| ID de la hoja de Google | `__SPREADSHEET_ID__` | El real |
| ID de credencial de Sheets | `__CREDENCIAL_SHEETS__` | El real |
| ID de credencial de Gmail | `__CREDENCIAL_GMAIL__` | El real |
| Correos | Ninguno en el flujo: se leen de la hoja. En la hoja versionada, `comite@ejemplo.com` y `lider@ejemplo.com` | Correos reales, solo en la hoja de Google y en la copia local del libro |

- El flujo se genera con un script de `scripts/` (por ejemplo, `flujo_gobierno_construir.py`), que lee la lógica JS de `scripts/n8n/` y la incrusta en los nodos Code. Se edita el script o el JS, no el JSON a mano.
- La lógica de los nodos Code vive en un módulo JS sin dependencias, probado con `node --test scripts/n8n/`. El nodo Code solo llama a esas funciones.
- Antes de un commit: `grep -rnE "[A-Za-z0-9._%+-]+@(gmail|hotmail)\.com|client_secret" docs/ scripts/ .claude/` no debe devolver nada.
- Nombres de nodos en español, iguales a los del diseño: el código de los nodos los usa en `$('Nombre del nodo')`.

## Importar, exportar y ejecutar

- Importar: `npx n8n@2.47.7 import:workflow --input=D:/dev/n8n/peti/flujo-con-ids.json`. Usar rutas con `/` aunque sea Windows (con `\` falla). Si la interfaz no muestra el flujo, reiniciar n8n o importar desde la interfaz (*Import from File*).
- Exportar: `npx n8n@2.47.7 export:workflow --all --output=D:/dev/n8n/peti/exportado.json`. Credenciales, solo para ver `id` y `name`: `export:credentials --all` (sin `--decrypted`).
- Los comandos de la CLI necesitan las mismas variables de entorno que el arranque (`N8N_USER_FOLDER` sobre todo); si no, abren una base vacía.
- n8n anuncia que dejará estos comandos de importación y exportación a favor de un CLI nuevo. Si dejan de funcionar, usar la interfaz.
- Para conocer el `type`, la `typeVersion` y los nombres de parámetros de un nodo, no se adivinan: se crea el nodo en la interfaz, se exporta y se copian. Anotar abajo lo que se confirme.

## Aprobaciones por correo (human in the loop)

- El nodo Gmail en la operación *Send and Wait for Approval* manda botones de aprobar y rechazar, y el flujo queda en espera. Se le pone un límite de espera y una rama para cuando no hay respuesta.
- Los botones apuntan a `http://localhost:5678`: **solo funcionan si se abren en este equipo** con n8n encendido. Desde el celular no. Por eso el aprobador es la cuenta Gmail que se abre en este navegador.
- Si hay varios ítems, agruparlos antes en uno solo (nodo Code) para mandar una sola solicitud de aprobación.
- Un flujo con disparo programado solo corre si n8n está encendido a esa hora.

## Nodos confirmados en n8n 2.47.7

Verificados el 16 de noviembre de 2026 contra `n8n-nodes-base` 2.47.5 (el que instala n8n 2.47.7). La fuente es `dist/types/nodes.json` del paquete, en la caché de npx (`D:\dev\cache\npm\_npx\<hash>\node_modules\n8n-nodes-base`): trae las versiones y los parámetros de cada nodo, sin tener que crear nodos en la interfaz.

| Nodo | `type` y `typeVersion` | Parámetros que usa el flujo |
|---|---|---|
| Disparo programado | `n8n-nodes-base.scheduleTrigger` 1.2 | `rule.interval[0]`: `field: "months"`, `monthsInterval`, `triggerAtDayOfMonth`, `triggerAtHour` |
| Disparo manual | `n8n-nodes-base.manualTrigger` 1 | ninguno |
| Google Sheets | `n8n-nodes-base.googleSheets` 4.7 | `authentication: "oAuth2"`, `operation` (`read`, `append`, `appendOrUpdate`), `documentId` y `sheetName` como `{"__rl": true, "mode": "id"/"name", "value": …}`; `columns` es un *resource mapper* (`mappingMode: "autoMapInputData"`, `matchingColumns`); `options.cellFormat` (`USER_ENTERED` por defecto, `RAW`). Leer devuelve números sin formato (`UNFORMATTED_VALUE`) |
| Code | `n8n-nodes-base.code` 2 | `mode: "runOnceForAllItems"`, `language: "javaScript"`, `jsCode` |
| Switch | `n8n-nodes-base.switch` 3.2 | `rules.values[]` con `conditions` (filtro, operador `string`/`equals`), `renameOutput`, `outputKey` |
| Gmail enviar | `n8n-nodes-base.gmail` 2.1 | `sendTo`, `subject`, `emailType` (`html`), `message`, `options.appendAttribution` |
| Gmail aprobación | `n8n-nodes-base.gmail` 2.1 | `operation: "sendAndWait"`, `responseType` (`approval` por defecto), `approvalOptions.values`: `approvalType` (`single`/`double`), `approveLabel`, `disapproveLabel`; `options.limitWaitTime.values`: `limitType: "afterTimeInterval"`, `resumeAmount`, `resumeUnit` (`minutes`/`hours`/`days`) |

Cuidados que salieron de leer el código del paquete:

- El correo de *Send and Wait* **escapa el HTML** del mensaje y lo muestra con `white-space: pre-line`. Mandar texto plano con saltos de línea, no tablas HTML.
- Las escrituras en Sheets con `USER_ENTERED` convierten textos como `2027-09` en fechas. Para claves y ciclos usar `cellFormat: "RAW"`.
- Un nodo de Google Sheets que recibe varios ítems se ejecuta una vez por ítem. Las lecturas encadenadas llevan `executeOnce: true`.
- En los nodos Code no existe `module`: el constructor quita la línea `module.exports` antes de incrustar el módulo.

## Problemas conocidos

| Síntoma | Causa | Qué hacer |
|---|---|---|
| `npm error ECONNRESET` al descargar n8n | Corte de red al bajar el paquete | Repetir; el registro de npm responde |
| La credencial de Google se desconecta | Token de 7 días en modo Testing | Volver a iniciar sesión en la credencial |
| La aprobación no reanuda el flujo | Se abrió el correo en otro dispositivo o n8n estaba apagado | Abrir el correo en este equipo con n8n encendido |
| `import:workflow` no encuentra el archivo | Ruta con `\` | Usar `/` |
| La CLI no ve los flujos | Faltan las variables de entorno | Ejecutar con `N8N_USER_FOLDER=D:\dev\n8n` |

## Relacionado

- ISO/IEC 38500 y correspondencia con el PETI: `marcos-referencia` ([iso-38500.md](../marcos-referencia/iso-38500.md)).
- Textos del flujo (correos, informe, hoja): `redaccion-peti`. Datos sintéticos y evidencia: `evidencias-peti`.
