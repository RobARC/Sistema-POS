from flask import Flask, jsonify, request
from jwt import encode, decode, exceptions
from datetime import datetime, timedelta
import os
from ConnectDB import get_connection


def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""SELECT username, puntos_fidelizacion FROM clientes WHERE email = ? AND username = ?""", (email, password))
    user = cursor.fetchone()
    cursor.close()

    if user:
        username = user["username"] if user else None
        puntos = user["puntos_fidelizacion"] if user else None
        token = generate_token({'username': username})
        return jsonify({'token': token, 'username': username, "puntos": puntos})
    else:
        response = jsonify({'message': 'User not found'})
        print(response)
        response.status_code = 404
        return response
    
def generate_token(data: dict):
   token = encode(payload={**data, 'exp': expire_date(1)}, key=os.getenv('SSK'), algorithm='HS256')
   print(token)
   return token

#Obtener dias de expiración
def expire_date(hours: int):
    now = datetime.now()
    new_date = now + timedelta(hours)
    return new_date

#Función para validar el token
def validate_token(token, output=False):
    try:
        if output:
            return decode(token, key=os.getenv('SSK'), algorithms=['HS256'])
        decode(token, key=os.getenv('SSK'), algorithms=['HS256'])
    except exceptions.DecodeError:
        response = jsonify({'message': ' Invalid Token'})
        response.status_code = 401
        return response
    except exceptions.ExpiredSignatureError:
        response = jsonify({'message': ' Token Expired'})
        response.status_code = 401
        return response