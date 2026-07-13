class Graph():
    def __init__(self, dinh):
        self.x = dinh
        self.graph = [[0 for column in range(dinh)] for row in range(dinh)]

    def bieu_dien_do_thi(self):
        adj_list = {}
        for u in range(self.x):
            adj_list[u] = []
            for v in range(self.x):
                if self.graph[u][v] > 0:
                    adj_list[u].append((v, self.graph[u][v]))
        return adj_list

g = Graph(6)
g.graph = [
    [0, 7, 0, 14, 0, 0],
    [0, 0, 4, 1, 0, 0],
    [0, 0, 0, 0, 2, 1],
    [0, 0, 1, 0, 5, 0],
    [0, 0, 0, 0, 0, 5],
    [0, 0, 0, 0, 0, 0]
]
print(g.bieu_dien_do_thi())