def quan_ly_danh_ba():
    he_thong_danh_ba = []
    
    while True:
        print("\n--- CHƯƠNG TRÌNH QUẢN LÝ DANH BẠ ---")
        print("1. Thêm số liên hệ")
        print("2. Tìm kiếm số điện thoại theo tên")
        print("3. Tìm kiếm tên theo số điện thoại")
        print("4. Thống kê số điện thoại theo đầu số")
        print("5. Thoát")
        
        chon = input("Nhập tính năng cần thực hiện từ một đến năm: ")
        
        if chon == "1":
            ten = input("Nhập tên liên hệ: ")
            sdt = input("Nhập số điện thoại liên hệ: ")
            he_thong_danh_ba.append({"Ten": ten, "SDT": sdt})
            print("Đã thêm liên hệ vào danh bạ thành công")
            
        elif chon == "2":
            ten_tim = input("Nhập tên cần tra cứu số điện thoại: ").lower()
            tim_thay = False
            for i in range(len(he_thong_danh_ba)):
                if he_thong_danh_ba[i]["Ten"].lower() == ten_tim:
                    print(f"Số điện thoại của người này là: {he_thong_danh_ba[i]['SDT']}")
                    tim_thay = True
                    break
            if not tim_thay:
                print("Tên liên hệ này chưa có trong danh bạ")
                
        elif chon == "3":
            sdt_tim = input("Nhập số điện thoại cần tra cứu tên chủ sở hữu: ")
            tim_thay = False
            for i in range(len(he_thong_danh_ba)):
                if he_thong_danh_ba[i]["SDT"] == sdt_tim:
                    print(f"Tên chủ sở hữu của số điện thoại này là: {he_thong_danh_ba[i]['Ten']}")
                    tim_thay = True
                    break
            if not tim_thay:
                print("Số điện thoại này chưa đăng ký trong danh bạ")
                
        elif chon == "4":
            dau_so = input("Nhập đầu số điện thoại cần thống kê: ")
            bo_dem = 0
            for i in range(len(he_thong_danh_ba)):
                so_dt = he_thong_danh_ba[i]["SDT"]
                if so_dt[:len(dau_so)] == dau_so:
                    bo_dem += 1
            print(f"Số lượng liên hệ bắt đầu bằng đầu số {dau_so} là: {bo_dem}")
            
        elif chon == "5":
            print("Chương trình dừng hoạt động")
            break
        else:
            print("Lựa chọn vừa nhập không đúng định dạng yêu cầu")

if __name__ == "__main__":
    quan_ly_danh_ba()