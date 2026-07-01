def count_inversions_by_shift(arr):
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

arr = [2, 4, 1, 3]
print("So nghich the (so shift):", count_inversions_by_shift(arr))