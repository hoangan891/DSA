class BoundedQueue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = []
    def enqueue(self, val):
        if len(self.queue) >= self.max_size: raise Exception("Queue Overflow")
        self.queue.append(val)
    def dequeue(self):
        if not self.queue: raise Exception("Queue Underflow")
        return self.queue.pop(0)
bq = BoundedQueue(2)
bq.enqueue(5)
print(len(bq.queue))