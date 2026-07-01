def insertion_sort_k_steps(arr, k):
    n = len(arr)
    for i in range(1, min(k + 1, n)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = [4, 3, 2, 1]
insertion_sort_k_steps(arr, 1)
print(arr)