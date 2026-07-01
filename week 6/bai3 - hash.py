def count_frequencies(arr):
    freq = {}
    for x in arr: freq[x] = freq.get(x, 0) + 1
    return freq
print(count_frequencies(['a', 'b', 'a', 'c', 'a']))