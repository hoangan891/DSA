def insertion_sort_stability_pairs(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key[0] < arr[j][0]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = [(2, 'a'), (1, 'b'), (2, 'c')]
insertion_sort_stability_pairs(arr)
print(arr)