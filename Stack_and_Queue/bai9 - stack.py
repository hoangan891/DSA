def infix_to_postfix(expr):
    prec = {"+": 1, "-": 1, "*": 2, "/": 2}
    stack, postfix = [], []
    for char in expr:
        if char.isalnum(): postfix.append(char)
        elif char in prec:
            while stack and stack[-1] in prec and prec[stack[-1]] >= prec[char]: postfix.append(stack.pop())
            stack.append(char)
    while stack: postfix.append(stack.pop())
    return "".join(postfix)
print(infix_to_postfix("a+b*c"))