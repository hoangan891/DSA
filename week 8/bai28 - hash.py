def rolling_hash_2d(matrix, p=3): return sum(hash(tuple(r)) for row in matrix) % p
print(rolling_hash_2d([[1, 2]]))