def search_rotated(arr, key):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            return mid
        if arr[left] <= arr[mid]:
            if arr[left] <= key < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if arr[mid] < key <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

arr = [4, 5, 6, 7, 0, 1, 2]
key = 0
result = search_rotated(arr, key)
print("vi tri tim thay thu i la:", result)