def dectohex(n):
    if n != 0:
        r = n % 16
        if r < 10:
            print(r, end="")
        else:
            print(chr(r + 55), end="")
        dectohex(n//16)
    return

if __name__ == '__main__':
    dectohex(995)