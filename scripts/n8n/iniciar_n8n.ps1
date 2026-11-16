# Arranca n8n en local para los flujos del curso (skill .claude/skills/flujos-n8n).
# Los datos de n8n (base SQLite, credenciales cifradas, clave de cifrado) quedan en D:\dev\n8n,
# fuera del repositorio. Se abre en http://localhost:5678. Ctrl+C lo detiene.
$ErrorActionPreference = 'Stop'

$env:N8N_USER_FOLDER = 'D:\dev\n8n'
$env:GENERIC_TIMEZONE = 'America/Bogota'
$env:TZ = 'America/Bogota'
$env:N8N_PORT = '5678'
$env:N8N_DIAGNOSTICS_ENABLED = 'false'
$env:N8N_PERSONALIZATION_ENABLED = 'false'

New-Item -ItemType Directory -Force -Path (Join-Path $env:N8N_USER_FOLDER 'peti') | Out-Null

$version = (node -v)
if (-not $version.StartsWith('v24.')) {
    throw "n8n 2.47.7 pide Node 24 o superior; el activo es $version. Cambia con: nvm use 24.12.0"
}

npx --yes n8n@2.47.7
