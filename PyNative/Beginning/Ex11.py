n = str(input())
list1 = [int(i) for i in n]
list1.reverse()
print("Given number: ",n)

for i in list1:
    print(i, end=" ")