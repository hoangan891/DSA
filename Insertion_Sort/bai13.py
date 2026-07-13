import sys

class Graph():
    def __init__(self, dinh):
        self.x = dinh
        self.graph = [[0 for column in range(dinh)] for row in range(dinh)]

    def check_negative_weights(self):
        for u in range(self.x):
            for v in range(self.x):
                if self.graph[u][v] < 0:
                    return True
        return False

g = Graph(3)
g.graph = [
    [0, 4, -1],
    [0, 0, 2],
    [0, 0, 0]
]
print("Do thi co canh am hay khong:", g.check_negative_weights())