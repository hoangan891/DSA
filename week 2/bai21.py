def split_array(arr, k):
    def check(max_sum):
        splits = 1
        curr_sum = 0
        for num in arr:
            if curr_sum + num > max_sum:
                splits += 1
                curr_sum = num
            else:
                curr_sum += num
        return splits <= k

    left = max(arr)
    right = sum(arr)
    res = right
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            res = mid
            right = mid - 1
        else:
            left = mid + 1
    return res

arr = [7, 2, 5, 10, 8]
k = 2
result = split_array(arr, k)
print("Tong lon nhat nho nhat la:", result)