def group_by_first_letter(words):
    groups = {}
    for w in words: groups.setdefault(w[0], []).append(w)
    return groups
print(group_by_first_letter(['abc', 'apple', 'bat']))