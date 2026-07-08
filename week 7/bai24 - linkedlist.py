class Node:
    def __init__(self, val): self.val, self.next = val, None
def merge_two_lists(l1, l2):
    dummy = Node(0); curr = dummy
    while l1 and l2:
        if l1.val < l2.val: curr.next = l1; l1 = l1.next
        else: curr.next = l2; l2 = l2.next
        curr = curr.next
    curr.next = l1 or l2; return dummy.next
h1, h2 = Node(1), Node(2); print(merge_two_lists(h1, h2).val)