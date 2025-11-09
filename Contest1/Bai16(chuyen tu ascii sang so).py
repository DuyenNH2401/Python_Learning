char = str(input())
num = ord(char)

if 96 < num < 122:
    print(chr(num+1))
elif 64 < num < 90:
    print(chr(num+1).lower())
else: print("a")