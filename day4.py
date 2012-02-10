#!/usr/bin/env python

"""
A y-loop.
"""

# > is greater than, < less than >= greater than or equal to, != not equal to, == is comparitive equal: checks if left is = to right. second = stands for to, ie5 is =to 5. "and" "or" "not" are other commands that function EXACTLY as you'd expect.

count=raw_input("Count down from: ")
count=int(count)

while count>0:
    print count
    count-=1

print "Brastoff."
