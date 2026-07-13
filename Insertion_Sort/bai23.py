import sys

class Graph():
    def __init__(self, dinh):
        self.x = dinh
        self.graph = [[0 for column in range(dinh)] for row in range(dinh)]

    def nhieu_truy_van_short_path(self, queries):
        memo = {}
        for s, t in queries:
            if s not in memo:
                L = [sys.maxsize] * self.x
                L[s] = 0
                P = [False] * self.x
                for _ in range(self.x):
                    min_v = sys.maxsize
                    u = -1
                    for x in range(self.x):
                        if not P[x] and L[x] < min_v:
                            min_v = L[x]
                            u = x
                    if u == -1: break
                    P[u] = True
                    for x in range(self.x):
                        if self.graph[u][x] > 0 and not P[x] and L[x] > L[u] + self.graph[u][x]:
                            L[x] = L[u] + self.graph[u][x]
                memo[s] = L
            print(f"Truy van ({s}, {t}) -> Do dai: {memo[s][t]}")

g = Graph(4)
g.graph = [
    [0, 3, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 5],
    [0, 0, 0, 0]
]
g.nhieu_truy_van_short_path([(0, 2), (0, 3)])