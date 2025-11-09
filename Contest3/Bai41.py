"""số gần thuận nghịch
chữ số đầu gấp đôi chữ số cuối hoặc ngược lại
chữ số thứ 2 đảo về gần cuối là số thuận nghịch"""

def check_dau_cuoi(n):
    head = n // (10**(len(str(n))-1))
    end = n % 10
    if end == 0: return False
    return head / end == 2 or end / head == 2

def so_thuan_nghich(n):
    re_num = 0
    n -= (n // 10 ** (len(str(n)) - 1)) * 10**(len(str(n)) - 1)
    n //= 10
    tmp = n
    while n != 0:
        pass
        re_num = re_num * 10 + n % 10
        n //= 10
    return re_num == tmp

if __name__ == '__main__':
     n = int(input())
     if check_dau_cuoi(n) and so_thuan_nghich(n):
         print("Yes")
     else: print("No")