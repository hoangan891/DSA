def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        l, h = 0, j = i - 1
        while l <= h:
            m = (l + h) // 2
            if arr[m] > key: h = m - 1
            else: l = m + 1
        while j >= l: arr[j + 1] = arr[j]; j -= 1
        arr[l] = key
    return arr
print(binary_insertion_sort([3, 2, 1]))