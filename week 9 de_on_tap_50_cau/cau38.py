class Node:
    def __init__(self, val): self.val = val; self.next = None
def find_cycle_start(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next; fast = fast.next.next
        if slow == fast:
            curr = head
            while curr != slow: curr = curr.next; slow = slow.next
            return curr
    return None
h = Node(1); print(find_cycle_start(h))