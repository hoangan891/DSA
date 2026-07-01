def remove_dup(arr):
    seen = set()
    return [x for x in arr if not (x in seen or seen.add(x))]
print(remove_dup([3, 1, 3, 2, 1]))