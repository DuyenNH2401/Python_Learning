
if __name__ == '__main__':
    arr = list(map(int, input().split()))
    cnt = [0] * (len(arr) + 1)

    for i in arr:
        cnt[i] += 1

    for i in arr:
        print(i, cnt[i])