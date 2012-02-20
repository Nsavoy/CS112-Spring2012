#!/usr/bin/env python
"""
Selection sort

This is my selection sort, it's not working right!!!
I used this:
    http://en.wikipedia.org/wiki/Selection_sort
"""
from hwtools import input_nums

nums = input_nums()


print "Before sort:"
print nums

N = len(nums)
for ipos in range(N):
    imin = ipos
    for i in range(ipos + 1, N):
        if nums[i] < nums[imin]:
            imin = i
    nums[ipos], nums[imin] = nums[imin], nums[ipos]

final = []
for i in (nums):
    final.append(i)
print "After sort:"
print final
