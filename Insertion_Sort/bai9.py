import heapq
import sys

class Graph():
    def __init__(self, dinh):
        self.x = dinh
        self.graph = [[0 for column in range(dinh)] for row in range(dinh)]

    def dijkstra_heap(self, a):
        L = [sys.maxsize] * self.x
        L[a] = 0
        pq = [(0, a)]
        while pq:
            curr_d, u = heapq.heappop(pq)
            if curr_d > L[u]:
                continue
            for v in range(self.x):
                if self.graph[u][v] > 0 and L[v] > L[u] + self.graph[u][v]:
                    L[v] = L[u] + self.graph[u][v]
                    heapq.heappush(pq, (L[v], v))
        print(L)

g = Graph(4)
g.graph = [
    [0, 2, 4, 0],
    [0, 0, 1, 7],
    [0, 0, 0, 3],
    [0, 0, 0, 0]
]
g.dijkstra_heap(0)