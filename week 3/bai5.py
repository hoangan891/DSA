def count_comparisons(arr):
    n = len(arr)
    comparisons = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return comparisons

arr = [1, 2, 3]
result = count_comparisons(arr)
print("Tong so lan so sanh la:", result)