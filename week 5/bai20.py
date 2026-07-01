import heapq
import sys

class Graph():
    def __init__(self, dinh):
        self.x = dinh
        self.graph = [[0 for column in range(dinh)] for row in range(dinh)]

    def k_duong_di_ngan_nhat(self, s, t, k):
        count = [0] * self.x
        pq = [(0, s)]
        res = []
        while pq and count[t] < k:
            d, u = heapq.heappop(pq)
            count[u] += 1
            if u == t:
                res.append(d)
            if count[u] <= k:
                for v in range(self.x):
                    if self.graph[u][v] > 0:
                        heapq.heappush(pq, (d + self.graph[u][v], v))
        print(f"{k} duong di ngan nhat den dich la:", res)

g = Graph(4)
g.graph = [
    [0, 2, 4, 0],
    [0, 0, 1, 7],
    [0, 0, 0, 3],
    [0, 0, 0, 0]
]
g.k_duong_di_ngan_nhat(0, 3, 2)