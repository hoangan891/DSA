def binary_insertion_sort(arr):
    n = len(arr)
    comparisons = 0
    for i in range(1, n):
        key = arr[i]
        left = 0
        right = i - 1
        while left <= right:
            mid = (left + right) // 2
            comparisons += 1
            if key < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        j = i - 1
        while j >= left:
            arr[j + 1] = arr[j]
            j -= 1
        arr[left] = key
    return comparisons

arr = [4, 3, 2, 1]
print("So lan so sanh:", binary_insertion_sort(arr))