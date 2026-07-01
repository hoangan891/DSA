def tim_sinh_vien(danh_sach_lop, ma_tim):
    for i in range(len(danh_sach_lop)):
        if danh_sach_lop[i]["MaSV"] == ma_tim:
            sinh_vien = danh_sach_lop[i]
            print("Đã tìm thấy thông tin sinh viên:")
            print("Mã số sinh viên:", sinh_vien["MaSV"])
            print("Họ và tên:", sinh_vien["HoTen"])
            print("Điểm trung bình:", sinh_vien["DiemTB"])
            return i
    print("Không tồn tại mã sinh viên cần tìm trong hệ thống")
    return -1

if __name__ == "__main__":
    du_lieu_lop = [
        {"MaSV": "SV01", "HoTen": "Nguyễn Văn Bảo", "DiemTB": 7.5},
        {"MaSV": "SV02", "HoTen": "Võ Hoàng An", "DiemTB": 8.5},
        {"MaSV": "SV03", "HoTen": "Trần Thành Đạt", "DiemTB": 6.8}
    ]
    tim_sinh_vien(du_lieu_lop, "SV02")