def bubble_sort_nearly_k_correct(arr, k):
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

arr = [2, 1, 3, 5, 4]
key_k = 1
result = bubble_sort_nearly_k_correct(arr, key_k)
print("Thuc thi o toc do nhanh voi so luot la:", result)