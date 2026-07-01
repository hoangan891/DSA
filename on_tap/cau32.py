def remove_if_even(arr):
    w = 0
    for r in range(len(arr)):
        if arr[r] % 2 != 0: arr[w] = arr[r]; w += 1
    return arr[:w]
print(remove_if_even([1, 2, 3, 4]))