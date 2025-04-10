import streamlit as st
from viewmodels.car_vm import (
    init_cart, add_to_cart, update_quantity,
    remove_from_cart, calculate_totals,
    calculate_points, apply_discount
)
import os
import time
from components.header import show_header
from viewmodels.compras import guardar_puntos
from utils.factura import generar_factura_pdf

API = os.getenv('BACKEND_URL')

def show_cart():
    st.title("🛒 Carrito de Compras")
    init_cart()

    cart = st.session_state['cart']

    if not cart:
        st.info("Tu carrito está vacío.")
        return

    st.subheader("Productos en el carrito")

    for product_id, item in cart.items():
        producto = item["producto"]
        cantidad = item["quantity"]
        col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
        with col1:
            st.write(f"**{producto['title']}**")
            st.image(producto['image'], width=100)
            st.caption(producto['description'][:80] + "...")
        with col2:
            qty = st.number_input(
                f"Cantidad ({producto['title']})", min_value=1, step=1, value=cantidad, key=f"qty_{product_id}"
            )
            update_quantity(product_id, qty)
        with col3:
            st.write(f"Precio: ${producto['price']:.2f}")
        with col4:
            if st.button("Eliminar", key=f"remove_{product_id}"):
                remove_from_cart(product_id)
                st.rerun()

    st.markdown("---")
    subtotal, total_items = calculate_totals()
    puntos_ganados = calculate_points(subtotal)

    st.subheader("Selecciona el método de pago:")
    metodo_pago = st.radio(
    "Método de pago",
    options=["Efectivo", "Tarjeta de crédito/débito", "Transferencia bancaria"]
)


    st.write(f"**Subtotal:** ${subtotal:.2f}")
    st.write(f"**Artículos:** {total_items}")
    st.write(f"🎁 **Puntos que ganarás:** {puntos_ganados}")

    st.markdown("### 🎟️ Canjear puntos")
    puntos_cliente = st.session_state.get("puntos", 0)
    st.write(f"Puntos disponibles: **{puntos_cliente}**")

    puntos_a_canjear = st.number_input(
        "¿Cuántos puntos deseas canjear?", min_value=0, max_value=puntos_cliente, step=1, key="canjear_puntos"
    )
    descuento = apply_discount(puntos_a_canjear)
    total_final = subtotal - descuento

    st.write(f"Descuento: **-${descuento:.2f}**")
    st.success(f"**Total a pagar:** ${total_final:.2f}")

    if st.button("Finalizar Compra"):
        total = sum(item['producto']['price'] * item['quantity'] for item in st.session_state.cart.values())
        puntos_ganados = int(total // 10)  # 1 punto por cada $10

        puntos_actualizados = (puntos_cliente - puntos_a_canjear ) + puntos_ganados

        print(puntos_actualizados)

        username=st.session_state.get("username", "Invitado")
        
        guardar_puntos(username, puntos_actualizados,)

        nombre_archivo = generar_factura_pdf(
        username=username,
        productos=st.session_state.cart,
        total=total,
        metodo_pago=metodo_pago,
        puntos_ganados=puntos_ganados,
        puntos_usados=puntos_a_canjear
    )

        st.success("Compra realizada con éxito 🎉")
       
        with open(nombre_archivo, "rb") as f:
            st.download_button("📄 Descargar Factura", f, file_name=nombre_archivo, mime="application/pdf")

        st.session_state["cliente_puntos"] = puntos_cliente - puntos_a_canjear
        st.session_state["cart"] = {}
        time.sleep(5)
        st.rerun()
