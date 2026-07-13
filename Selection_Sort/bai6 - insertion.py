def insertion_sort_count_comparisons(arr):
    n = len(arr)
    comparisons = 0
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
        arr[j + 1] = key
    return comparisons

arr = [1, 2, 3]
print(insertion_sort_count_comparisons(arr))