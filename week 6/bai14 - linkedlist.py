class Node:
    def __init__(self, val): self.val = val; self.next = None
def add_two_numbers(l1, l2):
    dummy = Node(0); curr = dummy; carry = 0
    while l1 or l2 or carry:
        val = carry
        if l1: val += l1.val; l1 = l1.next
        if l2: val += l2.val; l2 = l2.next
        carry, val = divmod(val, 10)
        curr.next = Node(val); curr = curr.next
    return dummy.next
h1 = Node(2); h2 = Node(5)
print(add_two_numbers(h1, h2).val)