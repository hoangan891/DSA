def get_front_and_rear(q):
    return (q[0], q[-1]) if q else (None, None)
print(get_front_and_rear([4, 5, 6]))