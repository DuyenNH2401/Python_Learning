"""
a == cúp
b == huy chương
1, 2, 3 == nhất nhì ba (ko quan trọng)
n = số kệ
một kệ max 5 cúp(trophy), 10 huy chương(metal)
"""


a1, a2, a3 = map(int, input().split())
b1, b2, b3 = map(int, input().split())
n = int(input())

sum_tro = a1 + a2 + a3
sum_me = b1 + b2 + b3
count = 0
while sum_tro >= 0 and count <= n:
    sum_tro -= 5
    count += 1
while sum_me >= 0 and count <= n:
    sum_me -= 10
    count+=1

if sum_me == 0 and sum_tro == 0:
    print("Nes")
else: print("No")
