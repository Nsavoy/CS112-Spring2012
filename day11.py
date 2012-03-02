#!/usr/bin/env python

import pygame
from pygame.locals import *
RED = 255, 0, 0
GREEN = 0, 255, 0
WHITE = 255, 255, 255
BACKGROUND = 80, 80, 80
SCREEN_SIZE = 800, 600
RECT_SIZE = 120, 80
FPS = 30

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

bounds = screen.get_rect()
rects = [ pygame.Rect((0,0), RECT_SIZE),
          pygame.Rect((0,0), RECT_SIZE),
          pygame.Rect((0,0), RECT_SIZE),
          pygame.Rect((0,0), RECT_SIZE) ]

bigfont = pygame.font.Font(None, 80)

rects[0].topleft = bounds.topleft
rects[1].topright = bounds.topright
rects[2].bottomleft = bounds.bottomleft
rects[3].bottomright = bounds.bottomright


clock = pygame.time.Clock()
done = False
grabbed = False

while not done:
    for evt in pygame.event.get():
        if evt.type == QUIT:
            done = True
        elif evt.type == KEYDOWN and evt.key == K_ESCAPE:
            done = True
        elif evt.type == MOUSEBUTTONDOWN:
            for rect in rects:
                if rect.collidepoint(pygame.mouse.get_pos()):
#this makes it ONLY respond if the rectangle is clicked on.
                    grabbed = rect
            if grabbed:
                rects.remove(grabbed)
                rects.append(grabbed)
        elif evt.type == MOUSEBUTTONUP:
            grabbed = None
        
        if grabbed:
            grabbed.center = pygame.mouse.get_pos()
            grabbed.clamp_ip(bounds)

    screen.fill(BACKGROUND)

    text = bigfont.render("Rag the Drectangles", True, (0, 0, 0), BACKGROUND)
    loc = text.get_rect()
    loc.center = bounds.center
    screen.blit(text, loc)

    for rect in rects:
        others = rects[:]
        others.remove(rect)
        if rect == grabbed:
            color = WHITE
        elif rect.collidelist(others) != -1:
            color = GREEN
        else:
            color = RED

        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, (0, 0, 0), rect, 5)


    pygame.display.flip()
    clock.tick(FPS)
