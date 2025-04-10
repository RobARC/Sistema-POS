import streamlit as st
from dotenv import load_dotenv
import os
from utils.config import auth_url
from viewmodels.products_vm import get_products
from components.header import show_header 

load_dotenv()  # Carga las variables del entorno
API = os.getenv('BACKEND_URL')

def show_products():
    st.title('🛍️ Lista de Productos')
    
    products = get_products()

    if "error" in products:
        st.error(products["error"])
        return

    seleccionados = []

    for product in products:
        with st.container():
            cols = st.columns([1, 2])
            with cols[0]:
                st.image(product['image'], width=150)
            with cols[1]:
                st.subheader(product['title'])
                st.write(product['description'])
                st.markdown(f"**💲 Precio:** ${product['price']}")
                # Checkbox para seleccionar
                seleccionado = st.checkbox("Seleccionar", key=f"check_{product['id']}")
                if seleccionado:
                    seleccionados.append(product)

    if st.button("Agregar productos seleccionados al carrito"):
        for product in seleccionados:
            pid = str(product['id'])
            if pid in st.session_state.cart:
                st.session_state.cart[pid]['quantity'] += 1
            else:
                st.session_state.cart[pid] = {
                    'producto': product,
                    'quantity': 1
                }
        st.success("Productos agregados al carrito")
        st.rerun()

if __name__ == "__main__":
    show_products()