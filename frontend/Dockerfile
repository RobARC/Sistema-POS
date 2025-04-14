# Usa una imagen base de Python
FROM python:3.12-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos al contenedor
COPY . .

COPY .streamlit/config.toml .streamlit/config.toml

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto de Streamlit
EXPOSE 8501

# Comando para correr la app con Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
