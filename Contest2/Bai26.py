a, b, n = map(int,input().split())
y = 0
for x in range(0, n//a+1):
    if (n-a*x)%b == 0 and (n-a*x)>0:
        print("Yes")
        break
    else:
        print("No")
        break