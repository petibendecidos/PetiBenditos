"""Genera los datos semilla del dashboard de CIO del PETI Colombia (escenario simulado).

Los registros son inventados por reglas: no salen de Perficient ni de ninguna cuenta de cliente.
Simulan los primeros 12 meses del PETI (octubre de 2026 a septiembre de 2027) con una mejora
gradual por efecto de los proyectos. mostly.ai entrena sobre estas tablas y genera la versión
sintética que alimenta el dashboard (ver dashboard_sintetizar.py).

Uso: python scripts/dashboard_semilla.py <carpeta_salida>
Solo usa la biblioteca estándar. Los valores van en ASCII (Si, Critica, C05): en Windows,
mostly.ai corrompe las tildes de las categorías; dashboard_construir.py las restituye al mostrar.
"""
import csv
import random
import sys
from datetime import date, timedelta
from pathlib import Path

random.seed(20261104)

MESES = [date(2026, 10, 1)]
for _ in range(11):
    m = MESES[-1]
    MESES.append(date(m.year + (m.month == 12), m.month % 12 + 1, 1))

CELULAS = [f"C{i:02d}" for i in range(1, 13)]
CATEGORIAS = ["Acceso y permisos", "Ambientes de desarrollo", "Pipeline CI/CD", "Herramientas de IA",
              "Red y VPN", "Equipo de computo", "Licencias"]
PRIORIDADES = [("P1", 0.06, 4), ("P2", 0.19, 8), ("P3", 0.45, 24), ("P4", 0.30, 72)]  # nombre, peso, ANS en horas
SEVERIDADES = [("Critica", 0.10), ("Alta", 0.25), ("Media", 0.40), ("Baja", 0.25)]
ORIGENES = ["SAST", "SCA", "DAST", "Pentest"]


def dia_aleatorio(mes: date) -> date:
    fin = date(mes.year + (mes.month == 12), mes.month % 12 + 1, 1)
    return mes + timedelta(days=random.randrange((fin - mes).days))


def elegir(pares):
    r, acum = random.random(), 0.0
    for item in pares:
        acum += item[1]
        if r <= acum:
            return item
    return pares[-1]


def tickets():
    random.seed(1)
    filas = []
    for i, mes in enumerate(MESES):
        mejora = i / 11  # 0 al inicio, 1 al mes 12
        for _ in range(random.randint(140, 175) - int(20 * mejora)):
            prio, _, ans = elegir(PRIORIDADES)
            factor = random.lognormvariate(0, 0.45) * (1.25 - 0.4 * mejora)
            horas = round(max(0.3, ans * 0.7 * factor), 1)
            fcr = random.random() < 0.52 + 0.18 * mejora
            if fcr:
                horas = round(min(horas, random.uniform(0.3, 2.0)), 1)
            csat = max(1, min(5, round(random.gauss(3.6 + 0.6 * mejora - (horas > ans) * 0.9, 0.8))))
            filas.append({
                "fecha": dia_aleatorio(mes).isoformat(), "celula": random.choice(CELULAS),
                "categoria": random.choice(CATEGORIAS), "prioridad": prio,
                "horas_resolucion": horas, "dentro_ans": "Si" if horas <= ans else "No",
                "primer_contacto": "Si" if fcr else "No", "csat": csat,
            })
    return filas


def vulnerabilidades():
    random.seed(2)
    base = {"Critica": 150, "Alta": 260, "Media": 520, "Baja": 900}  # horas promedio al inicio
    filas = []
    for i, mes in enumerate(MESES):
        mejora = i / 11
        for _ in range(random.randint(180, 240)):
            sev, _ = elegir(SEVERIDADES)
            media = base[sev] * (1 - 0.40 * mejora)
            filas.append({
                "fecha_deteccion": dia_aleatorio(mes).isoformat(), "celula": random.choice(CELULAS),
                "severidad": sev, "origen": random.choice(ORIGENES),
                "horas_deteccion": round(max(1, random.lognormvariate(3.3 - 0.6 * mejora, 0.5)), 1),
                "horas_remediacion": round(max(2, random.lognormvariate(0, 0.35) * media), 1),
            })
    return filas


def personas():
    random.seed(3)
    roles = [("Desarrollo", 0.55), ("QA", 0.15), ("DevOps y nube", 0.12), ("Datos e IA", 0.10), ("Arquitectura", 0.08)]
    filas = []
    for i in range(1, 221):
        rol, _ = elegir(roles)
        antig = random.choice([3, 5, 8, 12, 18, 24, 30, 36, 48, 60])
        prob_cert = 0.18 + 0.17 * (antig > 6) + 0.10 * (rol in ("DevOps y nube", "Arquitectura"))
        certs = sum(random.random() < prob_cert * 0.8 for _ in range(3))
        filas.append({
            "persona": f"P{i:03d}", "rol": rol, "celula": random.choice(CELULAS),
            "antiguedad_meses": antig, "certificaciones": certs,
            "rotado_ultimo_anio": "Si" if random.random() < 0.35 else "No",
        })
    return filas


def escribir(ruta: Path, filas):
    with ruta.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(filas[0]))
        w.writeheader()
        w.writerows(filas)
    print(f"{ruta.name}: {len(filas)} filas")


if __name__ == "__main__":
    salida = Path(sys.argv[1])
    salida.mkdir(parents=True, exist_ok=True)
    escribir(salida / "semilla_tickets.csv", tickets())
    escribir(salida / "semilla_vulnerabilidades.csv", vulnerabilidades())
    escribir(salida / "semilla_personas.csv", personas())
