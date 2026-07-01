def find_peak(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left

arr = [1, 2, 3, 1]
result = find_peak(arr)
print("vi tri dinh tim thay la:", result)