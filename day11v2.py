#!/usr/bin.env python

"""
ARRAY FUNCTIONS
"""


grid = []
for i in range (10):# num of rows
    row = []
    for j in range (10):# num of columns
        row.append(0)
    grid.append(row)


for i, row in enumerate(grid):
    for j, val in enumerate(row):
        print "[", i, j, "]:", val,
    print ""
#WHAT THE FORK DOES THIS DO.
    #Why is this indented:
        #you shut your mouth.


#setup:
#while not one:
#  Input
#  Update
#  Draw
#  Refresh
