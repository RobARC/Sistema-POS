import streamlit as st
import requests
from utils.config import auth_url
from dotenv import load_dotenv
import os
from utils.config import auth_url

load_dotenv() #Carga las variables del entorno
API = os.getenv('BACKEND_URL')

@st.cache_data
def get_clientes():
    URL = auth_url + '/api/clientes'

    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return {'error': 'Error al llamar a la API'}