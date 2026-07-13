def count_subarrays(arr, target):
    prefix_sum = 0
    count = 0

    # Hash Map lưu số lần xuất hiện của Prefix Sum
    prefix_map = {0: 1}

    print("i\tA[i]\tPrefixSum\tCount")

    for i in range(len(arr)):
        prefix_sum += arr[i]

        # Nếu đã tồn tại (prefix_sum - target)
        if (prefix_sum - target) in prefix_map:
            count += prefix_map[prefix_sum - target]

        # Cập nhật Hash Map
        if prefix_sum in prefix_map:
            prefix_map[prefix_sum] += 1
        else:
            prefix_map[prefix_sum] = 1

        print(i, "\t", arr[i], "\t", prefix_sum, "\t\t", count)

    return count


# Chương trình chính
A = [3, 4, 7, 2, -3, 1, 4, 2]
S = 7

print("Mảng:", A)
print("Tổng cần tìm:", S)

result = count_subarrays(A, S)

print("\nSố mảng con có tổng bằng", S, "là:", result)