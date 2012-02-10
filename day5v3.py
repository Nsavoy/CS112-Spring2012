#!/usr/bin/env python

"""
forloops
"""

titles = ["Hitchiker's guide to the galaxy.",
          "Restraunt at the end of the universe.",
          "Life the universe and everything."]
titles.append("So long and thanks for all the fish.")#adds to the list, second print command shows all five.
titles.append("Mostly harmless.")

for title in titles[0:3]:#goes through the entire list, gives each element its own line. but with the [0:3], only shows first three, which would be numbered 0,1 and 2.
    print title
for i in range(10):#creates a list that goes up to 1 before the specificed number, in this case it stops at 9 instead of 10.
    print i
for i in range(1,11):#counts to ten
    print i
for i in range(1,11,2):#counts by twos.
    print i
