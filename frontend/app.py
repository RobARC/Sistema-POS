import streamlit as st
from views.home_page import show_home
from views.clientes_page import show_clientes
from views.products_page import show_products
from views.login_page import show_login
from views.cart_page import show_cart
from components.header import show_header
from utils import auth

def main():
   
  if 'logged_in' not in st.session_state:
       st.session_state['logged_in'] = False 
  if 'page' not in st.session_state:
      st.session_state['page'] = 'home' 
  if 'cart' not in st.session_state:
      st.session_state['cart'] = {} 

  # Verificación de login
  if not st.session_state['logged_in']:
      st.session_state['page'] = 'login'  # Asegura que la página sea login
      show_login()
      return
  
    # Mostrar header solo si no está en la página de login
  if st.session_state['logged_in'] == True:
        show_header()

  # Controlador de navegación
  if st.session_state['page'] == 'home':
        show_home()
  elif st.session_state['page'] == 'products':
        show_products()
  elif st.session_state['page'] == 'clientes':
        show_clientes()
  elif st.session_state['page'] == 'cart':
          show_cart()
 

if __name__ == "__main__":
    main()