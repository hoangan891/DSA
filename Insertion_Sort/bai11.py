import sys

class Graph():
    def __init__(self, dinh):
        self.x = dinh
        self.graph = [[0 for column in range(dinh)] for row in range(dinh)]

    def tim_so_duong_di_ngan_nhat(self, a):
        L = [sys.maxsize] * self.x
        L[a] = 0
        P = [False] * self.x
        count = [0] * self.x
        count[a] = 1
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
                if self.graph[u][x] > 0 and P[x] == False:
                    if L[x] > L[u] + self.graph[u][x]:
                        L[x] = L[u] + self.graph[u][x]
                        count[x] = count[u]
                    elif L[x] == L[u] + self.graph[u][x]:
                        count[x] += count[u]
        print("So luong duong di ngan nhat den cac dinh:", count)

g = Graph(4)
g.graph = [
    [0, 2, 2, 0],
    [0, 0, 3, 3],
    [0, 0, 0, 3],
    [0, 0, 0, 0]
]
g.tim_so_duong_di_ngan_nhat(0)