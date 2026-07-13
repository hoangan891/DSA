class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertion_sort_linked_list(head):
    sorted_list = None
    curr = head
    while curr is not None:
        next_node = curr.next
        if sorted_list is None or sorted_list.data >= curr.data:
            curr.next = sorted_list
            sorted_list = curr
        else:
            s_curr = sorted_list
            while s_curr.next is not None and s_curr.next.data < curr.data:
                s_curr = s_curr.next
            curr.next = s_curr.next
            s_curr.next = curr
        curr = next_node
    return sorted_list

node1 = Node(3)
node2 = Node(1)
node3 = Node(2)
node1.next = node2
node2.next = node3
res = insertion_sort_linked_list(node1)
print(res.data, res.next.data, res.next.next.data)