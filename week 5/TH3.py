import sys

class Graph():
    def __init__(self, dinh):
        self.x = dinh
        self.graph = [[0 for column in range(dinh)] for row in range(dinh)]

    def inketqua(self, L, a):
        print("dinh nguon xuat phat tu: ")
        for nut in range(self.x):
            print(a, " den dinh ", nut, "do dai duong di la: ", L[nut])

    def duongdinhonhat(self, L, P):
        min_val = sys.maxsize
        min_index = -1
        for x in range(self.x):
            if L[x] < min_val and P[x] == False:
                min_val = L[x]
                min_index = x
        return min_index

    def timduongdi(self, a):
        L = [sys.maxsize] * self.x
        L[a] = 0
        P = [False] * self.x
        for cout in range(self.x):
            u = self.duongdinhonhat(L, P)
            if u == -1:
                break
            P[u] = True
            for x in range(self.x):
                if self.graph[u][x] > 0 and P[x] == False and L[x] > L[u] + self.graph[u][x]:
                    L[x] = L[u] + self.graph[u][x]
        self.inketqua(L, a)

g = Graph(5)
g.graph = [
    [0, 3, 0, 1, 0],
    [0, 0, 7, 0, 0],
    [0, 0, 0, 0, 3],
    [0, 0, 9, 0, 2],
    [0, 0, 3, 0, 0]
]
g.timduongdi(0)