
def countdigital(n):
    if n < 10:
        return 1
    else: return 1 + countdigital(n//10)




if __name__ == '__main__':
    print(countdigital(123456))
    