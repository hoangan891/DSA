def dem_xuat_hien(arr, key):
    def tim_dau(arr, key):
        left, right = 0, len(arr) - 1
        res = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == key:
                res = mid
                right = mid - 1
            elif arr[mid] < key:
                left = mid + 1
            else:
                right = mid - 1
        return res

    def tim_cuoi(arr, key):
        left, right = 0, len(arr) - 1
        res = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == key:
                res = mid
                left = mid + 1
            elif arr[mid] < key:
                left = mid + 1
            else:
                right = mid - 1
        return res

    dau = tim_dau(arr, key)
    if dau == -1:
        return 0
    cuoi = tim_cuoi(arr, key)
    return cuoi - dau + 1

arr = [1, 2, 2, 2, 3]
key = 2
result = dem_xuat_hien(arr, key)
print("So lan xuat hien la:", result)