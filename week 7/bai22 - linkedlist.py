class Node:
    def __init__(self, val): self.val, self.next = val, None
def find_middle(head):
    slow = fast = head
    while fast and fast.next: slow = slow.next; fast = fast.next.next
    return slow.val if slow else None
h = Node(1); h.next = Node(2); h.next.next = Node(3); print(find_middle(h))