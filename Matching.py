lst_match = [
    "Lyon-Manchester City"
    ,"Lyon-Chelsea"
    ,"Arsenal-Liverpool"
    ,"AC Milan-Barcelona"
    ,"Real Madrid-Chelsea"
    ,"Real Madrid-Manchester City"
    ,"Lyon-Liverpool"
    ,"Liverpool-Manchester United"
    ,"Barcelona-HAGL"
    ,"Liverpool-Lyon"
    ,"AC Milan-Lyon"
    ,"AC Milan-Chelsea"
    ,"Fullham-Barcelona"
    ,"Fullham-Real Madrid"
    ,"28Tech FC-Lyon"
    ]

if __name__ == '__main__':
    lst = []
    for i in lst_match:
        index = i.index("-")
        tmp1 = i[:index]
        tmp2 = i[index + 1:]

        if tmp1 not in lst:
            lst.append(tmp1)
        if tmp2 not in lst:
            lst.append(tmp2)

    lst.sort()

    dic = {key: "" for key in lst}

    for i in lst_match:
        index = i.index("-")
        tmp1 = i[:index]
        tmp2 = i[index + 1:]
        dic[tmp1] = dic[tmp1] + tmp2+" "
        dic[tmp2] = dic[tmp2] + tmp1+" "

    for key, value in dic.items():
        print(f"{key} : {value}")