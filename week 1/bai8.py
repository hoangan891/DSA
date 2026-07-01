def dem_xuat_hien(a, x):
    so_lan = 0
    for i in range(len(a)):
        if a[i] == x:
            so_lan += 1
    return so_lan

if __name__ == "__main__":
    mang_mau = [2, 5, 2, 7, 2]
    print("Số lần xuất hiện của số 2 là:", dem_xuat_hien(mang_mau, 2))