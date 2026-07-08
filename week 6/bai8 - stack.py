def evaluate_postfix(expr):
    stack = []
    for token in expr.split():
        if token in "+-*/":
            b, a = stack.pop(), stack.pop()
            if token == "+": stack.append(a + b)
            elif token == "-": stack.append(a - b)
            elif token == "*": stack.append(a * b)
            elif token == "/": stack.append(int(a / b))
        else: stack.append(int(token))
    return stack[0]
print(evaluate_postfix("3 4 +"))