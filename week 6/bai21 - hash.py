def rabin_karp(text, pattern):
    m, n = len(pattern), len(text)
    p_hash, t_hash = hash(pattern), hash(text[:m])
    for i in range(n - m + 1):
        if p_hash == t_hash and text[i:i+m] == pattern: return i
        if i < n - m: t_hash = hash(text[i+1:i+1+m])
    return -1
print(rabin_karp("zabcd", "abc"))