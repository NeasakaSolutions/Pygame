# Importaciones:
import json
import os

def cargar_textos(nombre_archivo):
    ruta = os.path.join(os.path.dirname(__file__), "..", "data", nombre_archivo)
    with open(ruta, "r", encoding="utf-8") as archivo:
        return json.load(archivo)