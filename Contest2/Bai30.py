n = int(input())
while n > 0:
    n-=1
    num = int(input())
    tmp = "EVEN" if num%2==0 else "ODD"
    print(tmp)