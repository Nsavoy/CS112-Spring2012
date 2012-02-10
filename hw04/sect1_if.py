#!/usr/bin/env python
from hwtools import *

print "Section 1:  If Statements"
print "-----------------------------"

# 1.  Is n even or odd?
n = raw_input("Enter a number: ")
n = int(n)

if  n % 2 == 0 :#couldn't figure this out, Jonah helped to find the modulo command.
    print "1.",n," is an even number."
    print "2.",n
else:
    print "1.",n," is an odd number."
    print "2.",n*2
new=2*n

# 2. If n is odd, double it


# 3. If n is evenly divisible by 3, add four
if n % 3 == 0 :
   if n % 2 != 0:
       print "3.",2*n+4
   else:
       print "3.",n+4


# 4. What is grade's letter value (eg. 90-100)
grade = raw_input("Enter a grade [0-100]: ")
grade = int(grade)

if grade in range (0,50):
    print "4. F."
elif grade in range (51,69):
    print "4. D."
elif grade in range (70,79):
    print "4. C."
elif grade in range (80,89):
    print "4. B."
elif grade in range (90,100):
    print "4. A."


