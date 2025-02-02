# Point Object
# =====================================
# Create a Point point class.  Point objects, when created, look like this:
#     >>> pt = Point(3,4)
#     >>> print pt.x
#     3
#     >>> print pt.y
#     4
#
# In addition points have the following methods:
#    distance(self, other):
#        calculates the distance between this point and another
#    
#    move(self, x, y):
#        sets the points location to x,y
# 
#    translate(self, x, y):
#        offsets the point by x and y
# 
#    When all done, points should work like this:
#
#    >>> a = Point(0,0)
#    >>> b = Point(0,0)
#    >>> b.move(2, 2)
#    >>> print b.x, b.y
#    2 2
#    >>> b.translate(1,2)
#    >>> print b.x, b.y
#    3 4
#    >>> print a.distance(b)
#    5
#


import math

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def distance(self, other):
        d = math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)
        return d

    def move(self, x, y):
        self.x = x
        self.y = y

    def translate(self, x, y):
        self.x += x
        self.y += y
