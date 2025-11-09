n = int(input())
count = 1
for i in range(n):
    for j in range(n):
        print(count, end =" ")
        count+=1
    print("")

print("")

for i in range(1,n+1):
    for j in range(i,n+i):
        print(j, end="")
    print("")

print("")

for i in range(1,n+1):
    for j in range(n):
        prt = "~" if j < n-i else i
        print(prt, end = "")
    print("")

print("")

for i in range(1, n+1):
    for j in range(1, n+1):
        print(i, end="")

print("")
count = 1
for i in range(1, n+1):
    count2 = n-1
    for j in range(0, count):
        if j == 0:
            print(i, end=" ")
        else:
            if j == 1:
                num = i+count2
            else: num+=count2
            print(num, end=" ")
            count2-=1
    count += 1
    print("")