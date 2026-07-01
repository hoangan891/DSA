import sys

class Graph():
    def __init__(self, dinh):
        self.x = dinh
        self.graph = [[0 for column in range(dinh)] for row in range(dinh)]

    def kiem_tra_lien_thong_dijkstra(self, a):
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
        res = True
        for i in range(self.x):
            if L[i] == sys.maxsize:
                res = False
        print("Co den duoc moi dinh hay khong:", res)

g = Graph(6)
g.graph = [
    [0, 7, 0, 14, 0, 0],
    [0, 0, 4, 1, 0, 0],
    [0, 0, 0, 0, 2, 1],
    [0, 0, 1, 0, 5, 0],
    [0, 0, 0, 0, 0, 5],
    [0, 0, 0, 0, 0, 0]
]
g.kiem_tra_lien_thong_dijkstra(0)