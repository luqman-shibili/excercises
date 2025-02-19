#implementation of IDS
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def dls(node, depth):
    if depth == 0:
        print(node, end=' ')
        return
    if depth > 0:
        for neighbor in graph[node]:
            dls(neighbor, depth - 1)

def ids(start, max_depth):
    for depth in range(max_depth + 1):
        print(f"\nDepth {depth}: ", end='')
        dls(start, depth)

ids('A', 3)