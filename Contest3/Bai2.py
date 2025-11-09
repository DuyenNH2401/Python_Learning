"""So sphenic"""
import math

def sphenic(n):
    for i in range(2, int(math.sqrt(n)+1)):
        count = 0
        while n % i == 0:
            count+=1
            n/=i
            if count>1: return 0
    return 1

if __name__ == '__main__':
    n = int(input())
    print(sphenic(n))