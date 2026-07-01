def dfs_iterative(graph, start):
    visited, stack, res = set(), [start], []
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.add(v)
            res.append(v)
            for n in reversed(graph.get(v, [])):
                if n not in visited: stack.append(n)
    return res
g = {0: [1, 2], 1: [2], 2: [3], 3: []}
print(dfs_iterative(g, 0))