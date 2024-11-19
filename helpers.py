import pygame

# building the table for the game, table and card area
def build_background(width, height, table_color):
    background = pygame.Surface((width, height))
    # table area
    background.fill(table_color)
    return background


# displaying the cards on the screen for the player and dealer
def display_hand(screen, hand, x, y, card_images, card_back, hidden=False):

    card_width = 76
    card_height = 91
    space = 80

    for i, card in enumerate(hand):
        # creates the boundaries for the cards, centered
        card_x = 250 + x + i * space

        if hidden and i == 0:
            screen.blit(card_back, (card_x, y))  # Draw the back of a card image to hide the dealer's second card
        else:
            if card in card_images:
                # displays your cards for you
                screen.blit(card_images[card], (card_x, y))


def calculate_hand(hand, card_values):

    # this is your total score of your hand
    total = 0
    # keeps track of your aces in case of their special rule where they either equal 1 or 11
    aces = 0

    # creates the loop to calculate the total
    for card in hand:
        # card[0] pulls the value from our cards dictionary to see if you have an Ace and to calculate your total score.
        total += card_values[card[0]]
        if card[0] == 'A':
            aces += 1
    # this is the loop where the special rule is put into play
    # if the total is greater than 21 and you have more than 0 Aces, it will deduct ten points from your score and take away the ace value from your hand
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total