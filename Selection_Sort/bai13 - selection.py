def selection_sort_students(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j][1] < arr[min_index][1]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

arr = [('An', 8), ('Ba', 5)]
selection_sort_students(arr)
print(arr)