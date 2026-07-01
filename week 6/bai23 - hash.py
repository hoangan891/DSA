def distribution_check(keys, m):
    b = [0]*m
    for k in keys: b[hash(k)%m] += 1
    return b
print(distribution_check([1, 2, 3, 11, 12], 10))