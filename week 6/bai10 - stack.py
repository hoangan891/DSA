from collections import deque
class QueueStack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
    def push(self, x):
        self.q2.append(x)
        while self.q1: self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1
    def pop(self):
        if self.q1: return self.q1.popleft()
qs = QueueStack()
qs.push(1)
qs.push(2)
print(qs.pop())