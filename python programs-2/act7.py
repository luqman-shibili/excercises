import heapq

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('A', 1), ('C', 1), ('D', 4)],
    'C': [('A', 3), ('B', 1), ('D', 1)],
    'D': [('B', 4), ('C', 1)]
}

def prim(graph, start):
    mst = []  
    visited = set([start]) 
    edges = []

    for neighbor, weight in graph[start]:
        heapq.heappush(edges, (weight, start, neighbor))

    while edges:
        weight, frm, to = heapq.heappop(edges) 
        if to not in visited:
            visited.add(to)
            mst.append((frm, to, weight))
            
            for neighbor, weight in graph[to]:
                if neighbor not in visited:
                    heapq.heappush(edges, (weight, to, neighbor))
    
    return mst

mst = prim(graph, 'A')
print("Minimum Spanning Tree:", mst)