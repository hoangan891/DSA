class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def selection_sort_linked_list(head):
    res_head = None
    res_tail = None
    while head is not None:
        min_node = head
        min_prev = None
        curr = head
        prev = None
        while curr is not None:
            if curr.data < min_node.data:
                min_node = curr
                min_prev = prev
            prev = curr
            curr = curr.next
        if min_node == head:
            head = head.next
        else:
            min_prev.next = min_node.next
        min_node.next = None
        if res_head is None:
            res_head = min_node
            res_tail = min_node
        else:
            res_tail.next = min_node
            res_tail = min_node
    return res_head

node1 = Node(3)
node2 = Node(1)
node3 = Node(2)
node1.next = node2
node2.next = node3
res = selection_sort_linked_list(node1)
print(res.data, res.next.data, res.next.next.data)