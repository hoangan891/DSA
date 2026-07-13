import heapq, sys
def dijkstra_heap(graph, src, n):
    L = [sys.maxsize] * n; L[src] = 0; pq = [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > L[u]: continue
        for v, w in graph.get(u, []):
            if L[v] > L[u] + w: L[v] = L[u] + w; heapq.heappush(pq, (L[v], v))
    print(L)
g = {0: [(1, 2)], 1: [(2, 3)], 2: []}
dijkstra_heap(g, 0, 3)