# make a snake game

import pygame
import random
import builders

# all of my variables
    # screen
width = 680
height = 680

    # square
square_color = (0, 255, 0)  # Green color
square_size = 10
square_x, square_y = width // 2, height // 2
speed = 5  # Speed of movement


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

    square_x = max(0, min(width - square_size, square_x))
    square_y = max(0, min(height - square_size, square_y))

    builders.Snake.snake()
    builders.Snake.square()



    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()