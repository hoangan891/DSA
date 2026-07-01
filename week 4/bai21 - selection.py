def selection_sort_fixed_comparisons(arr):
    n = len(arr)
    comp = 0
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comp += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return comp

arr_best = [1, 2, 3, 4, 5]
print("So phep so sanh luon la n(n-1)/2 =", selection_sort_fixed_comparisons(arr_best))