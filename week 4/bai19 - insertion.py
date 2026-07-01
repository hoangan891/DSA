def gnome_sort(arr):
    n = len(arr)
    idx = 0
    while idx < n:
        if idx == 0:
            idx += 1
        if arr[idx] >= arr[idx - 1]:
            idx += 1
        else:
            arr[idx], arr[idx - 1] = arr[idx - 1], arr[idx]
            idx -= 1

arr = [3, 2, 1]
gnome_sort(arr)
print(arr)