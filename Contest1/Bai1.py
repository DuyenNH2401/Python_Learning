import math
def func(x):
    return math.pow(x,3)+3*math.pow(x, 2)+x+1
def main():
    num = int(input("x = "))
    print(int(func(num)))

if __name__ == "__main__":
    main()