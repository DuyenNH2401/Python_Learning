n = int(input("n = "))
k = int(input("k = "))
a = []
print("Nhập điểm của các thành viên:")
for _ in range(n):
    num = int(input())
    a.append(num)
a.sort()
x = a[k-1] - a[0]
for i in range(1,n-k+1):
    if (a[i+k-1] - a[i]) < x:
        x = a[i+k-1] - a[i]
        min_index = i

for j in range(min_index,min_index+k):
    print(a[j])