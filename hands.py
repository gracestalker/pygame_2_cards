import pygame
# this is to make the decks random everytime they are dealt
import random
# for the sound effects
import sounds


# creates and shuffles the deck for the game using list comprehension. ex: ('2', 'Clubs'), ('2', 'Hearts')...
def create_deck(values, suits):
    deck = [(value, suit.title()) for value in values for suit in suits]
    random.shuffle(deck)
    # returns a different deck for every game
    return deck


# building the table for the game
def build_background(width, height, table_color):
    background = pygame.Surface((width, height))
    # table area
    background.fill(table_color)
    return background


# displaying the cards on the screen for the player and dealer, hides the dealer's first card
def display_hand(screen, hand, x, y, card_images, card_back, hidden=False):

    space = 80

    for i, card in enumerate(hand):
        # creates the boundaries for the cards, centered
        card_x = 250 + x + i * space

        if hidden and i == 0:
            # creates the back of a card image to hide the dealer's first card
            screen.blit(card_back, (card_x, y))
        else:
            if card in card_images:
                # displays your cards for you
                screen.blit(card_images[card], (card_x, y))

# calculates the hand so the program knows when you bust and who wins/loses
def calculate_hand(hand, card_values):

    # this is your total score of your hand
    total = 0
    # keeps track of your aces in case of their special rule where they either equal 1 or 11
    aces = 0

    # creates the loop to calculate the total
    for card in hand:
        value = card[0]
        # card[0] pulls the value from our cards dictionary to see if you have an Ace and to calculate your total score.
        total += card_values[value]
        if value == 'A':
            aces += 1
    # this is the loop where the special rule is put into play
    # if the total is greater than 21 and you have more than 0 Aces, it will deduct ten points from your score and take away the ace value from your hand leaving you with an Ace acting as a 1
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

# screen that will display the results of your hand(regular and split)
def result_screen(results, result, screen, width, height, table_color, state):

    # variables
    play_f = "assets/fonts/play_again.ttf"
    info_f = "assets/fonts/game_text.ttf"
    font1 = pygame.font.Font(play_f, 100)
    font2 = pygame.font.Font(info_f, 36)
    result_surface = font2.render(result, True, (255,255,255))

    # clear screen with background color
    screen.fill(table_color)

    # spacings for results
    y_offset = height // 4
    line_spacing = 50

    # loop to create two outcomes if necessary for the results screen
    for idx, result in enumerate(results):
        result_surface = font2.render(result, True, (255, 255, 255))
        screen.blit(result_surface, (width // 2 - result_surface.get_width() // 2, y_offset))
        y_offset += line_spacing

    # player total
    total_info = font2.render(f"Total = {state['total']}", True, (255, 255, 255))
    screen.blit(total_info, (width // 2 - total_info.get_width() // 2, y_offset + 20))

    # how to play again or quit
    restart_text = font1.render("Play again", True, (255, 255, 255))
    restart_info = font2.render("Press [R] to Redeal  Press [Q] to Quit", True, (255, 255, 255))

    # variables
    text_width, text_height = restart_text.get_size()
    rect_x = (width - text_width) // 2
    rect_y = y_offset + 100

    # Draw a rectangle for the restart section
    pygame.draw.rect(screen, table_color, (rect_x - 10, rect_y - 10, text_width + 20, text_height + 20))
    screen.blit(restart_text, (rect_x, rect_y))
    screen.blit(restart_info, (width // 5 + 30, rect_y + 130))

    pygame.display.update()


# plays out dealer's turn so you can see what their turn looks like
def dealer_turn(screen, dealer_hand, player_hand, deck, card_images, card_back, table_color, card_values, split_hands, width, ):

    # displays the dealer's hand
    display_hand(screen, dealer_hand, 100, 100, card_images, card_back, hidden=False)

    # if the player has split hands, show those instead of the original unsplit hand
    if split_hands:
        # variables for displaying the split hands
        num_hands = len(split_hands)
        hand_width = 350
        base_offset = -200
        spacing = (width - (num_hands * hand_width)) // (num_hands + 1)
        
        # loop to position the hands
        for idx, split_hand in enumerate(split_hands):
            x_offset = base_offset + spacing + idx * (hand_width + spacing)
            y_offset = 400
            
            # Draw the split hand
            display_hand(screen, split_hand, x_offset, y_offset, card_images, card_back)

    pygame.display.flip()

    # Main loop for dealer turn
    while True:
        dealer_total = calculate_hand(dealer_hand, card_values)

        # check for soft 17 (dealer holds 17 with an Ace counted as 11), using the and function account for aces that are counted as 11 and 1 in the dealer's hand
        soft_17 = dealer_total == 17 and any(card[0] == 'A' and card_values[card[0]] == 11 for card in dealer_hand)

        # dealer hits on less than 17 or a soft 17 (Ace counted as 11), makes a sound when they get dealt a card
        if dealer_total < 17 or soft_17:
            sounds.deal_sound()
            dealer_hand.append(deck.pop())

            # Update the screen to show the dealer's hand
            screen.fill(table_color)
            display_hand(screen, dealer_hand, 100, 100, card_images, card_back, hidden=False)


            if split_hands:
                # display split hands
                for idx, split_hand in enumerate(split_hands):
                    x_offset = base_offset + spacing + idx * (hand_width + spacing)
                    y_offset = 400
                    display_hand(screen, split_hand, x_offset, y_offset, card_images, card_back)
            
            else:
                # display the single hand
                display_hand(screen, player_hand, 100, 400, card_images, card_back)                

            pygame.display.flip()
            pygame.time.wait(1000)  # Wait between dealer's moves

        else:
            # dealer stops when they have higher than a 17
            break

# function splits the player's hand into two if the cards are the same value
def split(player_hand, deck):
    
    # loop splits the hand in two
    if len(player_hand) == 2 and player_hand[0][0] == player_hand[1][0]:
        hand1 = [player_hand[0], deck.pop()]
        hand2 = [player_hand[1], deck.pop()]
        return hand1, hand2
    
    else:
        # if you can't split it, it stays as one hand
        return None, None