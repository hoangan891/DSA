def longest_consec(arr):
    s = set(arr); longest = 0
    for x in s:
        if x - 1 not in s:
            curr, streak = x, 1
            while curr + 1 in s: curr += 1; streak += 1
            longest = max(longest, streak)
    return longest
print(longest_consecutive([100, 4, 200, 1, 3, 2]))