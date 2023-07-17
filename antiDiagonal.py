# Give a N * N square matrix A, return an array of its anti-diagonals. Look at the example for more details.
# Input
# 1 2 3
# 4 5 6
# 7 8 9
# Output
# 1 0 0
# 2 4 0
# 3 5 7
# 6 8 0
# 9 0 0
# def anti_diagonal(matrix,row,column):
#     for i in range(row):
#         for j in range(column):
#             print(matrix[i][j])
def anti_diagonal(row,column,matrix):
    for x in range(row-1):
        i=0
        j=x
        while i<row:
            if 0<=j<column:
                print(matrix[i][j],end=" ")
            else:
                print("0",end=" ")
            i+=1
            j-=1
        print()

    for y in range(column):
        i=y
        j=column-1
        while j>=0:
            if 0<=i<row:
                print(matrix[i][j], end=" ")
            else:
                print("0", end=" ")
            i += 1
            j -= 1
        print()


matrix=[]
row=int(input())
column=int(input())
for i in range(row):
    matrix.append(list(map(int,input().split())))
anti_diagonal(row,column,matrix)