def ship_within_days(weights, days):
    def check(capacity):
        d = 1
        curr = 0
        for w in weights:
            if curr + w > capacity:
                d += 1
                curr = w
            else:
                curr += w
        return d <= days

    left = max(weights)
    right = sum(weights)
    res = right
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            res = mid
            right = mid - 1
        else:
            left = mid + 1
    return res

weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
days = 5
result = ship_within_days(weights, days)
print("Suc chua nho nhat la:", result)