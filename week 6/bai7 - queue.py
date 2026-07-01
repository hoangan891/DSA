def reverse_queue(q):
    stack = []
    while q: stack.append(q.pop(0))
    while stack: q.append(stack.pop())
    return q
print(reverse_queue([1, 2, 3]))