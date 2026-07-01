import sys
def grid_dijkstra(grid):
    m, n = len(grid), len(grid[0])
    dist = [[sys.maxsize]*n for _ in range(m)]; dist[0][0] = grid[0][0]
    P = [[False]*n for _ in range(m)]
    for _ in range(m * n):
        min_v, ux, uy = sys.maxsize, -1, -1
        for r in range(m):
            for c in range(n):
                if not P[r][c] and dist[r][c] < min_v: min_v = dist[r][c]; ux, uy = r, c
        if ux == -1: break
        P[ux][uy] = True
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            vx, vy = ux + dx, uy + dy
            if 0 <= vx < m and 0 <= vy < n and not P[vx][vy]:
                if dist[vx][vy] > dist[ux][uy] + grid[vx][vy]:
                    dist[vx][vy] = dist[ux][uy] + grid[vx][vy]
    return dist[m-1][n-1]
matrix = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
print("Chi phi luoi:", grid_dijkstra(matrix))