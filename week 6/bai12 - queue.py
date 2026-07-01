def josephus(n, k):
    q = list(range(1, n + 1))
    while len(q) > 1:
        for _ in range(k - 1): q.append(q.pop(0))
        q.pop(0)
    return q[0]
print(josephus(5, 2))