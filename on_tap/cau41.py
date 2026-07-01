class DNode:
    def __init__(self, k, v): self.k, self.v = k, v; self.prev = self.next = None
class LRUCache:
    def __init__(self, cap):
        self.cap, self.cache = cap, {}
        self.head, self.tail = DNode(0,0), DNode(0,0)
        self.head.next = self.tail; self.tail.prev = self.head
    def _remove(self, n): p, nxt = n.prev, n.next; p.next, nxt.prev = nxt, p
    def _add(self, n): nxt = self.head.next; self.head.next = n; n.prev = self.head; n.next = nxt; nxt.prev = n
    def get(self, k):
        if k in self.cache: node = self.cache[k]; self._remove(node); self._add(node); return node.v
        return -1
    def put(self, k, v):
        if k in self.cache: self._remove(self.cache[k])
        node = DNode(k, v); self._add(node); self.cache[k] = node
        if len(self.cache) > self.cap: lru = self.tail.prev; self._remove(lru); del self.cache[lru.k]
cache = LRUCache(2); cache.put(1, 10); print(cache.get(1))