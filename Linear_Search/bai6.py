def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == "__main__":
    mang_so = [12, 2, 5, 8, 1, 6, 4]
    so_can_tim = 6
    ket_qua = linear_search(mang_so, so_can_tim)
    print("Vị trí tìm thấy đầu tiên là:", ket_qua)