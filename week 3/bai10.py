def count_total_passes(arr):
    n = len(arr)
    passes = 0
    for i in range(n - 1):
        swapped = False
        passes += 1
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                swapped = True
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
        if not swapped:
            break
    return passes

arr = [2, 1, 3, 4]
result = count_total_passes(arr)
print("So luot can thiet la:", result)