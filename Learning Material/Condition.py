#b = 10
#a = 100 if b > 100 else 0
#print(a)

#Nested if
n = int(input("n = "))
if n > 50:
    if n%3==0 or n%5==0 or n%7==0: print("n là số thỏa mãn cả 2 điều kiện")
    else: print("n là số thỏa dk > 50")
else: print("n không thỏa 2 dk")