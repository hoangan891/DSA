def kth_smallest_element(arr, k):
    n = len(arr)
    for i in range(k):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr[k - 1]

arr = [7, 2, 5, 1, 9]
print("Phan tu nho thu k=3 la:", kth_smallest_element(arr, 3))