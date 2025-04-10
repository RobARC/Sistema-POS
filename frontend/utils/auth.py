import streamlit as st
import requests
from utils.config import auth_url

def authenticate(username, password):
    print(username)
    print(password)
 
    auth_data = {
        "email": username,
        "password": password
    }   

    url = auth_url + "/login"

    try:
        response = requests.post(url, json=auth_data)
       # return response.status_code == 200
        if response.status_code == 200:
            response_data = response.json()
            st.session_state["token"] = response_data["token"]
            st.session_state["username"] = response_data["username"]
            st.session_state["puntos"] = response_data["puntos"]
            print(response_data)
            token = response_data
            return {"token": token}
        else:
            error_message = response.json().get("error", "Error de autenticación")
            return{"error": error_message}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}





