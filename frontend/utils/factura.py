from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas
from datetime import datetime
import os

def generar_factura_pdf(username, productos, total, metodo_pago, puntos_ganados, puntos_usados=0):
    fecha = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nombre_archivo = f"factura_{username}_{fecha}.pdf"
    ruta = os.path.join("facturas", nombre_archivo)

    if not os.path.exists("facturas"):
        os.makedirs("facturas")

    c = canvas.Canvas(ruta, pagesize=LETTER)
    width, height = LETTER

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, height - 50, "Factura de Compra")

    c.setFont("Helvetica", 12)
    c.drawString(50, height - 80, f"Cliente: {username}")
    c.drawString(50, height - 100, f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    c.drawString(50, height - 120, f"Método de Pago: {metodo_pago}")

    c.drawString(50, height - 150, "Productos:")

    y = height - 170
    for item in productos.values():
        nombre = item["producto"]["title"]
        precio = item["producto"]["price"]
        cantidad = item["quantity"]
        subtotal = precio * cantidad
        c.drawString(60, y, f"{nombre} - ${precio} x {cantidad} = ${subtotal}")
        y -= 20

    c.drawString(50, y - 10, f"Total: ${total}")
    c.drawString(50, y - 30, f"Puntos usados: {puntos_usados}")
    c.drawString(50, y - 50, f"Puntos ganados: {puntos_ganados}")

    c.save()
    return ruta
