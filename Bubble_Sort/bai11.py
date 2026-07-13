def bubble_sort_absolute(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if abs(arr[j]) > abs(arr[j + 1]):
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

arr = [-3, 1, 2, 2]
bubble_sort_absolute(arr)
print(arr)