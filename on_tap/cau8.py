def bubble_sort_optimized(arr):
    n, rounds = len(arr), 0
    for i in range(n):
        swapped = False
        rounds += 1
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped: break
    return rounds
print("Vòng lặp chạy:", bubble_sort_optimized([1, 2, 3, 4]))