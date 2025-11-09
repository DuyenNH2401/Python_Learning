def check(arr, n):
    for i in arr:
        if i % n == 0: print(i)

def main():
    n = int(input("Devide for? "))

    arr = list(map(int, input().split()))
    print(f"Devide by {n}")
    check(arr, n)

main()
