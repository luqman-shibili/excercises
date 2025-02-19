import heapq

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

def dijkstra(graph, start):
    heap = [(0, start)]
    visited = {}
    
    while heap:
        (cost, node) = heapq.heappop(heap)
        if node not in visited:
            visited[node] = cost
            for neighbor, weight in graph[node].items():
                if neighbor not in visited:
                    heapq.heappush(heap, (cost + weight, neighbor))
    return visited

print(dijkstra(graph, 'A'))