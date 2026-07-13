def stable_sort_records(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j][0] > arr[j + 1][0]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

arr = [(2, "Label A"), (1, "Label B"), (2, "Label C")]
stable_sort_records(arr)
print(arr)