import streamlit as st

def show_home():
    st.title("🏪 Bienvenido al Sistema POS")

    st.markdown("Selecciona una opción para comenzar:")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🛍️ Ver Productos"):
            st.session_state["previous_page"] = st.session_state["page"]
            st.session_state["next_page"] = None
            st.session_state['page'] = 'products'
            st.rerun()

    with col2:
        if st.button("👥 Ver Clientes"):
            st.session_state["previous_page"] = st.session_state["page"]
            st.session_state["next_page"] = None
            st.session_state['page'] = 'clientes'
            st.rerun()