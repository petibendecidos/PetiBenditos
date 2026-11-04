---
name: trazabilidad-peti
description: Usar cuando se crea, modifica o elimina una brecha, oportunidad, proyecto, indicador, riesgo u objetivo de TI en el PETI de Perficient; cuando hay que comprobar que cada brecha tiene proyecto, cada proyecto tiene indicador y cada objetivo tiene metas; cuando se construye la matriz de trazabilidad o las fichas del portafolio; cuando se compara el PETI con los IDs y columnas del Anexo 1; o cuando el usuario sospecha que las cifras del README o de un numeral no cuadran.
argument-hint: "[ID o numeral]"
---

# Trazabilidad interna del PETI

## Principio

Un PETI se sostiene por una cadena que se puede recorrer en los dos sentidos:

```
motivador / hallazgo AS-IS (con evidencia)
        → objetivo estratégico de TI (con metas por año y línea base)
        → brecha (elemento, acción, dominio, tiempo, costo)
        → iniciativa o proyecto (fase, responsable, costo, entregable)
        → indicador (fórmula, línea base, meta, fuente, responsable)
        ↔ riesgo (qué lo materializa, qué proyecto o control lo trata)
```

Un eslabón suelto es un defecto: una brecha sin proyecto no se cierra, un proyecto sin brecha no se justifica, un proyecto sin indicador no se puede seguir y un objetivo sin meta no es un objetivo (guía, Actividades 8, 11, 13 y 14).

## Comprobación automática

```
python .claude/skills/trazabilidad-peti/scripts/verificar_trazabilidad.py
```

Imprime conteos, hallazgos `T-nn` por severidad, la matriz brecha → proyectos y las brechas por dominio. Comprueba: brechas y oportunidades sin proyecto; proyectos sin origen; IDs citados sin definir (incluida la evidencia contra el registro); viñetas del AS-IS sin ID; indicadores y riesgos sin vínculo; columnas del Anexo 1 que faltan en brechas, portafolio e indicadores; cifras del README. Por defecto revisa el PETI regional v2.1; para el PETI Colombia, pasa `docs/perficient_peti_colombia_2026_2028.md` como primer argumento. Ejecútalo antes y después de tocar cualquiera de esos numerales y reporta la diferencia. Las filas `PUB-` del registro que solo usan las entregas del curso (por ejemplo, PUB-016 a PUB-025) aparecen como "no citadas" con severidad baja: es esperado.

El script no juzga calidad (si la brecha está bien justificada o la meta es realista); eso lo hacen el agente `auditor-conformidad` y la lectura.

## IDs: los del PETI y los del Anexo 1

| Elemento | PETI v2.1 y Colombia | Anexo 1 | Regla |
|---|---|---|---|
| Objetivo estratégico de TI | `OETI01…` (§7) | `OETI01…` | Mismo ID que el Anexo 1 (en la v1.1 histórica eran 1-4) |
| Meta de TI | `METI01…` (§7) | `METI01…` | Con línea base y meta por año (Act. 8) |
| Brecha | `BRE-001…` | `B001…` | Mantener `BRE-` |
| Oportunidad | `OPT-001…` | — | Mantener |
| Proyecto | `P<fase>.<n>` | `IT001…` | Mantener `P1.1`; si el profesor exige el catálogo del Anexo 1, añadir tabla de equivalencias |
| Indicador | `KPI-01…` | `IND.ES.01…` (código por dominio) | Mantener `KPI-`; la hoja de vida puede llevar ambos |
| Riesgo | `R01…` | — | Mantener |
| Evidencia | `PUB-/PRV-` (registro) | — | Ver `evidencias-peti` |

**No se renumera.** Si un elemento se elimina, su ID no se reutiliza; se deja constancia en el control de cambios. Un ID nuevo toma el siguiente número libre.

## Al crear o cambiar un elemento

| Si cambias… | Revisa también |
|---|---|
| Una brecha | Hallazgo de la situación actual (§6) que la origina; proyecto en el portafolio (§9); dominio; mapa de ruta; README; DOFA y entregas del curso que la citan |
| Un proyecto | Brecha u oportunidad; fase y meses en el mapa de ruta; indicador (§10); riesgo (§11); responsable (rol propuesto); costo; DOFA cruzada y libro de matrices de `docs/entregas-*/` |
| Un indicador | Proyecto u objetivo que mide; hoja de vida completa (fórmula, línea base, fuente, responsable, frecuencia, meta, rangos) |
| Un riesgo | Proyecto o control que lo trata; propietario; riesgo residual |
| Un objetivo de TI | Objetivo corporativo que apoya; metas por año; proyectos que contribuyen |
| Una fecha o una fase | Mapa de ruta visual; dependencias (lo que requiere que otro termine antes); hitos externos (vencimiento ISO 27001) |

## Contrato de salida

1. **Salida del script** (o su resumen) antes y después del cambio.
2. **Matriz de trazabilidad** del alcance pedido: objetivo → brecha → proyecto → indicador → riesgo, con "—" donde falte el eslabón.
3. **Cambios propuestos** para cerrar cada eslabón suelto, con el ID afectado y el numeral.

## Señales de alerta

- Un proyecto que atiende una brecha pero termina después de la fecha en que la brecha produce su daño (por ejemplo, renovar un certificado después de su vencimiento).
- Indicadores que no miden ningún proyecto y proyectos que no mide ningún indicador.
- Dominios del MRAE sin ninguna brecha: o el diagnóstico no encontró nada (decirlo) o falta análisis.
- Cifras del README distintas de las del PETI.
