def insertion_sort_k_bounded(arr, k):
    n = len(arr)
    shifts = 0
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            shifts += 1
        arr[j + 1] = key
    return shifts

arr = [2, 1, 3, 5, 4]
print("So shift trong mang lech k la:", insertion_sort_k_bounded(arr, 1))