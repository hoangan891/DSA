import sys

class Graph():
    def __init__(self, dinh):
        self.x = dinh
        self.graph = [[0 for column in range(dinh)] for row in range(dinh)]

    def dijkstra_luoi_2d(self, bat_dau, ket_thuc, m, n):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        dist = [[sys.maxsize for _ in range(n)] for _ in range(m)]
        dist[bat_dau[0]][bat_dau[1]] = self.graph[bat_dau[0]][bat_dau[1]]
        P = [[False for _ in range(n)] for _ in range(m)]
        
        for _ in range(m * n):
            min_val = sys.maxsize
            ux, uy = -1, -1
            for r in range(m):
                for c in range(n):
                    if not P[r][c] and dist[r][c] < min_val:
                        min_val = dist[r][c]
                        ux, uy = r, c
            if ux == -1:
                break
            P[ux][uy] = True
            if (ux, uy) == ket_thuc:
                break
            for i in range(4):
                vx, vy = ux + dx[i], uy + dy[i]
                if 0 <= vx < m and 0 <= vy < n and not P[vx][vy]:
                    if dist[vx][vy] > dist[ux][uy] + self.graph[vx][vy]:
                        dist[vx][vy] = dist[ux][uy] + self.graph[vx][vy]
        print("Chi phi thap nhat tren luoi la:", dist[ket_thuc[0]][ket_thuc[1]])

g = Graph(3)
g.graph = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
g.dijkstra_luoi_2d((0, 0), (2, 2), 3, 3)