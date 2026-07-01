def selection_sort_count_swaps(arr):
    n = len(arr)
    swaps = 0
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        swaps += 1
    return swaps

arr = [3, 2, 1]
print("So lan hoan doi:", selection_sort_count_swaps(arr))