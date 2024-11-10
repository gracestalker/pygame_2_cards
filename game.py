# make a snake game

import pygame
import random
import builders


width = 680
height = 680

# initial variables
pygame.display.set_caption("Snake Game")
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
background = builders.build_background(width, height)
running = True

# snake variables
square_color = (10, 120, 30) # Green Color for Snake
square_size = 15
square_x, square_y = width // 2, height // 2
speed = 1  # Speed of movement


while running:
    # poll for events DO NOT DELETE
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # keys functions
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        square_x -= speed
    elif keys[pygame.K_RIGHT]:
        square_x += speed
    elif keys[pygame.K_UP]:
        square_y -= speed
    elif keys[pygame.K_DOWN]:
        square_y += speed

    # Keep the square inside the screen boundaries
    square_x = max(0, min(width - square_size, square_x))
    square_y = max(0, min(height - square_size, square_y))


    # need to blit onto screen in order to see the colors
    screen.blit(background,(0,0))

    # draw snake onto screen
    pygame.draw.rect(screen, square_color, (square_x, square_y, square_size, square_size))


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()