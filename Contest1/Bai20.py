def main():
    a, m, n = map(int, input().split())
    row = count_brick(m, a)
    column = count_brick(n, a)
    nob = row * column
    print(nob)

def count_brick(size, a):
    count = 0
    while size > 0:
        size -= a
        count+=1
    return count

main()