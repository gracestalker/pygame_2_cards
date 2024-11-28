import pygame
import os # allows for a loop to be made to make all of the loaded images for the cards
import hands # functions for the game
from titlescreen import title_screen # function for title screen
import betting # functions for betting code
import sounds # functions for casino music and sound effects


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


def main_game(screen, state):

    # initializing betting values
    chip_values = [10, 50, 100, 500]
    bet = betting.betting(screen, state["total"], chip_values, width, height, table_color)
    total_bet = bet

    # initializing background
    background = hands.build_background(width, height, table_color)

    # set up game
    deck = hands.create_deck(values, suits)
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    # if it is still the players turn, it will not be the dealer's turn to draw cards yet
    
    # use different variables to tell which stages you are in in the game
    player_turn = True
    game_over = False
    result_processed = False

    # blackjack rules implemented
    if player_total == 21 or dealer_total == 21:
        player_turn = False
        game_over = True

        if player_total == 21 and dealer_total == 21:
            result = "It's a tie! Both have Blackjack!"
        elif player_total == 21:
            result = "Blackjack! You win!"
            state['total'] += total_bet * 2
        else:
            result = "Dealer has Blackjack! You lose."
            state['total'] -= total_bet

        
        # results screen
        hands.result_screen(result, screen, width, height, table_color, state)
        result_processed = True



    running = True
    while running:

        if not game_over:
            # starting the background from the top of the screen
            screen.blit(background, (0, 0))
            # deal hands to player and dealer in their spots
            hands.display_hand(screen, dealer_hand, 100, 100, card_images, card_back, hidden=player_turn and not game_over)
            hands.display_hand(screen, player_hand, 100, 400, card_images, card_back)

        # after the game ends, show the results of the game
        else:
            if not result_processed:

                # create new screen for the overlay of text
                end_screen = pygame.Surface((width, height))
                end_screen.fill((table_color))
                screen.blit(end_screen, (0,0))

                # display results
                player_total = hands.calculate_hand(player_hand, card_values)
                dealer_total = hands.calculate_hand(dealer_hand, card_values)
                result = ""
                
                if player_total > 21:
                    result = "Bust! Dealer wins."
                    state['total'] -= total_bet
                elif dealer_total > 21:
                    result = 'Dealer busts! You win!'
                    state['total'] += total_bet
                elif dealer_total > 21 or player_total > dealer_total:
                    result = "Congratulations! You win!"
                    state['total'] += total_bet
                elif player_total < dealer_total:
                    result = "You lost! Dealer wins."
                    state['total'] -= total_bet
                elif player_total == 21 and player_turn and not game_over:
                    result = 'BLACKJACK!'
                    state['total'] += int(total_bet * 1.5)
                else:
                    result = "It's a tie!"
            

                # results screen
                hands.result_screen(result, screen, width, height, table_color, state)
                result_processed = True
            
        
        hit_btn_rect, stand_btn_rect = hands.display_hand(screen, player_hand, 100, 400, card_images, card_back, draw_buttons = True)

        # event handling and initializing keys for game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if player_turn and not game_over:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if hit_btn_rect and hit_btn_rect.collidepoint(event.pos):
                        # this is to hit and gain a card for your hand
                        player_hand.append(deck.pop())
                        if hands.calculate_hand(player_hand, card_values) > 21:
                            player_turn = False
                            game_over = True
                    # this is to stop drawing cards and keep your hand.
                    elif stand_btn_rect and stand_btn_rect.collidepoint(event):
                        player_turn = False
                        # allows dealer to draw if their total is greater than 17
                        hands.dealer_turn(screen, dealer_hand, deck, card_images, card_back, table_color, card_values)
                        game_over = True


            if game_over and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    running = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    exit()


        pygame.display.flip()



# game loop to help shorten code
def main(result=''):

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
            main_game(screen, state)
            # start main game
    pygame.quit()

# Run the game
if __name__ == "__main__":
    main()
