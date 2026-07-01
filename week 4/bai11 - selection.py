def selection_sort_unstable_demo(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j][0] < arr[min_idx][0]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

arr = [(2, 'a'), (2, 'b'), (1, 'c')]
selection_sort_unstable_demo(arr)
print(arr)