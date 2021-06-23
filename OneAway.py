# One away --> There are three types  of edits that can be performed on strings : insert , remove or replace a character .
# Given 2 strings , write a function to check if they are one edit (or zero edits) away .

s1 = input("Enter a string to edit : ")
s2 = input("Enter an edited string : ")
flag1=0
flag2=0
flag3=0

def isinsert():
    c2 = 0
    c3 = 0
    if len(s1) + 1 == len(s2):
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                c2 = c2 + 1
        if s1 not in s2:
            c3 = c3 + 1
        if s1 != s2 and c2 <= 1 and c3 <= 1:
            flag1=1
            return True
        else:
            return False
    else:
        return False

def isreplace():
    c4 = 0
    if len(s1) == len(s2) :
        for i in range(len(s2)):
            if s1[i] != s2[i]:
                c4 = c4 + 1
        if s1 != s2 and c4 == 1:
            flag2 = 1
            return True
        else:
            return False
    else:
        return False


def isremove():
    count = 0
    c1 = 0
    if len(s2)==len(s1)-1:
        for i in range(len(s2)):
            if s1[i] != s2[i]:
                c1 = c1 + 1
        if s2 in s1:
            count = 1
        else:
            count = 0
        if count==1 or c1==len(s2)-1:
            flag3 = 1
            return True
        else:
            return False
    else:
        return False


def oneAway():
    if  len(s2)>len(s1)+1 or len(s2)<len(s1)-1:
        return print("False")
    elif isremove()==False and isreplace()==False and isinsert()==False:
        return print("False")
    else:
        print("isremove() :",isremove())
        print("isinsert() :", isinsert())
        print("isreplace() :",isreplace())

oneAway()