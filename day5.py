#!/usr/bin/env python

"""
lists?
"""

names=['bob','fred']#check out this list, bitches.

print names[0]#first item in a list is item 0, so even if there are 5 elements, you can only access 0-4
print names[1]
print len(names)#tells you number of elements

letters = ['a','d','f']#sticks together with lower, could also letters += ['b','c']
letters[1:1] = ['b','c']
print letters
print letters [-1]#accesses just the last element

letters2 = letters
letters[0] = 'huh'
print letters2
