import pygame
import button

width = 800
height = 500

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Button Demo')

start_image = pygame.image.load('assets/kenney_boardgame-pack/PNG/background/start_btn.png')
quit_image = pygame.image.load('assets/kenney_boardgame-pack/PNG/background/quit_btn.png')
blackjack_logo = pygame.image.load('assets/kenney_boardgame-pack/PNG/background/blackjack.png')

# changing the image sizes
new_width = 200
new_heightS = 200
new_heightQ = 100

start_image = pygame.transform.scale(start_image, (new_width, new_heightS))
quit_image = pygame.transform.scale(quit_image, (new_heightQ, new_heightQ))


# button class
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    def draw(self):

        # get mouse position
        pos = pygame.mouse.get_pos()
        
        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True


        # draw buttons
        screen.blit(self.image, (self.rect.x,self.rect.y))


# create button instance
start_button = Button(300, 250, start_image)
quit_button = Button(700, 0, quit_image)
blackjack_logo = Button(230, -10, blackjack_logo)


run = True
while run:

    screen.fill((53, 101, 77))

    start_button.draw()
    quit_button.draw()
    blackjack_logo.draw()

    # event handler
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()