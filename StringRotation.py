# String Rotation --> Assume you have a method is isSubstring which checks if one word is a substring of another.
# Given 2 strings , s1 and s2 , write code to check if s2 is a rotation of s1 using only one call to isSubstring
# Example --> "waterbottle" is a rotation of "erbottlewat"

s1 = input("ENTER A STRING : ")
s2 = input("ENTER ROTATED STRING : ")
s3 = ""
s4 = ""
def isSubstring():
    if len(s1)==len(s2):
        s4="".join([s1[i] for i in range(0,int(len(s1)/3))])
        s3="".join([s1[i] for i in range(int(len(s1)/3),len(s1))])
        s3=s3+s4
        if s2==s3:
            print(s2,"is the rotation of",s1)
        else:
            print(s2, "is the not rotation of", s1)
    else:
        print(s2, "is the not rotation of", s1)
isSubstring()