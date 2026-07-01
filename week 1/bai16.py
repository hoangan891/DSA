def tim_phan_tu_gan_nhat(a, x):
    if len(a) == 0:
        return None, -1
        
    khoang_cach_nho_nhat = abs(a[0] - x)
    gia_tri_gan_nhat = a[0]
    vi_tri_gan_nhat = 0
    
    for i in range(1, len(a)):
        khoang_cach_hien_tai = abs(a[i] - x)
        if khoang_cach_hien_tai < khoang_cach_nho_nhat:
            khoang_cach_nho_nhat = khoang_cach_hien_tai
            gia_tri_gan_nhat = a[i]
            vi_tri_gan_nhat = i
            
    return gia_tri_gan_nhat, vi_tri_gan_nhat

if __name__ == "__main__":
    mang_so = [10, 22, 28, 29, 40]
    so_x = 26
    g_tri, v_tri = tim_phan_tu_gan_nhat(mang_so, so_x)
    print(f"Phần tử gần với {so_x} nhất là {g_tri} tại vị trí {v_tri}")