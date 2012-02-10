#!/usr/bin/env python
from hwtools import *

print "Section 3:  Lists"
print "-----------------------------"

nums = input_nums()
# 1. "nums" is a list of numbers entered from the command line.  How many
#    numbers were entered?

print "1.",len(nums)

# 2.  Append 3 and 5 to nums
nums.append(3)
nums.append(5)

print "2.", nums

# 3.  Remove the last element from nums
del nums[-1]
print "3.", nums


# 4.  Set the 3rd element to 7
nums2 = nums
nums[2] = 7
print "4.", nums

