#!/usr/bin/env python
"""nims.py

A simple competitive game where players take stones from stone piles.
"""

#first block of code gets the number of stones in the pile, and makes it an integer, it also sets the player to "1"
total = raw_input("Number of stones in the pile: ")
total = int(total)
player = 1

print "Max number of stones per turn: 5"

while total > 0:
    print total,"stones left.","Player",player,#updates player on game status.
    num = raw_input("[1-5]: ")
    num = int(num)
    if num > 0 and num <= total and num <= 5:#checking to see if number is valid
        total -= num
        if player == 1:#these four lines swap which player is going.
            player = 2
        elif player == 2:
            player = 1
    else:
        print "Invalid number."
        
print "Game over. Player",player," wins!"
