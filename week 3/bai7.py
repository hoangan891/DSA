def bubble_sort_chars(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

arr = ['d', 'a', 'c', 'b']
bubble_sort_chars(arr)
print(arr)