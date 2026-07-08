class BoundedStack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.stack = []
    def push(self, val):
        if len(self.stack) >= self.max_size: raise Exception("Overflow Error")
        self.stack.append(val)
    def pop(self):
        if not self.stack: raise Exception("Underflow Error")
        return self.stack.pop()
s = BoundedStack(2)
s.push(1)
try: s.push(3)
except Exception as e: print(e)