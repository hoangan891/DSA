import sys
class Graph:
    def __init__(self, dinh):
        self.x = dinh
        self.graph = [[0 for _ in range(dinh)] for _ in range(dinh)]
    def dijkstra(self, a):
        L = [sys.maxsize] * self.x; L[a] = 0; P = [False] * self.x
        for _ in range(self.x):
            min_v, u = sys.maxsize, -1
            for x in range(self.x):
                if not P[x] and L[x] < min_v: min_v = L[x]; u = x
            if u == -1: break
            P[u] = True
            for x in range(self.x):
                if self.graph[u][x] > 0 and not P[x] and L[x] > L[u] + self.graph[u][x]:
                    L[x] = L[u] + self.graph[u][x]
        print(L)
g = Graph(3); g.graph = [[0, 4, 1], [4, 0, 2], [1, 2, 0]]; g.dijkstra(0)