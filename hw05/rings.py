#!/usr/bin/env python

import pygame
from pygame.locals import *

## COLORS
blu = 0, 133, 199
red = 223, 0, 36
yel = 244, 195, 0
gre = 0, 159, 61
bla = 0, 0, 0
whi = 255, 255, 255

thick = 20


## MAIN
pygame.init()
screen = pygame.display.set_mode((800, 388))
pygame.display.set_caption("Olympic Rings   [press ESC to quit]")

## Draw
screen.fill(whi)

pygame.draw.circle(screen, blu, (170, 150), 100, thick)
pygame.draw.circle(screen, bla, (400, 150), 100, thick)
pygame.draw.circle(screen, red, (630, 150), 100, thick)
pygame.draw.circle(screen, yel, (285, 250), 100, thick)
pygame.draw.circle(screen, gre, (515, 250), 100, thick)


#################################
##  DRAW OLYPIC RINGS HERE
##
##  hint, lookup pygame.draw
##  specifically circle, ellipse,
##  and arc.  Also, the width
##  parameter
#################################


## Loop
clock = pygame.time.Clock()
done = False
while not done:
    event = pygame.event.poll()
    if event.type == QUIT:
        done = True
    elif event.type == KEYDOWN and event.key == K_ESCAPE:
        done = True

    pygame.display.flip()
    clock.tick(30)

print "ByeBye"
