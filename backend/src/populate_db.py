import sqlite3
import requests
from ConnectDB import get_connection, init_db  
import os

URL_PRODUCTS = os.getenv('URL_API_PRODUCTS')
URL_CLIENTS = os.getenv('URL_API_CLIENTS')

def fill_products():
   
    response = requests.get(URL_PRODUCTS)
    products = response.json()

    conn = get_connection()
    cursor = conn.cursor()

    # Verificar si ya hay productos
    cursor.execute("SELECT COUNT(*) FROM products")
    productos_count = cursor.fetchone()[0]
    
    if productos_count == 0:
        print("Llenando tabla de productos...")
        for product in products:
            rating = product.get("rating", {})
            cursor.execute("""
                INSERT INTO products (title, price, description, category, image, rating_rate, rating_count)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                product["title"],
                product["price"],
                product["description"],
                product["category"],
                product["image"],
                rating.get("rate"),
                rating.get("count")
            ))

        conn.commit()
        conn.close()
        print("Productos insertados correctamente.")
    else:
        print("La tabla de productos ya tiene datos. No se insertaron nuevos productos.")
        

def fill_clients():
   
    response = requests.get(URL_CLIENTS)
    users = response.json()

    conn = get_connection()
    cursor = conn.cursor()
    

    # Verificar si ya hay clientes
    cursor.execute("SELECT COUNT(*) FROM clientes")
    clientes_count = cursor.fetchone()[0]

    if clientes_count == 0:

        print("Llenando tabla de clientes...")

        for user in users:
            address = user.get("address", {})
            geo = address.get("geo", {})
            company = user.get("company", {})  
            data = (user.get("name", ""),
                    user.get("username", ""),
                    user.get("email", ""),
                    address.get("street", ""),
                    address.get("suite", ""),
                    address.get("city", ""),
                    address.get("zipcode", ""),
                    geo.get("lat", ""),
                    geo.get("lng", ""),
                    user.get("phone", ""),
                    user.get("website", ""),
                    company.get("name", ""),
                    company.get("catchPhrase", ""),
                    company.get("bs", ""),
                    0  # puntos de fidelización inicial
            ) 


            cursor.execute("""
                INSERT OR IGNORE INTO clientes (
                    name, username, email, street, suite, city, zipcode,
                    lat, lng, phone, website,
                    company_name, catch_phrase, bs,
                    puntos_fidelizacion
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, 
          data
            )

        conn.commit()
        conn.close()
        print("Clientes insertados correctamente.")
    else:
        print("La tabla de clientes ya tiene datos. No se insertaron nuevos clientes.")