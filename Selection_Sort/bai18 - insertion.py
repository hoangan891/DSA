def insertion_sort_strategies(arr):
    n = len(arr)
    comp_right_to_left = 0
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0:
            comp_right_to_left += 1
            if key < arr[j]:
                j -= 1
            else:
                break
    return comp_right_to_left

arr = [1, 2, 3, 5, 4]
print("So phep so sanh tu phai sang trai:", insertion_sort_strategies(arr))