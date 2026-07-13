def insertion_sort_students(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0:
            if arr[j][1] < key[1]:
                arr[j + 1] = arr[j]
                j -= 1
            elif arr[j][1] == key[1] and arr[j][0] > key[0]:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
        arr[j + 1] = key

arr = [('An', 8), ('Ba', 9), ('Cu', 8)]
insertion_sort_students(arr)
print(arr)