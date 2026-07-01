def next_greater_element(arr):
    res = [-1] * len(arr)
    stack = []
    for i in range(len(arr)):
        while stack and arr[stack[-1]] < arr[i]: res[stack.pop()] = arr[i]
        stack.append(i)
    return res
print(next_greater_element([2, 1, 3]))