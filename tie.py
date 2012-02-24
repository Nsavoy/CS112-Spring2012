#!/usr/bin/env python
"""
tiefighter
"""
#voodoo
import pygame #brings us that delicious pygame function libraries.
from pygame import draw
from pygame.locals import *
#settings

pygame.init()

screen = pygame.display.set_mode((800,600)) #Voodoo.
screen.fill((0,0,0))

col=0
dir=1
done = False
def draw_tie(surf, color, pos):
    x, y = pos
    draw.rect(surf, color, (x, y, 5, 40))
    draw.rect(surf, color, (x+35, y, 5, 40))
    draw.rect(surf, color, (x, y+17, 40, 5))
    draw.circle(surf, color, (x+20, y+20), (10))

pygame.key.set_repeat(100,100)
while not done:
    for event in pygame.event.get():#more quitting rules.
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True
    col += dir
    if col > 255 or col < 0:#reverses loop
        dir *= -1
        col += dir
    draw_tie(screen, (col, 0, col), (20, 30))
    draw_tie(screen, (col, col, 0), (200, 130))
    draw_tie(screen, (0, col, col), (300, 400))

    pygame.display.flip()
