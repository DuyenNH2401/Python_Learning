
def check(arr):
    print("Given list: ", arr)
    if arr[0] == arr[len(arr)-1]:
        return True
    else: return False


def main():
    arr = list(map(int,input().split()))
    print("Result is ", check(arr))

main()