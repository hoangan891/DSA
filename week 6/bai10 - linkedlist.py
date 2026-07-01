class Node:
    def __init__(self, val): self.val = val; self.next = None
def remove_nth_from_end(head, k):
    dummy = Node(0); dummy.next = head
    first = second = dummy
    for _ in range(k + 1): first = first.next
    while first: first = first.next; second = second.next
    second.next = second.next.next
    return dummy.next
h = Node(1); h.next = Node(2)
print(remove_nth_from_end(h, 1).val)