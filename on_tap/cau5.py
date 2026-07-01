import math
def min_eating_speed(piles, h):
    def check(s): return sum(math.ceil(p / s) for p in piles) <= h
    low, high = 1, max(piles)
    res = high
    while low <= high:
        mid = (low + high) // 2
        if check(mid): res = mid; high = mid - 1
        else: low = mid + 1
    return res
print(min_eating_speed([3, 6, 7, 11], 8))