# Example file showing a basic pygame "game loop"
import pygame

# all of my tiles and variables
width = 1180
height = 600
background = pygame.Surface((width, height))
background.fill('white')
water = pygame.image.load('assets/Tiles/tile_73.png') # how to prep images to be loaded onto screen

# pygame setup
pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True


tile_size = water.get_width() # get the tile size

for x in range(0, width, tile_size):
    for y in range(0, height, tile_size):
        background.blit(water, (x,y))
        # commented out to try again later with more tiles
        #if x < tile_size:
           # background.blit(grass, (x,y))
       # elif y < (2*tile_size):
            #background.blit(sand, (x,y))



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()