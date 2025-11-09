
def fibo(n):
    fn = 0
    f1, f2 = 1, 1
    print(f1)
    print(f2)
    for i in range(n-2):
        fn = f1 + f2
        f1 = f2
        f2 = fn
        print(fn)

if __name__ == '__main__':
    n = int(input())
    fibo(n)