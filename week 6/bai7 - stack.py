class MinStack:
    def __init__(self):
        self.stack, self.min_stack = [], []
    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]: self.min_stack.append(val)
    def pop(self):
        if self.stack:
            val = self.stack.pop()
            if val == self.min_stack[-1]: self.min_stack.pop()
            return val
    def getMin(self): return self.min_stack[-1] if self.min_stack else None
ms = MinStack()
ms.push(5); ms.push(3); print(ms.getMin())