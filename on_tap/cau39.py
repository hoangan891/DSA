class Node:
    def __init__(self, val): self.val = val; self.next = None
def remove_nth_end(head, k):
    dummy = Node(0); dummy.next = head
    f = s = dummy
    for _ in range(k + 1): f = f.next
    while f: f = f.next; s = s.next
    s.next = s.next.next; return dummy.next
h = Node(1); h.next = Node(2); print(remove_nth_end(h, 1).val)