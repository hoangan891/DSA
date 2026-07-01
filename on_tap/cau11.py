def selection_sort_count(arr):
    n, comps = len(arr), 0
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comps += 1
            if arr[j] < arr[min_idx]: min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return comps
print("Số phép so sánh luon bang n(n-1)/2:", selection_sort_count([5, 4, 3, 2, 1]))