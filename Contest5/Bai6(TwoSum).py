
def twosum(arr, k):
    checked = []
    result = []
    for num in arr:
        tmp = k - num
        if tmp in checked:
            result.append((num, tmp))
        else:
            checked.append(num)
    return result
if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7, 8,9]
    a = twosum(nums, 11)
    print(a)