# make a snake game

import pygame
import random
import builders


width = 680
height = 680


pygame.display.set_caption("Snake Game")
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
background = builders.build_background(width, height)
running = True


while running:
    # poll for events DO NOT DELETE
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # need to blit onto screen in order to see the colors
    
    screen.blit(background,(0,0))

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()