import streamlit as st
import requests
from utils.config import auth_url
from dotenv import load_dotenv
import os
from utils.config import auth_url
import streamlit as st

load_dotenv() #Carga las variables del entorno
API = os.getenv('BACKEND_URL')

@st.cache_data
def guardar_puntos(username, puntos):
    URL = auth_url + '/api/compra'
    data = {"username": username, "puntos": puntos}
    try:
        response = requests.post(URL,  json=data)
        if response.status_code == 200:
            st.write(f"Estado de respuesta: {response.status_code}")
            st.write(f"Respuesta: {response.text}")
            
        else:
            st.error("Error al actualizar puntos.")
    except Exception as e:
        st.error(f"Error de conexión: {e}")