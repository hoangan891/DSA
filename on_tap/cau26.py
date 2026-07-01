class CircularQueue:
    def __init__(self, k):
        self.k, self.queue = k, [0]*k
        self.f = self.r = -1
    def enqueue(self, val):
        if (self.r + 1) % self.k == self.f: return False
        if self.f == -1: self.f = self.r = 0
        else: self.r = (self.r + 1) % self.k
        self.queue[self.r] = val; return True
    def dequeue(self):
        if self.f == -1: return None
        res = self.queue[self.f]
        if self.f == self.r: self.f = self.r = -1
        else: self.f = (self.f + 1) % self.k
        return res
cq = CircularQueue(3); cq.enqueue(1); print(cq.dequeue())