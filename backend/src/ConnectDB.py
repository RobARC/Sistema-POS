import sqlite3
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    conn = sqlite3.connect("sistemaPOS.db")
    conn.row_factory = sqlite3.Row  # Para acceder por nombre a las columnas
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    # Tabla de usuarios
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    """)
     # Tabla de productos
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            price REAL NOT NULL,
            description TEXT,
            category TEXT,
            image TEXT,
            rating_rate REAL,
            rating_count INTEGER
        )
    """)

     # Tabla de clientes
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        username TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        street TEXT,
        suite TEXT,
        city TEXT,
        zipcode TEXT,
        lat TEXT,
        lng TEXT,
        phone TEXT,
        website TEXT,
        company_name TEXT,
        catch_phrase TEXT,
        bs TEXT,
        puntos_fidelizacion INTEGER DEFAULT 0
    )
""")
    conn.commit()
    conn.close()