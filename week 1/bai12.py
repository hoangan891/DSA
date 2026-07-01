def tim_min_max_dong_thoi(a):
    if len(a) == 0:
        return None, -1, None, -1
        
    nho_nhat = lon_nhat = a[0]
    vi_tri_nho = vi_tri_lon = 0
    
    for i in range(1, len(a)):
        if a[i] < nho_nhat:
            nho_nhat = a[i]
            vi_tri_nho = i
        if a[i] > lon_nhat:
            lon_nhat = a[i]
            vi_tri_lon = i
            
    return nho_nhat, vi_tri_nho, lon_nhat, vi_tri_lon

if __name__ == "__main__":
    mang_so = [7, 3, 9, 12, 5, 8, 1]
    val_min, idx_min, val_max, idx_max = tim_min_max_dong_thoi(mang_so)
    print(f"Nhỏ nhất: {val_min} tại vị trí {idx_min}")
    print(f"Lớn nhất: {val_max} tại vị trí {idx_max}")