
a = [1, 2, 1, 2, 3, 1, 4, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
length = len(a) + 1
cnt = [0] * length

for x in a:
    cnt[x]+=1
#in theo thứ tự từ bé đến lớn
l, r = min(a), max(a)
for i in range(l, r+1):
    print(i, cnt[i])
print()
#tìm xem có bao nhiêu giá trị khác nhau
count = 0
for i in a:
    if cnt[i] != 0:
        count+=1
        cnt[i] = 0
print(f"{count} giá trị khác nhau")
print()
dem = 0
for i in range(l, r+1):
    if cnt[i] != 0:
        dem+=1
print(f"{count} giá trị khác nhau")
print()
#in theo thứ tự xuất hiện
for i in a:
    if cnt[i] != 0:
        print(i, cnt[i])
        cnt[i] = 0
print()