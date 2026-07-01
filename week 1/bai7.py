def ton_tai(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return True
    return False

if __name__ == "__main__":
    mang_so = [12, 2, 5, 8, 1, 6, 4]
    print("Số 5 có tồn tại không:", ton_tai(mang_so, 5))
    print("Số 10 có tồn tại không:", ton_tai(mang_so, 10))