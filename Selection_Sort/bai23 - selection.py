def analyze_selection_cases(arr):
    n = len(arr)
    comp = 0
    swaps = 0
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comp += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1
    return comp, swaps

arr_test = [3, 2, 1]
c, s = analyze_selection_cases(arr_test)
print("So sanh luon la O(n^2):", c, "So swap:", s)