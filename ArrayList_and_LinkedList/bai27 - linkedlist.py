class Node:
    def __init__(self, val): self.val, self.next = val, None
def detect_cycle_start(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next; fast = fast.next.next
        if slow == fast:
            curr = head
            while curr != slow: curr, slow = curr.next, slow.next
            return curr
    return None
h = Node(1); print(detect_cycle_start(h))