from queue import Queue

q = Queue(maxsize=5)

print("Kích thước ban đầu:", q.qsize())
q.put('data analytics')
q.put('data structures and algorithms')
q.put('big data')
q.put('learning data analytics')

print("Kích thước sau khi thêm:", q.qsize())
print("Lấy phần tử ra (Get):", q.get())
print("Lấy phần tử ra (Get):", q.get())
print("Kích thước hiện tại:", q.qsize())