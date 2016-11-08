import pygame
from pygame.locals import *
import os
import random
import time

pygame.init()

blank_time = 5
message_time = 1

commands = ['DO NOT QUESTION AUTHORITY', 
'SUBMIT', 'OBEY AND CONFORM', 'THEY LIVE', 
'OBEY', 'CONSUME', 'CONFORM', 'SLEEP', 
'BUY', 'WATCH TV', 'REPRODUCE']

def toggle_fullscreen():
    screen = pygame.display.get_surface()
    tmp = screen.convert()
    w,h = screen.get_width(),screen.get_height()
    flags = screen.get_flags()
    bits = screen.get_bitsize()
    pygame.display.quit()
    pygame.display.init()
    screen = pygame.display.set_mode((w,h),flags^FULLSCREEN,bits)
    screen.blit(tmp,(0,0))
    pygame.mouse.set_visible(False)
    return screen

if __name__ == '__main__':
    state = 'blank'
    clock = pygame.time.Clock()
    SW,SH = 1920,1080
    screen = pygame.display.set_mode((SW,SH), pygame.NOFRAME)
    screen.fill((0, 0, 0))

    _quit = False
    start = time.time()
    toggle_fullscreen()

    while not _quit:
        for e in pygame.event.get():
            if e.type is QUIT: _quit = True
            if e.type is KEYDOWN and e.key == K_ESCAPE: 
                _quit = True
                pygame.quit()
                os._exit(1)
        
        if state == 'blank' and time.time() - start > blank_time:
            state = 'mind-fuck'
            message = commands[random.randrange(0, len(commands) - 1)]
            start = time.time()

        if state == 'mind-fuck':
            screen = pygame.display.get_surface()
            font = pygame.font.Font(None, 250)
            text = font.render(message, 1, (255, 255, 255))
            textpos = text.get_rect()
            textpos.centerx = screen.get_rect().centerx
            textpos.centery = screen.get_rect().centery
            screen.blit(text, textpos)
            if time.time() - start > message_time:
                state = 'blank'
                screen.fill((0, 0, 0))

        pygame.display.flip()
        clock.tick(40)
