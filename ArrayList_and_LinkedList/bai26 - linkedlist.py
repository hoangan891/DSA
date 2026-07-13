class DNode:
    def __init__(self, val): self.val, self.prev, self.next = val, None, None
class DoublyLinkedList:
    def __init__(self): self.head = None
    def pushFront(self, val):
        node = DNode(val)
        if self.head: self.head.prev = node; node.next = self.head
        self.head = node
dll = DoublyLinkedList(); dll.pushFront(5); print(dll.head.val)