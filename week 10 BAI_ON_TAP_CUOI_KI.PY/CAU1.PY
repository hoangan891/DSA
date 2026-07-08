def can_split(weights, k, limit):
    trucks = 1
    current = 0

    for w in weights:
        if current + w <= limit:
            current += w
        else:
            trucks += 1
            current = w

    return trucks <= k


def split_array(weights, limit):
    result = []
    current = []
    total = 0

    for w in weights:
        if total + w <= limit:
            current.append(w)
            total += w
        else:
            result.append(current)
            current = [w]
            total = w

    result.append(current)
    return result


def min_capacity(weights, k):
    left = max(weights)
    right = sum(weights)

    while left < right:
        mid = (left + right) // 2

        if can_split(weights, k, mid):
            right = mid
        else:
            left = mid + 1

    return left


# ----------------- Chương trình chính -----------------
W = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
K = 5

capacity = min_capacity(W, K)
groups = split_array(W, capacity)

print("Danh sách kiện hàng:", W)
print("Số xe:", K)
print("Tải trọng tối thiểu của mỗi xe:", capacity)
print()

print("Cách chia hàng:")

for i, truck in enumerate(groups, 1):
    print(f"Xe {i}: {truck} --> Tổng = {sum(truck)}")