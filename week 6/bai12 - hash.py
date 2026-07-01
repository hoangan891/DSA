def subarray_sum(arr, k):
    count = pref_sum = 0
    sums = {0: 1}
    for x in arr:
        pref_sum += x
        count += sums.get(pref_sum - k, 0)
        sums[pref_sum] = sums.get(pref_sum, 0) + 1
    return count
print(subarray_sum([1, 1, 1], 2))