def count_swaps_fast(arr):
    def merge_sort_count(arr, temp_arr, left, right):
        inv_count = 0
        if left < right:
            mid = (left + right) // 2
            inv_count += merge_sort_count(arr, temp_arr, left, mid)
            inv_count += merge_sort_count(arr, temp_arr, mid + 1, right)
            inv_count += merge(arr, temp_arr, left, mid, right)
        return inv_count

    def merge(arr, temp_arr, left, mid, right):
        i = left
        j = mid + 1
        k = left
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
    return merge_sort_count(arr, temp, 0, len(arr) - 1)

arr = [2, 3, 1]
result = count_swaps_fast(arr)
print("Tong so lan swap tinh theo O(n log n) la:", result)