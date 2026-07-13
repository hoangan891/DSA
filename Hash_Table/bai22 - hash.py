def hash_combine(a, b):
    return hash(a) ^ (hash(b) + 0x9e3779b9 + (hash(a) << 6) + (hash(a) >> 2))
print(hash_combine(1, 2))