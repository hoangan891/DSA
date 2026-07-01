def round_robin(tasks, quantum):
    q = [[i, t] for i, t in enumerate(tasks)]
    time, res = 0, {}
    while q:
        idx, rem = q.pop(0)
        if rem <= quantum: time += rem; res[idx] = time
        else: time += quantum; q.append([idx, rem - quantum])
    return res
print(round_robin([4, 2, 3], 2))