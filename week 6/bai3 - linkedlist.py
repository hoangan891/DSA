class Node:
    def __init__(self, val): self.val = val; self.next = None
def find_value(head, target):
    idx = 0
    while head:
        if head.val == target: return idx
        idx += 1; head = head.next
    return -1
h = Node(1); h.next = Node(2)
print(find_value(h, 2))