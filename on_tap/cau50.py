class BloomFilter:
    def __init__(self, size=50): self.size, self.bits = size, [0]*size
    def add(self, item):
        self.bits[hash(item) % self.size] = 1
        self.bits[hash(f"{item}-alt") % self.size] = 1
    def contains(self, item):
        return self.bits[hash(item) % self.size] == 1 and self.bits[hash(f"{item}-alt") % self.size] == 1
bf = BloomFilter(); bf.add("hello"); print(bf.contains("hello"))