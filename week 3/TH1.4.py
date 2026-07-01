def bubbleSort_descending(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

arr = [25, 17, 7, 14, 6, 3, 100, -2, -10, -50]
print("Mạng chưa được sắp xếp là: ", arr)
bubbleSort_descending(arr)
print("Mạng được sắp xếp giảm dần là: ", arr)