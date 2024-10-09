from collections import deque

def bfs_shortest_path(graph, start, target):
    queue = deque([start])
    visited = {start}
    parent = {start: None}
    
    while queue:
        current = queue.popleft()
        
        if current == target:
            break
        
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)
    
    path = []
    if target in visited:
        while target is not None:
            path.append(target)
            target = parent[target]
        path.reverse()
    
    return path if path else "No path exists"


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = 'A'
target_node = 'F'
print(bfs_shortest_path(graph, start_node, target_node))
