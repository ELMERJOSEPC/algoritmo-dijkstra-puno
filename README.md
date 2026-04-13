

```markdown
# 🗺️ Buscador de Rutas IA - Mapa de Puno

Este proyecto es una Aplicación Web interactiva que implementa el **Algoritmo de búsqueda de Dijkstra** para encontrar la ruta más corta entre puntos turísticos y de interés en la ciudad de Puno, Perú. 

Utiliza **Python (Flask)** para el cálculo matemático del backend y la **API de Google Maps con JavaScript** para la visualización del grafo, la animación de exploración en tiempo real y el trazado de la ruta sobre las calles exactas.

## ⚙️ Requisitos previos
Para ejecutar este proyecto en tu máquina local, necesitas tener instalado Python y la librería Flask.

## 🚀 Instrucciones de Instalación y Uso

1. Clona este repositorio o descarga los archivos en tu computadora.
2. Abre una terminal en la carpeta principal del proyecto e instala Flask ejecutando:
   ```bash
   pip install -r requirements.txt
   ```
3. **Configuración de la API Key (Importante):**
   * Abre el archivo `templates/index.html`.
   * Busca la línea de código donde se carga el script de Google Maps (casi al final).
   * Reemplaza el texto `"PON_TU_API_KEY_AQUI"` por una clave de API propia que sea válida y que tenga habilitados los servicios de **Maps JavaScript API** y **Directions API**.
4. Inicia el servidor de Python con el siguiente comando:
   ```bash
   python app.py
   ```
5. Abre tu navegador web de preferencia e ingresa a la siguiente dirección: `http://127.0.0.1:5000`

## 🖱️ Cómo interactuar con el mapa
* Haz clic en cualquier marcador azul del mapa de Puno para seleccionarlo como **Origen** (el icono cambiará a verde).
* Haz clic en otro marcador para elegir tu **Destino** (el icono cambiará a rojo).
* Observa la animación (líneas grises) que demuestra cómo el algoritmo de Inteligencia Artificial evalúa los costos de las calles vecinas.
* Una vez calculada, la ruta óptima final se trazará automáticamente respetando el sentido y la forma de las calles reales.
* Utiliza el botón de "Reiniciar Mapa" para limpiar la pantalla y calcular una nueva ruta.
```
