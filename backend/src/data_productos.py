from flask import Flask, jsonify, request
from ConnectDB import get_connection

def get_products():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
                   SELECT id, title, price, description,
                   category, image, rating_rate, rating_count
                    FROM products""")
    rows = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    data = []
    for row in rows:
        data.append(dict(zip(columns, row)))
    return jsonify(data)

