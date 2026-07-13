def count_swaps(arr):
    n = len(arr)
    swaps = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                swaps += 1
    return swaps

arr = [3, 2, 1]
result = count_swaps(arr)
print("Tong so lan hoan doi la:", result)