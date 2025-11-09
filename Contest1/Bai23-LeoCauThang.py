n, m = map(int, input().split())
count = 0
min_step, max_step = 0, n
if n % 2 ==0:
    min_step = n//2
else: min_step = n//2+1

for i in range(min_step,max_step+1):
    if i % m == 0:
        print(i)
        break