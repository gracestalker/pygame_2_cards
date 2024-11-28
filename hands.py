import pygame
import random

class Button:
    def __init__(self, x, y, image, text, font, font_color):
        self.image = image
        self.rect = self.image.get_rect(topleft = (x,y))
        self.text = text
        self.font = font
        self.font_color = font_color

    def draw(self, screen):
        # draw the buttons
        screen.blit(self.image, self.rect)

        # draw buttont text
        text_surf = self.font.render(self.text, True, self.font_color)
        text_rect = text_surf.get_rect(center = self.rect.center)
        screen.blit(text_surf, text_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False

# creates and shuffles the deck for the game using list comprehension. ex: ('2', 'Clubs'), ('2', 'Hearts')...
def create_deck(values, suits):
    deck = [(value, suit.title()) for value in values for suit in suits]
    random.shuffle(deck)
    return deck


# building the table for the game, table and card area
def build_background(width, height, table_color):
    background = pygame.Surface((width, height))
    # table area
    background.fill(table_color)
    return background


# displaying the cards on the screen for the player and dealer
def display_hand(screen, hand, x, y, card_images, card_back, hidden=False, draw_buttons = False):

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
    
    if draw_buttons:
        # draw and scale images
        btn_width = 150
        btn_height = 50
        h_btn = pygame.image.load('assets/kenney_boardgame-pack/PNG/background/hs_btn.png')
        s_btn = pygame.image.load('assets/kenney_boardgame-pack/PNG/background/hs_btn.png')
        h_btn = pygame.transform.scale(h_btn, (btn_width, btn_height))
        s_btn = pygame.transform.scale(s_btn, (btn_width, btn_height))

        # font
        info_f = "assets/fonts/game_text.ttf"
        font2 = pygame.font.Font(info_f, 36)

        # button positions
        hit_btn_x = x - 200
        hit_btn_y = y + 40
        stand_btn_x = x - 200
        stand_btn_y = y + 110

        # draw hit button
        screen.blit(h_btn, (hit_btn_x, hit_btn_y))
        hit_text = font2.render("HIT", True, (255,255,255))
        hit_text_rect = hit_text.get_rect(center = (hit_btn_x + btn_width // 2, hit_btn_y + btn_height // 2))
        screen.blit(hit_text, hit_text_rect)

        # draw stand button
        screen.blit(s_btn, (stand_btn_x, stand_btn_y))
        stand_text = font2.render("STAND", True, (255,255,255))
        stand_text_rect = stand_text.get_rect(center = (stand_btn_x + btn_width // 2, stand_btn_y + btn_height // 2))
        screen.blit(stand_text, stand_text_rect)

        return (pygame.Rect(hit_btn_x, hit_btn_y, btn_width, btn_height),
                pygame.Rect(stand_btn_x, stand_btn_y, btn_width, btn_height))
    
    else:
        return None, None


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

def result_screen(result, screen, width, height, table_color, state):

    # variables

    play_f = "assets/fonts/play_again.ttf"
    info_f = "assets/fonts/game_text.ttf"
    font1 = pygame.font.Font(play_f, 100)
    font2 = pygame.font.Font(info_f, 36)
    result_surface = font2.render(result, True, (255,255,255))

    screen.blit(result_surface, (width // 2 - result_surface.get_width() // 2, height // 3 - 20))

    restart_text = font1.render("Play again", True, (255,255,255))
    restart_info = font2.render("Press [R] to redeal  Press [Q] to quit", True, (255,255,255))
    total_info = font2.render(f"Total = {state['total']}", True, (255,255,255))

    # draw a rectangle for the restart screen
    text_width, text_height = restart_text.get_size()
    rect_x = (width - text_width) // 2
    rect_y = (height // 2) + 50
    pygame.draw.rect(screen, (table_color), (rect_x - 10, rect_y - 10, text_width + 20, text_height + 20))
    screen.blit(restart_text, (rect_x,rect_y-100))
    screen.blit(restart_info, (width // 5 + 30, rect_y + 50))
    screen.blit(total_info, (width // 3 + 85, rect_y + 100))


# plays out dealer's turn so you can see what their turn looks like
def dealer_turn(screen, dealer_hand, deck, card_images, card_back, table_color, card_values):
    
    while True:
        # calculate dealer total
        dealer_total = calculate_hand(dealer_hand, card_values)

        # check for soft 17
        soft_17 = dealer_total == 17 and any(card[0] == 'A' for card in card_values)

        # causes dealer to hit on less than 17 or a 17 with an Ace
        if dealer_total < 17 or soft_17:
            dealer_hand.append(deck.pop())

            screen.fill(table_color)
            display_hand(screen, dealer_hand, 100, 100, card_images, card_back, hidden = False)
            pygame.time.wait(1000)
            pygame.display.flip()
            
            pygame.time.wait(1000)

        else:
            break

