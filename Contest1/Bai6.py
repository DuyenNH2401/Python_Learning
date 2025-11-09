import math

def check(n):
    # chia 2
    if n % 2 == 0: Print("Yes")
    else: print("No")
    # chia 3 và 5
    if n % 3 == 0 and n % 5 == 0: print("Yes")
    else: print("No")
    # chia 3 va không chia hết cho 7
    if n % 3 == 0 and n % 7 != 0: print("Yes")
    else: print("No")
    # chia het cho 3 hoặc 7
    if n % 3 == 0 or n % 5 ==0: print("Yes")
    else: print("No")
    #  30<N<50
    if 30<n<50: print("Yes")
    else: print("No")
    # n>30 và chia hết cho 1 trong 3 số
    if n > 30 and (n % 2== 0 or n % 3 == 0 or n % 5 == 0):
        print("Yes")
    else: print("No")
    # n số có hai chữ số và tận cùng là số nguyên tố
    tmp = n % 10
    if 9<n<100 and (tmp == 2 or tmp == 3 or tmp == 5 or tmp == 7):
        print("Yes")
    else: print("No")
    # n<100 và chia hết cho 23
    if n <= 100 and n % 23 == 0:
        print("Yes")
    else: print("No")
    # n không thuộc [10;20]
    if 10 <= n <= 20:
        print("No")
    else: print("Yes")
    # chữ số tận cùng là bội số của 3
    if (n % 10) % 3 == 0:
        print("Yes")
    else: print("No")

def main():
    while True:
        n=int(input("Nhập số N không âm: "))
        if n > 0: break
    check(n)
main()

