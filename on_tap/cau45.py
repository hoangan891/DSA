def sub_sum_k(arr, k):
    count = pref = 0; mapping = {0: 1}
    for x in arr:
        pref += x
        count += mapping.get(pref - k, 0)
        mapping[pref] = mapping.get(pref, 0) + 1
    return count
print(sub_sum_k([1, 1, 1], 2))