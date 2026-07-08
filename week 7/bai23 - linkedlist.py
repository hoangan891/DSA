class Node:
    def __init__(self, val): self.val, self.next = val, None
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next; fast = fast.next.next
        if slow == fast: return True
    return False
h = Node(1); print(has_cycle(h))