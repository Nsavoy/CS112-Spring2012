#!/usr/bin/env python
from hwtools import *

print "Section 4:  For Loops"
print "-----------------------------"

nums = input_nums()
# 1. What is the sum of all the numbers in nums?


total=0
for num in nums:
    total+=num
print "1.",total



# 2. Print every even number in nums
for num in nums:
    if num % 2 == 0:
        print "2. Even numbers: ",num
    


#CODE GOES HERE


# 3. Does nums only contain even numbers? 

some_odd = False
for num in nums:
    if num % 2 != 0:
        some_odd = True
if some_odd == True:
    print "3. Some odd."
else:
    print "3. All even."


# 4. Generate a list every odd number less than 100. Hint: use range()
odds = []

for i in range (1,100,2):
    odds.append(i)
print "4. " odds 
