import pygame
import os
# contains logic for the titlescreen and instructions
from titlescreen import title_screen
# contains music/sound effects for game
import sounds
# contain game code
import mg

# Initialize variables of game
width = 1000
height = 600
table_color = (53, 101, 77)
card_back = pygame.image.load('assets/kenney_boardgame-pack/PNG/Cards/cardBack_red5.png')
title_color = (0, 0, 255)


# create a dictionary for the images to be loaded into the game
card_images = {}
suits = ['clubs', 'diamonds', 'hearts', 'spades']
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'A', 'J', 'Q', 'K']


# loop for images instead of creating each individual card variable
for suit in suits:
    for value in values:
        image_path = os.path.join('assets', 'kenney_boardgame-pack', 'PNG', 'Cards', f"card{suit.title()}{value}.png")
        if os.path.exists(image_path):
            card_images[(value, suit.title())] = pygame.image.load(image_path)
        # this debugs the game so it doesn't crash
        else:
            print(f"Missing image: {image_path}")


# define card values to determine score during game
card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'A': 11, 'J': 10, 'Q': 10, 'K': 10}


# game loop to help shorten code
def main(result=''):

    # initialize variables
    state = {'total': 1500}
    pygame.init()
    pygame.mixer.init()
    sounds.background_music()
    screen = pygame.display.set_mode((width, height))
    # caption means game title at the top of the screen
    pygame.display.set_caption("Blackjack")

    # title screen loop
    show_game = title_screen(screen, result, state, width, height)
    if show_game:
        while True:
            mg.main_game(screen, state, width, height, table_color, values, suits, card_values, card_images, card_back)
            # start main game
    pygame.quit()

# Run the game
if __name__ == "__main__":
    main()
