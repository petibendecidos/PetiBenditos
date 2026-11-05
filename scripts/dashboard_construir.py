"""Calcula los indicadores del dashboard de CIO del PETI Colombia y arma la instantánea de Grafana.

Lee los CSV sintéticos (o los semilla si no hay sintéticos), calcula los indicadores del mes 12 del
escenario simulado, proyecta al mes 24 con una tendencia lineal y escribe:
  - datos/series_mensuales.csv y datos/indicadores_mes12.csv (para el informe)
  - grafana/snapshot.json: carga útil de POST /api/snapshots (paneles con los datos incluidos)
  - grafana/dashboard.json: el mismo tablero como modelo de dashboard de Grafana

Uso: python scripts/dashboard_construir.py <carpeta_dashboard>
Solo usa la biblioteca estándar (no importa numpy).
"""
import copy
import csv
import io
import json
import sys
from collections import defaultdict
from datetime import date, datetime, timezone
from pathlib import Path
from statistics import mean

MESES_ES = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"]
FECHAS = [date(2026 + (9 + i) // 12, (9 + i) % 12 + 1, 1) for i in range(24)]  # mes 1 = oct 2026
ETIQ = [f"{MESES_ES[d.month - 1]} {str(d.year)[2:]}" for d in FECHAS]


def ms(d: date) -> int:
    return int(datetime(d.year, d.month, 15, tzinfo=timezone.utc).timestamp() * 1000)


def mes_de(texto: str) -> int:
    d = date.fromisoformat(texto[:10])
    return (d.year - 2026) * 12 + d.month - 10 + 1


def leer(carpeta: Path, nombre: str):
    ruta = carpeta / f"sintetico_{nombre}.csv"
    if not ruta.exists():
        ruta = carpeta / f"semilla_{nombre}.csv"
    tildes = {"Si": "Sí", "Critica": "Crítica", "Equipo de computo": "Equipo de cómputo"}
    with ruta.open(encoding="utf-8") as f:
        filas = [{k: tildes.get(v, v) for k, v in fila.items()} for fila in csv.DictReader(f)]
    return filas, ruta.name


def tendencia(xs, ys, x_obj):
    mx, my = mean(xs), mean(ys)
    b = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    return my + b * (x_obj - mx)


# --------------------------------------------------------------------------- escenario del portafolio
# (proyecto, mes de fin planeado, mes de fin simulado o None si sigue abierto al mes 12)
PORTAFOLIO = [
    ("P1.1", 5, 5), ("P1.2", 6, 6), ("P1.3", 4, 4), ("P1.4", 6, 7), ("P1.5", 8, 8), ("P1.6", 3, 3),
    ("P1.7", 5, 5), ("P1.8", 6, None), ("P1.9", 3, 3), ("P2.1", 10, 10), ("P2.2", 11, None),
    ("P2.3", 12, None), ("P2.4", 12, 12), ("P2.5", 10, 10), ("P2.6", 12, None), ("P2.7", 9, 9),
    ("P2.8", 9, 9), ("P3.1", 18, None), ("P3.2", 16, None), ("P3.3", 18, None), ("P3.4", 18, None),
    ("P3.5", 18, None), ("P4.1", 24, None), ("P4.2", 21, None), ("P4.3", 24, None),
]
INICIO = {"P1.1": 0, "P1.2": 1, "P1.3": 1, "P1.4": 4, "P1.5": 1, "P1.6": 1, "P1.7": 1, "P1.8": 3,
          "P1.9": 1, "P2.1": 7, "P2.2": 9, "P2.3": 8, "P2.4": 9, "P2.5": 7, "P2.6": 7, "P2.7": 7,
          "P2.8": 7, "P3.1": 13, "P3.2": 13, "P3.3": 13, "P3.4": 13, "P3.5": 13, "P4.1": 13,
          "P4.2": 19, "P4.3": 21}

# Series de escenario que no salen de registros detallados (valores por mes, None = sin medición)
ADOPCION_IA = [None, None, 52, 55, 58, 61, 64, 67, 70, 73, 76, 78]          # KPI-04, línea base mes 3
CONCILIACION = [None] * 5 + [61, 66, 70, 74, 78, 81, 84]                    # KPI-06, línea base mes 6
INVENTARIO_IA = {3: 40, 6: 70, 9: 85, 12: 93}                               # KPI-08, trimestral
IAC = [0, 0, 0, 0, 0, 0, 4, 9, 15, 21, 27, 33]                               # KPI-11
COSTO_NUBE = [None] * 6 + [188.0, 191.5, 186.5, 185.0, 182.6, 180.4]        # USD miles, tablero P2.7 desde mes 7


def construir(base: Path):
    datos = base / "datos"
    tickets, f_t = leer(datos, "tickets")
    vulns, f_v = leer(datos, "vulnerabilidades")
    personas, f_p = leer(datos, "personas")
    fuentes = [f_t, f_v, f_p]

    # ------------------------------------------------------------------ mesa de servicio
    por_mes = defaultdict(list)
    for t in tickets:
        m = mes_de(t["fecha"])
        if 1 <= m <= 12:
            por_mes[m].append(t)
    serv = []
    for m in range(1, 13):
        ts = por_mes[m]
        serv.append({
            "mes": m, "tickets": len(ts),
            "mttr_h": round(mean(float(t["horas_resolucion"]) for t in ts), 1),
            "ans_pct": round(100 * sum(t["dentro_ans"] == "Sí" for t in ts) / len(ts), 1),
            "fcr_pct": round(100 * sum(t["primer_contacto"] == "Sí" for t in ts) / len(ts), 1),
            "csat_pct": round(100 * sum(int(float(t["csat"])) >= 4 for t in ts) / len(ts), 1),
        })
    mttr_prio = {}
    for p in ["P1", "P2", "P3", "P4"]:
        hs = [float(t["horas_resolucion"]) for t in tickets if t["prioridad"] == p and mes_de(t["fecha"]) >= 10]
        mttr_prio[p] = round(mean(hs), 1) if hs else 0
    cat_cnt = defaultdict(int)
    for t in tickets:
        cat_cnt[t["categoria"]] += 1

    # ------------------------------------------------------------------ seguridad
    sev_orden = ["Crítica", "Alta", "Media", "Baja"]
    vul_mes = defaultdict(list)
    for v in vulns:
        m = mes_de(v["fecha_deteccion"])
        if 1 <= m <= 12:
            vul_mes[m].append(v)
    seg = []
    for m in range(1, 13):
        vs = vul_mes[m]
        crit = [float(v["horas_remediacion"]) for v in vs if v["severidad"] == "Crítica"]
        fila = {"mes": m, "mttd_h": round(mean(float(v["horas_deteccion"]) for v in vs), 1),
                "remed_critica_h": round(mean(crit), 1) if crit else None}
        for s in sev_orden:
            fila[s] = sum(v["severidad"] == s for v in vs)
        seg.append(fila)
    # KPI-05 tiene línea base en el mes 3: los meses 1 y 2 no se reportan
    for f in seg[:2]:
        f["remed_critica_h"] = None

    # ------------------------------------------------------------------ talento
    mas6 = [p for p in personas if int(float(p["antiguedad_meses"])) > 6]
    kpi09 = round(100 * sum(int(float(p["certificaciones"])) >= 1 for p in mas6) / len(mas6), 1)
    kpi10 = round(100 * sum(p["rotado_ultimo_anio"] == "Sí" for p in personas) / len(personas), 1)
    cert_rol = {}
    for p in personas:
        cert_rol.setdefault(p["rol"], []).append(p)
    cert_rol = {r: round(100 * sum(int(float(x["certificaciones"])) >= 1 for x in ps if int(float(x["antiguedad_meses"])) > 6)
                         / max(1, sum(int(float(x["antiguedad_meses"])) > 6 for x in ps)), 1)
                for r, ps in sorted(cert_rol.items())}
    # KPI-09 trimestral: el registro detallado da el mes 12; meses 3, 6 y 9 del escenario
    kpi09_trim = {3: round(kpi09 - 12, 1), 6: round(kpi09 - 8, 1), 9: round(kpi09 - 4, 1), 12: kpi09}

    # ------------------------------------------------------------------ portafolio (KPI-01)
    plan_acum = [sum(1 for _, fin, _ in PORTAFOLIO if fin <= m) for m in range(1, 25)]
    real_acum = [sum(1 for _, _, fin in PORTAFOLIO if fin is not None and fin <= m) for m in range(1, 13)]
    kpi01 = round(100 * real_acum[-1] / 25, 1)
    x = list(range(4, 13))
    proy01 = min(100.0, round(100 * tendencia(x, [real_acum[i - 1] for i in x], 24) / 25, 1))
    estados = []
    for pid, fin_plan, fin_real in PORTAFOLIO:
        if fin_real is not None:
            est = "Terminado"
        elif INICIO[pid] > 12:
            est = "Por iniciar"
        elif fin_plan <= 12:
            est = "Atrasado"
        else:
            est = "En ejecución"
        estados.append((pid, est))

    # ------------------------------------------------------------------ proyecciones
    rem = [(f["mes"], f["remed_critica_h"]) for f in seg if f["remed_critica_h"] is not None]
    kpi05 = round(mean(h for m, h in rem if m >= 10), 1)  # promedio del último trimestre
    proy05 = max(1.0, round(tendencia([m for m, _ in rem], [h for _, h in rem], 24), 1))
    proy04 = min(100.0, round(tendencia(list(range(3, 13)), ADOPCION_IA[2:], 24), 1))
    proy06 = min(100.0, round(tendencia(list(range(6, 13)), CONCILIACION[5:], 24), 1))
    proy11 = min(100.0, round(tendencia(list(range(7, 13)), IAC[6:], 24), 1))
    base_costo = mean(COSTO_NUBE[6:9])
    var_costo = [None if c is None or i < 9 else round(100 * (c - base_costo) / base_costo, 1)
                 for i, c in enumerate(COSTO_NUBE)]
    kpi02 = var_costo[11]
    proy02 = round(tendencia([10, 11, 12], var_costo[9:12], 24), 1)

    def cumpl(valor, meta, menor_mejor=False):
        if menor_mejor:
            return 100.0 if valor <= meta else round(100 * meta / valor, 1)
        return round(min(100.0, 100 * valor / meta), 1) if meta else 100.0

    def estado(c):
        return "Bueno" if c >= 95 else ("Intermedio" if c > 70 else "Bajo")

    # Metas intermedias marcadas (*) son supuesto del equipo: interpolación lineal de la meta del mes 24
    tabla = [
        ("KPI-01", "Ejecución acumulada del PETI", f"{kpi01:.0f} %", "55 %", cumpl(kpi01, 55), f"{proy01:.0f} %", "95 %",
         "Recuperar P1.8, P2.2, P2.3 y P2.6 (atrasados)"),
        ("KPI-02", "Variación del costo de nube", f"{kpi02:+.1f} %", "−3 % *", 100.0 if kpi02 <= -3 else cumpl(-kpi02, 3),
         f"{proy02:+.0f} %", "−15 %", "Mantener P2.7 (tablero FinOps)"),
        ("KPI-03", "Casos de IA en producción", "0", "0 *", 100.0, "Inicia mes 13", "5", "Arrancar P3.1 y P3.3 en el mes 13"),
        ("KPI-04", "Adopción de IA en células", f"{ADOPCION_IA[-1]} %", "85 %", cumpl(ADOPCION_IA[-1], 85), f"{proy04:.0f} %",
         "95 %", "Acelerar P1.8 (CoE de IA) y P1.6 (licencias)"),
        ("KPI-05", "Remediación de vulnerabilidades críticas", f"{kpi05:.0f} h", "< 72 h", cumpl(kpi05, 72, True),
         f"{proy05:.0f} h", "< 24 h", "Cerrar P2.2 y P2.3 (pruebas de seguridad en el pipeline)"),
        ("KPI-06", "Conciliación de horas y tareas", f"{CONCILIACION[-1]} %", "95 %", cumpl(CONCILIACION[-1], 95),
         f"{proy06:.0f} %", "95 %", "Estabilizar P2.4 (conciliación con la ALM)"),
        ("KPI-07", "No conformidades mayores ISO/IEC 27001", "0", "0", 100.0, "0", "0", "Mantener el SGSI (P1.1 cerrado)"),
        ("KPI-08", "Cobertura del inventario de IA", f"{INVENTARIO_IA[12]} %", "90 %", cumpl(INVENTARIO_IA[12], 90), "100 %",
         "100 %", "Mantener P1.3"),
        ("KPI-09", "Personal técnico certificado", f"{kpi09:.0f} %", "70 %", cumpl(kpi09, 70), "—", "90 %",
         "Reforzar P1.7 en los roles con menor cobertura"),
        ("KPI-10", "Rotación entre células", f"{kpi10:.0f} %", "50 % *", cumpl(kpi10, 50), "—", "100 %",
         "Plan de rotación con Line Managers (R06)"),
        ("KPI-11", "Ambientes con infraestructura como código", f"{IAC[-1]} %", "50 % *", cumpl(IAC[-1], 50), f"{proy11:.0f} %",
         "100 %", "Recuperar P2.6 (atrasado)"),
        ("KPI-13", "Informe SOC 2 sin salvedades", "En preparación", "—", 100.0, "Sí", "Sí", "P4.1 inicia en el mes 13"),
        ("KPI-14", "Sesiones de comité con acta", "100 %", "90 %", 100.0, "100 %", "90 %", "Mantener el Comité Directivo del PETI"),
    ]
    filas_semaforo = [dict(id=t[0], indicador=t[1], valor_mes12=t[2], meta_mes12=t[3], cumplimiento=t[4],
                           estado=estado(t[4]), proyeccion_mes24=t[5], meta_mes24=t[6], accion=t[7]) for t in tabla]
    conteo = {e: sum(f["estado"] == e for f in filas_semaforo) for e in ["Bueno", "Intermedio", "Bajo"]}

    # ------------------------------------------------------------------ salidas tabulares
    with (datos / "indicadores_mes12.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(filas_semaforo[0]))
        w.writeheader()
        w.writerows(filas_semaforo)
    with (datos / "series_mensuales.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["mes", "etiqueta", "proyectos_plan", "proyectos_real", "tickets", "mttr_h", "ans_pct", "fcr_pct",
                    "csat_pct", "mttd_h", "remed_critica_h", "adopcion_ia", "conciliacion", "iac", "costo_nube_kusd"])
        for i in range(12):
            w.writerow([i + 1, ETIQ[i], plan_acum[i], real_acum[i], serv[i]["tickets"], serv[i]["mttr_h"], serv[i]["ans_pct"],
                        serv[i]["fcr_pct"], serv[i]["csat_pct"], seg[i]["mttd_h"], seg[i]["remed_critica_h"],
                        ADOPCION_IA[i], CONCILIACION[i], IAC[i], COSTO_NUBE[i]])

    # ------------------------------------------------------------------ paneles de Grafana
    paneles, y, pid = [], 0, [0]

    def frame(campos):
        return [{"refId": "A", "fields": [{"name": n, "type": t, "config": c or {}, "values": v} for n, t, v, c in campos]}]

    def a_csv(campos):
        """Mismos datos en CSV para la fuente TestData (dashboard editable, fuera de la instantánea)."""
        buf = io.StringIO()
        w = csv.writer(buf, lineterminator="\n")
        w.writerow([n for n, _, _, _ in campos])
        for fila_v in zip(*[v for _, _, v, _ in campos]):
            w.writerow(["" if val is None else
                        (datetime.fromtimestamp(val / 1000, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
                         if t == "time" else val)
                        for (_, t, _, _), val in zip(campos, fila_v)])
        return buf.getvalue()

    def panel(tipo, titulo, w, h, x, campos, opciones=None, field=None, overrides=None, desc=""):
        pid[0] += 1
        snap = frame(campos)
        paneles.append({
            "_csv": a_csv(campos),
            "id": pid[0], "type": tipo, "title": titulo, "description": desc,
            "gridPos": {"h": h, "w": w, "x": x, "y": y},
            "datasource": {"type": "datasource", "uid": "grafana"},
            "targets": [{"refId": "A", "datasource": {"type": "datasource", "uid": "grafana"},
                         "queryType": "snapshot", "snapshot": snap}],
            "snapshotData": snap,
            "options": opciones or {},
            "fieldConfig": {"defaults": field or {}, "overrides": overrides or []},
        })

    def fila(titulo):
        nonlocal y
        pid[0] += 1
        paneles.append({"id": pid[0], "type": "row", "title": titulo, "collapsed": False,
                        "gridPos": {"h": 1, "w": 24, "x": 0, "y": y}, "panels": []})
        y += 1

    def umbral(pasos):
        return {"mode": "absolute", "steps": [{"color": c, "value": v} for c, v in pasos]}

    verde, amarillo, rojo, azul, gris = "green", "#EAB839", "red", "#5794F2", "#8F8F8F"
    stat_op = {"reduceOptions": {"calcs": ["lastNotNull"], "fields": "", "values": False}, "colorMode": "background",
               "graphMode": "none", "justifyMode": "center", "textMode": "value_and_name", "orientation": "auto"}
    ts_op = {"legend": {"displayMode": "list", "placement": "bottom", "showLegend": True},
             "tooltip": {"mode": "multi", "sort": "none"}}
    bar_op = {"legend": {"displayMode": "list", "placement": "bottom", "showLegend": True}, "tooltip": {"mode": "multi"},
              "xTickLabelRotation": 0, "showValue": "auto", "barWidth": 0.7, "groupWidth": 0.7, "orientation": "auto",
              "stacking": "none"}
    t12 = [ms(d) for d in FECHAS[:12]]
    t24 = [ms(d) for d in FECHAS]

    # Fila 1 - resumen ejecutivo
    fila("Resumen ejecutivo · corte al mes 12 (septiembre de 2027) · escenario simulado")
    panel("gauge", "KPI-01 Ejecución del PETI", 5, 7, 0,
          [("KPI-01", "number", [kpi01], {"unit": "percent", "min": 0, "max": 100})],
          {"reduceOptions": {"calcs": ["lastNotNull"]}, "showThresholdMarkers": True, "showThresholdLabels": False},
          {"unit": "percent", "min": 0, "max": 100, "thresholds": umbral([(rojo, None), (amarillo, 38.5), (verde, 52.3)])},
          desc="Proyectos terminados / 25. Meta mes 12: 55 %. Verde desde el 95 % de la meta.")
    panel("stat", "Estado bueno", 3, 7, 5, [("Bueno", "number", [conteo["Bueno"]], None)], stat_op,
          {"color": {"mode": "fixed", "fixedColor": verde}})
    panel("stat", "Estado intermedio", 3, 7, 8, [("Intermedio", "number", [conteo["Intermedio"]], None)], stat_op,
          {"color": {"mode": "fixed", "fixedColor": amarillo}})
    panel("stat", "Estado bajo", 3, 7, 11, [("Bajo", "number", [conteo["Bajo"]], None)], stat_op,
          {"color": {"mode": "fixed", "fixedColor": rojo}})
    est_cnt = {e: sum(1 for _, s in estados if s == e) for e in ["Terminado", "En ejecución", "Atrasado", "Por iniciar"]}
    panel("piechart", "Portafolio: 25 proyectos por estado", 10, 7, 14,
          [(e, "number", [n], None) for e, n in est_cnt.items()],
          {"reduceOptions": {"calcs": ["lastNotNull"], "fields": "", "values": False}, "pieType": "donut",
           "legend": {"displayMode": "table", "placement": "right", "values": ["value"], "showLegend": True},
           "displayLabels": ["value"]},
          None,
          [{"matcher": {"id": "byName", "options": e}, "properties": [{"id": "color", "value": {"mode": "fixed", "fixedColor": c}}]}
           for e, c in [("Terminado", verde), ("En ejecución", azul), ("Atrasado", rojo), ("Por iniciar", gris)]])
    y += 7
    semaforo_campos = [
        ("ID", "string", [f["id"] for f in filas_semaforo], None),
        ("Indicador", "string", [f["indicador"] for f in filas_semaforo], None),
        ("Valor mes 12", "string", [f["valor_mes12"] for f in filas_semaforo], None),
        ("Meta mes 12", "string", [f["meta_mes12"] for f in filas_semaforo], None),
        ("Cumplimiento", "number", [f["cumplimiento"] for f in filas_semaforo], {"unit": "percent"}),
        ("Estado", "string", [f["estado"] for f in filas_semaforo], None),
        ("Proyección mes 24", "string", [f["proyeccion_mes24"] for f in filas_semaforo], None),
        ("Meta mes 24", "string", [f["meta_mes24"] for f in filas_semaforo], None),
        ("Acción recomendada", "string", [f["accion"] for f in filas_semaforo], None),
    ]
    mapeo_estado = [{"type": "value", "options": {"Bueno": {"color": verde, "index": 0},
                                                  "Intermedio": {"color": amarillo, "index": 1},
                                                  "Bajo": {"color": rojo, "index": 2}}}]
    panel("table", "Semáforo de indicadores del PETI y acción recomendada", 24, 15, 0, semaforo_campos,
          {"showHeader": True, "cellHeight": "sm", "footer": {"show": False}},
          {"custom": {"align": "auto", "cellOptions": {"type": "auto"}, "inspect": True}},
          [{"matcher": {"id": "byName", "options": "Estado"},
            "properties": [{"id": "mappings", "value": mapeo_estado},
                           {"id": "custom.cellOptions", "value": {"type": "color-background", "mode": "basic"}},
                           {"id": "custom.width", "value": 105}]},
           {"matcher": {"id": "byName", "options": "Cumplimiento"},
            "properties": [{"id": "custom.cellOptions", "value": {"type": "gauge", "mode": "basic"}},
                           {"id": "thresholds", "value": umbral([(rojo, None), (amarillo, 70.01), (verde, 95)])},
                           {"id": "min", "value": 0}, {"id": "max", "value": 100}, {"id": "custom.width", "value": 150}]},
           {"matcher": {"id": "byName", "options": "ID"}, "properties": [{"id": "custom.width", "value": 70}]},
           {"matcher": {"id": "byRegexp", "options": "Valor mes 12|Meta mes 12|Meta mes 24"},
            "properties": [{"id": "custom.width", "value": 105}]},
           {"matcher": {"id": "byName", "options": "Proyección mes 24"}, "properties": [{"id": "custom.width", "value": 145}]},
           {"matcher": {"id": "byName", "options": "Indicador"}, "properties": [{"id": "custom.width", "value": 330}]}],
          desc="Rangos del PETI: bueno ≥ 95 % de la meta; intermedio 71–94 %; bajo ≤ 70 %. "
               "(*) Meta intermedia supuesta: interpolación lineal de la meta del mes 24. "
               "La proyección al mes 24 es una tendencia lineal de los últimos meses.")
    y += 15

    # Fila 2 - portafolio
    fila("Avance del portafolio (KPI-01) y proyección")
    proy_serie = [None] * 11 + [real_acum[-1]] + [round(tendencia(x, [real_acum[i - 1] for i in x], m), 1) for m in range(13, 25)]
    panel("trend", "Proyectos terminados: plan, real y proyección al mes 24", 14, 9, 0,
          [("Mes del PETI", "number", list(range(1, 25)), None), ("Plan", "number", plan_acum, None),
           ("Real", "number", real_acum + [None] * 12, None), ("Proyección (tendencia)", "number", proy_serie, None)],
          {**ts_op, "xField": "Mes del PETI"}, {"custom": {"lineWidth": 2, "fillOpacity": 0, "spanNulls": False, "showPoints": "auto"}, "min": 0, "max": 25},
          [{"matcher": {"id": "byName", "options": "Plan"},
            "properties": [{"id": "color", "value": {"mode": "fixed", "fixedColor": gris}},
                           {"id": "custom.lineStyle", "value": {"fill": "dash", "dash": [10, 10]}}]},
           {"matcher": {"id": "byName", "options": "Real"},
            "properties": [{"id": "color", "value": {"mode": "fixed", "fixedColor": azul}}, {"id": "custom.lineWidth", "value": 3}]},
           {"matcher": {"id": "byName", "options": "Proyección (tendencia)"},
            "properties": [{"id": "color", "value": {"mode": "fixed", "fixedColor": "orange"}},
                           {"id": "custom.lineStyle", "value": {"fill": "dot", "dash": [0, 10]}}]}],
          desc="Predictivo: regresión lineal sobre los meses 4 a 12 del avance real.")
    fases = ["Fase 1", "Fase 2", "Fase 3", "Fase 4"]
    por_fase = {e: [sum(1 for p, s in estados if s == e and p[1] == str(i + 1)) for i in range(4)]
                for e in ["Terminado", "En ejecución", "Atrasado", "Por iniciar"]}
    panel("barchart", "Estado de los proyectos por fase", 10, 9, 14,
          [("Fase", "string", fases, None)] + [(e, "number", v, None) for e, v in por_fase.items()],
          {**bar_op, "stacking": "normal"}, None,
          [{"matcher": {"id": "byName", "options": e}, "properties": [{"id": "color", "value": {"mode": "fixed", "fixedColor": c}}]}
           for e, c in [("Terminado", verde), ("En ejecución", azul), ("Atrasado", rojo), ("Por iniciar", gris)]])
    y += 9

    # Fila 3 - seguridad y cumplimiento
    fila("Seguridad y cumplimiento")
    proy_rem = [None] * 11 + [seg[11]["remed_critica_h"]] + [max(1, round(tendencia([m for m, _ in rem], [h for _, h in rem], m), 1))
                                                           for m in range(13, 25)]
    panel("trend", "KPI-05 Horas promedio para remediar vulnerabilidades críticas", 12, 9, 0,
          [("Mes del PETI", "number", list(range(1, 25)), None), ("Horas (real)", "number", [f["remed_critica_h"] for f in seg] + [None] * 12, None),
           ("Proyección (tendencia)", "number", proy_rem, None),
           ("Meta", "number", [None] * 2 + [72] * 10 + [72 - 4 * i for i in range(1, 13)], None)],
          {**ts_op, "xField": "Mes del PETI"}, {"unit": "suffix: h", "custom": {"lineWidth": 2, "spanNulls": True}, "min": 0},
          [{"matcher": {"id": "byName", "options": "Mes del PETI"}, "properties": [{"id": "unit", "value": "none"}]},
           {"matcher": {"id": "byName", "options": "Meta"},
            "properties": [{"id": "color", "value": {"mode": "fixed", "fixedColor": rojo}},
                           {"id": "custom.lineStyle", "value": {"fill": "dash", "dash": [10, 10]}}]},
           {"matcher": {"id": "byName", "options": "Proyección (tendencia)"},
            "properties": [{"id": "color", "value": {"mode": "fixed", "fixedColor": "orange"}},
                           {"id": "custom.lineStyle", "value": {"fill": "dot", "dash": [0, 10]}}]}],
          desc="Meta < 72 h al mes 12 y < 24 h al mes 24 (la rampa entre ambas es supuesto del equipo). Línea base mes 3.")
    panel("barchart", "Vulnerabilidades detectadas por mes y severidad", 12, 9, 12,
          [("Mes", "string", ETIQ[:12], None)] + [(s, "number", [f[s] for f in seg], None) for s in sev_orden],
          {**bar_op, "stacking": "normal", "xTickLabelRotation": -45}, None,
          [{"matcher": {"id": "byName", "options": s}, "properties": [{"id": "color", "value": {"mode": "fixed", "fixedColor": c}}]}
           for s, c in [("Crítica", "dark-red"), ("Alta", "orange"), ("Media", amarillo), ("Baja", "#73BF69")]])
    y += 9
    panel("stat", "KPI-07 No conformidades ISO 27001", 6, 6, 0,
          [("No conformidades mayores", "number", [0], None)], {**stat_op, "textMode": "value"},
          {"thresholds": umbral([(verde, None), (rojo, 1)])},
          desc="No conformidades mayores en la auditoría de recertificación ISO/IEC 27001 del mes 5 (supuesto del escenario).")
    panel("timeseries", "Tiempo medio de detección de vulnerabilidades (MTTD, horas)", 9, 6, 6,
          [("time", "time", t12, None), ("MTTD", "number", [f["mttd_h"] for f in seg], None)],
          ts_op, {"unit": "suffix: h", "custom": {"lineWidth": 2, "fillOpacity": 15}, "color": {"mode": "fixed", "fixedColor": "purple"}})
    panel("barchart", "KPI-08 Cobertura del inventario de IA (trimestral)", 9, 6, 15,
          [("Trimestre", "string", ["mes 3", "mes 6", "mes 9", "mes 12"], None),
           ("Cobertura", "number", list(INVENTARIO_IA.values()), None)],
          {**bar_op, "showValue": "always", "legend": {"showLegend": False, "displayMode": "list", "placement": "bottom"}},
          {"unit": "percent", "min": 0, "max": 100, "color": {"mode": "thresholds"},
           "thresholds": umbral([(rojo, None), (amarillo, 63.1), (verde, 85.5)])})
    y += 6

    # Fila 4 - servicio y operación
    fila("Servicio y operación (mesa de servicio de TI interna)")
    panel("timeseries", "Cumplimiento de ANS, resolución al primer contacto y satisfacción", 14, 9, 0,
          [("time", "time", t12, None), ("Dentro de ANS", "number", [f["ans_pct"] for f in serv], None),
           ("Primer contacto (FCR)", "number", [f["fcr_pct"] for f in serv], None),
           ("CSAT (4 o 5)", "number", [f["csat_pct"] for f in serv], None)],
          ts_op, {"unit": "percent", "min": 0, "max": 100, "custom": {"lineWidth": 2}})
    panel("barchart", "Tiempo medio de resolución por prioridad (último trimestre)", 10, 9, 14,
          [("Prioridad", "string", list(mttr_prio), None), ("Horas", "number", list(mttr_prio.values()), None)],
          {**bar_op, "showValue": "always", "legend": {"showLegend": False, "displayMode": "list", "placement": "bottom"}},
          {"unit": "suffix: h", "color": {"mode": "fixed", "fixedColor": azul}})
    y += 9
    panel("barchart", "Tickets por mes", 8, 8, 0,
          [("Mes", "string", ETIQ[:12], None), ("Tickets", "number", [f["tickets"] for f in serv], None)],
          {**bar_op, "xTickLabelRotation": -45, "legend": {"showLegend": False, "displayMode": "list", "placement": "bottom"}},
          {"color": {"mode": "fixed", "fixedColor": azul}})
    panel("timeseries", "KPI-04 Adopción de IA y KPI-06 Conciliación de horas", 16, 8, 8,
          [("time", "time", t12, None), ("KPI-04 Adopción de IA", "number", ADOPCION_IA, None),
           ("KPI-06 Conciliación", "number", CONCILIACION, None),
           ("Meta KPI-04 (85 %)", "number", [85] * 12, None), ("Meta KPI-06 (95 %)", "number", [95] * 12, None)],
          ts_op, {"unit": "percent", "min": 40, "max": 100, "custom": {"lineWidth": 2, "spanNulls": False}},
          [{"matcher": {"id": "byRegexp", "options": "Meta.*"},
            "properties": [{"id": "custom.lineStyle", "value": {"fill": "dash", "dash": [10, 10]}},
                           {"id": "custom.lineWidth", "value": 1}]}])
    y += 8

    # Fila 5 - costo y talento
    fila("Costo y talento")
    panel("barchart", "Costo mensual de nube administrada (USD miles) y KPI-02", 10, 8, 0,
          [("Mes", "string", ETIQ[6:12], None), ("Costo", "number", COSTO_NUBE[6:12], None)],
          {**bar_op, "showValue": "always", "legend": {"showLegend": False, "displayMode": "list", "placement": "bottom"}},
          {"color": {"mode": "fixed", "fixedColor": "#B877D9"}},
          desc=f"Línea base: promedio de abril a junio de 2027 (meses 7–9, tablero P2.7). Variación al mes 12: {kpi02:+.1f} %.")
    panel("bargauge", "KPI-09 Personal certificado por rol (más de 6 meses)", 7, 8, 10,
          [("Rol", "string", list(cert_rol), None), ("Certificado", "number", list(cert_rol.values()), None)],
          {"orientation": "horizontal", "displayMode": "gradient", "showUnfilled": True,
           "reduceOptions": {"calcs": ["lastNotNull"], "values": True}},
          {"unit": "percent", "min": 0, "max": 100, "thresholds": umbral([(rojo, None), (amarillo, 49.1), (verde, 66.5)])})
    panel("bargauge", "KPI-10 Rotación y KPI-11 Infraestructura como código", 7, 8, 17,
          [("Indicador", "string", ["KPI-10 Rotación", "KPI-11 IaC"], None), ("Valor", "number", [kpi10, IAC[-1]], None)],
          {"orientation": "horizontal", "displayMode": "gradient", "showUnfilled": True,
           "reduceOptions": {"calcs": ["lastNotNull"], "values": True}},
          {"unit": "percent", "min": 0, "max": 100, "thresholds": umbral([(rojo, None), (amarillo, 35.1), (verde, 47.5)])},
          desc="Meta intermedia supuesta al mes 12: 50 % para ambos (100 % al mes 24).")
    y += 8

    dashboard = {
        "title": "PETI Colombia 2026-2028 · Dashboard de CIO (escenario simulado)",
        "description": "Trabajo académico, Equipo Firmes por la Gobernanza. Datos sintéticos generados con mostly.ai: "
                       "no son datos reales de Perficient ni de ningún cliente.",
        "uid": "peti-colombia-cio", "tags": ["PETI", "CIO", "datos sinteticos"],
        "timezone": "utc", "editable": False, "graphTooltip": 1, "schemaVersion": 39,
        "time": {"from": "2026-10-01T00:00:00Z", "to": "2027-09-30T23:59:59Z"},
        "panels": paneles,
    }
    gdir = base / "grafana"
    gdir.mkdir(exist_ok=True)
    # Instantánea: los datos van en cada panel (consulta "snapshot"). Dashboard editable: fuente TestData con CSV.
    instantanea, editable = copy.deepcopy(dashboard), copy.deepcopy(dashboard)
    for p in instantanea["panels"]:
        p.pop("_csv", None)
    ds = {"type": "grafana-testdata-datasource", "uid": "peti-testdata"}
    for p in editable["panels"]:
        if p["type"] == "row":
            continue
        p["datasource"] = ds
        p["targets"] = [{"refId": "A", "datasource": ds, "scenarioId": "csv_content", "csvContent": p.pop("_csv")}]
        p.pop("snapshotData", None)
    (gdir / "dashboard.json").write_text(json.dumps(editable, ensure_ascii=False, indent=1), encoding="utf-8")
    (gdir / "snapshot.json").write_text(json.dumps({"dashboard": instantanea, "name": dashboard["title"], "expires": 0},
                                                   ensure_ascii=False), encoding="utf-8")
    print("Fuentes:", ", ".join(fuentes))
    print(f"KPI-01 {kpi01} %, KPI-05 {kpi05} h, KPI-09 {kpi09} %, KPI-10 {kpi10} %, KPI-02 {kpi02} %")
    print("Semáforo:", conteo, "| proyección KPI-01 mes 24:", proy01, "| KPI-05 mes 24:", proy05)
    for f in filas_semaforo:
        print(f"  {f['id']} {f['estado']:<10} {f['cumplimiento']:>6} {f['valor_mes12']:>14} -> {f['proyeccion_mes24']}")


if __name__ == "__main__":
    construir(Path(sys.argv[1]))
