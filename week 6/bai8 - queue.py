class CustomDeque:
    def __init__(self): self.items = []
    def pushFront(self, x): self.items.insert(0, x)
    def pushBack(self, x): self.items.append(x)
    def popFront(self): return self.items.pop(0) if self.items else None
    def popBack(self): return self.items.pop() if self.items else None
dq = CustomDeque()
dq.pushFront(1)
print(dq.items)