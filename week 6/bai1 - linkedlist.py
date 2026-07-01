class Node:
    def __init__(self, val): self.val = val; self.next = None
class LinkedList:
    def __init__(self): self.head = None
    def pushFront(self, val):
        node = Node(val); node.next = self.head; self.head = node
    def pushBack(self, val):
        if not self.head: self.head = Node(val); return
        curr = self.head
        while curr.next: curr = curr.next
        curr.next = Node(val)
ll = LinkedList()
ll.pushFront(2); ll.pushBack(5)
print(ll.head.val)