
def s(n):
    if n == 0:
        return n
    else:
        return n % 10 + s(n//10)

if __name__ == '__main__':
    print(s(12345))