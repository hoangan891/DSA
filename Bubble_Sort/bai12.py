def bubble_sort_string_length(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if len(arr[j]) > len(arr[j + 1]):
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

arr = ['abc', 'a', 'ab']
bubble_sort_string_length(arr)
print(arr)