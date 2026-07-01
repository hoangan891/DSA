def check_sorted_after_k_passes(arr, k):
    n = len(arr)
    for i in range(min(k, n)):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

arr = [3, 2, 1]
key_k = 1
result = check_sorted_after_k_passes(arr, key_k)
print("Mang da sap xep hoan toan chua:", result)