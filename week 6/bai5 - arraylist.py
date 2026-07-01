def count_even(arr):
    return sum(1 for x in arr if x % 2 == 0)
print(count_even([1, 2, 3, 4]))