def split_array(arr, k):
    def check(max_sum):
        segments, curr_sum = 1, 0
        for x in arr:
            if curr_sum + x > max_sum: segments += 1; curr_sum = x
            else: curr_sum += x
        return segments <= k
    low, high = max(arr), sum(arr)
    res = high
    while low <= high:
        mid = (low + high) // 2
        if check(mid): res = mid; high = mid - 1
        else: low = mid + 1
    return res
print(split_array([7, 2, 5, 10, 8], 2))