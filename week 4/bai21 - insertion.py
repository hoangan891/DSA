def get_shifts_large_array(arr):
    def merge_sort(arr, temp_arr, left, right):
        inv_count = 0
        if left < right:
            mid = (left + right) // 2
            inv_count += merge_sort(arr, temp_arr, left, mid)
            inv_count += merge_sort(arr, temp_arr, mid + 1, right)
            inv_count += merge(arr, temp_arr, left, mid, right)
        return inv_count

    def merge(arr, temp_arr, left, mid, right):
        i, j, k = left, mid + 1, left
        inv_count = 0
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp_arr[k] = arr[i]
                i += 1
            else:
                temp_arr[k] = arr[j]
                inv_count += (mid - i + 1)
                j += 1
            k += 1
        while i <= mid:
            temp_arr[k] = arr[i]
            i += 1
            k += 1
        while j <= right:
            temp_arr[k] = arr[j]
            j += 1
            k += 1
        for loop_i in range(left, right + 1):
            arr[loop_i] = temp_arr[loop_i]
        return inv_count

    temp = [0] * len(arr)
    return merge_sort(arr, temp, 0, len(arr) - 1)

arr = [2, 4, 1, 3]
print("Tong so shift tinh nhanh bang:", get_shifts_large_array(arr))