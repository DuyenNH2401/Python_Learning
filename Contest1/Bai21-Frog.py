a, b, k = map(int, input().split())
tmp = k // 2
if k % 2 == 0:
    print(tmp*a-tmp*b)
else: print((tmp+1)*a-tmp*b)