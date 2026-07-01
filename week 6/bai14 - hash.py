class LazyDeletionHash:
    def __init__(self, size=5):
        self.size, self.keys = size, [None]*size
    def remove(self, key):
        idx = hash(key) % self.size
        while self.keys[idx] is not None:
            if self.keys[idx] == key: self.keys[idx] = "TOMBSTONE"; return
            idx = (idx + 1) % self.size
ld = LazyDeletionHash()
ld.keys[0] = 'a'; ld.remove('a'); print(ld.keys[0])