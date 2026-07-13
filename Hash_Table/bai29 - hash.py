class BloomFilter:
    def __init__(self, size=100): self.size, self.bit_array = size, [0]*size
    def add(self, item):
        self.bit_array[hash(item) % self.size] = 1
        self.bit_array[hash(f"{item}-alt") % self.size] = 1
    def contains(self, item):
        return self.bit_array[hash(item) % self.size] == 1 and self.bit_array[hash(f"{item}-alt") % self.size] == 1
bf = BloomFilter(); bf.add("test"); print(bf.contains("test"))