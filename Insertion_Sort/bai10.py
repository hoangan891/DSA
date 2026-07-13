import sys

class Graph():
    def __init__(self, dinh):
        self.x = dinh
        self.graph = [[0 for column in range(dinh)] for row in range(dinh)]

    def dijkstra_vo_huong(self, a):
        L = [sys.maxsize] * self.x
        L[a] = 0
        P = [False] * self.x
        for cout in range(self.x):
            min_val = sys.maxsize
            u = -1
            for x in range(self.x):
                if L[x] < min_val and P[x] == False:
                    min_val = L[x]
                    u = x
            if u == -1:
                break
            P[u] = True
            for x in range(self.x):
                if self.graph[u][x] > 0 and P[x] == False and L[x] > L[u] + self.graph[u][x]:
                    L[x] = L[u] + self.graph[u][x]
        print(L)

g = Graph(4)
g.graph = [
    [0, 5, 1, 0],
    [5, 0, 2, 1],
    [1, 2, 0, 8],
    [0, 1, 8, 0]
]
g.dijkstra_vo_huong(0)