
def create_matrix(n, row1, row2, col1, col2):
    matrix = [[0] * n for _ in range(n)]
    cnt = n**2
    while col1 <= col2 and row1 <= row2:

        for i in range(col2, col1-1,-1):
            matrix[row1][i] = cnt
            cnt -= 1
        row1 += 1

        for i in range(row1, row2+1):
            matrix[i][col1] = cnt
            cnt -= 1
        col1 +=1

        for i in range(col1, col2+1):
            matrix[row2][i] = cnt
            cnt -= 1
        row2 -=1

        for i in range(row2,row1-1,-1):
            matrix[i][col2] = cnt
            cnt -=1
        col2 -= 1

    return matrix
def sum_of_diagonals(n):
    total = 0


    return total

if __name__ == '__main__':
    n = int(input("size= "))
    col1, col2 = 0, n - 1
    row1, row2 =  0, n - 1
    matrix = create_matrix(n, row1, row2, col1, col2)
    for i in matrix:
        print(i)