def bubble_sort_stability_test(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j][0] > arr[j + 1][0]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

arr = [(2, 'a'), (1, 'b'), (2, 'c')]
bubble_sort_stability_test(arr)
print(arr)