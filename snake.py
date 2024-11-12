# make a snake game

import pygame



class Snake:
    def __init__(self, square_x, square_y, width, height, screen, color, square_size):
        self.x = square_x
        self.y = square_y
        self.speed = 0
        self.width = width
        self.height = height
        self.screen = screen
        self.color = color
        self.size = square_size


    def snake(self, width, height):
        self.x = width // 2
        self.y = height // 2
        self.size = 15
        self.speed = 0
        self.color = (10, 120, 30)
    
    def speed(self, speed):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= speed
        elif keys[pygame.K_RIGHT]:
            self.x += speed
        elif keys[pygame.K_UP]:
            self.y -= speed
        elif keys[pygame.K_DOWN]:
            self.y += speed

        return speed

    
