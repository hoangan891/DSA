def bubble_sort_multi_keys(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j][1] < arr[j + 1][1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
            elif arr[j][1] == arr[j + 1][1]:
                if arr[j][0] > arr[j + 1][0]:
                    temp = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = temp

arr = [('An', 8), ('Ba', 9), ('Cu', 8)]
bubble_sort_multi_keys(arr)
print(arr)