#!/usr/bin/env python
"""
lines
"""
#voodoo
import pygame #brings us that delicious pygame function libraries.
from pygame.locals import *
#settings
black = 0,0,0
red = 255,0,0
size = 400,400
pygame.init()
screen = pygame.display.set_mode(size) #Voodoo.

done=False
sep=8
pygame.key.set_repeat(100,100)
while not done:
    for event in pygame.event.get():#more quitting rules.
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True
        elif event.type == KEYDOWN and event.key == K_UP:
            sep += 1
        elif event.type == KEYDOWN and event.key == K_DOWN:
            sep -= 1
#draw

    screen.fill(black)
    for i in range (0,400,sep):#to seperate, set up a counting range.as is done here from 0-400, counting by eights.
        pygame.draw.line(screen,red,(i,0),(399,i))
        pygame.draw.line(screen,red,(0,i),(i,399))#goes to 399, cause the list ends at 400. Structure is as follows (surface, color, startpos, endpos, width=1, unless you put in a value.
        pygame.draw.line(screen,red,(i,399),(399,399-i))
        pygame.draw.line(screen,red,(399-i,0),(0,i))
    pygame.display.flip()
                       
