class Dynamic2DArray:
    def __init__(self): self.matrix = []
    def add_row(self, row): self.matrix.append(row)
    def get(self, i, j): return self.matrix[i][j]
    def set(self, i, j, val): self.matrix[i][j] = val
d2 = Dynamic2DArray()
d2.add_row([1, 2])
print(d2.get(0, 1))