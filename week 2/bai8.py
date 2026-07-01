def can_bac_hai(key):
    if key < 2:
        return key
    left = 1
    right = key // 2
    res = 1
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == key:
            return mid
        elif mid * mid < key:
            res = mid
            left = mid + 1
        else:
            right = mid - 1
    return res

key = 8
result = can_bac_hai(key)
print("Phan nguyen can bac hai la:", result)