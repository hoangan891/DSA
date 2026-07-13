class FailFastArrayList:
    def __init__(self): self.arr, self.modCount = [], 0
    def add(self, val): self.arr.append(val); self.modCount += 1
    def get_iterator(self):
        expected = self.modCount
        for x in self.arr:
            if expected != self.modCount: raise Exception("ConcurrentModificationException")
            yield x
ff = FailFastArrayList(); ff.add(1); print(list(ff.get_iterator()))