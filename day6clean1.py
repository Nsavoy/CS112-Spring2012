#!/usr/bin/env python
inputList=[]
inputNumber=None

#getting a list of numbers from user.
while inputNumber != "":
    inputNumber = raw_input()#inputNumber variable 3 is a number from raw input
    if inputNumber.isDigit():
        inputList.append(float(inputNumber))

#total the list of numbers.
total=0
for num in inputList:
    total += num

#print average of list.
print total/len(inputList)
