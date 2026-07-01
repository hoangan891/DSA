class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def bubble_sort_linked_list(head):
    if not head:
        return None
    
    end = None
    while end != head.next:
        curr = head
        while curr.next != end:
            next_node = curr.next
            if curr.data > next_node.data:
                temp = curr.data
                curr.data = next_node.data
                next_node.data = temp
            curr = curr.next
        end = curr
    return head

node1 = Node(1)
node2 = Node(3)
node3 = Node(2)
node1.next = node2
node2.next = node3

head_node = bubble_sort_linked_list(node1)
print(head_node.data, head_node.next.data, head_node.next.next.data)