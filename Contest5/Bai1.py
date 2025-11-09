import math

def isprime(n):
    if n <= 2: return False
    for i in range(3, math.isqrt(n)+1):
        if n % i == 0: return False
    return True

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    sum = 0
    count = 0
    for i in arr:
        if isprime(i):
            count+=1
            sum+=i
    print(f"{sum/count:.3f}")