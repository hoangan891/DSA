class Node:
    def __init__(self, val): self.val = val; self.next = None
def insert_after(prev_node, new_val):
    if not prev_node: return
    node = Node(new_val); node.next = prev_node.next; prev_node.next = node
h = Node(1); insert_after(h, 2)
print(h.next.val)