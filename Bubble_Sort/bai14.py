def cocktail_shaker_sort(arr):
    n = len(arr)
    start = 0
    end = n - 1
    passes = 0
    while start < end:
        swapped = False
        passes += 1
        for j in range(start, end):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                swapped = True
        if not swapped:
            break
        
        end -= 1
        swapped = False
        for j in range(end - 1, start - 1, -1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                swapped = True
        start += 1
        if not swapped:
            break
    return passes

arr = [5, 1, 4, 2, 8]
result = cocktail_shaker_sort(arr)
print(arr, "chay trong:", result, "luot")