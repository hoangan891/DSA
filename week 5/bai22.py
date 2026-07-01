import sys

class Graph():
    def __init__(self, dinh):
        self.x = dinh
        self.graph = [[0 for column in range(dinh)] for row in range(dinh)]

    def gioi_han_canh_trung_chuyen(self, s, t, k):
        dist = [[sys.maxsize for _ in range(k + 2)] for _ in range(self.x)]
        dist[s][0] = 0
        P = [[False for _ in range(k + 2)] for _ in range(self.x)]
        
        for _ in range(self.x * (k + 2)):
            min_val = sys.maxsize
            u, c = -1, -1
            for i in range(self.x):
                for j in range(k + 2):
                    if not P[i][j] and dist[i][j] < min_val:
                        min_val = dist[i][j]
                        u, c = i, j
            if u == -1: break
            P[u][c] = True
            if u == t: break
            if c <= k:
                for v in range(self.x):
                    if self.graph[u][v] > 0:
                        if dist[v][c + 1] > dist[u][c] + self.graph[u][v]:
                            dist[v][c + 1] = dist[u][c] + self.graph[u][v]
        min_res = min(dist[t])
        print("Duong di re nhat gioi han k trung chuyen:", min_res)

g = Graph(4)
g.graph = [
    [0, 2, 10, 0],
    [0, 0, 3, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 0]
]
g.gioi_han_canh_trung_chuyen(0, 3, 1)