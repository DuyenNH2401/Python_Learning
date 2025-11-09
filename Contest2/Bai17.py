n = int(input())
sum = 0
while n>0:
    tmp = n % 10
    n //= 10
    sum+=tmp
print(sum)

