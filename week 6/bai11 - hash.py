class CustomHashSet:
    def __init__(self): self.set = {}
    def add(self, val): self.set[val] = True
    def contains(self, val): return val in self.set
    def remove(self, val): self.set.pop(val, None)
hs = CustomHashSet()
hs.add(1); hs.add(1); print(list(hs.set.keys()))