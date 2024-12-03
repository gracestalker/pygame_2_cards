# button class
import pygame

# this is the button class where all of the information for our 'START' and 'QUIT' buttons go
class Button():
    # defining all of the variables
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    # function to draw the buttons onto the screen
    def draw(self, screen):

        # lets you know what phase you are in
        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()
        
        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            # if you click on an area that you can, then it will activate that action
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        # if you clicj on an inactive area, it will not do anything
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False


        # draw buttons
        screen.blit(self.image, (self.rect.x,self.rect.y))

        # action is now true and the function will get carried out
        return action
