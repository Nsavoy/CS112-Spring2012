#!/usr/bin/env python


"""
Maze pesudocode
"""

define the player #
define the boundaries #(Must hit walls, and must NOT be able to leave through the enterence.)

while in maze:####ASSUMING MAZE EXISTS####
    if player x, y = x, y of Exit: # if ent = exit, win.
        quit
    else:
        go east (x+=1)
        if cant go east#collide with wall:
            go north (y-=1)
            if cant go north:#same as top
                go west (x-=1)
                if cant go west: # same as top
                    go south(y+=1)
                    if cant go south:
                        go east
                        until all routes(NOT POINTS) on path checked:
                        then try middle routes
        update x, y 




sotre xy
while not at end
check directions
if one option, take it
if more, check each store the loc, present dir.
have we been here before?
true? GO other places
False Continue
Eother way update loc


class room:
    loc
    possible directions out





#
Check availabe directions
Go down avaialble directions until are possibilities exhausted
???
profit.


