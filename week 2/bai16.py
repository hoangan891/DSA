def min_eating_speed(piles, h):
    def check(speed):
        hours = 0
        for p in piles:
            hours += (p + speed - 1) // speed
        return hours <= h

    left = 1
    right = max(piles)
    res = right
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            res = mid
            right = mid - 1
        else:
            left = mid + 1
    return res

piles = [3, 6, 7, 11]
h = 8
result = min_eating_speed(piles, h)
print("Toc do nho nhat la:", result)