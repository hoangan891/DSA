def lower_bound(arr, x):
    l, h, res = 0, len(arr) - 1, len(arr)
    while l <= h:
        m = (l + h) // 2
        if arr[m] >= x: res = m; h = m - 1
        else: l = m + 1
    return res
def upper_bound(arr, x):
    l, h, res = 0, len(arr) - 1, len(arr)
    while l <= h:
        m = (l + h) // 2
        if arr[m] > x: res = m; h = m - 1
        else: l = m + 1
    return res
print("Lower:", lower_bound([1, 3, 5, 7], 4))