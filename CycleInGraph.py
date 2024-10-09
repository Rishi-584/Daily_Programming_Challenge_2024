from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def is_cyclic_util(self, v, visited, parent):
        visited[v] = True

        for i in self.graph[v]:
            if not visited[i]:
                if self.is_cyclic_util(i, visited, v):
                    return True
            elif i != parent:
                return True
        
        return False

    def is_cyclic(self):
        visited = [False] * self.V

        for i in range(self.V):
            if not visited[i]:
                if self.is_cyclic_util(i, visited, -1):
                    return True
        
        return False

def build_graph(V, edges):
    g = Graph(V)
    for u, v in edges:
        g.add_edge(u, v)
    return g


V, E = map(int, input("Enter number of vertices and edges (V E): ").split())
edges = []

print("Enter the edges (format: u v):")
for _ in range(E):
    u, v = map(int, input().split())
    edges.append((u, v))

graph = build_graph(V, edges)

print(graph.is_cyclic())
