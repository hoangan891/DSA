def tim_tat_ca(a, x):
    danh_sach_vi_tri = []
    for i in range(len(a)):
        if a[i] == x:
            danh_sach_vi_tri.append(i)
    return danh_sach_vi_tri

if __name__ == "__main__":
    mang_mau = [4, 1, 4, 9, 4]
    print("Tất cả các vị trí của số 4 là:", tim_tat_ca(mang_mau, 4))