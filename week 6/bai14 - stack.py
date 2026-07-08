def calculate_span(prices):
    span, stack = [0] * len(prices), []
    for i in range(len(prices)):
        while stack and prices[stack[-1]] <= prices[i]: stack.pop()
        span[i] = i + 1 if not stack else i - stack[-1]
        stack.append(i)
    return span
print(calculate_span([100, 80, 60, 75, 85]))