from collections import deque
def max_sliding_window(arr, k):
    if not arr: return []
    res, dq = [], deque()
    for i in range(len(arr)):
        if dq and dq[0] < i - k + 1: dq.popleft()
        while dq and arr[dq[-1]] < arr[i]: dq.pop()
        dq.append(i)
        if i >= k - 1: res.append(arr[dq[0]])
    return res
print(max_sliding_window([1, 3, -1, -3, 5, 3], 3))