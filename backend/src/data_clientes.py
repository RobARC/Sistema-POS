from flask import Flask, jsonify, request
from ConnectDB import get_connection

def get_clientes():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""

                   SELECT id, name, username, email, street, suite,
                   city, zipcode, lat, lng, phone, website,
                   company_name, catch_phrase, bs, puntos_fidelizacion
                   FROM clientes""")
    rows = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    data = []
    for row in rows:
        data.append(dict(zip(columns, row)))
    return jsonify(data)