"""
cho n
biểu diện n dưới dạng tổng các số nguyên tố sao cho số lượng số hạng trong
tổng là lớn nhất
"""

n = int(input())
if n <= 1: print("-1")
elif n % 2 == 0:
    print(n//2)
    for _ in range(n//2): print(2, end=" ")
else:
    print(n//2)
    for _ in range(n//2-1):
        print(2, end=" ")
    print(3)