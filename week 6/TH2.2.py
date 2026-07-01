from collections import deque

q = deque()

q.append('data analytics')
q.append('data structures and algorithms')
q.append('big data')
q.append('learning data analytics')

print("Trạng thái Deque Queue ban đầu:", q)
print("Xóa đầu hàng đợi (popleft):", q.popleft())
print("Xóa đầu hàng đợi (popleft):", q.popleft())
print("Trạng thái Deque Queue hiện tại:", q)