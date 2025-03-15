def dfs_iterativo(grafo, inicio):
    visitados = set()
    pilha = [inicio]

    while pilha:
        nodo = pilha.pop()
        if nodo not in visitados:
            print(nodo, end=" ")  
            visitados.add(nodo)
            pilha.extend(reversed(grafo[nodo]))  


grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}


dfs_iterativo(grafo, 'A')
