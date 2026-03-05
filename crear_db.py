import sqlite3


def crear_base_datos():
    conexion = sqlite3.connect("carlend.db")
    cursor = conexion.cursor()

    sql_tablas = """
    CREATE TABLE IF NOT EXISTS vehiculos (
        id_vehiculo INTEGER PRIMARY KEY AUTOINCREMENT,
        marca TEXT NOT NULL,
        modelo TEXT NOT NULL,
        precio_dia REAL NOT NULL,
        imagen_url TEXT,
        ciudad TEXT NOT NULL,
        plazas INTEGER NOT NULL,
        categoria TEXT NOT NULL,
        disponible INTEGER DEFAULT 1
    );

    CREATE TABLE IF NOT EXISTS usuarios (
        id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_completo TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        tipo_cuenta TEXT DEFAULT 'PERSONAL',
        centro_coste TEXT,
        limite_gasto REAL DEFAULT 0.0,
        mfa_enabled BOOLEAN DEFAULT 0,
        telefono TEXT,
        dni_documento TEXT,
        carnet_valido_hasta DATE
    );

    CREATE TABLE IF NOT EXISTS sesiones (
        id_sesion INTEGER PRIMARY KEY AUTOINCREMENT,
        id_usuario INTEGER,
        dispositivo TEXT,
        ubicacion TEXT,
        fecha_acceso DATETIME DEFAULT CURRENT_TIMESTAMP,
        es_actual BOOLEAN DEFAULT 0,
        FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
    );

    CREATE TABLE IF NOT EXISTS metodos_pago (
        id_pago INTEGER PRIMARY KEY AUTOINCREMENT,
        id_usuario INTEGER,
        proveedor TEXT,
        numero_enmascarado TEXT,
        expiracion TEXT,
        token_pasarela TEXT,
        FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
    );

    CREATE TABLE IF NOT EXISTS reservas (
        id_reserva INTEGER PRIMARY KEY AUTOINCREMENT,
        id_usuario INTEGER,
        id_vehiculo INTEGER,
        tipo_seguro TEXT,
        franquicia_aplicada REAL,
        fecha_inicio DATETIME,
        fecha_fin DATETIME,
        punto_recogida TEXT,
        estado TEXT DEFAULT 'CONFIRMADA',
        total_pago REAL,
        id_metodo_pago INTEGER,
        FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
        FOREIGN KEY (id_vehiculo) REFERENCES vehiculos(id_vehiculo),
        FOREIGN KEY (id_metodo_pago) REFERENCES metodos_pago(id_pago)
    );

    CREATE TABLE IF NOT EXISTS tarjetas (
        id INTEGER PRIMARY KEY,
        usuario TEXT,
        numero TEXT,
        exp TEXT
    );
    """

    cursor.executescript(sql_tablas)
    conexion.commit()
    conexion.close()
    print("Base de datos 'carlend.db' creada/actualizada con tablas compatibles.")


if __name__ == "__main__":
    crear_base_datos()
