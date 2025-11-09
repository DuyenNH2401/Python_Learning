"""Số thuần nguyên tố"""
import math

#kiểm tra số nguyên tố
def prime_check(n):
    if n < 2: return False
    for i in range(2, math.isqrt(n)):
        if n % i == 0: return False
    return True

#Tách số và tính tổng của các số
def nums(n):
    Sum = 0
    while n != 0:
        tmp = n % 10
        if tmp != 2 and tmp != 3 and tmp != 5 and tmp != 7:
            return False
        Sum+=tmp
        n//=10
    return prime_check(Sum)

if __name__ == '__main__':
    a, b = map(int,input().split())
    count = 0
    for i in range(a, b + 1):
        if prime_check(i) and nums(i):
            count += 1
    print(count)