class HashTableChaining:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
    def put(self, key, val):
        idx = hash(key) % self.size
        for pair in self.table[idx]:
            if pair[0] == key: pair[1] = val; return
        self.table[idx].append([key, val])
    def get(self, key):
        idx = hash(key) % self.size
        for pair in self.table[idx]:
            if pair[0] == key: return pair[1]
        return None
ht = HashTableChaining()
ht.put('a', 1)
print(ht.get('a'))