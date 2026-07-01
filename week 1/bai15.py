def kiem_tra_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def tim_so_nguyen_to_dau_tien(a):
    for i in range(len(a)):
        if kiem_tra_nguyen_to(a[i]):
            return a[i], i
    return None, -1

if __name__ == "__main__":
    mang_so = [4, 6, 9, 7, 11]
    gia_tri_snt, vi_tri_snt = tim_so_nguyen_to_dau_tien(mang_so)
    print(f"Số nguyên tố đầu tiên là {gia_tri_snt} tại vị trí {vi_tri_snt}")