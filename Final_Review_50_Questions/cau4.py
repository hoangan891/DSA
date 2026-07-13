def search_rotated(arr, x):
    l, h = 0, len(arr) - 1
    while l <= h:
        m = (l + h) // 2
        if arr[m] == x: return m
        if arr[l] <= arr[m]:
            if arr[l] <= x < arr[m]: h = m - 1
            else: l = m + 1
        else:
            if arr[m] < x <= arr[h]: l = m + 1
            else: h = m - 1
    return -1
print(search_rotated([4, 5, 6, 7, 0, 1, 2], 0))