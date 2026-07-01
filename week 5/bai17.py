import sys

class Graph():
    def __init__(self, dinh):
        self.x = dinh
        self.graph = [[0 for column in range(dinh)] for row in range(dinh)]

    def tim_duong_an_toan_nhat(self, a):
        L = [0.0] * self.x
        L[a] = 1.0
        P = [False] * self.x
        for cout in range(self.x):
            max_prob = -1.0
            u = -1
            for x in range(self.x):
                if L[x] > max_prob and P[x] == False:
                    max_prob = L[x]
                    u = x
            if u == -1:
                break
            P[u] = True
            for x in range(self.x):
                if self.graph[u][x] > 0 and P[x] == False:
                    xs_moi = L[u] * (self.graph[u][x] / 100.0)
                    if xs_moi > L[x]:
                        L[x] = xs_moi
        print(L)

g = Graph(3)
g.graph = [
    [0, 90, 50],
    [0, 0, 80],
    [0, 0, 0]
]
g.tim_duong_an_toan_nhat(0)