def find_min_index_range(arr, i):
    n = len(arr)
    min_index = i
    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j
    return min_index

arr = [9, 3, 7, 1, 5]
print("Chi so phan tu nho nhat tu i=1:", find_min_index_range(arr, 1))