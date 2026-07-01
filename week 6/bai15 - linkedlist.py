class DNode:
    def __init__(self, k, v): self.key = k; self.val = v; self.prev = self.next = None
class LRUCache:
    def __init__(self, capacity):
        self.capacity, self.cache = capacity, {}
        self.head, self.tail = DNode(0, 0), DNode(0, 0)
        self.head.next = self.tail; self.tail.prev = self.head
    def _remove(self, node):
        p, n = node.prev, node.next; p.next, n.prev = n, p
    def _add(self, node):
        n = self.head.next; self.head.next = node; node.prev = self.head; n.prev = node; node.next = n
    def get(self, key):
        if key in self.cache:
            node = self.cache[key]; self._remove(node); self._add(node); return node.val
        return -1
    def put(self, key, value):
        if key in self.cache: self._remove(self.cache[key])
        node = DNode(key, value); self._add(node); self.cache[key] = node
        if len(self.cache) > self.capacity:
            lru = self.tail.prev; self._remove(lru); del self.cache[lru.key]
cache = LRUCache(2)
cache.put(1, 1); print(cache.get(1))