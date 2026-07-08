class QuadraticProbingHash:
    def __init__(self, size=11): self.size, self.keys = size, [None]*size
    def put(self, key):
        idx, i = hash(key) % self.size, 0
        while self.keys[(idx + i*i) % self.size] is not None: i += 1
        self.keys[(idx + i*i) % self.size] = key
qp = QuadraticProbingHash(); qp.put('a'); print(qp.keys)