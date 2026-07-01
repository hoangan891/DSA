import sys

class Graph():
    def __init__(self, dinh):
        self.x = dinh
        self.graph = [[0 for column in range(dinh)] for row in range(dinh)]

    def tim_duong_max_min(self, a):
        L = [-1] * self.x
        L[a] = sys.maxsize
        P = [False] * self.x
        for cout in range(self.x):
            max_val = -1
            u = -1
            for x in range(self.x):
                if L[x] > max_val and P[x] == False:
                    max_val = L[x]
                    u = x
            if u == -1:
                break
            P[u] = True
            for x in range(self.x):
                if self.graph[u][x] > 0 and P[x] == False:
                    suc_chua_moi = min(L[u], self.graph[u][x])
                    if suc_chua_moi > L[x]:
                        L[x] = suc_chua_moi
        print(L)

g = Graph(4)
g.graph = [
    [0, 10, 5, 0],
    [0, 0, 2, 8],
    [0, 0, 0, 9],
    [0, 0, 0, 0]
]
g.tim_duong_max_min(0)