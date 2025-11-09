"""
(a+b)%c = ((a%c)+(b%c))%c
(a-b)%c = ((a%c)-(b%c)+c))%c
(a*b)%c = ((a%c)*(b%c))%c
(a/b)%c = ((a%c)*(b^-1%c))%c
"""
#Thần chú: khi tìm cái gì đó chia hết cho m
# thì ta lấy các phần tử chia hết cho m
if __name__ == "__main__":
# tính n! rồi tìm kq chia dư cho 10^9+7
    #n = int(input("n = "))
    m = 10000
    res = 1
    """for i in range(1,n+1):
        res *= i
        res %= m
    print(res)"""
# tính a^b rồi tìm kq chia hết cho c
    a, b, c = map(int, input().split())
    tmp = 1
    for _ in range(b):
        tmp *=a
        tmp %=c
    print(tmp)