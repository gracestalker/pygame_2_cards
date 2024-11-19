import pygame
import random


def build_background(width, height):

    background = pygame.Surface((width, height))
    background.fill((0,0,0))

   # prep to get images onto the screen
    grass = pygame.image.load('assets/tile_0050.png')

    # get the tile size
    grass_size = grass.get_width() 

    # loop to put image onto screen
    for x in range(0, width, grass_size):
        for y in range(0, height, grass_size):
            background.blit(grass, (x,y))

    return background


class Snake:
    def __init__(self, size, color, width, height, x, y):
        self.size = size
        self.color = color
        self.snake = [(width // 2, height // 2)]
        self.direction = (0,0)
        self.x = x
        self.y = y

    def snake_head(self):
        # update the head of the snake
        head_x, head_y = self.snake[0]
        direction_x, direction_y = self.direction
        update_head = (head_x + direction_x, head_y + direction_y)
        self.snake = [update_head] + self.snake[:-1]
    
    def body(self):
        # when the snake eats the apple, it adds one part to the BACK of the body
        self.snake.append(self.snake[-1])

    def reverse(self, direction_x, direction_y):
        # make sure the snake cannot reverse directions
        if (direction_x, direction_y) != (-self.direction[0], -self.direction[1]):
            self.direction = (direction_x, direction_y)


    def check_border(self, width, height):
        # the snake cannot leave these bounds
        square_x = max(0, min(width - self.size, square_x))
        square_y = max(0, min(height - self.size, square_y))
        
        has_collided = square_x or square_y
        if has_collided:
            self.kill()
    
    def square(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

        return
    


#class Food:
    def __init__(self, size, position = (0,0), color = (255, 0, 0)):
        self.position = position
        self.color = color
        self.size = size
        self.spawn()

    def spawn(self, width, height):
        # makes the food randomly appear on the screen
        self.position = (random.randint(0, (width - self.size) // self.size) * self.size,
                        random.randint(0, (height - self.size) // self.size) * self.size)




