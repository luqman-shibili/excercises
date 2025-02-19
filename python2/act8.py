class UnionFind:
    def __init__(self):
        self.parent = {}
    
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, u, v):
        root1 = self.find(u)
        root2 = self.find(v)
        self.parent[root1] = root2

def kruskal(edges):
    uf = UnionFind()
    mst = []
    
    for u, v, w in sorted(edges, key=lambda x: x[2]):
        if u not in uf.parent:
            uf.parent[u] = u
        if v not in uf.parent:
            uf.parent[v] = v
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, w))
    return mst

edges = [('A', 'B', 1), ('B', 'C', 3), ('A', 'C', 2)]
print(kruskal(edges))