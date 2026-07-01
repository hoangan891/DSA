class Stack:
    def __init__(self, capacity=1000):
        self.capacity = capacity
        self.stack = [0] * capacity
        self.top_idx = -1
    def push(self, data):
        if self.top_idx >= self.capacity - 1: return None
        self.top_idx += 1
        self.stack[self.top_idx] = data
        return True
    def pop(self):
        if self.isEmpty(): return None
        data = self.stack[self.top_idx]
        self.top_idx -= 1
        return data
    def top(self):
        if self.isEmpty(): return None
        return self.stack[self.top_idx]
    def isEmpty(self): return self.top_idx == -1

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.pop())