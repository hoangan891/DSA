def search_matrix_2d(matrix, key):
    if not matrix or not matrix[0]:
        return False
    m = len(matrix)
    n = len(matrix[0])
    left = 0
    right = m * n - 1
    while left <= right:
        mid = (left + right) // 2
        val = matrix[mid // n][mid % n]
        if val == key:
            return True
        elif val < key:
            left = mid + 1
        else:
            right = mid - 1
    return False

matrix = [[1, 3, 5], [7, 9, 11]]
key = 9
result = search_matrix_2d(matrix, key)
print("Ket qua tim kiem:", result)
