def print_and_count_stack(stack):
    temp, count = [], 0
    while stack:
        val = stack.pop(); print(val, end=" ")
        temp.append(val); count += 1
    print()
    while temp: stack.append(temp.pop())
    return count
print("So phan tu:", print_and_count_stack([1, 2, 3]))