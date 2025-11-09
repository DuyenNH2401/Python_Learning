import math
#math.pow dùng để tính giá trị lũy thừa có thể dùng pow(a, 1/n) để tính căn bậc n
print(math.pow(1024, 1/10))
print()
# sqrt: square root dùng để tính căn bậc 2 và isqrt dùng để tính căn bậc 2 và laly61 phần nguyên
print(math.sqrt(16))
print(math.isqrt(17))
print()
#ceil: ceilling dùng để làm tròn lên
#floor: florring dùng để làm tròn xuống
print(math.ceil(6.4))
print(math.floor(6.8))
print()
#factorial: giai thừa
print(math.factorial(10))
print()
#gdc : ước chung lớn nhất
print(math.gcd(15,25))
print()
#comb: tính tổ hợp chập k của n math.comb(n,k)
print(math.comb(15, 10))
print()
#perm : chỉnh hợp số cách chọn ra k phần tử từ n phần tử nếu không nhâp k thì thành hoán vị(giai thừa)
print(math.perm(3, 1))
print(math.perm(4))
print()
#abs: giá trị tuyệt đối không cần dùng math.
print(abs(-12.5))
print()
#có thể dùng max, min để tìm max và min và sum để tính tổng các phần tử
a = [1, 2, 3, 10, 12, 123]
print(max(a))
print(min(a))
print(sum(a))