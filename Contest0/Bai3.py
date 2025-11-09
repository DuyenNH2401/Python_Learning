import math
a = input()
x, y, z, t = map(int, a.split())

print(x, y, z, t, sep=", ")
print(x+y+z+t)
print(x-y+z*t)