#!/usr/bin/env python
from hwtools import *

print "Section 2:  Loops"
print "-----------------------------"

# 1. Keep getting a number from the input (num) until it is a multiple of 3.
num = 0
num = raw_input("count down from: ")
num = int(num)
print "1.", num

while num % 3 != 0:
    num = raw_input("count down from: ")
    num = int(num)

# 2. Countdown from the given number to 0 by threes. 
#    Example:
#      12...
#      9...
#      6...
#      3...
#      0

print "2. Countdown from", num
while num > 0:
    print num
    num-=3
#CODE GOES HERE



# num = int(raw_input("3. Countdown from: "))

