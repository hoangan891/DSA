class DNode:
    def __init__(self, val): self.val = val; self.prev = self.next = None
class DoublyLinkedList:
    def __init__(self): self.head = None
    def pushFront(self, val):
        node = DNode(val)
        if self.head: self.head.prev = node; node.next = self.head
        self.head = node
dll = DoublyLinkedList()
dll.pushFront(1)
print(dll.head.val)