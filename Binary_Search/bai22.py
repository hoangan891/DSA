def find_median_sorted_arrays(arr1, arr2):
    if len(arr1) > len(arr2):
        arr1, arr2 = arr2, arr1
    m, n = len(arr1), len(arr2)
    left, right = 0, m
    while left <= right:
        i = (left + right) // 2
        j = (m + n + 1) // 2 - i
        
        max_left1 = float('-inf') if i == 0 else arr1[i - 1]
        min_right1 = float('inf') if i == m else arr1[i]
        
        max_left2 = float('-inf') if j == 0 else arr2[j - 1]
        min_right2 = float('inf') if j == n else arr2[j]
        
        if max_left1 <= min_right2 and max_left2 <= min_right1:
            if (m + n) % 2 == 1:
                return float(max(max_left1, max_left2))
            else:
                return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2.0
        elif max_left1 > min_right2:
            right = i - 1
        else:
            left = i + 1
    return 0.0

arr1 = [1, 3]
arr2 = [2]
result = find_median_sorted_arrays(arr1, arr2)
print("Trung vi hai mang la:", result)