from collections import deque

def sliding_window_min(arr, k):
    dq = deque()
    result = []

    for i in range(len(arr)):

        # Loại bỏ các chỉ số đã ra khỏi cửa sổ
        while dq and dq[0] <= i - k:
            dq.popleft()

        # Loại bỏ các phần tử lớn hơn phần tử hiện tại
        while dq and arr[dq[-1]] >= arr[i]:
            dq.pop()

        # Thêm chỉ số hiện tại
        dq.append(i)

        # Khi đủ k phần tử thì lưu kết quả
        if i >= k - 1:
            result.append(arr[dq[0]])

        # In trạng thái Deque ở 3 bước đầu tiên
        if i >= k - 1 and len(result) <= 3:
            print(f"\nCửa sổ {len(result)}: {arr[i-k+1:i+1]}")
            print("Deque (chỉ số):", list(dq))
            print("Deque (giá trị):", [arr[x] for x in dq])
            print("Giá trị nhỏ nhất:", arr[dq[0]])

    return result


# Chương trình chính
A = [4, 2, 12, 11, -5, 8, 1, 5, 6]
k = 3

print("Mảng:", A)
print("Kích thước cửa sổ:", k)

answer = sliding_window_min(A, k)

print("\nKết quả cuối cùng:")
print(answer)