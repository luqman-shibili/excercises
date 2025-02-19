graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def dls(node, depth, visited):
    if depth == 0:
        print(node, end=' ')
        return
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            dls(neighbor, depth-1, visited)

def ids(start, max_depth):
    for depth in range(max_depth):
        visited = set()
        dls(start, depth, visited)

ids('A', 3)