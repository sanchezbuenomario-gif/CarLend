import sqlite3
import os

INSTANCE_PATH = os.path.join(os.path.dirname(__file__), "../../instance")
DB_PATH = os.path.join(INSTANCE_PATH, "carlend.db")
SQL_FILE = os.path.join(os.path.dirname(__file__), "../data/vehiculos.sql")

def crear_base_datos():
    os.makedirs(INSTANCE_PATH, exist_ok=True)
    with sqlite3.connect(DB_PATH) as conn, open(SQL_FILE, "r", encoding="utf-8") as f:
        conn.executescript(f.read())
