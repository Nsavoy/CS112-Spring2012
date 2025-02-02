#!/usr/bin/env python
"""
multidim.py

Multidimensional Arrays
=========================================================
This section checks to make sure you can create, use, 
search, and manipulate a multidimensional array.
"""


# 1.  find_coins
#       find every coin (the number 1) in a givven room
#          room: a NxN grid which contains coins

#          returns: a list of the location of coind
#
#       Example:
#       0 0 0 1 0 0
#       0 0 1 0 0 0
#       0 0 0 0 1 0
#       0 0 0 0 0 0
# 
#       >>> find_coins(room)
#       [ [3, 0], [2, 1], [4, 2] ]

def find_coins(room):
    ""    
    coins = []
    for y, row in enumerate(room):
        for x, val in enumerate(row):
            if val == 1:
                coins.append([x, y])
    return coins


# 2. distance_from_player
#      calculate the distance from the player for each 
#      square in a room.  Returns a new grid of given
#      width and height where each square is the distance
#      from the player
import math
def distance_from_player(player_x, player_y, width, height):
    "calculates the distance of each square from the player"
    grid = []
    for y in range(height):# num of rows
        row = []
        for x in range(width):# num of columns
            distance = math.sqrt((x - player_x)**2 + (y - player_y)**2)
            row.append(distance)
        grid.append(row)
    return grid
#FOG OF WAR
