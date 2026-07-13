class LinearProbingHash:
    def __init__(self, size=10): self.size, self.keys, self.vals = size, [None]*size, [None]*size
    def put(self, key, val):
        idx = hash(key) % self.size
        while self.keys[idx] is not None:
            if self.keys[idx] == key: self.vals[idx] = val; return
            idx = (idx + 1) % self.size
        self.keys[idx], self.vals[idx] = key, val
    def get(self, key):
        idx = hash(key) % self.size
        while self.keys[idx] is not None:
            if self.keys[idx] == key: return self.vals[idx]
            idx = (idx + 1) % self.size
        return None
lp = LinearProbingHash(); lp.put('a', 10); print(lp.get('a'))