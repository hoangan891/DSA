class CustomHashSet:
    def __init__(self): self.set = {}
    def add(self, val): self.set[val] = True
    def contains(self, val): return val in self.set
hs = CustomHashSet(); hs.add(1); print(hs.contains(1))