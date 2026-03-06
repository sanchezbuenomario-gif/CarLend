import sqlite3
import os

INSTANCE_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "instance")
DB_PATH = os.path.join(INSTANCE_PATH, "carlend.db")

class VehiculoModel:
    def __init__(self):
        self.db_path = DB_PATH

    def crear(self, marca, modelo, categoria, precio_dia, imagen_url=None, ciudad="Madrid",
              plazas=5, disponible=1, tipo_motor=None):
        with sqlite3.connect(self.db_path) as conexion:
            cursor = conexion.cursor()
            cursor.execute("""
                INSERT INTO vehiculos (marca, modelo, categoria, precio_dia, imagen_url, ciudad, plazas, disponible, tipo_motor)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (marca, modelo, categoria, precio_dia, imagen_url, ciudad, plazas, disponible, tipo_motor))
            return cursor.lastrowid

    def obtener_todos(self):
        with sqlite3.connect(self.db_path) as conexion:
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM vehiculos")
            return cursor.fetchall()

    def obtener_por_id(self, id_vehiculo):
        with sqlite3.connect(self.db_path) as conexion:
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM vehiculos WHERE id_vehiculo = ?", (id_vehiculo,))
            return cursor.fetchone()

    def actualizar(self, id_vehiculo, **kwargs):
        if not kwargs:
            return 0
        campos = []
        valores = []
        for k, v in kwargs.items():
            campos.append(f"{k} = ?")
            valores.append(v)
        valores.append(id_vehiculo)
        sql = f"UPDATE vehiculos SET {', '.join(campos)} WHERE id_vehiculo = ?"
        with sqlite3.connect(self.db_path) as conexion:
            cursor = conexion.cursor()
            cursor.execute(sql, tuple(valores))
            return cursor.rowcount

    def eliminar(self, id_vehiculo):
        with sqlite3.connect(self.db_path) as conexion:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM vehiculos WHERE id_vehiculo = ?", (id_vehiculo,))
            return cursor.rowcount