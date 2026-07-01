def magnetic_force(arr, m):
    arr.sort()
    def check(min_force):
        count = 1
        last = arr[0]
        for i in range(1, len(arr)):
            if arr[i] - last >= min_force:
                count += 1
                last = arr[i]
                if count >= m:
                    return True
        return False

    left = 1
    right = arr[-1] - arr[0]
    res = 1
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            res = mid
            left = mid + 1
        else:
            right = mid - 1
    return res

arr = [1, 2, 3, 4, 7]
m = 3
result = magnetic_force(arr, m)
print("Luc tu lon nhat la:", result)