def find_first_last(arr, x):
    def find_first():
        l, h, res = 0, len(arr) - 1, -1
        while l <= h:
            m = (l + h) // 2
            if arr[m] == x: res = m; h = m - 1
            elif arr[m] < x: l = m + 1
            else: h = m - 1
        return res
    def find_last():
        l, h, res = 0, len(arr) - 1, -1
        while l <= h:
            m = (l + h) // 2
            if arr[m] == x: res = m; l = m + 1
            elif arr[m] < x: l = m + 1
            else: h = m - 1
        return res
    f, last = find_first(), find_last()
    count = last - f + 1 if f != -1 else 0
    return f, last, count
print(find_first_last([1, 2, 2, 2, 3], 2))