class Node:
    def __init__(self, val): self.val = val; self.next = None
def get_length(head):
    count = 0
    while head: count += 1; head = head.next
    return count
h = Node(1); h.next = Node(2)
print(get_length(h))