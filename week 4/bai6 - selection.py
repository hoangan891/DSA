def selection_sort_total_comparisons(arr):
    n = len(arr)
    comparisons = 0
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return comparisons

arr = [5, 4, 3, 2, 1]
print("So lan so sanh:", selection_sort_total_comparisons(arr))