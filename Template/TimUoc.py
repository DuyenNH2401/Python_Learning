import math
lst = []

def divisor(n):
    count = 0
    for i in range(1, isqrt(n) + 1):
        if n % i == 0:
            count += 1
        if n // i != i:
            count += 1
    return count > 5

def tong_uoc(n):
    tong = 0
    for i in range(1,int(math.sqrt(n))+1):
        if n % i == 0 :
            tong += i
            if n // i != i:
                lst.append(n//i)
                tong+=n//i
    return tong - n

print(tong_uoc(4))