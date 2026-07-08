import random
class UniversalHash:
    def __init__(self, m, p=1000003):
        self.m, self.p, self.a, self.b = m, p, random.randint(1, p-1), random.randint(0, p-1)
    def hash(self, k): return ((self.a * k + self.b) % self.p) % self.m
print(UniversalHash(10).hash(123))