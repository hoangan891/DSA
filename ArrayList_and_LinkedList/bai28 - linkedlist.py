class Node:
    def __init__(self, val): self.val, self.next = val, None
def sort_list(head):
    if not head or not head.next: return head
    def split(h):
        slow = fast = h; prev = None
        while fast and fast.next: prev = slow; slow = slow.next; fast = fast.next.next
        prev.next = None; return h, slow
    def merge(l1, l2):
        d = Node(0); c = d
        while l1 and l2:
            if l1.val < l2.val: c.next = l1; l1 = l1.next
            else: c.next = l2; l2 = l2.next
            c = c.next
        c.next = l1 or l2; return d.next
    left, right = split(head); return merge(sort_list(left), sort_list(right))
h = Node(3); h.next = Node(1); print(sort_list(h).val)