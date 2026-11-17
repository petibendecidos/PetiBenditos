# Arquitectura y nodos

## Componentes

| Componente | Papel |
|---|---|
| n8n 2.47.7 | Motor del flujo. Corre en un equipo local (`http://localhost:5678`) con Node.js 24 |
| Google Sheets | Fuente de datos y registro: configuración, células, metas, mediciones, historial y decisiones |
| Gmail | Avisos a los líderes, solicitud de aprobación al Comité e informe mensual |
| Módulo de evaluación en JavaScript | La lógica de los nodos de código, probada fuera de n8n con 15 pruebas automáticas |

## Recorrido

```
Disparo mensual ─┐
Disparo manual ──┴─► Leer Config ─► Leer Células ─► Leer Umbrales ─► Leer Mediciones ─► Evaluar células
                                                                                              │
          ┌───────────────────────────────────────────────────────────────────────────────────┤
          ▼                                   ▼                                               ▼
  Preparar historial              Según estado (Switch)                              Armar informe
          ▼                        │ Intermedio        │ Bajo                                 ▼
  Registrar historial      Avisar a líderes     Agrupar rojos                         Enviar informe
                                                     ▼
                                          Aprobación del Comité (espera hasta 3 días)
                                                     ▼
                                          Preparar decisión ─► Registrar decisión
```

## Los 17 nodos

| Nodo | Tipo | Qué hace |
|---|---|---|
| Disparo mensual | Programado | Día 1 de cada mes, 7:00, hora de Colombia |
| Disparo manual | Manual | Para demostraciones y pruebas |
| Leer Config | Google Sheets, leer | Mes de corte y correos del Comité y de copia |
| Leer Células | Google Sheets, leer (una vez) | Las 12 células y el correo de sus líderes |
| Leer Umbrales | Google Sheets, leer (una vez) | Meta, sentido, unidad y proyecto de cada indicador |
| Leer Mediciones | Google Sheets, leer (una vez) | 576 mediciones: 12 células × 12 meses × 4 indicadores |
| Evaluar células | Código | Valida los correos, calcula cumplimiento y estado por célula y compara con el mes anterior |
| Preparar historial | Código | Deja solo las columnas de la pestaña Historial |
| Registrar historial | Google Sheets, agregar o actualizar | Una fila por célula y ciclo; la clave es ciclo y célula |
| Según estado | Switch | Separa las células en estado intermedio y en estado bajo |
| Avisar a líderes | Gmail, enviar | Un correo por célula en amarillo |
| Agrupar rojos | Código | Junta todas las células en rojo en una sola solicitud |
| Aprobación del Comité | Gmail, enviar y esperar | Dos botones: aprobar el plan correctivo o escalar; espera hasta tres días |
| Preparar decisión | Código | Convierte la respuesta en una fila por célula en rojo |
| Registrar decisión | Google Sheets, agregar | Bitácora de decisiones |
| Armar informe | Código | Células ordenadas de peor a mejor, con su estado del mes anterior |
| Enviar informe | Gmail, enviar | Informe al Comité, con copia |

## Decisiones de diseño

* **La lógica vive fuera de n8n.** Los nodos de código copian un módulo de JavaScript que se prueba aparte. Un script de Python arma el JSON del flujo e incrusta ese módulo, así que se corrige el módulo y no el JSON a mano.
* **El JSON no lleva secretos.** El identificador de la hoja y los de las credenciales van como marcadores en la versión publicada. Los correos no están en el flujo: se leen de la hoja.
* **Una sola aprobación por mes.** Si hay diez células en rojo, el Comité recibe un correo, no diez.
* **La aprobación va en texto plano.** El correo de "enviar y esperar" de n8n no muestra HTML; la solicitud se arma con saltos de línea.
* **Las escrituras en la hoja van sin interpretar.** Así el ciclo "2027-09" no se convierte en una fecha.
* **Las lecturas encadenadas se ejecutan una vez.** Sin esa opción, un nodo de Google Sheets que recibe 12 filas se ejecutaría 12 veces.
