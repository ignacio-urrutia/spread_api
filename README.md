# API de Alerta de Spread para Buda.com

Esta aplicación Flask calcula los spreads del mercado de criptomonedas utilizando la API de Buda.com y permite a los usuarios establecer y monitorear alertas de spread.

## Características

- Calcula el spread para cualquier mercado disponible en Buda.com.
- Obtiene spreads de todos los mercados en una sola llamada API.
- Establece alertas de spread y verifica si el spread actual supera estos umbrales.

## Primeros Pasos

### Prerrequisitos

- Python 3.9 o superior.
- Docker (opcional para contenerización).

### Instalación

1. Clona el repositorio:
    ``` bash
    git clone https://github.com/ignacio-urrutia/spread_api.git
    cd spread_api
    ```
2. Instala las dependencias:
    ``` bash
    pip install -r requirements.txt
    ```
3. Ejecuta la aplicación:

    ``` bash
    flask run
    ```

### Configuración con Docker
Para contenerizar la aplicación, sigue estos pasos:

1. Construye la imagen de Docker:
    ``` bash
    docker build -t buda_spread_api .
    ```
2. Ejecuta el contenedor:    
    ``` bash
    docker run -p 5000:5000 buda_spread_api
    ```

## Uso
Accede a los endpoints de la API para calcular spreads y gestionar alertas de spread. Para documentación detallada de la API, visita `/apidocs` después de iniciar la aplicación.
