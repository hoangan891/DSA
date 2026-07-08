class ConsistentHashing:
    def __init__(self): self.ring = {}
    def add_server(self, server):
        for i in range(3): self.ring[hash(f"{server}-{i}")] = server
    def get_server(self, key):
        if not self.ring: return None
        h = hash(key)
        for k in sorted(self.ring.keys()):
            if h <= k: return self.ring[k]
        return self.ring[min(self.ring.keys())]
ch = ConsistentHashing(); ch.add_server("S1"); print(ch.get_server("key"))