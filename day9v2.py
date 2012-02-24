#!/usr/bin/env python

def ftoc(temp):
    cent = temp - 32
    cent *= 5
    cent /= 9
    return cent

num = float(raw_input("Enter a temperature in F: "))
print "in C that is: ", ftoc(num)
