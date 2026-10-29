"""Saca las fotos de referencia que Codex tiene que rediseñar.

Uso (desde la raíz del repo):
    python3 pendientes-codex/extraer_referencias.py            # todo
    python3 pendientes-codex/extraer_referencias.py --prioridad 1

Lee pendientes-codex/lista.json y escribe cada foto actual de la galería en
pendientes-codex/referencias/<slug>/<slug>-color-NN.jpg (esa carpeta no se sube).
"""
import base64
import io
import json
import os
import sys

from PIL import Image

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SALIDA = os.path.join(RAIZ, "pendientes-codex", "referencias")


def cargar(img):
    if img.startswith("data:"):
        return Image.open(io.BytesIO(base64.b64decode(img.split(",", 1)[1])))
    return Image.open(os.path.join(RAIZ, img.split("?")[0]))


def guardar(im, ruta):
    im = im.convert("RGBA")
    fondo = Image.new("RGBA", im.size, (255, 255, 255, 255))
    fondo.alpha_composite(im)
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    fondo.convert("RGB").save(ruta, quality=92)


def main():
    solo = None
    if "--prioridad" in sys.argv:
        solo = int(sys.argv[sys.argv.index("--prioridad") + 1])
    lista = json.load(open(os.path.join(RAIZ, "pendientes-codex", "lista.json"), encoding="utf-8"))
    total = 0
    for item in lista["galerias"]:
        if solo and item["prioridad"] != solo:
            continue
        galeria = json.load(open(os.path.join(RAIZ, "m", item["slug"] + ".json"), encoding="utf-8"))
        for n in item["posiciones"]:
            nombre = f'{item["slug"]}-color-{n:02d}.jpg'
            guardar(cargar(galeria[n - 1]["img"]), os.path.join(SALIDA, item["slug"], nombre))
            total += 1
        for n in item.get("revisar", []):
            nombre = f'{item["slug"]}-color-{n:02d}.jpg'
            guardar(cargar(galeria[n - 1]["img"]), os.path.join(SALIDA, item["slug"], "revisar", nombre))
            total += 1
    for item in ([] if solo else lista["portadas"]):
        portada = json.load(open(os.path.join(RAIZ, "c", item["slug"] + ".json"), encoding="utf-8"))
        guardar(cargar(portada["img"]), os.path.join(SALIDA, "_portadas", item["slug"] + ".jpg"))
        total += 1
    print(f"{total} referencias en {SALIDA}")


if __name__ == "__main__":
    main()
