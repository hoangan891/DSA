class Node:
    def __init__(self, val): self.val = val; self.next = None
def mid_node(head):
    slow = fast = head
    while fast and fast.next: slow = slow.next; fast = fast.next.next
    return slow.val if slow else None
h = Node(1); h.next = Node(2); h.next.next = Node(3); print(mid_node(h))