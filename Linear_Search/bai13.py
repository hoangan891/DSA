def tim_kiem_chuoi_khong_phan_biet(danh_sach, chuoi_tim):
    chuoi_tim_chuan = chuoi_tim.lower()
    for i in range(len(danh_sach)):
        if danh_sach[i].lower() == chuoi_tim_chuan:
            return i
    return -1

if __name__ == "__main__":
    danh_sach_ten = ["An", "Bình", "Châu"]
    ten_can_tim = "an"
    print("Vị trí tìm thấy tên là:", tim_kiem_chuoi_khong_phan_biet(danh_sach_ten, ten_can_tim))