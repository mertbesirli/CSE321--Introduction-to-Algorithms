# -*- coding: utf-8 -*-

def test1():
    #Create array five size
    a = [None] * 5

    #Its necessary for binary to decimal
    temp = [None] * len(a)

    for i in range(len(a)):
        temp[i] = i
    
    #counter for binary to decimal
    count = 0
    #If last element is absent element,use it
    flag = 1
    #Array elements is 0,1,2,3 length 5
    #Absent element is 4
    a[0] = "0000"
    a[1] = "0001"
    a[2] = "0010"
    a[3] = "0011"

    for i in range(len(a)-1):
        x = split(a[i])
        convertint(x)
        binarytoDecimal(x,temp,count)
        count += 1
    
    for i in range(len(a)):
        if i != temp[i]:
            print("Found absent element is: ", i)
            flag = 0
    if flag != 0:
        print("Found absent element is: ", len(a))
def test2():
    #Create array five size
    a = [None] * 5

    #Its necessary for binary to decimal
    temp = [None] * len(a)

    for i in range(len(a)):
        temp[i] = i
    
    #counter for binary to decimal
    count = 0
    #If last element is absent element,use it
    flag = 1
    #Array elements is 0,1,2,3 length 5
    #Absent element is 4
    a[0] = "0000"
    a[1] = "0001"
    a[2] = "0010"
    a[3] = "0100"

    for i in range(len(a)-1):
        x = split(a[i])
        convertint(x)
        binarytoDecimal(x,temp,count)
        count += 1
    
    for i in range(len(a)):
        if i != temp[i]:
            print("Found absent element is: ", i)
            flag = 0
    if flag != 0:
        print("Found absent element is: ", len(a))
#String element is split char by char
def split(word):
    return [char for char in word]
#Convert to str type to integer type
def convertint(x):
    for i in range(0,len(x)):
        x[i] = int(x[i])
#Convert binary to decimal
def binarytoDecimal(x,temp,count):
    decimal = 0
    base = 1
    #binary to decimal processing
    for i in reversed(x):
        decimal += i * base
        base = base *2
    #Take temp array count index to decimal value    
    temp[count] = decimal

print("#Testing last element is absent#")
#For last element is absent
test1()
print("#Testing anything element is absent#")
#For anything element is absent
test2()

    


