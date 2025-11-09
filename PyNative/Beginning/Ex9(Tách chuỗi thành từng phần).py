def tach_ra(num):
    arr =[]
    for i in num:
        b = int(i)
        arr.append(b)
    return arr
def duyet(arr2):
    n = int(len(arr2))
    count = 0
    for i in range(int(n/2)):
        if arr2[i] == arr2[n-1-i]: count +=1

    if count == int(n/2): return True
    else : return False

def main():
    num = str(input())
    arr2 = tach_ra(list(num))
    check = duyet(arr2)
    print(f"Original number {int(num)}")
    if check: print("Yes! given number is palindrome number")
    else: print("No! given number is not palindrome number")

main()