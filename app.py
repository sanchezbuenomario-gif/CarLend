import json
import sqlite3
from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime

DB_NAME = 'carlend.db'

class CarLendAPI(BaseHTTPRequestHandler):
    
    def _set_headers(self, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_OPTIONS(self):
        self._set_headers()

    # --- READ: Ver flota ---
    def do_GET(self):
        if self.path == '/api/coches':
            conn = sqlite3.connect(DB_NAME)
            conn.row_factory = sqlite3.Row
            coches = [dict(row) for row in conn.execute('SELECT * FROM coches').fetchall()]
            conn.close()
            self._set_headers(200)
            self.wfile.write(json.dumps(coches).encode())

    # --- CREATE & LOGIN ---
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = json.loads(self.rfile.read(content_length))
        
        if self.path == '/api/coches':
            conn = sqlite3.connect(DB_NAME)
            conn.execute('INSERT INTO coches (marca, modelo, disponible, imagen_url) VALUES (?, ?, 1, ?)',
                       (post_data['marca'], post_data['modelo'], post_data['imagen_url']))
            conn.commit()
            conn.close()
            self._set_headers(201)
            self.wfile.write(json.dumps({"msg": "Coche creado"}).encode())

    # --- UPDATE: Marcar como reservado o editar datos ---
    def do_PUT(self):
        if self.path.startswith('/api/coches/'):
            id_coche = self.path.split('/')[-1]
            content_length = int(self.headers['Content-Length'])
            data = json.loads(self.rfile.read(content_length))
            
            conn = sqlite3.connect(DB_NAME)
            # Ejemplo: Actualizamos el estado de disponibilidad
            conn.execute('UPDATE coches SET disponible = ? WHERE id = ?', (data['disponible'], id_coche))
            conn.commit()
            conn.close()
            
            self._set_headers(200)
            self.wfile.write(json.dumps({"msg": f"Coche {id_coche} actualizado"}).encode())

    # --- DELETE: Eliminar coche de la flota ---
    def do_DELETE(self):
        if self.path.startswith('/api/coches/'):
            id_coche = self.path.split('/')[-1]
            
            conn = sqlite3.connect(DB_NAME)
            conn.execute('DELETE FROM coches WHERE id = ?', (id_coche,))
            conn.commit()
            conn.close()
            
            self._set_headers(200)
            self.wfile.write(json.dumps({"msg": f"Coche {id_coche} eliminado"}).encode())

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = json.loads(self.rfile.read(content_length))
        
        # --- NUEVA RUTA: GESTIÓN DE RESERVAS ---
        if self.path == '/api/reservar':
            try:
                # 1. Obtener datos de la reserva
                coche_id = post_data['coche_id']
                fecha_inicio = datetime.strptime(post_data['inicio'], '%Y-%m-%d')
                fecha_fin = datetime.strptime(post_data['fin'], '%Y-%m-%d')
                
                # 2. Calcular días (mínimo 1 día)
                dias = (fecha_fin - fecha_inicio).days
                if dias <= 0: dias = 1
                
                # 3. Consultar el precio diario del coche en la DB del compañero
                conn = sqlite3.connect(DB_NAME)
                cursor = conn.cursor()
                cursor.execute('SELECT precio_dia FROM coches WHERE id = ?', (coche_id,))
                resultado = cursor.fetchone()
                
                if resultado:
                    precio_total = resultado[0] * dias
                    
                    # 4. Registrar la reserva y marcar coche como NO disponible
                    conn.execute('''INSERT INTO reservas (coche_id, fecha_inicio, fecha_fin, precio_total) 
                                   VALUES (?, ?, ?, ?)''', (coche_id, post_data['inicio'], post_data['fin'], precio_total))
                    conn.execute('UPDATE coches SET disponible = 0 WHERE id = ?', (coche_id,))
                    conn.commit()
                    
                    self._set_headers(201)
                    self.wfile.write(json.dumps({
                        "status": "success",
                        "dias": dias,
                        "precio_total": precio_total,
                        "mensaje": "Reserva confirmada"
                    }).encode())
                else:
                    self._set_headers(404)
                    self.wfile.write(json.dumps({"error": "Coche no encontrado"}).encode())
                conn.close()

            except Exception as e:
                self._set_headers(400)
                self.wfile.write(json.dumps({"error": str(e)}).encode())

if __name__ == '__main__':
    print("Servidor CarLend (CRUD Completo) en puerto 5000...")
    HTTPServer(('localhost', 5000), CarLendAPI).serve_forever()