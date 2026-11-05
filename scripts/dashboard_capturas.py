"""Toma la captura completa de una instantánea de Grafana con Edge sin interfaz y la corta por filas del tablero.

Uso: python scripts/dashboard_capturas.py <url_instantanea> <carpeta_salida> <dashboard.json>

Los cortes salen de gridPos de las filas ("row") del tablero: cada unidad de alto de Grafana mide
30 px más 8 px de margen, con la ventana de 1600 px de ancho.
"""
import json
import subprocess
import sys
import tempfile
import time
from pathlib import Path

from PIL import Image

EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"


def main():
    url, salida, dash = sys.argv[1], Path(sys.argv[2]), json.loads(Path(sys.argv[3]).read_text(encoding="utf-8"))
    salida.mkdir(parents=True, exist_ok=True)
    total = max(p["gridPos"]["y"] + p["gridPos"]["h"] for p in dash["panels"])
    alto = 80 + total * 38 + 60
    completa = (salida / "dashboard_completo.png").resolve()
    completa.unlink(missing_ok=True)
    perfil = Path(tempfile.mkdtemp())
    subprocess.run([EDGE, "--headless=new", "--disable-gpu", "--hide-scrollbars", f"--user-data-dir={perfil}",
                    f"--window-size=1600,{alto}", "--virtual-time-budget=60000", f"--screenshot={completa}",
                    f"{url}?kiosk&theme=light"], timeout=240)
    for _ in range(60):
        if completa.exists() and completa.stat().st_size > 0:
            break
        time.sleep(1)
    time.sleep(1)
    img = Image.open(completa)
    filas = sorted((p["gridPos"]["y"], p["title"]) for p in dash["panels"] if p["type"] == "row")
    # Desplazamiento del primer panel: se mide buscando la primera fila no blanca bajo la barra superior
    origen = 48
    for i, (y, titulo) in enumerate(filas):
        y_fin = filas[i + 1][0] if i + 1 < len(filas) else total
        top, bottom = origen + y * 38, min(img.height, origen + y_fin * 38 + 4)
        img.crop((0, top, img.width, bottom)).save(salida / f"seccion_{i + 1}.png")
        print(f"seccion_{i + 1}.png  {titulo}")


if __name__ == "__main__":
    main()
