import math
def multiplication_hash(k, m):
    A = (math.sqrt(5) - 1) / 2
    return math.floor(m * ((k * A) % 1))
print(multiplication_hash(123456, 100))