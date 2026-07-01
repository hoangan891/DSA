def kth_smallest_matrix(matrix, k):
    n = len(matrix)
    def count_less_equal(target):
        count = 0
        c = n - 1
        for r in range(n):
            while c >= 0 and matrix[r][c] > target:
                c -= 1
            count += (c + 1)
        return count

    left = matrix[0][0]
    right = matrix[n - 1][n - 1]
    res = left
    while left <= right:
        mid = (left + right) // 2
        if count_less_equal(mid) >= k:
            res = mid
            right = mid - 1
        else:
            left = mid + 1
    return res

matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
k = 8
result = kth_smallest_matrix(matrix, k)
print("Phan tu nho thu k la:", result)