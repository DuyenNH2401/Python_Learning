#số thuận nghịch có 3 ước nguyên tố

import math

def thuan_nghich(n):
    tmp = n
    re_num = 0
    while n != 0:
        re_num = re_num * 10 + n % 10
        n//=10
    if re_num == tmp: return True
    else: False

def check(n):
    count = 0
    for i in range(2, math.isqrt(n)+1):
        if n % i == 0:
            while n % i == 0:
                count+=1
                n/=i
    if n!= 1: count+=1
    if n > 3: return True
    else: return False

if __name__ == '__main__':
    a, b = map(int, input().split())
    count = 0
    for i in range(a, b+1):
        if check(i) and thuan_nghich(i):
            print(i)
            count+=1
    if count == 0: print(-1)