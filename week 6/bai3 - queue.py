def simulate_queue(commands):
    queue = []
    for cmd in commands:
        if cmd.startswith("enq"): queue.append(int(cmd.split()[1]))
        elif cmd == "deq" and queue: print(f"Dequeue: {queue.pop(0)}")
    print("Trang thai cuoi:", queue)
simulate_queue(["enq 5", "enq 7", "deq"])