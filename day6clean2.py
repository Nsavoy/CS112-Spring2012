#!/usr/bin/env python
from random import randint
s=1
t=int(raw_input())#ask for a value
rr=[]

#takes the user input and adds a number of random integers to list rr equal to the user input.
for temp in range(t):
    rr.append(randint(0,20))
print rr

"""
this rearranges all the inputs from rr.
"""

while s:
    s=0
    for i in range(1,t):
        if rr[i-1] > rr[i]:
            t1 = rr[i-1]
            t2 = rr[i]
            rr[i-1] = t2
            rr[i] = t1
            s=1
print rr
