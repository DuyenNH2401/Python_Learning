def main():
    print("odd or even?")
    print("1. odd")
    print("2. even")
    num = int(input())
    n = input("Original String is ")
    print(f"Printing only {"even" if num == 2 else "odd"} index chars")
    match num:
        case 1:
            odd(n)
        case 2:
            even(n)
def odd(n):
    for i in range(0, len(n), 2):
            print(n[i+1])
def even(n):
    for i in range(1, len(n), 2):
            print(n[i-1])
main()