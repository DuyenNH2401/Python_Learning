
def sumofnum(n):
    sum = 0
    while n>0:
        sum+=n%10
        n = n//10
    return sum
def main():
    n = int(input())
    while n>=10:
        n = sumofnum(n)
        print(n)

if __name__ == '__main__':
    main()