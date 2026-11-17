# Instalación y operación

## Requisitos

| Requisito | Detalle |
|---|---|
| Node.js | Versión 24 o superior (n8n 2.47.7 lo exige) |
| n8n | Se ejecuta con `npx n8n@2.47.7`; no hace falta Docker |
| Cuenta de Google | Para Gmail y Google Sheets, con un proyecto en Google Cloud |

## Instalación

1. **Arrancar n8n.** En el repositorio, `scripts/n8n/iniciar_n8n.ps1` fija la carpeta de datos, la zona horaria de Colombia y el puerto 5678. La primera vez descarga n8n y tarda varios minutos. Al abrir `http://localhost:5678` se crea la cuenta de dueño de la instalación.
2. **Preparar Google Cloud.** En un proyecto propio, activar Gmail API, Google Sheets API y Google Drive API. Crear un cliente OAuth de tipo web con la URI de redirección `http://localhost:5678/rest/oauth2-credential/callback`. Dejar la pantalla de consentimiento en modo de prueba y agregar como usuario de prueba la cuenta que va a enviar los correos.
3. **Crear las credenciales en n8n.** Una de tipo *Google Sheets OAuth2 API* y otra de tipo *Gmail OAuth2 API*, con el ID y el secreto del cliente. Iniciar sesión con la cuenta que envía los correos. Google avisa que la app no está verificada; como es propia, se acepta.
4. **Subir la hoja.** Subir `hoja-gobierno-celulas.xlsx` a Google Drive, abrirla como hoja de Google y escribir los correos reales en las pestañas Config y Celulas.
5. **Importar el flujo.** Importar `flujo-gobierno-celulas.json` y, en los nodos de Google, elegir la hoja y las credenciales. El script `scripts/flujo_gobierno_construir.py` también puede generar el JSON con los identificadores ya puestos.
6. **Probar y activar.** Ejecutar con el disparo manual, aprobar el correo del Comité y revisar las pestañas Historial y Decisiones. Después activar el flujo para que corra cada mes.

## Operación

| Situación | Qué hacer |
|---|---|
| Cambió una meta del PETI | Editar la pestaña Umbrales; no hay que tocar el flujo |
| Llegaron las mediciones de un mes nuevo | Cargarlas en Mediciones y subir el mes de corte en Config |
| Entra o sale una célula | Editar la pestaña Celulas |
| El Comité quiere más días para decidir | Cambiar el límite de espera del nodo "Aprobación del Comité" |
| Hay que volver a evaluar un mes | Ejecutar de nuevo: el historial se actualiza y la bitácora agrega las decisiones nuevas |

## Problemas conocidos

| Síntoma | Causa | Qué hacer |
|---|---|---|
| Google bloquea el acceso: "no completó el proceso de verificación" | La cuenta no está en los usuarios de prueba | Agregarla en Google Cloud, en Público, Usuarios de prueba |
| "Missing required parameter: scope" | La credencial de Gmail tiene encendidos los alcances personalizados sin alcances, o es del tipo genérico | Apagar los alcances personalizados o crear una credencial de tipo *Gmail OAuth2 API* |
| Google entra con otra cuenta y no deja elegir | El navegador tiene una sesión de Google abierta | Conectar la credencial desde una ventana privada |
| La credencial deja de funcionar a los siete días | En modo de prueba, Google vence la autorización a los siete días | Volver a iniciar sesión en la credencial |
| Los botones de aprobación no responden | El correo se abrió en otro dispositivo o n8n estaba apagado | Abrirlo en el equipo donde corre n8n, con n8n encendido |
| El disparo mensual no corrió | n8n estaba apagado a esa hora | Dejar n8n encendido o llevarlo a un servidor |

## Seguridad de la información

* El archivo del cliente OAuth y su secreto no se guardan en el repositorio; se pegan en n8n, que los guarda cifrados en su carpeta de datos.
* El JSON publicado no lleva el identificador de la hoja ni el de las credenciales.
* Los correos reales solo están en la hoja de Google, no en el flujo ni en el repositorio.
