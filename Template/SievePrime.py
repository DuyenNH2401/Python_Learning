from math import isqrt

n = 6*(10**6)
prime = [True] * (n+1)
def sieve():
    global prime
    prime[0], prime[1] = False, False
    for i in range(2, isqrt(n)+1):
        if prime[i]:
            for j in range(i*i, n, i):
                prime[j] = False


if __name__ == '__main__':
    sieve()
    num_check = int(input())
    if prime[num_check]:
        print("Yes")
    else: print("No")