class Node:
    def __init__(self, val): self.val = val; self.next = None
def remove_node(head, x):
    dummy = Node(0); dummy.next = head
    curr = dummy
    while curr.next:
        if curr.next.val == x: curr.next = curr.next.next; break
        curr = curr.next
    return dummy.next
h = Node(1); h.next = Node(2)
print(remove_node(h, 2).val)