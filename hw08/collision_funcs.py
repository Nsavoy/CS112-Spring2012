#!/usr/bin/python env

# Calculate if a point is within a box
#    check if a point is inside a given box.  
#
#    Parameters:
#       pt: list of 2 numbers (x,y)
#       box: list of 4 numbers (x,y,w,h).  x,y is the top left point.  w,h is the width and height

# def point_in_box(pt, box):
def point_in_box(pt, box):
    px, py = pt
    bx, by, bw, bh = box
    return px >= bx and px < bx + bw and py >= by and py < by + bh

