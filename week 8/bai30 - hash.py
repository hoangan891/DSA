def jaccard_minhash_approx(set1, set2):
    return min([hash(x) for x in set1]) == min([hash(x) for x in set2])
print(jaccard_minhash_approx({1, 2}, {2, 3}))