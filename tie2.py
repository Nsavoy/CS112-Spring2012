#!/usr/bin/env python
"""
tiefighter
"""
#voodoo
import pygame #brings us that delicious pygame function libraries.
from random import randint
from pygame import draw
from pygame.locals import *
#settings

pygame.init()

screen = pygame.display.set_mode((800,600)) #Voodoo.
screen.fill((0,0,0))

col=200
dir=1
color=[]
pos=[]
size=[]
done = False
def draw_tie(surf, color, pos, size=40):
    x, y = pos
    width =  size / 8
    height = size / 8
    draw.rect(surf, color, (x, y, width, size))
    draw.rect(surf, color, (x+size-width, y, width, size))
    draw.rect(surf, color, (x, y+(size-width)/2, size, width))
    draw.circle(surf, color, (x+size/2, y+size/2), (size/4))

pygame.key.set_repeat(100,100)
while not done:
    for event in pygame.event.get():#more quitting rules.
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True
        elif event.type == MOUSEBUTTONDOWN:
            color.append((col, 0, col))
            pos.append(pygame.mouse.get_pos())
            size.append(randint(20, 80))#includes 80

    col += dir
    if col > 255 or col < 100:#reverses loop
        dir *= -1
        col += dir


    screen.fill((0,0,0))
    for i in range(len(color)-1, -1, -1):
        size[i] -= 2
        if size[i] <= 0:
            size.pop(i)
            color.pop(i)
            pos.pop(i)
        else:
            draw_tie(screen, color[i], pos[i], size[i])
    pygame.display.flip()
