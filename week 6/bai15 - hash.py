import heapq
class ConsistentHashing:
    def __init__(self): self.ring = {}
    def add_server(self, server):
        for i in range(3):
            val = hash(f"{server}-node-{i}"); self.ring[val] = server
    def get_server(self, key):
        if not self.ring: return None
        h_val = hash(key)
        for k in sorted(self.ring.keys()):
            if h_val <= k: return self.ring[k]
        return self.ring[min(self.ring.keys())]
ch = ConsistentHashing()
ch.add_server("Server1"); print(ch.get_server("my_key"))