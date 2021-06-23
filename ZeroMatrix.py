# Zero Matrix --> Write an algorithm such that if an element in an M*N matrix is 0 , its entire row and column are set to 0.
# CLONING ERROR

arr = [[1,2,0],[4,5,6],[7,8,0]]
len_r=len(arr)
len_c=len(arr[0])

print("GIVEN MATRIX : ")
for i in arr:
    print(i)
print()

flag=0
zero_matrix=[[1,2,0],[4,5,6],[7,8,0]]
#zero_matrix=arr --> cloning problem
#zero_matrix=arr.copy() --> cloning problem
for i in range(len_r):
    m=i
    for j in range(len_c):
        n=j
        if arr[i][j]==0:
            print("O found at row  : ",i+1," , column : ",j+1)
            flag=1
            for y in range(len_r):
                zero_matrix[m][y]=0
            for y in range(len_r):
                zero_matrix[y][n]=0
        continue
if flag==0:
    print("No 0's found as an element of matrix . Hence , Zero matrix is same as original matrix.")
print()
print("Zero Matrix is : ")
for k in zero_matrix:
    print(k)
print()
