class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))

    def bellman_ford(self, src):
  
        dist = {i: float("Inf") for i in range(self.V)}
        dist[src] = 0

        
        for _ in range(self.V - 1):
            for u, v, weight in self.edges:
                if dist[u] != float("Inf") and dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight

        
        for u, v, weight in self.edges:
            if dist[u] != float("Inf") and dist[u] + weight < dist[v]:
                print("O grafo contém ciclo de peso negativo")
                return None

        return dist

# Exemplo de uso:
g = Graph(5)
g.add_edge(0, 1, -1)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 2)
g.add_edge(1, 4, 2)
g.add_edge(3, 2, 5)
g.add_edge(3, 1, 1)
g.add_edge(4, 3, -3)

resultado = g.bellman_ford(0)

if resultado:
    print("Menores distâncias a partir do vértice 0:", resultado)
