import pygame


def build_background(width, height):

    background = pygame.Surface((width, height))
    background.fill((0,0,0))

    return background

def update_square_position(x, y, speed):
        # Get keys pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        square_x -= speed
    if keys[pygame.K_RIGHT]:
        square_x += speed
    if keys[pygame.K_UP]:
        square_y -= speed
    if keys[pygame.K_DOWN]:
        square_y += speed

    return x, y

class Snake:
    def __init__(self, x, y, size, color, speed, width, height):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.speed = speed
        self.screen_w = width
        self.screen_h = height


    def snake(self):
        self.x = 630
        self.y = 340
        self.size = 10
        self.color = (0, 255, 0)
        self.speed = 5
    
    def keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        elif keys[pygame.K_RIGHT]:
            self.x += self.speed
        elif keys[pygame.K_DOWN]:
            self.y -= self.speed
        elif keys[pygame.K_UP]:
            self.y += self.speed


    def check_border(self):

        if not border_rect.contains(self.rect):
            has_collided = pygame.sprite.collide_rect()
            if has_collided:
                Snake.kill()
        # make sure snake stays inside the rect we set as the border
        border_rect = pygame.rect.Rect(0,0,self.screen_w,self.screen_h)
        self.rect.clamp_ip(border_rect)

    def square(self):
        screen = pygame.display.set_mode((self.size))
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))



# when it hits the wall it ends the game and displays your score


