import streamlit as st
from utils.auth import authenticate

def show_login():
    st.title('Inicio de Sesión')
    username = st.text_input('Email')
    password = st.text_input('Password', type="password")

    if st.button('Iniciar Sesión'):
        if username and password:
            result = authenticate(username, password)
            if "error" in result:
                st.error(result["error"])
                st.session_state['logged_in'] = False
                st.rerun()
            else:
                st.session_state['logged_in'] = True
                st.session_state['page'] = 'home'  # ← control manual
                st.success('Inicio de sesión exitoso!')
                st.rerun()  # Recarga la app para cambiar la vista
        else:
            st.error("Usuario o password incorrectos")

if __name__ == "__main__":
    show_login()