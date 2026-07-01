def lower_bound(arr, key):
    left = 0
    right = len(arr) - 1
    res = len(arr)
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= key:
            res = mid
            right = mid - 1
        else:
            left = mid + 1
    return res

arr = [1, 3, 5, 7]
key = 4
result = lower_bound(arr, key)
print("vi tri tim thay thu i la:", result)