
def dectobin(n):
    if n != 0:
        dectobin(n // 2)
        print(n % 2, end=" ")
    return


if __name__ == '__main__':
    dectobin(11)