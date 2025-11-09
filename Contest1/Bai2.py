def func(a, b, c):
    return a*(b+c)+b*(a+c)
def main():
    a, b, c = map(int, input().split())
    print(func(a, b, c))

main()