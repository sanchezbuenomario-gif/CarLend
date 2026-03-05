import json
import sqlite3


DB_PATH = "carlend.db"


def ensure_coches_table(cursor):
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS coches (
            id_coche INTEGER PRIMARY KEY AUTOINCREMENT,
            marca TEXT,
            modelo TEXT NOT NULL,
            categoria TEXT,
            precio_dia REAL NOT NULL,
            imagen_url TEXT,
            ciudad TEXT DEFAULT 'Madrid',
            plazas INTEGER DEFAULT 5,
            combustible TEXT DEFAULT 'gasolina',
            transmision TEXT DEFAULT 'manual',
            disponible INTEGER DEFAULT 1
        )
        """
    )

    cursor.execute("PRAGMA table_info(coches)")
    existentes = {row[1] for row in cursor.fetchall()}
    nuevas = [
        ("marca", "TEXT"),
        ("ciudad", "TEXT DEFAULT 'Madrid'"),
        ("plazas", "INTEGER DEFAULT 5"),
        ("combustible", "TEXT DEFAULT 'gasolina'"),
        ("transmision", "TEXT DEFAULT 'manual'"),
        ("disponible", "INTEGER DEFAULT 1"),
    ]
    for nombre, tipo in nuevas:
        if nombre not in existentes:
            cursor.execute(f"ALTER TABLE coches ADD COLUMN {nombre} {tipo}")


def cargar_datos():
    with open("vehiculos.json", "r", encoding="utf-8-sig") as f:
        vehiculos = json.load(f)

    extras_flota = [
        {
            "marca": "Ford",
            "modelo": "Ranger",
            "categoria": "suv",
            "precio_dia": 65.0,
            "imagen_url": "Ford-Ranger.jpg",
            "ciudad": "Madrid",
            "plazas": 7,
            "combustible": "gasolina",
            "transmision": "manual",
            "disponible": 1,
        },
    ]

    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
    ensure_coches_table(cursor)

    cursor.execute("DELETE FROM vehiculos")
    cursor.executemany(
        """
        INSERT INTO vehiculos (
            id_vehiculo, marca, modelo, precio_dia, imagen_url, ciudad, plazas, categoria, disponible
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        [
            (
                v.get("id_vehiculo"),
                v.get("marca"),
                v.get("modelo"),
                v.get("precio_dia"),
                v.get("imagen_url"),
                v.get("ciudad"),
                v.get("plazas"),
                v.get("categoria"),
                v.get("disponible", 1),
            )
            for v in vehiculos
        ],
    )

    cursor.execute("DELETE FROM coches")
    cursor.executemany(
        """
        INSERT INTO coches (
            marca, modelo, categoria, precio_dia, imagen_url, ciudad, plazas, combustible, transmision, disponible
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        [
            (
                v.get("marca"),
                v.get("modelo"),
                v.get("categoria"),
                v.get("precio_dia"),
                v.get("imagen_url"),
                v.get("ciudad"),
                v.get("plazas"),
                "electrico" if v.get("categoria") == "electrico" else ("hibrido" if v.get("categoria") == "hibrido" else "gasolina"),
                "automatico",
                v.get("disponible", 1),
            )
            for v in vehiculos
        ]
        + [
            (
                c["marca"],
                c["modelo"],
                c["categoria"],
                c["precio_dia"],
                c["imagen_url"],
                c["ciudad"],
                c["plazas"],
                c["combustible"],
                c["transmision"],
                c["disponible"],
            )
            for c in extras_flota
        ],
    )

    conexion.commit()
    conexion.close()
    print(f"Datos insertados en vehiculos: {len(vehiculos)}")
    print(f"Datos insertados en coches: {len(vehiculos) + len(extras_flota)}")


if __name__ == "__main__":
    cargar_datos()
