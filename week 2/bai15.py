def find_closest_elements(arr, k, key):
    left = 0
    right = len(arr) - k
    while left < right:
        mid = (left + right) // 2
        if key - arr[mid] > arr[mid + k] - key:
            left = mid + 1
        else:
            right = mid
    return arr[left : left + k]

arr = [1, 2, 3, 4, 5]
k = 4
key = 3
result = find_closest_elements(arr, k, key)
print("Danh sach cac phan tu gan nhat la:", result)