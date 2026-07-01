class SimpleHash:
    def __init__(self, size=5): self.size, self.table = size, [[] for _ in range(size)]
    def put(self, k, v):
        idx = hash(k) % self.size
        for pair in self.table[idx]:
            if pair[0] == k: pair[1] = v; return
        self.table[idx].append([k, v])
    def get(self, k):
        idx = hash(k) % self.size
        for pair in self.table[idx]:
            if pair[0] == k: return pair[1]
        return None
h = SimpleHash(); h.put('a', 1); print(h.get('a'))