from math import isqrt
from unittest.util import sorted_list_difference


def prime(n):
    if n < 3: return n>1
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            return False
    return True

def thuan_nghich(n):
    tmp = n
    result = 0
    while n != 0:
        result = result * 10 + n % 10
        n //= 10
    return result == tmp

def chinh_phuong(n):
    tmp = n
    n = isqrt(n)
    return tmp == n * n

def sumdigital(n):
    sod = 0
    while n != 0:
        sod += n % 10
        n = n // 10
    return sod
if __name__ == '__main__':
    a = list(map(int, input().split()))
    cnt = [0]*4
    for i in a:
        if prime(i):
            print(f"{i} là prime")
            cnt[0]+=1
        if thuan_nghich(i):
            print(f"{i} la thuan nghich")
            cnt[1]+=1
        if chinh_phuong(i):
            print(f"{i} la cp")
            cnt[2]+=1
        if prime(sumdigital(i)):
            print(f"{i} co sum digital la prime")
            cnt[3]+=1

    for i in cnt:
        print(i)