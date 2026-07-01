from collections import deque

myStack = deque()

myStack.append('data science')
myStack.append('data structures and algorithms')
myStack.append('learning data analytics')
myStack.append('big data')

print("Trạng thái Deque Stack ban đầu:", myStack)
print("Pop phần tử:", myStack.pop())
print("Pop phần tử:", myStack.pop())
print("Trạng thái Deque Stack hiện tại:", myStack)