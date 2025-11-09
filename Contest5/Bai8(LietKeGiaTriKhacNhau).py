
def lietke(arr):
    cnt = [False] * (len(arr)-1)
    for i in arr:
        if not cnt[i]:
            print(i, end= " ")
            cnt[i] = True

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    lietke(arr)