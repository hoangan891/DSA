def partial_bubble_sort(arr, k):
    n = len(arr)
    for i in range(k):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr

arr = [3, 1, 4, 1, 5]
key_k = 2
result = partial_bubble_sort(arr, key_k)
print(result)