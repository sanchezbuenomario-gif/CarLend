import sqlite3

def ejecutar_script():
    try:
        # Nos conectamos a tu base de datos
        conexion = sqlite3.connect('carlend.db')
        cursor = conexion.cursor()

        # Aquí pegamos todo el código que te dio el asistente
        script_sql = """
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



        INSERT INTO vehiculos (marca, modelo, precio_dia, imagen_url, ciudad, plazas, categoria, disponible) VALUES
        ('Tesla', 'Model 3', 85.0, 'tesla-model3.jpg', 'Madrid', 5, 'electrico', 1),
        ('Seat', 'Ibiza', 35.0, 'seat-ibiza.jpg', 'Madrid', 5, 'economico', 1),
        ('BMW', 'Serie 1', 60.0, 'bmw-serie1.jpg', 'Barcelona', 5, 'compacto', 1),
        ('Audi', 'A3', 62.0, 'audi-a3.jpg', 'Sevilla', 5, 'compacto', 1),
        ('Mercedes', 'Clase C', 95.0, 'mercedes-clasec.jpg', 'Madrid', 5, 'premium', 1),
        ('Volkswagen', 'Golf', 52.0, 'vw-golf.jpg', 'Sevilla', 5, 'compacto', 1),
        ('Renault', 'Clio', 34.0, 'renault-clio.jpg', 'Bilbao', 5, 'economico', 1),
        ('Peugeot', '208', 36.0, 'peugeot-208.jpg', 'Bilbao', 5, 'economico', 1),
        ('Hyundai', 'Tucson', 68.0, 'hyundai-tucson.jpg', 'Madrid', 5, 'suv', 1),
        ('Kia', 'Sportage', 66.0, 'kia-sportage.jpg', 'Barcelona', 5, 'suv', 1),
        ('Toyota', 'Corolla', 48.0, 'toyota-corolla.jpg', 'Valencia', 5, 'hibrido', 1),
        ('Nissan', 'Qashqai', 64.0, 'nissan-qashqai.jpg', 'Sevilla', 5, 'suv', 1),
        ('Ford', 'Focus', 45.0, 'ford-focus.jpg', 'Madrid', 5, 'compacto', 1),
        ('Opel', 'Corsa', 33.0, 'opel-corsa.jpg', 'Valencia', 5, 'economico', 1),
        ('Citroen', 'C3', 32.0, 'citroen-c3.jpg', 'Madrid', 5, 'economico', 1),
        ('Skoda', 'Octavia', 49.0, 'skoda-octavia.jpg', 'Sevilla', 5, 'familiar', 1),
        ('Volvo', 'XC60', 105.0, 'volvo-xc60.jpg', 'Madrid', 5, 'premium', 1),
        ('Mazda', 'CX-5', 72.0, 'mazda-cx5.jpg', 'Barcelona', 5, 'suv', 1),
        ('Fiat', '500', 31.0, 'fiat-500.jpg', 'Valencia', 4, 'urbano', 1),
        ('Mini', 'Cooper', 58.0, 'mini-cooper.jpg', 'Madrid', 4, 'urbano', 1),
        ('Jeep', 'Compass', 74.0, 'jeep-compass.jpg', 'Sevilla', 5, 'suv', 1),
        ('Honda', 'Civic', 50.0, 'honda-civic.jpg', 'Bilbao', 5, 'compacto', 1),
        ('Lexus', 'UX 250h', 88.0, 'lexus-ux250h.jpg', 'Madrid', 5, 'hibrido', 1),
        ('Cupra', 'Formentor', 78.0, 'cupra-formentor.jpg', 'Barcelona', 5, 'deportivo', 1),
        ('Dacia', 'Duster', 55.0, 'dacia-duster.jpg', 'Valencia', 5, 'suv', 1),
        ('Alfa Romeo', 'Giulia', 92.0, 'alfa-giulia.jpg', 'Madrid', 5, 'premium', 1),
        ('Subaru', 'Outback', 81.0, 'subaru-outback.jpg', 'Sevilla', 5, 'familiar', 1),
        ('Mitsubishi', 'Eclipse Cross', 67.0, 'mitsubishi-eclipsecross.jpg', 'Bilbao', 5, 'suv', 1),
        ('Porsche', 'Macan', 140.0, 'porsche-macan.jpg', 'Bilbao', 5, 'premium', 1),
        ('Tesla', 'Model Y', 110.0, 'tesla-modely.jpg', 'Madrid', 5, 'electrico', 1),
        ('MINI', 'Electric Cooper SE', 35.0, 'Mini-SE.jpg', 'Madrid', 2, 'electrico', 1),
        ('Ford', 'Expedition', 65.0, 'Ford-Expedition.jpg', 'Madrid', 7, 'suv', 1),
        ('BMW', 'M3 Competition', 120.0, 'BMW-Serie 3.jpg', 'Madrid', 4, 'deportivo', 1),
        ('Ferrari', '488 GTB', 150.0, 'Ferrari-488.jpg', 'Madrid', 2, 'deportivo', 1),
        ('Porsche', '911 Carrera', 140.0, 'Porsche-911.jpg', 'Madrid', 2, 'deportivo', 1);

        INSERT INTO usuarios (nombre_completo, email, password)
        VALUES ('Juan Perez', 'juan@email.com', '12345');
        """

        # Ejecutamos todo el bloque
        cursor.executescript(script_sql)
        conexion.commit()
        print("¡Base de datos actualizada con 35 coches y nuevas tablas!")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        conexion.close()

if __name__ == "__main__":
    ejecutar_script()
