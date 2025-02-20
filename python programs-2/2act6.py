import heapq

def dijkstra(graph, start):
    heap = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous = {}  # To track the shortest path
    visited = set()
    
    while heap:
        cost, node = heapq.heappop(heap)

        if node in visited:
            continue
        visited.add(node)

        for neighbor, weight in graph[node].items():
            new_cost = cost + weight
            if new_cost < distances[neighbor]:
                distances[neighbor] = new_cost
                previous[neighbor] = node
                heapq.heappush(heap, (new_cost, neighbor))

    return distances, previous  # Returns shortest distances and path tree

# Example usage
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

distances, paths = dijkstra(graph, 'A')
print("Shortest distances:", distances)
print("Shortest paths:", paths)
