# URLify --> Replace all spaces with "%20"
# INPUT --> "Kashish Dwivedi "
# OUTPUT --> "Kashish%20Dwivedi%20"

str = input("Enter any string : ")
for i in range(len(str)):
    str = str.replace(" ","%20")
print("Output String :",str)