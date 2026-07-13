import heapq

# ---------------- Dijkstra ----------------
def dijkstra(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0

    pq = [(0, start)]
    visited = [False] * n

    while pq:
        d, u = heapq.heappop(pq)

        if visited[u]:
            continue

        visited[u] = True

        for v, w in graph[u]:
            if not visited[v] and dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))

    return dist


# ---------------- Bellman-Ford ----------------
def bellman_ford(edges, V, start):
    dist = [float('inf')] * V
    dist[start] = 0

    for _ in range(V - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[v] > dist[u] + w:
                dist[v] = dist[u] + w

    return dist


# ---------------- Đồ thị phản ví dụ ----------------
# A = 0, B = 1, C = 2

graph = [
    [(1, 2), (2, 5)],   # A -> B (2), A -> C (5)
    [],                 # B
    [(1, -4)]           # C -> B (-4)
]

edges = [
    (0, 1, 2),
    (0, 2, 5),
    (2, 1, -4)
]

print("=== Dijkstra ===")
d1 = dijkstra(graph, 0)
print("Khoảng cách từ A:")
print("A -> A =", d1[0])
print("A -> B =", d1[1])
print("A -> C =", d1[2])

print("\n=== Bellman-Ford ===")
d2 = bellman_ford(edges, 3, 0)
print("Khoảng cách từ A:")
print("A -> A =", d2[0])
print("A -> B =", d2[1])
print("A -> C =", d2[2])