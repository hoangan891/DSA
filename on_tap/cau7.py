def bubble_sort_count(arr):
    n, swaps = len(arr), 0
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
    return swaps
print("Swaps:", bubble_sort_count([2, 3, 1]))