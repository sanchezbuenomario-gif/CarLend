import json
import os
from models.vehiculosModel import VehiculoModel

BASE_DIR = os.path.dirname(__file__)
JSON_FILE = os.path.join(BASE_DIR, "../data/vehiculos.json")

vehiculo_model = VehiculoModel()

with open(JSON_FILE, "r", encoding="utf-8-sig") as f:
    vehiculos_json = json.load(f)

for v in vehiculos_json:
    vehiculo_model.crear(
        marca=v["marca"],
        modelo=v["modelo"],
        categoria=v["categoria"],
        precio_dia=v["precio"],
        imagen_url=v["imagen"],
        ciudad=v["ciudad"],
        plazas=v["pasajeros"],
        disponible=v["disponible"],
        tipo_motor=v["tipo_motor"]
    )