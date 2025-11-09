import math

def main():
    a = []
    n = int(input())
    for _ in range(n):
        a.append(int(input()))

    for num in a:
        print(dem_so(num))


def dem_so(n):
    count = 0
    for b in range(1, math.ceil(n/2)):
        a = n-b
        if a>b:
            count+=1
    return count

main()