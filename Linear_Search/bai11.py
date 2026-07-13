def tim_gia_tri_lon_nhat(a):
    if len(a) == 0:
        return None, -1
    
    lon_nhat = a[0]
    vi_tri_lon_nhat = 0
    for i in range(1, len(a)):
        if a[i] > lon_nhat:
            lon_nhat = a[i]
            vi_tri_lon_nhat = i
    return lon_nhat, vi_tri_lon_nhat

if __name__ == "__main__":
    mang_so = [7, 3, 9, 12, 5, 8, 1]
    gia_tri, vi_tri = tim_gia_tri_lon_nhat(mang_so)
    print(f"Giá trị lớn nhất là {gia_tri} nằm tại vị trí {vi_tri}")