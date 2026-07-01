def count_inversions(arr):
    def merge_sort(a):
        if len(a) <= 1: return a, 0
        mid = len(a) // 2
        left, left_inv = merge_sort(a[:mid])
        right, right_inv = merge_sort(a[mid:])
        merged, merge_inv = [], 0
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]: merged.append(left[i]); i += 1
            else: merged.append(right[j]); j += 1; merge_inv += (len(left) - i)
        merged.extend(left[i:]); merged.extend(right[j:])
        return merged, left_inv + right_inv + merge_inv
    _, total_inv = merge_sort(arr)
    return total_inv
print("So nghich the:", count_inversions([3, 2, 1]))