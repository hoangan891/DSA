def minimize_max_dist(arr, k):
    def check(max_dist):
        added = 0
        for i in range(len(arr) - 1):
            added += int((arr[i + 1] - arr[i]) / max_dist)
        return added <= k

    left = 0.0
    right = float(arr[-1] - arr[0])
    while right - left > 1e-6:
        mid = (left + right) / 2.0
        if check(mid):
            right = mid
        else:
            left = mid
    return round(left, 6)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 9
result = minimize_max_dist(arr, k)
print("Khoang cach lon nhat nho nhat la:", result)