def linear_search(arr, val):
    try: return arr.index(val)
    except ValueError: return -1
print(linear_search([5, 3, 7], 7))