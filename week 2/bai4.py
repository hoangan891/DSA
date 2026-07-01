def binary_search(arr, key):
    left = 0
    right = len(arr) - 1
    res = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            res = mid
            left = mid + 1
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return res

arr = [1, 2, 2, 2, 3]
key = 2
result = binary_search(arr, key)
print("vi tri tim thay thu i la:", result)