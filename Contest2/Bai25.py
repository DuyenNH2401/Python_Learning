
def factorial(n):
    if n < 2: return 1
    else: return n*factorial(n-1)
def main():
    n = int(input())
    sum = 2
    for i in range(n):
        sum+= 1 / factorial(n)
        print(sum)
    print(f"{sum:.4f}")

if __name__ == '__main__':
    main()