
def shortest(arr):
    diff = min_val = 10**8
    for i in range(1,len(arr)):
        diff = abs(arr[i]-arr[i-1])
        min_val = min(diff, min_val)
    return min_val


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int,input().split()))
    print(shortest(arr))