def jaccard_minhash_approx(set1, set2):
    h1 = [hash(x) for x in set1]; h2 = [hash(x) for x in set2]
    return min(h1) == min(h2)
print(jaccard_minhash_approx({1, 2}, {2, 3}))