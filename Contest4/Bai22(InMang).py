
def printarr(arr, place, n):
    if place < 0:
        return
    printarr(arr, place - 1, n)
    print(arr[place], end=" ")

def reprintarr(arr, place, n):
    if place > n-1:
        return
    printarr(arr, place + 1, n)
    print(arr[place], end=" ")

if __name__ == '__main__':
    n = 5
    arr = [1, 2, 3, 4, 5]
    printarr(arr, n - 1, n)
    print()
    reprintarr(arr, 0, n)
