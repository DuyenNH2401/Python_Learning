import math

def fact(n):
    for i in range(2, int(math.sqrt(n))+1):
        while n % i == 0:
            print(i, end=" x ")
            n/=i
    else:
        print(int(n))

def main():
    while True:
        n = int(input("Number = "))
        if n>0:break

    fact(n)
main()