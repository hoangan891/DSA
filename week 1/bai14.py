def tim_so_chan_dau_tien(a):
    for i in range(len(a)):
        if a[i] % 2 == 0:
            return i
    return -1

if __name__ == "__main__":
    mang_so = [3, 7, 11, 8, 5, 4]
    print("Vị trí số chẵn đầu tiên xuất hiện:", tim_so_chan_dau_tien(mang_so))