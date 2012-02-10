#!/usr/bin/env python

"""
Black screen.
"""
#voodoo
import pygame #brings us that delicious pygame function libraries.
from pygame.locals import *

screen_size = 640,480 #screensize
background = 75,55,105 #colors, amount of red, green and blue respectively 0-255.

#initiate pygame
pygame.init()
screen = pygame.display.set_mode(screen_size) #Voodoo.

done=False
while not done:#as long as it is not done, we goood.
    event = pygame.event.poll()#click something, or type key, poll checks for all.
    if event.type == QUIT:#if quit was pressed.
        done = True
    elif event.type == KEYDOWN and event.key == K_ESCAPE:
        done = True
    elif event.type == KEYDOWN and event.key == K_w:
        background=200,52,89
    elif event.type == KEYDOWN and event.key == K_s:
        background=75,55,105
    elif event.type == MOUSEBUTTONDOWN:
        print "Mouse",pygame.mouse.get_pos()
    screen.fill(background)#fills a background with color.
    pygame.display.flip()#Double buffering?
print "byebye!"
