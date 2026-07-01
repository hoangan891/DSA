def simulate_stack(commands):
    stack = []
    for cmd in commands:
        if cmd.startswith("push"):
            stack.append(int(cmd.split()[1]))
        elif cmd == "pop" and stack:
            print(f"Pop: {stack.pop()}")
    print("Trang thai cuoi:", stack)
simulate_stack(["push 5", "push 7", "pop"])