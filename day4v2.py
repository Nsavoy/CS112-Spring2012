#!/usr/bin/env python

"""
if statements
"""

name_in=raw_input("enter a name: ")
if name_in == "Paul":
    print "You are cool."
elif name_in == "Alec" or name_in == "Jonah" or name_in == "jack": #elif is else/if
    print "you smell bad."
else: #refers to any other answer than "paul" or the other names mentioned.
    print "You, you are not so cool."
