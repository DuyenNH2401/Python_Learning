
money = int(input())
cash = 0
if money>=100:
    cash = money//100
    money -= cash*100
print(cash, money)
if money >=20:
    count = money // 20
    cash += count
    money -= count * 20
print(cash, money)
if money >=10:
    count = money // 10
    cash += count
    money -= count * 10
print(cash, money)
if money >=5:
    count = money // 5
    cash += count
    money -= count * 5
print(cash, money)
