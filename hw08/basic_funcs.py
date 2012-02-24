#!/usr/bin/env python

# Create a greeter
#    create a greeter that says hello to someone in all lower case.  Use print statements
#



def greeter(name): #gets an input for greeter
    name = str(name) #makes sure that an int will pass through the function w/o barfing
    print "hello,", name.lower() #lowercases every letter.



def box(w, h):

#checks the parameters to make sure every value is valid.
    if w <= 0 or h <= 0 or type(w) != int or type(h) != int:
        print "Error: Invalid Dimensions"
        return #goes back to start
#establishes the variables top and sides.
    if w == 1:
        top = "+"
        sides = "|"
    else:
        top = "+" + "-"*(w-2) + "+"
        sides = "|" + " "*(w-2) + "|"
    print top
    for i in range(h-2):
        print sides
    if h > 1:
        print top




# Draw a box
#    given a width and a height, draw a box in the terminal.  Use print statements
#
#  



# ADVANCED
# Draw a Festive Tree
#    draw a festive tree based on the specifications.  You will need to discover the arguments 
#    and behavior by running the unittests to see where it fails.  Return a string, do not print.
#
#  ex:
#    >>> print tree()
#        *
#        ^
#       ^-^
#      ^-^-^
#     ^-^-^-^
#    ^-^-^-^-^
#       | |
#       | |

# def tree()
