"""Biểu diễn số dưới dạng 11, 111, 1111,...
VD: 144 =111 + 11 + 11 + 11 + 11"""

def length_cal(n):
    minus = 0
    length = 10**(len(str(n))-1)
    while length>0:
        minus = minus * 10 + 1
        length //=10
    return minus

def check(n, length):
    while True:
        if n-length > 0:
            n-=length
        elif n - length < 0:
            length //= 10
        elif n - length == 0:
            return True
        if n < 11: return False

if __name__ == '__main__':
    n = int(input())
    length = length_cal(n)
    if check(n, length):
        print("Yes")
    else: print("No")