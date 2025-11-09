def create_and_check_fibo(n):
    fn, f1, f2 = 0, 1, 1
    if n == 1: return True
    for i in range(100):
        fn = f1 + f2
        f1 = f2
        f2 = fn
        if fn == n:
            return True
        if fn > n:
            return False

if __name__ == '__main__':
    n = int(input())
    print(create_and_check_fibo(n))