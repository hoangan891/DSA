def get_front_and_rear(q):
    if not q: return None, None
    return q[0], q[-1]
print(get_front_and_rear([4, 5, 6]))