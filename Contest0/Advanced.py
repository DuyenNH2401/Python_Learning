
n = int(input())
i = 1
while True:
    i *= 10
    y = n / i
    if y >= 1: print(n % i)
    else: print(n);break
