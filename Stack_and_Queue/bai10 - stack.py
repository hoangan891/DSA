from collections import deque
class QueueStack:
    def __init__(self): self.q1, self.q2 = deque(), deque()
    def push(self, x):
        self.q2.append(x)
        while self.q1: self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1
    def pop(self): return self.q1.popleft() if self.q1 else None
qs = QueueStack(); qs.push(1); print(qs.pop())