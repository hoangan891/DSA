def merge_sorted_lists(l1, l2):
    res, i, j = [], 0, 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]: res.append(l1[i]); i += 1
        else: res.append(l2[j]); j += 1
    res.extend(l1[i:]); res.extend(l2[j:])
    return res
print(merge_sorted_lists([1, 3, 5], [2, 4]))