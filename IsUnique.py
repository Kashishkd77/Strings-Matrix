# Is Unique --> Implement an algorithm to determine if a string has all unique characters .
str=input("Enter a string : ")
print("Entered string is : ",str)
flag=0
for i in range(len(str)):
    for j in range(len(str)):
        if i!=j:
            if str[i]==str[j] and str[j]!=" ":
                print("Given string is not unique")
                exit()
            else:
                flag=1
if flag==1:
    print("Given string is unique")
