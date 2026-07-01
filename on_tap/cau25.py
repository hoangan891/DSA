def max_histogram(heights):
    stack, max_a, i = [], 0, 0
    while i < len(heights):
        if not stack or heights[stack[-1]] <= heights[i]: stack.append(i); i += 1
        else:
            tp = stack.pop()
            w = (i - stack[-1] - 1) if stack else i
            max_a = max(max_a, heights[tp] * w)
    while stack:
        tp = stack.pop()
        w = (i - stack[-1] - 1) if stack else i
        max_a = max(max_a, heights[tp] * w)
    return max_a
print(max_histogram([2, 1, 5, 6, 2, 3]))