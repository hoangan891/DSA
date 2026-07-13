def analyze_insertion_performance(arr):
    n = len(arr)
    comparisons = 0
    shifts = 0
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
                shifts += 1
            else:
                break
        arr[j + 1] = key
    return comparisons, shifts

arr_test = [3, 2, 1]
comp, shf = analyze_insertion_performance(arr_test)
print("So sanh:", comp, "Dich chuyen:", shf)