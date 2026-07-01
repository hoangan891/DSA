def recover_minimum_passes(initial, current):
    n = len(initial)
    passes = 0
    while initial != current and passes < n:
        for j in range(0, n - 1):
            if initial[j] > initial[j + 1]:
                temp = initial[j]
                initial[j] = initial[j + 1]
                initial[j + 1] = temp
        passes += 1
    return passes

initial_state = [4, 3, 2, 1]
current_state = [3, 2, 1, 4]
result = recover_minimum_passes(initial_state, current_state)
print("So luot thap nhat da thuc hien la:", result)