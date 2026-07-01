def two_sum(arr, target):
    seen = {}
    for i, x in enumerate(arr):
        if target - x in seen: return (seen[target - x], i)
        seen[x] = i
print(two_sum([2, 7, 11], 9))