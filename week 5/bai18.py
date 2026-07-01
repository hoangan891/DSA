import sys

class Graph():
    def __init__(self, dinh):
        self.x = dinh
        self.graph = [[0 for column in range(dinh)] for row in range(dinh)]

    def tim_canh_ngan_nhat_giam_gia(self, a, t):
        L_source = [sys.maxsize] * self.x
        L_source[a] = 0
        P = [False] * self.x
        for _ in range(self.x):
            min_v = sys.maxsize
            u = -1
            for x in range(self.x):
                if not P[x] and L_source[x] < min_v:
                    min_v = L_source[x]
                    u = x
            if u == -1: break
            P[u] = True
            for x in range(self.x):
                if self.graph[u][x] > 0 and not P[x] and L_source[x] > L_source[u] + self.graph[u][x]:
                    L_source[x] = L_source[u] + self.graph[u][x]

        L_dest = [sys.maxsize] * self.x
        L_dest[t] = 0
        P = [False] * self.x
        for _ in range(self.x):
            min_v = sys.maxsize
            u = -1
            for x in range(self.x):
                if not P[x] and L_dest[x] < min_v:
                    min_v = L_dest[x]
                    u = x
            if u == -1: break
            P[u] = True
            for x in range(self.x):
                if self.graph[x][u] > 0 and not P[x] and L_dest[x] > L_dest[u] + self.graph[x][u]:
                    L_dest[x] = L_dest[u] + self.graph[x][u]

        min_total = L_source[t]
        for u in range(self.x):
            for v in range(self.x):
                if self.graph[u][v] > 0:
                    cost = L_source[u] + (self.graph[u][v] // 2) + L_dest[v]
                    if cost < min_total:
                        min_total = cost
        print("Chi phi thap nhat sau giam gia 1 canh:", min_total)

g = Graph(4)
g.graph = [
    [0, 4, 10, 0],
    [0, 0, 0, 5],
    [0, 0, 0, 1],
    [0, 0, 0, 0]
]
g.tim_canh_ngan_nhat_giam_gia(0, 3)