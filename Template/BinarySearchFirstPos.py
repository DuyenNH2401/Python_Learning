"""
tìm vị trí đầu tiên xuất hiện của x
"""

def binary_search(lst,x):
    l = 0
    r = len(lst) - 1
    pos = -1
    while l < r:
        m = (l + r) // 2
        if lst[m] == x:
            pos = m
            r = m - 1
        if lst[m] < x:
            l = m + 1
        if lst[m] > x:
            r = m - 1
    return pos

lst = [1, 1, 3, 9, 8 ,7, 6, 6, 6, 6, 6, 5, 4, 3, 2]
lst.sort()
print(lst)
a = binary_search(lst, 6)
print(a)