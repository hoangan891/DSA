def insertion_sort_absolute(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and abs(key) < abs(arr[j]):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = [-3, 1, 2, 2]
insertion_sort_absolute(arr)
print(arr)