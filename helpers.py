import pygame
def build_background(width, height):

    # Green image for card table, make area for discarded cards, make area for current cards

    background = pygame.Surface((width, height))
    background.fill((53,101,77))


   # prep to get images onto the screen
    #current_cards_area = pygame.image.load('assets/Tiles/tile_68.png')
    #discarded_cards_area = pygame.image.load('assets/Tiles/tile_85.png')
    #current_cards = pygame.image.load('assets/Tiles/tile_35.png')
    #b_chips = pygame.image.load('assets/Tiles/tile_01.png')
    #r_chips = pygame.image.load('assets/Tiles/tile_33.png')
    #g_chips = pygame.image.load('assets/Tiles/tile_03.png')
    #bet = pygame.image.load('assets/Tiles/tile_03.png')
    #current_amount = pygame.image.load('assets/Tiles/tile_03.png')

    # pygame setup

    # get the tile size
    #table_size = table.get_width() 
    #current_cards_area_size = current_cards_area.get_width()
    #discarded_cards_area_size = discarded_cards_area.get_width()
    #current_cards_size = current_cards.get_width()
    #b_chips_size = b_chips.get_width()
    #r_chips_sand_size = r_chips.get_width()
    #g_chips_size = g_chips.get_width()
    #bet_size = bet.get_width()
    #current_amount_size = current_amount.get_width()


    #for x in range(0, width, table_size):
        #for y in range(0, height, table_size):
            #background.blit(table, (x,y))

            #if x == table_size:
                #background.blit(current_cards_area, (x,y))
            #elif y == (2*table):
                #background.blit(current_cards_area, (x,y))

    # return background
    return background
    return card_area


###  THIS IS TO HELP YOU WITH CARD GAME IF NEEDED  ###


import pygame
import random
import os


def build_background(WIDTH, HEIGHT):
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Blackjack Game")


# Colors
GREEN = (34, 139, 34)
WHITE = (255, 255, 255)

# Load card images
card_images = {}
suits = ['hearts', 'diamonds', 'clubs', 'spades']
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

for suit in suits:
    for value in values:
        card_name = f"card{suit.title()}{value}.png"
        image_path = os.path.join(f"PNG/{card_name}")
        card_images[(value, suit)] = pygame.image.load(image_path)

# Define card values
card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

# Functions for deck and game logic
def create_deck():
    deck = [(value, suit) for value in values for suit in suits]
    random.shuffle(deck)
    return deck

def calculate_hand(hand):
    total, aces = 0, 0
    for card in hand:
        total += card_values[card[0]]
        if card[0] == 'A':
            aces += 1
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

# Display cards on screen
def display_hand(hand, x, y, hidden=False):
    for i, card in enumerate(hand):
        if hidden and i == 0:
            pygame.draw.rect(screen, WHITE, (x + i * 80, y, 71, 96))  # Draw a white rectangle to hide the card
        else:
            screen.blit(card_images[card], (x + i * 80, y))

# Game loop
def main():
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    player_turn = True
    game_over = False

    # Main loop
    running = True
    while running:
        screen.fill(GREEN)

        # Draw dealer and player hands
        display_hand(dealer_hand, 100, 100, hidden=player_turn)
        display_hand(player_hand, 100, 400)

        # Display score if game is over
        if game_over:
            player_total = calculate_hand(player_hand)
            dealer_total = calculate_hand(dealer_hand)
            result_text = ""
            if player_total > 21:
                result_text = "Bust! Dealer wins."
            elif dealer_total > 21 or player_total > dealer_total:
                result_text = "Congratulations! You win!"
            elif player_total < dealer_total:
                result_text = "You lost! Dealer wins."
            else:
                result_text = "It's a tie!"
            
            font = pygame.font.Font(None, 36)
            result_surface = font.render(result_text, True, WHITE)
            screen.blit(result_surface, (WIDTH // 2 - result_surface.get_width() // 2, HEIGHT // 2 - 20))

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Player actions
            if player_turn and not game_over:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_h:  # Hit
                        player_hand.append(deck.pop())
                        if calculate_hand(player_hand) > 21:
                            player_turn = False
                            game_over = True

                    elif event.key == pygame.K_s:  # Stand
                        player_turn = False
                        while calculate_hand(dealer_hand) < 17:
                            dealer_hand.append(deck.pop())
                        game_over = True

        pygame.display.flip()

    pygame.quit()