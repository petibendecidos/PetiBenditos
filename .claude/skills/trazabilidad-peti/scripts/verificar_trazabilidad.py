"""Verifica la trazabilidad interna del PETI y las columnas mínimas del Anexo 1.

Uso:
    python .claude/skills/trazabilidad-peti/scripts/verificar_trazabilidad.py [ruta_peti] [ruta_registro]

Por defecto usa docs/perficient_peti_v2_2026_2028.md y docs/registro-de-evidencias.md.
Imprime un informe en Markdown. Solo biblioteca estándar. No modifica archivos.

Comprueba:
  - brechas (BRE-) y oportunidades (OPT-) sin proyecto que las atienda
  - proyectos sin brecha ni oportunidad
  - IDs referenciados que no están definidos (BRE, OPT, PUB, PRV, INT)
  - evidencia del registro que el PETI no usa
  - viñetas del AS-IS (§9) sin ID de evidencia
  - indicadores y riesgos sin vínculo explícito con proyectos o brechas
  - columnas que el Anexo 1 exige en brechas (Act. 11), iniciativas (Act. 13) e indicadores (Act. 14B)
  - cifras del README (brechas, proyectos) frente al conteo real
"""
import os
import re
import sys
import unicodedata

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
PETI = os.path.join(RAIZ, "docs", "perficient_peti_v2_2026_2028.md")
REGISTRO = os.path.join(RAIZ, "docs", "registro-de-evidencias.md")
README = os.path.join(RAIZ, "README.md")

RE_BRE = r"BRE-\d{3}"
RE_OPT = r"OPT-\d{3}"
RE_PROY = r"\bP\d\.\d+\b"
RE_KPI = r"KPI-\d{2}"
RE_RIESGO = r"\bR\d{2}\b"
RE_EVID = r"\b(?:PUB|PRV|INT)-\d{3}\b"

DOMINIOS = [
    "estrategia", "gobierno", "informacion", "sistemas de informacion",
    "infraestructura", "uso y apropiacion", "seguridad",
]


def normalizar(texto):
    texto = unicodedata.normalize("NFD", texto.lower())
    return "".join(c for c in texto if unicodedata.category(c) != "Mn")


def clasificar_dominio(parte):
    """Asigna un fragmento de la celda 'Dominio' a uno de los 7 dominios, del más específico al más general."""
    for clave, dominio in [("sistemas de informacion", "sistemas de informacion"), ("seguridad", "seguridad"),
                           ("uso y apropiacion", "uso y apropiacion"), ("infraestructura", "infraestructura"),
                           ("servicios", "infraestructura"), ("gobierno", "gobierno"),
                           ("estrategia", "estrategia"), ("informacion", "informacion")]:
        if clave in parte:
            return dominio
    return None


def leer(ruta):
    with open(ruta, encoding="utf8") as f:
        return f.read()


def secciones(texto):
    """Devuelve {numero: (titulo, cuerpo)} para los títulos '## N. Título'."""
    partes = {}
    actual, titulo, lineas = None, "", []
    for linea in texto.splitlines():
        m = re.match(r"^##\s+(\d+)\.\s+(.*)", linea)
        if m:
            if actual is not None:
                partes[actual] = (titulo, "\n".join(lineas))
            actual, titulo, lineas = int(m.group(1)), m.group(2).strip(), []
        elif actual is not None:
            lineas.append(linea)
    if actual is not None:
        partes[actual] = (titulo, "\n".join(lineas))
    return partes


def tablas(cuerpo):
    """Lista de tablas; cada una es (encabezado, filas) con celdas ya separadas."""
    resultado, bloque = [], []
    for linea in cuerpo.splitlines() + [""]:
        if linea.strip().startswith("|"):
            bloque.append([c.strip() for c in linea.strip().strip("|").split("|")])
        elif bloque:
            filas = [f for f in bloque[1:] if not all(re.fullmatch(r":?-+:?", c or "-") for c in f)]
            resultado.append((bloque[0], filas))
            bloque = []
    return resultado


def filas_con_id(cuerpo, patron):
    """{id: (encabezado, fila)} para filas cuya primera celda es un ID que cumple el patrón."""
    encontrados = {}
    for encabezado, filas in tablas(cuerpo):
        for fila in filas:
            m = re.fullmatch(r"\**(" + patron + r")\**", fila[0]) if fila else None
            if m:
                # La primera tabla con el ID es la que lo define (catálogo); las siguientes (fichas) no la sustituyen.
                encontrados.setdefault(m.group(1), (encabezado, fila))
    return encontrados


def columna(encabezado, fila, nombre):
    for i, c in enumerate(encabezado):
        if nombre in normalizar(c) and i < len(fila):
            return fila[i]
    return ""


def falta_columnas(encabezado, requeridas):
    enc = " | ".join(normalizar(c) for c in encabezado)
    return [r for r in requeridas if not any(alt in enc for alt in r.split("/"))]


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ruta_peti = sys.argv[1] if len(sys.argv) > 1 else PETI
    ruta_reg = sys.argv[2] if len(sys.argv) > 2 else REGISTRO
    texto = leer(ruta_peti)
    registro = leer(ruta_reg)
    sec = secciones(texto)

    # Las secciones se buscan por título para servir a la v1.x (§9, §11-§15) y a la v2.x (§6, §8-§11).
    claves = {"asis": r"situaci.n actual", "brechas": r"brecha|oportunidad", "portafolio": r"portafolio",
              "indicadores": r"^indicador", "riesgos": r"riesgo"}

    def cuerpo(clave):
        return "\n".join(c for t, c in sec.values() if re.search(claves[clave], normalizar(t)))

    brechas = filas_con_id(cuerpo("brechas"), RE_BRE)
    oportunidades = filas_con_id(cuerpo("brechas"), RE_OPT)
    proyectos = filas_con_id(cuerpo("portafolio"), RE_PROY)
    kpis = {}
    for encabezado, filas in tablas(cuerpo("indicadores")):
        for fila in filas:
            for c in fila:
                m = re.fullmatch(r"\**(" + RE_KPI + r")\**", c)
                if m:
                    kpis[m.group(1)] = (encabezado, fila)
    riesgos = filas_con_id(cuerpo("riesgos"), RE_RIESGO)
    evid_def = set(re.findall(r"^\|\s*((?:PUB|PRV|INT)-\d{3})\s*\|", registro, re.M))

    print("# Informe de trazabilidad del PETI\n")
    print(f"Archivo: `{os.path.relpath(ruta_peti, RAIZ)}`\n")
    print("## Conteo\n")
    print("| Elemento | Definidos |\n|---|---|")
    for nombre, d in [("Brechas", brechas), ("Oportunidades", oportunidades),
                      ("Proyectos", proyectos), ("Indicadores", kpis),
                      ("Riesgos", riesgos)]:
        print(f"| {nombre} | {len(d)} |")
    print(f"| Evidencias en el registro | {len(evid_def)} |")
    print()

    hallazgos = []

    # Brechas y oportunidades -> proyectos
    atendidas = {}
    sin_origen = []
    for pid, (enc, fila) in proyectos.items():
        refs = re.findall(RE_BRE + "|" + RE_OPT, columna(enc, fila, "brecha") or " ".join(fila[1:]))
        for r in refs:
            atendidas.setdefault(r, []).append(pid)
        if not refs:
            sin_origen.append(pid)
    for bid in brechas:
        if bid not in atendidas:
            hallazgos.append(("Alta", f"{bid} no tiene proyecto que la atienda (§13)."))
    for oid in oportunidades:
        if oid not in atendidas:
            hallazgos.append(("Media", f"{oid} no tiene proyecto que la desarrolle (§13)."))
    for pid in sin_origen:
        hallazgos.append(("Media", f"{pid} no declara brecha ni oportunidad de origen."))

    # IDs referenciados sin definir
    for patron, definidos, nombre in [(RE_BRE, brechas, "brecha"), (RE_OPT, oportunidades, "oportunidad")]:
        for ref in sorted(set(re.findall(patron, texto)) - set(definidos)):
            hallazgos.append(("Alta", f"{ref} se menciona pero no está definida como {nombre}."))
    evid_usadas = set(re.findall(RE_EVID, texto))
    for ref in sorted(evid_usadas - evid_def):
        hallazgos.append(("Alta", f"{ref} se cita en el PETI pero no existe en el registro de evidencias."))
    for ref in sorted(evid_def - evid_usadas):
        hallazgos.append(("Baja", f"{ref} está en el registro pero el PETI no la cita."))

    # AS-IS sin evidencia
    asis = cuerpo("asis")
    vinetas = [l for l in asis.splitlines() if re.match(r"^\s*[-*]\s+", l)]
    sin_id = [l for l in vinetas if not re.search(RE_EVID, l)]
    if vinetas:
        hallazgos.append(("Alta" if sin_id else "Baja",
                          f"§9 AS-IS: {len(sin_id)} de {len(vinetas)} afirmaciones en viñeta no llevan ID de evidencia."))

    # Indicadores y riesgos sin vínculo
    fuera_14 = texto.replace(cuerpo("indicadores"), "")
    for kid in kpis:
        if kid not in fuera_14:
            hallazgos.append(("Media", f"{kid} no se vincula con ningún proyecto, brecha u objetivo fuera del §14."))
    proyectos_con_kpi = [p for p in proyectos if re.search(RE_KPI, " ".join(proyectos[p][1]))]
    if proyectos and not proyectos_con_kpi:
        hallazgos.append(("Media", "Ningún proyecto del §13 declara el indicador (KPI) con el que se mide."))
    for rid, (enc, fila) in riesgos.items():
        if not re.search(RE_PROY + "|" + RE_BRE, " ".join(fila)):
            hallazgos.append(("Baja", f"{rid} no referencia el proyecto o la brecha que lo trata."))

    # Dominios cubiertos por las brechas
    por_dominio = {d: 0 for d in DOMINIOS}
    for enc, fila in brechas.values():
        celda = normalizar(columna(enc, fila, "dominio"))
        for d in {clasificar_dominio(parte) for parte in celda.split("/")} - {None}:
            por_dominio[d] += 1
    vacios = [d for d, n in por_dominio.items() if n == 0]
    if vacios:
        hallazgos.append(("Media", "Dominios sin ninguna brecha: " + ", ".join(vacios) + "."))

    # Columnas del Anexo 1
    requisitos = [
        (brechas, "Brechas (Anexo 1, Act. 11)", ["accion", "justificacion/descripcion", "tiempo", "costo"]),
        (proyectos, "Portafolio (Anexo 1, Act. 13)",
         ["dominio", "objetivo estrategico de ti/objetivo de ti", "meta", "area lider/responsable",
          "tiempo/meses", "costo/presupuesto", "brecha"]),
        (kpis, "Indicadores (Anexo 1, Act. 14B)",
         ["formula", "frecuencia", "origen/fuente", "responsable", "meta", "rango/umbral", "linea base"]),
    ]
    for definidos, nombre, req in requisitos:
        encabezados = {tuple(enc) for enc, _ in definidos.values()}
        faltan = set()
        for enc in encabezados:
            faltan.update(falta_columnas(list(enc), req))
        if faltan:
            hallazgos.append(("Alta", f"{nombre}: faltan columnas " + ", ".join(sorted(faltan)) + "."))

    # README
    if os.path.exists(README):
        readme = leer(README)
        for patron, real, nombre in [(r"(\d+)\s+brechas", len(brechas), "brechas"),
                                     (r"(\d+)\s+proyectos", len(proyectos), "proyectos")]:
            for m in re.finditer(patron, readme):
                if int(m.group(1)) != real:
                    hallazgos.append(("Baja", f"README dice {m.group(1)} {nombre}; el PETI tiene {real}."))

    orden = {"Alta": 0, "Media": 1, "Baja": 2}
    hallazgos.sort(key=lambda h: orden[h[0]])
    print("## Hallazgos\n")
    if not hallazgos:
        print("Sin hallazgos.")
    else:
        print("| # | Severidad | Hallazgo |\n|---|---|---|")
        for i, (sev, txt) in enumerate(hallazgos, 1):
            print(f"| T-{i:02d} | {sev} | {txt} |")
    print("\n## Matriz brecha → proyectos\n")
    print("| Brecha / oportunidad | Proyectos |\n|---|---|")
    for bid in list(brechas) + list(oportunidades):
        print(f"| {bid} | {', '.join(atendidas.get(bid, [])) or '—'} |")
    print("\n## Brechas por dominio\n")
    print("| Dominio | Brechas |\n|---|---|")
    for d, n in por_dominio.items():
        print(f"| {d} | {n} |")


if __name__ == "__main__":
    main()
