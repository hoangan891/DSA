def benchmark_sorts(arr):
    def insertion(a):
        shf = 0
        for i in range(1, len(a)):
            key = a[i]
            j = i - 1
            while j >= 0 and key < a[j]:
                a[j + 1] = a[j]
                j -= 1
                shf += 1
            a[j + 1] = key
        return shf
    return insertion(arr)

arr = [3, 1, 2]
print("So luong shift do duoc:", benchmark_sorts(arr))