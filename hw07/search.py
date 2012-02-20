#!/usr/bin/env python
"""
Binary Search

This was supposed to be a binary search algorithm but it isn't working...
I used the Iterative implementation from here:
    http://en.wikipedia.org/wiki/Binary_search_algorithm
"""
from hwtools import input_nums

inpnums = input_nums()
nums = sorted(inpnums)
#type x

print "I have sorted your numbers"
x = raw_input("Which number should I find: ")
lo = 0#little m is min, big M is max.
hi = len(nums)-1
x = int(x)
md = (hi + lo)/2

while hi >= lo:
    md = (hi + lo)/2
    if nums[md] == x:
        break#this section checks the length of the list
   
    elif x > nums[md]:
       lo = md + 1
       
    else:
        hi = md - 1

if nums[md] == x:

    print "Found", x ,"at", md
else:
    print "Could not find", x#Why can't it find any numbers?
