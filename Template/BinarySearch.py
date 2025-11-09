
def binary_search(lst, x):
    l = 0
    r = len(lst)
    while l <= r:
        m = (l+r) // 2
        if lst[m] == x:
            return True
        if lst[m] < x:
            l = m + 1
        if lst[m] > x:
            r = m - 1
    return False

if __name__ == '__main__':
    lst = [1, 11, 13, 7, 9, 8, 6, 5, 3, 4, 2]
    lst.sort()
    a = binary_search(lst, 11 )
    print(a)