#cách nhập nhiều số trên một dòng lệnh input
from os.path import split

a = input("Nhap 3 so: ")
b = a.split()
#sử dụng map để chuyển giá trị sang int không thì in ra sẽ có giá trị str
x, y, z = map(int, b)
print(type(x), type(y), type(z), sep='\n')