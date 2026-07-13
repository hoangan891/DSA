def daily_temperatures(T):
    n = len(T)
    answer = [0] * n
    stack = []  # Lưu chỉ số các ngày

    for i in range(n):
        while stack and T[i] > T[stack[-1]]:
            idx = stack.pop()
            answer[idx] = i - idx

        stack.append(i)

    return answer


# Chương trình chính
T = [73, 74, 75, 71, 69, 72, 76, 73]

result = daily_temperatures(T)

print("Nhiệt độ:", T)
print("Số ngày phải chờ:", result)