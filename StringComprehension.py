# INPUT - abbcaccaddddb
# OUTPUT - a1b2c1a1c2a1d4b1 or
# OUTPUT - Return input string if its length is more than the required output string
str = input("Enter string : ")
print("Given string :",str)
i=0
str1=""
while i<len(str):
    count = 1
    for j in range(i+1,len(str)):
        if str[i]==str[j]:
            count = count + 1
        else:
            break
    count_s="%s"%count
    str1=str1+str[i]+count_s
    i=i+count
    # print(str1)
if len(str) <= len(str1):
    print("String Comprehension :",str)
else:
    print("String Comprehension :",str1)