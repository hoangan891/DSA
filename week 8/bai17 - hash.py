def string_sum_hash(s, m): return sum(ord(c) for c in s) % m
print(string_sum_hash('abc', 10))