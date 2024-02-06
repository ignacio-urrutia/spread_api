# Usa una imagen oficial de Python como imagen padre
FROM python:3.9-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos de requisitos primero para aprovechar la caché de capas de Docker
COPY requirements.txt .

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código fuente de la aplicación en el contenedor
COPY . .

# Expone el puerto en el que la aplicación estará disponible
EXPOSE 5000

# Define el comando para ejecutar la aplicación
CMD ["flask", "run", "--host=0.0.0.0"]
