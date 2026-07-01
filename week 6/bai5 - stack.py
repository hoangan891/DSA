def print_and_count_stack(stack):
    temp = []
    count = 0
    while stack:
        val = stack.pop()
        print(val, end=" ")
        temp.append(val)
        count += 1
    print()
    while temp: stack.append(temp.pop())
    return count
s = [1, 2, 3]
print("So phan tu:", print_and_count_stack(s))