import sys

class Graph():
    def __init__(self, dinh):
        self.x = dinh
        self.graph = [[0 for column in range(dinh)] for row in range(dinh)]

    def tim_diem_gap_nhau_toi_uu(self, an_start, ba_start):
        def dijkstra(start):
            L = [sys.maxsize] * self.x
            L[start] = 0
            P = [False] * self.x
            for _ in range(self.x):
                min_v = sys.maxsize
                u = -1
                for x in range(self.x):
                    if not P[x] and L[x] < min_v:
                        min_v = L[x]
                        u = x
                if u == -1: break
                P[u] = True
                for x in range(self.x):
                    if self.graph[u][x] > 0 and not P[x] and L[x] > L[u] + self.graph[u][x]:
                        L[x] = L[u] + self.graph[u][x]
            return L

        L_an = dijkstra(an_start)
        L_ba = dijkstra(ba_start)
        min_max_time = sys.maxsize
        best_node = -1
        for i in range(self.x):
            if L_an[i] != sys.maxsize and L_ba[i] != sys.maxsize:
                max_time = max(L_an[i], L_ba[i])
                if max_time < min_max_time:
                    min_max_time = max_time
                    best_node = i
        print(f"Dinh gap nhau toi uu la dinh {best_node} voi thoi gian {min_max_time}")

g = Graph(4)
g.graph = [
    [0, 2, 4, 0],
    [2, 0, 1, 5],
    [4, 1, 0, 3],
    [0, 5, 3, 0]
]
g.tim_diem_gap_nhau_toi_uu(0, 3)