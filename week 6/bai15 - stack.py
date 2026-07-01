def sort_stack(stack):
    temp = []
    while stack:
        tmp = stack.pop()
        while temp and temp[-1] < tmp: stack.append(temp.pop())
        temp.append(tmp)
    return temp
print(sort_stack([3, 1, 2]))