def tim_kiem_ma_tran_hai_chieu(ma_tran, x):
    for dong in range(len(ma_tran)):
        for cot in range(len(ma_tran[dong])):
            if ma_tran[dong][cot] == x:
                return dong, cot
    return -1, -1

if __name__ == "__main__":
    ma_tran_so = [
        [5, 8, 1],
        [3, 9, 7],
        [2, 6, 4]
    ]
    toa_do_dong, toa_do_cot = tim_kiem_ma_tran_hai_chieu(ma_tran_so, 9)
    print(f"Tìm thấy số 9 tại vị trí dòng {toa_do_dong} và cột {toa_do_cot}")