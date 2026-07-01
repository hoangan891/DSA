def analyze_performance(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                swaps += 1
    return comparisons, swaps

arr_random = [3, 1, 4, 2]
comp, swp = analyze_performance(arr_random)
print("So sanh:", comp, "Hoan doi:", swp)