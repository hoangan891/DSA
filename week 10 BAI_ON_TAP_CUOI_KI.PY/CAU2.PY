def insertion_sort_count(arr):
    a = arr.copy()
    shift = 0

    print("Mảng ban đầu:", a)
    print()

    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            shift += 1
            j -= 1

        a[j + 1] = key

        print(f"Bước {i}: {a}")

    print("\nMảng sau khi sắp xếp:", a)
    print("Tổng số lần dịch chuyển (Shift):", shift)

    return shift


A = [5, 2, 4, 6, 1, 3]

insertion_sort_count(A)