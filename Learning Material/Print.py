"""cú pháp
print(object, sep=seperator, end = end)
nếu không có lệnh end thì sau print nó hiểu là tự Enter"""
#sep=
print("Hello","Vietnam", sep="-")
print("Vietnam","I'm from", "Vietnam", sep="#")
#end=
print("Hello", end=" ")
print("I'm from", end="\n")
#có thể dùng end="\n" để xuống dòng
print("Vietnam")