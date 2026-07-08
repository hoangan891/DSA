class ResizingHash:
    def __init__(self): self.size, self.count, self.table = 4, 0, [[] for _ in range(4)]
    def put(self, k, v):
        idx = hash(k) % self.size; self.table[idx].append([k, v]); self.count += 1
        if self.count / self.size > 0.75:
            self.size *= 2; old = self.table; self.table = [[] for _ in range(self.size)]
            for b in old:
                for pair in b: self.table[hash(pair[0]) % self.size].append(pair)
rh = ResizingHash(); rh.put(1, 'a'); print(rh.size)