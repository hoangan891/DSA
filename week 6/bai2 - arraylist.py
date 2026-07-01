class ListPopBack:
    def __init__(self): self.arr = []
    def append(self, val): self.arr.append(val)
    def popBack(self): return self.arr.pop() if self.arr else None
l = ListPopBack()
l.append(1)
print(l.popBack())