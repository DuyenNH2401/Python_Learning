
year = int(input())
if year % 400 == 0 or (year % 4 == 0 and year % 100 !=0):
    print("Nam nhuan")
else: print("Nam khong nhuan")