def bfs_tree(graph, start):
    visited, queue, res = set([start]), [start], []
    while queue:
        v = queue.pop(0); res.append(v)
        for n in graph.get(v, []):
            if n not in visited: visited.add(n); queue.append(n)
    return res
print(bfs_tree({0: [1, 2], 1: [], 2: []}, 0))