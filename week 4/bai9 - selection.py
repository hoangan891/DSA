def double_selection_sort(arr):
    n = len(arr)
    left = 0
    right = n - 1
    while left < right:
        min_idx = left
        max_idx = left
        for j in range(left + 1, right + 1):
            if arr[j] < arr[min_idx]:
                min_idx = j
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[left], arr[min_idx] = arr[min_idx], arr[left]
        if max_idx == left:
            max_idx = min_idx
        arr[right], arr[max_idx] = arr[max_idx], arr[right]
        left += 1
        right -= 1

arr = [5, 1, 4, 2, 8]
double_selection_sort(arr)
print(arr)