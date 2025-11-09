"""
k2 chữ số 2
k3 chữ số 3
k5 chữ số 5
k6 chữ số 6
số yêu thích 32, 256
"""
k2, k3, k5, k6 = map(int, input().split())
count_k2 = k2
if min(k2, k5, k6) == k2:
    print(f"Tạo tối đa {k2} số nguyên yêu thích và tổng của chúng bằng {256*k2}")
else:
    tmp = min(k5, k6)
    count_k2 -= tmp
    if count_k2 > 0:
        sum = (256*tmp + 32*k3) if k2>k3 else (256*tmp + 32*count_k2)
        add = k3 if k2>k3 else count_k2
        print(f"Tạo tối đa {tmp+add} số nguyên yêu thích và tổng của chúng bằng {sum}")
    else: print(f"Tạo tối đa")

"""
Cách 2
k2, k3, k5, k6 = map(int, input().split())
k256 = min(k2, k5, k6)
k32 = min(k3, k2-k256)
print(k32*32+k245*256)  
"""