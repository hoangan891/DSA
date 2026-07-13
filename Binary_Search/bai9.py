def search_insert(arr, key):
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

arr = [1, 3, 5, 6]
key = 4
result = search_insert(arr, key)
print("vi tri chen thich hop la:", result)