import heapq

def dijkstra(grafo, inicio):
    
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0

     
    fila_prioridade = [(0, inicio)]

    while fila_prioridade:
        distancia_atual, nodo_atual = heapq.heappop(fila_prioridade)

      
        if distancia_atual > distancias[nodo_atual]:
            continue

        
        for vizinho, peso in grafo[nodo_atual].items():
            distancia = distancia_atual + peso

            
            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                heapq.heappush(fila_prioridade, (distancia, vizinho))

    return distancias


grafo = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 5, 'D': 10},
    'C': {'A': 2, 'B': 5, 'D': 3, 'E': 6},
    'D': {'B': 10, 'C': 3, 'E': 1},
    'E': {'C': 6, 'D': 1}
}


resultado = dijkstra(grafo, 'A')
print(resultado)
