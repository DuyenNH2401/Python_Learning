"""số smith"""
import math

def is_prime(n):
    for i in range(2, math.isqrt(n)+1):
        if n % i == 0: return False
    return True

def sum_of_nums(n):
    sum_of_nums = 0
    while n>0:
        sum_of_nums+= n % 10
        n//=10
    return sum_of_nums

def sum_of_num_of_prime(n):
    sum = 0
    for i in range(2, n):
        while n % i == 0:
            if i < 10:
                sum+=i
            else:
                sum+=sum_of_nums(i)
            n//=i
    return sum

def main():
    n = int(input())
    if is_prime(n) : print("No1")
    else:
        if sum_of_num_of_prime(n) == sum_of_nums(n):
            print("Yes")
        else: print("No")

def loop():
    for i in range(1, 10000):
        if is_prime(i): continue
        else:
            if sum_of_num_of_prime(i) == sum_of_nums(i):
                print(i)
            else: continue

if __name__ == '__main__':
    loop()
