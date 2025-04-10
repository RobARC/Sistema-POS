import streamlit as st
from dotenv import load_dotenv
import os
import json
import requests
from utils.config import auth_url
from viewmodels.clientes_vm import get_clientes

load_dotenv() #Carga las variables del entorno
API = os.getenv('BACKEND_URL')

def show_clientes():

    st.title('Lista de Clientes')
    clientes = get_clientes()

    if "error" in clientes:
        st.error(clientes["error"])
        return
    
    for client in clientes:
        with st.container():
            st.subheader(client["name"])
            st.write(f"📧 {client['email']}")
            st.markdown(f"🎁 **Puntos de fidelización:** {client.get('puntos_fidelizacion', 0)}")
    