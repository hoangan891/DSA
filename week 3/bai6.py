def last_element_after_one_pass(arr):
    n = len(arr)
    for j in range(0, n - 1):
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp
    return arr[n - 1]

arr = [4, 2, 7, 1, 3]
result = last_element_after_one_pass(arr)
print("Gia tri o vi tri cuoi cung la:", result)