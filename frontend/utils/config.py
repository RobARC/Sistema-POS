import toml

# Cargar configuración desde config.toml
config = toml.load(r"C:\\Projectos Backend\\python\\streamlit\\.streamlit\\config.toml")
auth_url = config["auth"]["auth_url"]