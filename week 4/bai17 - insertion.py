def insertion_sort_nearly_sorted(arr):
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

arr = [1, 2, 4, 3, 5]
print("So luong shift tren mang gan nhu da sap xep:", insertion_sort_nearly_sorted(arr))