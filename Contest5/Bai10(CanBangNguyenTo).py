from math import  isqrt
def nt(n):
    if n < 3:
        return n > 1
    for i in range(3, isqrt(n)):
        if n % i == 0:
            return False
    return True

def balance_prime(arr):
    sum_left = arr[0]
    sum_right = sum(arr[2:])
    for i in range(1, len(arr)-1):
        if nt(sum_left) and nt(sum_right):
            print(i)
        sum_left += arr[i]
        sum_right -= arr[i+1]

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    balance_prime(arr)
