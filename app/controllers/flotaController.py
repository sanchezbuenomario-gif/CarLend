from flask import render_template, jsonify
from models.vehiculosModel import VehiculoModel
import random

vehiculo_model = VehiculoModel()

def register_flota_routes(app):
    
    @app.route('/flota')
    def flota():
        vehiculos_db = [dict(v) for v in vehiculo_model.obtener_todos() if v["disponible"] == 1]
        vehiculos = [
            {
                "id_vehiculo": v["id_vehiculo"],
                "marca": v["marca"],
                "modelo": v["modelo"],
                "precio": v.get("precio_dia", 0),
                "imagen": v.get("imagen_url", "default.jpg"),
                "ciudad": v.get("ciudad", "Madrid"),
                "pasajeros": v.get("plazas", 5),
                "categoria": v.get("categoria", "economico"),
                "disponible": v.get("disponible", 1),
                "transmision": v.get("transmision", "automatico"),
                "tipo_motor": v.get("tipo_motor", "gasolina")
            }
            for v in vehiculos_db
        ]
        return render_template('flota.html', vehiculos=vehiculos)

    @app.route('/api/vehiculos_destacados')
    def vehiculos_destacados():
        vehiculos = [v for v in vehiculo_model.obtener_todos() if v["disponible"] == 1]
        vehiculos_aleatorios = random.sample(vehiculos, min(5, len(vehiculos)))
        return jsonify([
            {
                "id_vehiculo": v["id_vehiculo"],
                "marca": v["marca"],
                "modelo": v["modelo"],
                "precio": v["precio_dia"],
                "imagen": v["imagen_url"],
                "ciudad": v["ciudad"],
                "plazas": v["plazas"],
                "categoria": v["categoria"]
            }
            for v in vehiculos_aleatorios
        ])
    