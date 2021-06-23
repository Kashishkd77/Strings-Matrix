# Rotate Matrix --> Given an image represented by an N*N matrix , where each pixel in the image is 4 bytes .Rotate the image 90 degrees.

# ERROR --> Rotation in same matrix

arr = [[1,2,3],[4,5,6],[7,8,9]]
len_r=len(arr)
len_c=len(arr[0])
print("GIVEN MATRIX : ")
for i in arr:
    print(i)
print()

rotate_arr=[]
print("ROTATE MATRIX : (in another matrix)")
for i in range(len_r-1,-1,-1):
    x=[]
    for j in range(len_c):
        x.extend([arr[j][i]])
    rotate_arr.append(x)
for i in rotate_arr:
    print(i)

print()
print("ROTATE MATRIX : (in the matrix)")
for i in range(len_r-1,-1,-1):
    x=[]
    for j in range(len_c):
        x.extend([arr[j][i]])
    arr.append(x)
for i in range(3,len(arr)):
    print(arr[i])