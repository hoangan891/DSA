def count_inversions(arr):
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

arr = [2, 3, 1]
result = count_inversions(arr)
print("So nghich the bang so lan hoan doi va bang:", result)