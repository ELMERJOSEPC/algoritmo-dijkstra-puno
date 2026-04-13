from flask import Flask, render_template, request, jsonify
import heapq

app = Flask(__name__)

# Mapa ampliado para que la animación de búsqueda se note más
mapa_puno = {
    'Plaza de Armas': {'Parque Pino': 3, 'Puerto Muelle': 7, 'Catedral': 1},
    'Catedral': {'Plaza de Armas': 1, 'Mercado Central': 4, 'Hospital': 6},
    'Parque Pino': {'Plaza de Armas': 3, 'Mercado Central': 2, 'Estadio': 5},
    'Mercado Central': {'Parque Pino': 2, 'Catedral': 4, 'Terminal Terrestre': 5},
    'Puerto Muelle': {'Plaza de Armas': 7, 'Terminal Terrestre': 4, 'Universidad': 8},
    'Terminal Terrestre': {'Mercado Central': 5, 'Puerto Muelle': 4, 'Universidad': 3},
    'Hospital': {'Catedral': 6, 'Estadio': 4},
    'Estadio': {'Parque Pino': 5, 'Hospital': 4, 'Universidad': 7},
    'Universidad': {'Puerto Muelle': 8, 'Terminal Terrestre': 3, 'Estadio': 7}
}

def algoritmo_dijkstra_visual(grafo, inicio, destino):
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    rutas = {nodo: None for nodo in grafo}
    cola_prioridad = [(0, inicio)]
    
    historial_busqueda = [] # <-- Aquí guardaremos los pasos visuales
    
    while cola_prioridad:
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)
        
        if nodo_actual == destino:
            break
            
        if distancia_actual > distancias[nodo_actual]:
            continue
            
        for vecino, peso in grafo[nodo_actual].items():
            distancia_alternativa = distancia_actual + peso
            
            # Registramos que el algoritmo está "mirando" esta calle
            historial_busqueda.append({'desde': nodo_actual, 'hacia': vecino})
            
            if distancia_alternativa < distancias[vecino]:
                distancias[vecino] = distancia_alternativa
                rutas[vecino] = nodo_actual
                heapq.heappush(cola_prioridad, (distancia_alternativa, vecino))
                
    ruta_optima = []
    nodo_paso = destino
    if rutas[destino] is not None or inicio == destino:
        while nodo_paso is not None:
            ruta_optima.insert(0, nodo_paso)
            nodo_paso = rutas[nodo_paso]
            
    return ruta_optima, historial_busqueda

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular_dijkstra', methods=['POST'])
def calcular():
    datos = request.json
    origen = datos.get('origen').strip()
    destino = datos.get('destino').strip()
    
    if origen not in mapa_puno or destino not in mapa_puno:
        return jsonify({"error": "Nodo no encontrado", "ruta": [], "exploracion": []})

    ruta_final, pasos_exploracion = algoritmo_dijkstra_visual(mapa_puno, origen, destino)
    
    return jsonify({
        "ruta": ruta_final, 
        "exploracion": pasos_exploracion
    })

if __name__ == '__main__':
    app.run(debug=True)