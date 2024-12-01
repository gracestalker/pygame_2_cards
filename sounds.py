import pygame


# background music, find a casino sounds
def background_music():
    pygame.mixer.music.load("assets/sounds/background_noise.mp3")
    pygame.mixer.music.play(-1)


# deal card sound when you hit, dealer draws, or when the round starts
def game_set_up():
    pygame.mixer.load("assets/sounds/shuffle_cards_and_deal.mp3")
    pygame.mixer.music.play(-1)


# money noise after round ends and when you place your bet
def deal_sound():
    
    pygame.mixer.init()

    deal_sound = pygame.mixer.Sound("assets/sounds/cardPlace1.ogg")
    deal_sound.play(-1)

