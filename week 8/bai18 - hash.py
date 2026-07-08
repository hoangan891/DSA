def poly_rolling_hash(s, p=31, m=10**9+7):
    h = 0
    for c in s: h = (h * p + ord(c)) % m
    return h
print(poly_rolling_hash("abc"))