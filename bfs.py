from collections import deque

def bfs(grafo, inicio):
    visitados = set()
    fila = deque([inicio])
    
    while fila:
        nodo = fila.popleft()
        if nodo not in visitados:
            print(nodo, end=" ")  
            visitados.add(nodo)
            fila.extend(vizinho for vizinho in grafo[nodo] if vizinho not in visitados)


grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}


bfs(grafo, 'A')
