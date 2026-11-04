---
name: commit
description: Usar cuando el usuario pide confirmar cambios, hacer commit o preparar un mensaje de commit en el repositorio PetiBenditos.
disable-model-invocation: true
allowed-tools: Bash(git status *) Bash(git diff *) Bash(git log *) Bash(git add *) Bash(git commit *) Bash(git config --get *) Bash(git check-ignore *)
argument-hint: "[descripción breve opcional]"
---

# Commit en PetiBenditos

## Reglas inamovibles

- **Nunca** se confirman los insumos restringidos: `docs/informacion_jd-v2.md`, `docs/arquitectura-sistema-anonimizado.md`, `docs/evidencia-privada/`, `docs/privado/`, ni ningún archivo nuevo que contenga entrevistas o arquitectura de clientes. Antes de `git add`, ejecutar `git check-ignore -v` sobre los restringidos; si alguno no está ignorado o aparece en `git status`, detenerse y avisar.
- Revisar el diff de todo `.md` que vaya al commit en busca de nombres de clientes, sistemas o tablas de la cuenta analizada. Si aparece algo, detenerse y avisar (skill `evidencias-peti`, revisión de reidentificación).
- El mensaje no menciona a Claude, a Anthropic, a "IA" ni a herramientas de asistencia: sin `Co-Authored-By`, sin "Generated with". El autor es la identidad git del usuario; comprobarla con `git config --get user.name` y `git config --get user.email` y detenerse si no está configurada. (Regla tomada del repositorio Diabot del mismo usuario; si el usuario la quiere distinta aquí, se cambia esta línea.)
- No se hace `git push`. El usuario decide cuándo publicar.
- No se confirman archivos temporales ni de Office (`~$*`, `*.tmp`, `*.bak`), ni `.claude/settings.local.json`.
- Un commit por cambio lógico. Si el diff mezcla el PETI con `.claude/` o con el registro de evidencias sin relación, proponer commits separados.

## Formato del mensaje

```
tipo(ámbito): descripción en imperativo, minúscula inicial, sin punto final, máximo 72 caracteres

Cuerpo opcional: qué cambia y por qué, en español con tildes. Si el cambio toca el PETI,
indicar la versión y los numerales afectados, igual que en el control de cambios (§16 en la v2.1, §15 en Colombia).
```

Tipos: `docs`, `feat` (contenido nuevo del PETI, por ejemplo un numeral), `fix` (corrección de un error del PETI), `refactor` (reestructura sin cambiar contenido), `chore`, `revert`. Ámbitos: `peti`, `evidencias`, `insumos`, `readme`, `claude`. Se omite si el cambio cruza varios.

Ejemplos: `docs(peti): agregar hojas de vida de los indicadores KPI-01 a KPI-10`, `fix(peti): corregir SOC 2 como informe de atestación en §9.7`, `chore(claude): agregar skills y agentes del PETI`.

## Procedimiento

1. `git status` y `git diff --stat`; `git diff` de lo relevante.
2. Verificar identidad, rama y exclusión de restringidos.
3. Si el cambio toca §7 a §11 del PETI, ejecutar el script de `trazabilidad-peti` y mencionar en el cuerpo si quedaron hallazgos de severidad alta.
4. Si el cambio toca el PETI, comprobar que el control de cambios (§16 en la v2.1, §15 en Colombia) y la versión del encabezado se actualizaron; si no, avisar antes de confirmar.
5. Proponer el mensaje con `$ARGUMENTS` como pista.
6. `git add` de archivos concretos (nunca `git add -A` sin revisar) y `git commit -m`.
7. Mostrar `git log -1 --stat`.
