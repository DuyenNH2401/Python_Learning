def main():
    n = int(input())
    print(f"Printing current and previous number in a range({n})")
    sum(n)
def sum(n):
    for i in range(n):
        cur_num = i
        pre_num = 0
        if cur_num > 0:
            pre_num = cur_num-1
        sum = cur_num + pre_num
        print(f"Current Number {i} Previous Number {pre_num} Sum:{sum}")

main()