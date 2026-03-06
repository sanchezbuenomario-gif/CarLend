CREATE TABLE IF NOT EXISTS vehiculos (
    id_vehiculo INTEGER PRIMARY KEY AUTOINCREMENT,
    marca TEXT NOT NULL,
    modelo TEXT NOT NULL,
    precio_dia REAL NOT NULL,
    imagen_url TEXT,
    ciudad TEXT NOT NULL DEFAULT 'Madrid',
    plazas INTEGER NOT NULL DEFAULT 5,
    categoria TEXT NOT NULL,
    disponible INTEGER DEFAULT 1,
    tipo_motor TEXT
);
