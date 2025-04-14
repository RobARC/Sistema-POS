import toml
import os
from dotenv import load_dotenv  

# Cargar configuración desde config.toml
#config = toml.load(r"C:\\Projectos Backend\\python\\streamlit\\.streamlit\\config.toml")
config = toml.load(os.path.join(os.path.dirname(__file__), '..', '.streamlit', 'config.toml'))
auth_url = config["auth"]["auth_url"]