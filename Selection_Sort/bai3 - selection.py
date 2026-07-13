def selection_sort_descending(arr):
    n = len(arr)
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if arr[max_idx] < arr[j]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]

arr = [5, 2, 4, 6, 1]
selection_sort_descending(arr)
print(arr)