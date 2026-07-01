def poly_hash(s, p=31, m=10**9+7):
    h_val = 0
    for c in s: h_val = (h_val * p + ord(c)) % m
    return h_val
print(poly_hash("abc"))