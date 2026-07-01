def select_first_min(arr):
    n = len(arr)
    if n > 0:
        min_idx = 0
        for j in range(1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[0], arr[min_idx] = arr[min_idx], arr[0]

arr = [4, 2, 7, 1, 3]
select_first_min(arr)
print(arr)