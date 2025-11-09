import math
def euclid(point1, point2):
    x = point1[0] - point2[0]
    y = point1[1] - point2[1]
    dis = math.sqrt(x**2+y**2)
    return dis

def inp(point, n):
    point = list(map(int, input(f"Nhap diem thu {n} ").split()))
    del point[2:]
    return point

def main():
    point1 = []
    point2 = []
    point1 = inp(point1, 1)
    point2 = inp(point2, 2)
    print(euclid(point1, point2))


main()