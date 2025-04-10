from flask import Flask,request, jsonify
from ConnectDB import get_connection

def guardar_compra_en_bd():

    data = request.get_json()
    username = data.get("username")
    puntos = data.get("puntos")

    print(data)
    print(username)
    print(puntos)
    conn = get_connection()
    cursor = conn.cursor()

    # Buscar puntos actuales del cliente
    cursor.execute("SELECT puntos_fidelizacion FROM clientes WHERE username = ?", (username,))
    result = cursor.fetchone()

    if result:
        nuevos_puntos = puntos

        # Actualizar los puntos en la tabla
        cursor.execute("""
            UPDATE clientes
            SET puntos_fidelizacion = ?
            WHERE username = ?
        """, (nuevos_puntos, username))

        conn.commit()
        print(f"Puntos actualizados correctamente: {nuevos_puntos}")
    else:
        print("❌ Usuario no encontrado en la base de datos.")

    cursor.close()
    conn.close()

    return jsonify({"message": "Puntos actualizados"}), 200
