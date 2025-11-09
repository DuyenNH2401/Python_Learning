"""
Polycarp có n tiền xu
    Alice có a tiền xu
    Barbara có  b tiền xu
    Cerene có c tiền xu
Chia làm sao để tiền của cả 3 bằng nhau nêu được thì in ra Yes else thì No
"""
n, a, b, c = map(int, input().split())

tmp = max(a, b, c)
n-= ((tmp-a)+(tmp-b)+(tmp-c))

if n % 3 == 0: print("Yes")
else: print("No")