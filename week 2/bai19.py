def aggressive_cows(arr, c):
    arr.sort()
    def check(dist):
        count = 1
        last = arr[0]
        for i in range(1, len(arr)):
            if arr[i] - last >= dist:
                count += 1
                last = arr[i]
                if count >= c:
                    return True
        return False

    left = 1
    right = arr[-1] - arr[0]
    res = 0
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            res = mid
            left = mid + 1
        else:
            right = mid - 1
    return res

arr = [1, 2, 4, 8, 9]
c = 3
result = aggressive_cows(arr, c)
print("Khoang cach lon nhat la:", result)