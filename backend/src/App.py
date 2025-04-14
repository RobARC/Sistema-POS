from flask import Flask,request, jsonify
from ConnectDB import get_connection, init_db
from data_productos import get_products
from data_clientes import get_clientes
from routes.auth import login
from populate_db import fill_products, fill_clients
import os
from utils.compra import guardar_compra_en_bd

app = Flask(__name__)

# Inicializamos la base de datos al iniciar
init_db()
fill_products()   # Llena tabla productos
fill_clients()    # Llena tabla clientes

@app.route('/login', methods=['POST'])
def get_login():
    print('llegue al login')
    return login()

@app.route('/api/products', methods=['GET'])
def get_products_api():
    return get_products()

@app.route('/api/clientes', methods=['GET'])
def get_clientes_api():
    return get_clientes()

@app.route('/api/compra', methods=['POST'])
def update_puntos_api():
    return guardar_compra_en_bd()


if __name__ == '__main__':
     app.run(host=os.getenv('API_HOST'), port=os.getenv('API_PORT'), debug=True)