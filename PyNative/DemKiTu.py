
s = input()
c_hoa = 0
c_thuong = 0
c_so = 0
for i in s:
    if i.isupper(): c_hoa+=1
    if i.islower(): c_thuong+=1
    if i.isdigit(): c_so+=1

print(f"""Trong day {s} ta co: 
{c_hoa} chu hoa
{c_thuong} chu thuong
{c_so} so""")