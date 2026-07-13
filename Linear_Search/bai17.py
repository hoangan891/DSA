def tim_kiem_linh_canh(a, x):
    chieu_dai_goc = len(a)
    if chieu_dai_goc == 0:
        return -1
        
    a.append(x)
    
    i = 0
    while a[i] != x:
        i += 1
        
    a.pop()
    
    if i < chieu_dai_goc:
        return i
    return -1

if __name__ == "__main__":
    mang_so = [12, 2, 5, 8, 1, 6, 4]
    print("Vị trí của phần tử 8 tính theo lính canh là:", tim_kiem_linh_canh(mang_so, 8))