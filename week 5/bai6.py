import sys

class Graph():
    def __init__(self, dinh):
        self.x = dinh
        self.graph = [[0 for column in range(dinh)] for row in range(dinh)]

    def in_chi_tiet_duong_di(self, a, t):
        L = [sys.maxsize] * self.x
        L[a] = 0
        P = [False] * self.x
        parent = [-1] * self.x
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
                    parent[x] = u
        if L[t] == sys.maxsize:
            print("Khong co duong di")
            return
        path = []
        curr = t
        while curr != -1:
            path.append(curr)
            curr = parent[curr]
        path.reverse()
        print(f"Duong di tu {a} den {t} la: {' -> '.join(map(str, path))}")

g = Graph(6)
g.graph = [
    [0, 7, 0, 14, 0, 0],
    [0, 0, 4, 1, 0, 0],
    [0, 0, 0, 0, 2, 1],
    [0, 0, 1, 0, 5, 0],
    [0, 0, 0, 0, 0, 5],
    [0, 0, 0, 0, 0, 0]
]
g.in_chi_tiet_duong_di(0, 5)