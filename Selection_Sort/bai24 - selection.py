def partial_selection_vs_heap(arr, k):
    n = len(arr)
    for i in range(k):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr[:k]

arr = [7, 2, 5, 1, 9]
print("K phan tu nho nhat bang selection:", partial_selection_vs_heap(arr, 3))