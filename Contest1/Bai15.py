
n, a, b = map(int, input().split())

if b//a >= 2:
    print(n*a)
else:
    if n % 2 == 0:
        print((n//2)*b)
    else: print((n-1)//2*b+a)