
d1, d2, d3 = map(int, input().split())

if max(d1, d2, d3) == d3:
    print(2*d1+2*d2)
elif max(d1, d2, d3) == d2:
    print(2*d1+2*d3)
else: print(2*d2+2*d3)
