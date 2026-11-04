"""Ejecuta en Python la priorización del mapa de calor (macro `vecinos`) de la herramienta del MinTIC.

La macro lee un botón ActiveX ("1, 2 o 3 Iniciativas") que Office no carga en un libro abierto por
automatización, así que no se puede correr desde un script. En lugar de reescribir el algoritmo, este
módulo saca el código VBA original del .xlsm (vbaProject.bin: contenedor OLE con compresión MS-OVBA),
toma la rama de la opción elegida y la traduce línea por línea a Python. Las celdas se emulan con las
reglas de VBA que el código usa: una celda vacía es `Empty`, vale 0 en sumas y comparaciones,
IsNumeric(Empty) es verdadero y Empty = "" también.

Uso como módulo: priorizar(xlsm, procesos, areas, matriz, iniciativas=3) -> lista de resultados.
"""
import re
import struct
import zipfile


# --- Lectura del proyecto VBA ---------------------------------------------------------------------

def _leer_cfb(data):
    ss = 1 << struct.unpack_from("<H", data, 30)[0]
    mss = 1 << struct.unpack_from("<H", data, 32)[0]
    n_fat, dir_start = struct.unpack_from("<II", data, 44)
    mini_cutoff, minifat_start, n_minifat, difat_start, n_difat = struct.unpack_from("<IIIII", data, 56)

    def sector(i):
        return data[512 + i * ss: 512 + (i + 1) * ss]

    difat = list(struct.unpack_from("<109I", data, 76))
    s = difat_start
    for _ in range(n_difat):
        vals = struct.unpack_from(f"<{ss // 4}I", sector(s))
        difat.extend(vals[:-1])
        s = vals[-1]
    fat = []
    for d in difat[:n_fat]:
        fat.extend(struct.unpack_from(f"<{ss // 4}I", sector(d)))

    def cadena(inicio):
        out, s = b"", inicio
        while s < 0xFFFFFFFA:
            out += sector(s)
            s = fat[s]
        return out

    dirs = cadena(dir_start)
    entradas = []
    for i in range(len(dirs) // 128):
        e = dirs[i * 128:(i + 1) * 128]
        nlen = struct.unpack_from("<H", e, 64)[0]
        entradas.append(dict(
            nombre=e[:max(nlen - 2, 0)].decode("utf-16-le", "ignore"), tipo=e[66],
            start=struct.unpack_from("<I", e, 116)[0], size=struct.unpack_from("<Q", e, 120)[0]))
    ministream = cadena(entradas[0]["start"])
    minifat = []
    if n_minifat:
        mf = cadena(minifat_start)
        minifat = list(struct.unpack_from(f"<{len(mf) // 4}I", mf))

    def leer(e):
        if e["size"] < mini_cutoff:
            out, s = b"", e["start"]
            while s < 0xFFFFFFFA:
                out += ministream[s * mss:(s + 1) * mss]
                s = minifat[s]
            return out[:e["size"]]
        return cadena(e["start"])[:e["size"]]

    return [leer(e) for e in entradas if e["tipo"] == 2]


def _descomprimir(buf, pos):
    if buf[pos] != 1:
        raise ValueError
    pos += 1
    out = bytearray()
    while pos < len(buf):
        hdr = struct.unpack_from("<H", buf, pos)[0]
        if (hdr >> 12) & 7 != 3:
            raise ValueError
        fin = min(pos + (hdr & 0x0FFF) + 3, len(buf))
        pos += 2
        inicio = len(out)
        if not hdr & 0x8000:
            out += buf[pos:pos + 4096]
            pos = fin
            continue
        while pos < fin:
            flags = buf[pos]
            pos += 1
            for bit in range(8):
                if pos >= fin:
                    break
                if not (flags >> bit) & 1:
                    out.append(buf[pos])
                    pos += 1
                    continue
                tok = struct.unpack_from("<H", buf, pos)[0]
                pos += 2
                bits = max((len(out) - inicio - 1).bit_length(), 4)
                largo = (tok & (0xFFFF >> bits)) + 3
                desp = (tok >> (16 - bits)) + 1
                for _ in range(largo):
                    out.append(out[-desp])
    return bytes(out)


def codigo_macro(xlsm, sub="vecinos"):
    """Devuelve el texto del módulo VBA que contiene `Sub <sub>()`."""
    data = zipfile.ZipFile(xlsm).read("xl/vbaProject.bin")
    marca = f"Sub {sub}()".encode()
    for buf in _leer_cfb(data):
        for i in range(len(buf)):
            if buf[i] != 1:
                continue
            try:
                texto = _descomprimir(buf, i)
            except Exception:
                continue
            if b"Attribute VB_Name" in texto[:200]:
                if marca in texto:
                    return texto.decode("cp1252")
                break
    raise ValueError(f"No se encontró Sub {sub}() en {xlsm}")


# --- Traducción de la rama ------------------------------------------------------------------------

class _Vacio:
    """Empty de VBA."""

    def _n(self, o):
        return 0 if o is VACIO else o

    def __eq__(self, o):
        return o is VACIO or o == "" or o == 0

    def __hash__(self):
        return 0

    def __add__(self, o):
        return 0 + self._n(o)

    __radd__ = __add__

    def __ge__(self, o):
        return 0 >= self._n(o)

    def __le__(self, o):
        return 0 <= self._n(o)

    def __gt__(self, o):
        return 0 > self._n(o)

    def __lt__(self, o):
        return 0 < self._n(o)


VACIO = _Vacio()


def _es_numero(x):
    if x is VACIO or isinstance(x, (int, float)):
        return True
    try:
        float(str(x).replace(",", "."))
        return True
    except ValueError:
        return False


def _num(x):
    return 0 if x is VACIO else x


def _comparar(a, op, b):
    # Números y textos no se comparan como iguales en VBA; Empty vale 0 o "".
    if a is VACIO or b is VACIO:
        izq, der = (VACIO, b) if a is VACIO else (VACIO, a)
        if op == "==":
            return izq == der
        if op == "!=":
            return not (izq == der)
    if isinstance(a, str) != isinstance(b, str) and a is not VACIO and b is not VACIO:
        return op == "!="
    a, b = _num(a), _num(b)
    return {"==": a == b, "!=": a != b, ">=": a >= b, "<=": a <= b, ">": a > b, "<": a < b}[op]


def _expresion(e):
    e = e.replace("Cells(", "C(").replace("IsNumeric(", "isnum(")
    e = re.sub(r"\bAnd\b", "and", e)
    e = re.sub(r"\bOr\b", "or", e)
    e = re.sub(r"\bNot\b", "not", e)
    # Comparaciones simples "A op B" dentro de una condición: se envuelven para aplicar las reglas de VBA.
    operando = r"(C\([^()]*\)|isnum\(C\([^()]*\)\)|[A-Za-z_][A-Za-z0-9_]*|\"\"|-?\d+(?:\.\d+)?)"
    e = re.sub(operando + r"\s*(<>|>=|<=|=|>|<)\s*" + operando,
               lambda m: f"cmp({m.group(1)}, {repr({'=': '==', '<>': '!='}.get(m.group(2), m.group(2)))}, {m.group(3)})",
               e)
    return e


def traducir(lineas):
    py, nivel = [], 0
    for cruda in lineas:
        l = cruda.strip()
        if not l or l.startswith("'"):
            continue
        sangria = "    " * nivel
        if m := re.fullmatch(r"If (.+) Then", l):
            py.append(f"{sangria}if {_expresion(m.group(1))}:")
            nivel += 1
        elif m := re.fullmatch(r"ElseIf (.+) Then", l):
            py.append(f"{sangria}pass")   # por si el bloque anterior quedó vacío
            py.append(f"{'    ' * (nivel - 1)}elif {_expresion(m.group(1))}:")
        elif l == "Else":
            py.append(f"{sangria}pass")
            py.append(f"{'    ' * (nivel - 1)}else:")
        elif l == "End If":
            py.append(f"{sangria}pass")
            nivel -= 1
        elif m := re.fullmatch(r"For (\w+) = (.+) To (.+)", l):
            py.append(f"{sangria}for {m.group(1)} in range({_expresion(m.group(2))}, {_expresion(m.group(3))} + 1):")
            nivel += 1
        elif re.fullmatch(r"Next( \w+)?", l):
            py.append(f"{sangria}pass")
            nivel -= 1
        elif m := re.fullmatch(r"(\w+) = (.+)", l):
            py.append(f"{sangria}{m.group(1)} = {_expresion(m.group(2))}")
        else:
            raise ValueError(f"Instrucción VBA no prevista: {l}")
    if nivel:
        raise ValueError("Bloques VBA sin cerrar")
    return "\n".join(py)


def rama(codigo, iniciativas):
    lineas = codigo.splitlines()
    inicio = next(i for i, l in enumerate(lineas)
                  if re.search(rf'If Sheets\("Heatmap"\)\.OptionButton{iniciativas}\.Value = True Then', l))
    fin = next(i for i in range(inicio + 1, len(lineas)) if lineas[i].strip().startswith("'impresi"))
    return lineas[inicio + 1:fin]


def priorizar(xlsm, procesos, areas, matriz, iniciativas=3):
    """Corre la rama de la macro sobre la matriz. Devuelve [(proceso, área, valor, índice), …]."""
    # Botón → rama del código: OptionButton1 = 1 iniciativa, OptionButton2 = 2, OptionButton3 = 3.
    codigo = traducir(rama(codigo_macro(xlsm), iniciativas))
    celdas = {}
    for j, p in enumerate(procesos):
        celdas[(5, 5 + j)] = p
    for i, a in enumerate(areas):
        celdas[(6 + i, 3)] = i + 1
        celdas[(6 + i, 4)] = a
        for j in range(len(procesos)):
            celdas[(6 + i, 5 + j)] = matriz[i][j]
    entorno = {"C": lambda r, c: celdas.get((r, c), VACIO), "isnum": _es_numero, "cmp": _comparar,
               "alto": len(areas), "largo": len(procesos),
               "max": 0, "max2": 0, "max3": 0, "maxvecino": 0, "maxvecino2": 0}
    for nombre in set(re.findall(r"^\s*(\w+) = ", codigo, re.M)) - set(entorno):
        entorno[nombre] = VACIO
    exec(codigo, entorno)
    sufijos = ["", "2", "3"][:iniciativas]
    return [(entorno["maxproceso" + s], entorno["maxdepartamento" + s], _num(entorno["max" + s]),
             _num(entorno["maxvecino" + s])) for s in sufijos]
