def allocate_books(arr, m):
    if m > len(arr):
        return -1
    def check(max_pages):
        students = 1
        curr_pages = 0
        for pages in arr:
            if curr_pages + pages > max_pages:
                students += 1
                curr_pages = pages
            else:
                curr_pages += pages
        return students <= m

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

arr = [12, 34, 67, 90]
m = 2
result = allocate_books(arr, m)
print("Gia tri nho nhat la:", result)