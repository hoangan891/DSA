class BloomFilter:
    def __init__(self, size=100):
        self.size, self.bit_array = size, [0]*size
    def add(self, item):
        h1, h2 = hash(item) % self.size, hash(f"{item}-alt") % self.size
        self.bit_array[h1] = self.bit_array[h2] = 1
    def contains(self, item):
        h1, h2 = hash(item) % self.size, hash(f"{item}-alt") % self.size
        return self.bit_array[h1] == 1 and self.bit_array[h2] == 1
bf = BloomFilter()
bf.add("test"); print(bf.contains("test"))