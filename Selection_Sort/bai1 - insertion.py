def insert_element_sorted(arr, key):
    arr.append(key)
    j = len(arr) - 2
    while j >= 0 and key < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key

arr = [1, 3, 5, 7]
key = 4
insert_element_sorted(arr, key)
print(arr)