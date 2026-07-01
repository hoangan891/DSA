def bubble_sort_one_pass(arr):
    n = len(arr)
    for j in range(0, n - 1):
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

arr = [5, 1, 4, 2, 8]
bubble_sort_one_pass(arr)
print(arr)