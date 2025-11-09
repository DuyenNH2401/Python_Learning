import math

def is_prime(n):
    for i in range(2, math.isqrt(n)+1):
        if n % i == 0:
            return False
    return True

def fill_prime_list(n):
    prime_list = []
    for i in range(4, n+1):
        if is_prime(i):
            put = i
            prime_list.append(put)
    return prime_list

def process(list, n):
    for i in list:
        for j in reversed(list):
            if i + j == n:
                print(i, j, sep=" ")
                continue

if __name__ == '__main__':
    test_case = int(input())
    while test_case > 0:
        n = int(input())
        prime_list = fill_prime_list(n)

        tmp = process(prime_list, n)
        test_case-=1