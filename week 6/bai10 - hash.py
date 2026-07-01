def first_uniq_char(s):
    freq = {}
    for c in s: freq[char] = freq.get(c, 0) + 1
    for i, c in enumerate(s):
        if freq[c] == 1: return i
    return -1
print(first_uniq_char('leetcode'))