class Node:
    def __init__(self, val): self.val = val; self.next = None
def reverse_linked_list(head):
    prev = None
    while head: nxt = head.next; head.next = prev; prev = head; head = nxt
    return prev
h = Node(1); h.next = Node(2); print(reverse_linked_list(h).val)