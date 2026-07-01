import sys

class Graph():
    def __init__(self, dinh):
        self.x = dinh
        self.graph = [[0 for column in range(dinh)] for row in range(dinh)]

    def dijkstra_trang_thai_mo_rong(self, s, t, max_gas):
        dist = [[sys.maxsize for _ in range(max_gas + 1)] for _ in range(self.x)]
        dist[s][max_gas] = 0
        P = [[False for _ in range(max_gas + 1)] for _ in range(self.x)]
        
        for _ in range(self.x * (max_gas + 1)):
            min_val = sys.maxsize
            u, g = -1, -1
            for i in range(self.x):
                for j in range(max_gas + 1):
                    if not P[i][j] and dist[i][j] < min_val:
                        min_val = dist[i][j]
                        u, g = i, j
            if u == -1: break
            P[u][g] = True
            if u == t: break
            for v in range(self.x):
                if self.graph[u][v] > 0 and g >= 1:
                    if dist[v][g - 1] > dist[u][g] + self.graph[u][v]:
                        dist[v][g - 1] = dist[u][g] + self.graph[u][v]
        min_cost = min(dist[t])
        print("Chi phi trang thai mo rong den dich la:", min_cost)

g = Graph(3)
g.graph = [
    [0, 5, 0],
    [0, 0, 3],
    [0, 0, 0]
]
g.dijkstra_trang_thai_mo_rong(0, 2, 2)