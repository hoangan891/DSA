import sys
def dijkstra_trace(graph, src, dest, n):
    L = [sys.maxsize] * n; L[src] = 0; P = [False] * n; parent = [-1] * n
    for _ in range(n):
        min_v, u = sys.maxsize, -1
        for x in range(n):
            if not P[x] and L[x] < min_v: min_v = L[x]; u = x
        if u == -1: break
        P[u] = True
        for v, w in graph.get(u, []):
            if not P[v] and L[v] > L[u] + w: L[v] = L[u] + w; parent[v] = u
    path, curr = [], dest
    while curr != -1: path.append(curr); curr = parent[curr]
    print(" -> ".join(map(str, reversed(path))))
g = {0: [(1, 4), (2, 1)], 1: [(3, 1)], 2: [(1, 2), (4, 8)], 3: [(4, 3)], 4: []}
dijkstra_trace(g, 0, 4, 5)