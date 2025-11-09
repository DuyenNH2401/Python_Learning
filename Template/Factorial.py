import math


def fact(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        count = 0
        while n % i == 0:
            count+=1
            n //= i
            if count>0:
                print(str(i)+"^"+str(count), end =" x ")
    else:
        print(str(n)+ "^1")


def main():
    while True:
        n = int(input("Number = "))
        if n > 0: break
    fact(n)

if __name__ == "__main__":
    main()