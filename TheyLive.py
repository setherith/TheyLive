import pygame
from pygame.locals import *
import os
import random

pygame.init()

commands = ['DO NOT QUESTION AUTHORITY', 'SUBMIT', 'OBEY AND CONFORM', 'THEY LIVE', 'OBEY', 'CONSUME', 'CONFORM', 'SLEEP', 'BUY', 'WATCH TV', 'REPRODUCE']

def toggle_fullscreen():
    screen = pygame.display.get_surface()
    tmp = screen.convert()
    caption = pygame.display.get_caption()
    cursor = pygame.mouse.get_cursor() 
    
    w,h = screen.get_width(),screen.get_height()
    flags = screen.get_flags()
    bits = screen.get_bitsize()
    
    pygame.display.quit()
    pygame.display.init()
    
    screen = pygame.display.set_mode((w,h),flags^FULLSCREEN,bits)
    screen.blit(tmp,(0,0))
    pygame.display.set_caption(*caption)
 
    pygame.key.set_mods(0) #HACK: work-a-round for a SDL bug??
 
    pygame.mouse.set_cursor(*cursor)
    
    return screen
 
com = commands[random.randrange(0, len(commands) - 1)]

if __name__ == '__main__':
    SW,SH = 1920,1080
    screen = pygame.display.set_mode((SW,SH))
    pygame.display.set_caption('TheyLive v1.0')
    screen.fill((100, 100, 100))

    _quit = False
    while not _quit:
        for e in pygame.event.get():
            if (e.type is KEYDOWN and e.key == K_RETURN
                    and (e.mod&(KMOD_LALT|KMOD_RALT)) != 0):
                toggle_fullscreen()
            if e.type is QUIT: _quit = True
            if e.type is KEYDOWN and e.key == K_ESCAPE: 
                _quit = True
                pygame.quit()
                os._exit(1)
            
        screen = pygame.display.get_surface()
        font = pygame.font.Font(None, 36)
        text = font.render(com, 1, (255, 255, 255))
        textpos = text.get_rect()
        textpos.centerx = screen.get_rect().centerx
        textpos.centery = screen.get_rect().centery
        screen.blit(text, textpos)
        pygame.display.flip()
