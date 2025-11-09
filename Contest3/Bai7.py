from rsa.prime import is_prime


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

def sum_of_nums(n):
    sum = 0
    while n!= 0:
        sum += n % 10
        n//=10
    return sum

if __name__ == '__main__':

    n = int(input())
    for i in range(n):
        tmp = sum_of_nums(i)
        if is_prime(i) and create_and_check_fibo(tmp):
            print(i, end=" ")