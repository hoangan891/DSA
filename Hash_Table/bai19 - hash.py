def count_collisions(keys, m):
    buckets = [0]*m
    for k in keys: buckets[hash(k) % m] += 1
    return sum(x - 1 for x in buckets if x > 1)
print(count_collisions([10, 20, 30], 10))