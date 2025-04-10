import streamlit as st

def show_header(title="Sistema POS"):
    
    cart = st.session_state.get('cart', {})
    total_items = sum(item['quantity'] for item in cart.values())

    col1,  col2,  col3, col4, col5, col6 = st.columns([0.2, 0.2, 0.5, 0.2, 0.2, 0.2])

   # Botón de retroceso
    if "previous_page" in st.session_state and st.session_state["previous_page"]:
        with col1:
            if st.button("⬅️ Back", use_container_width=True):
                st.session_state["page"] = st.session_state["previous_page"]
                st.rerun()

     # Botón adelante
    if "next_page" in st.session_state and st.session_state["next_page"]:
        with col2:
            st.button("➡️ Next", use_container_width=True)
            st.session_state["page"] = st.session_state["next_page"]
            st.rerun()  

     # Título
    with col3:
         st.markdown(f"<h3 style='text-align: center;'>{title}</h3>", unsafe_allow_html=True)

     # Icono del carrito
    cart_count = len(st.session_state.get("cart", {}))
    with col4: 
        if st.button(f"🛒 ({cart_count})", use_container_width=True):
            st.session_state["previous_page"] = st.session_state["page"]
            st.session_state["page"] = "cart"
            st.rerun()

  # Usuario y logout
    username = st.session_state.get("username", "Invitado")
    with col5:
        st.markdown(f"👤 {username}")

    with col6:
        if st.button("Cerrar sesión", use_container_width=True):
            st.session_state.clear()
            st.session_state["page"] = "login"
            st.rerun()

  