class CircularQueue:
    def __init__(self, k):
        self.k, self.queue = k, [0] * k
        self.front = self.rear = -1
    def enqueue(self, val):
        if ((self.rear + 1) % self.k == self.front): return False
        if (self.front == -1): self.front = self.rear = 0
        else: self.rear = (self.rear + 1) % self.k
        self.queue[self.rear] = val
        return True
    def dequeue(self):
        if (self.front == -1): return None
        res = self.queue[self.front]
        if (self.front == self.rear): self.front = self.rear = -1
        else: self.front = (self.front + 1) % self.k
        return res
cq = CircularQueue(4)
print(cq.enqueue(10))