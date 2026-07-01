class Queue:
    def __init__(self): self.queue = []
    def enqueue(self, data): self.queue.append(data)
    def dequeue(self):
        if self.isEmpty(): return None
        return self.queue.pop(0)
    def front(self):
        if self.isEmpty(): return None
        return self.queue[0]
    def isEmpty(self): return len(self.queue) == 0
q = Queue()
q.enqueue(1)
print(q.dequeue())