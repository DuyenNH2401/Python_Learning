"""
tìm ước chung lớn nhất của a! và b!
"""
def main():
    a, b = map(int, input().split())
    print(Euclid(factorial(a), factorial(b)))

def factorial(n):
    fac = 1
    if n<2: return 1
    else: return n*factorial(n-1)

def Euclid(a, b):
   while True:
        a, b = b, a % b
        if b == 0: return a

if __name__ == '__main__':
    main()