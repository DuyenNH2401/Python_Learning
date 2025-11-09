# số lộc phát

def thuan_nghich(n):
    if n < 10: return False
    tmp = n
    re_num = 0
    while n != 0:
        re_num = re_num * 10 + n % 10
        n //=10
    return re_num == tmp

def sum_of_nums(n):
    tong = 0
    while n != 0:
        tong += n % 10
        n //= 10
    return tong % 10 == 8

if __name__ == '__main__':
    a, b = map(int, input().split())
    for i in range(a,b+1):
        count = str(i).count("6")
        if thuan_nghich(i) and sum_of_nums(i) and count>=1:
            print(i)