import math
n = int(input("N = "))

for i in range(1, 100):
    a = math.isqrt(i*n)
    if a*a == n*i :
        print("số thỏa mãn là", n*i)
        break