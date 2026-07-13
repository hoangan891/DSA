class SimplePriorityQueue:
    def __init__(self): self.queue = []
    def push(self, item): self.queue.append(item); self.queue.sort()
    def pop(self): return self.queue.pop(0) if self.queue else None
pq = SimplePriorityQueue(); pq.push(3); pq.push(1); print(pq.pop())