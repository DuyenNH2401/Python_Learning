def xu_li(list,tmp, num):
    for i in list:
        if i % 2 == num:
            tmp.append(i)
    return tmp

def main():
    list1 = list(map(int, input("list1 = ").split()))
    list2 = list(map(int, input("list2 = ").split()))
    tmp_list = []
    xu_li_list1 = xu_li(list1, tmp_list, 1)
    xu_li_final = xu_li(list2, xu_li_list1, 0 )
    xu_li_final.sort()
    print(xu_li_final)

main()