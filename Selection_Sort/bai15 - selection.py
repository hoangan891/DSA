def partial_selection_sort(arr, k):
    n = len(arr)
    for i in range(min(k, n)):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

arr = [5, 3, 1, 4, 2]
print(partial_selection_sort(arr, 2))