# backend/Dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Establecer el directorio de trabajo como /app/src
WORKDIR /app/src

CMD ["python", "app.py"]