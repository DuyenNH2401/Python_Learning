
def doixung(left, right, arr):
    if left >= right:
        return True
    else:
        if arr[left] != arr[right]:
            return False
        else:
            doixung(left+1, right - 1, arr)
            print("1")

if __name__ == '__main__':
    arr = [1, 2, 3, 2, 1]

    if doixung(0, len(arr) - 1 , arr):
        print("Yes")
    else: print("No")

