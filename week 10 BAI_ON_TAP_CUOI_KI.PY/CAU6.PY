class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Thuật toán Floyd
def detect_cycle(head):
    slow = head
    fast = head

    # Giai đoạn 1: Phát hiện chu trình
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            print("Có chu trình.")
            break
    else:
        print("Không có chu trình.")
        return None

    # Giai đoạn 2: Tìm nút bắt đầu chu trình
    slow = head

    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow


# ---------------- Chương trình chính ----------------

# Tạo danh sách liên kết
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# Tạo chu trình: 5 -> 3
head.next.next.next.next.next = head.next.next

start = detect_cycle(head)

if start:
    print("Nút bắt đầu chu trình là:", start.data)