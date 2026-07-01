def get_intersection(arr1, arr2):
    return list(set(arr1) & set(arr2))
print(get_intersection([1, 2, 3], [2, 3, 4]))