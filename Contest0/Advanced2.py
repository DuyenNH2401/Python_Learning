
n = int(input())
first, end = -1, -1
a = list(map(int, input().split()))

for i in range(n):
    if a[i]<0:
        first = i+1
        break
j = n
while j>0:
    j -= 1
    if a[j] < 0:
        end = j+1
        break


print(first, end)