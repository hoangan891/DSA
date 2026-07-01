def selection_sort_absolute(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if abs(arr[j]) < abs(arr[min_idx]):
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

arr = [-3, 1, -2, 2]
selection_sort_absolute(arr)
print(arr)