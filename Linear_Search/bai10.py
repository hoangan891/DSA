def vi_tri_cuoi_cung(a, x):
    for i in range(len(a) - 1, -1, -1):
        if a[i] == x:
            return i
    return -1

if __name__ == "__main__":
    mang_mau = [4, 1, 4, 9, 4]
    print("Vị trí cuối cùng của số 4 là:", vi_tri_cuoi_cung(mang_mau, 4))