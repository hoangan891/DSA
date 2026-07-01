class ArrayList:
    def __init__(self): self.arr = []
    def add(self, val): self.arr.append(val)
    def get(self, idx): return self.arr[idx]
    def set(self, idx, val): self.arr[idx] = val
    def size(self): return len(self.arr)
al = ArrayList()
al.add(1)
print(al.get(0))