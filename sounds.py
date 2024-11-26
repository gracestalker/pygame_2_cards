import pygame


# background music, find a casino sounds
def background_music():
    pygame.mixer.music.load("assets/sounds/background_noise.mp3")
    pygame.mixer.music.play()


# deal card sound when you hit, dealer draws, or when the round starts
def game_set_up():
    pygame.mixer.load("assets/sounds/shuffle_cards_and_deal.mp3")
    pygame.mixer.music.play()


# money noise after round ends and when you place your bet
def deal_sound():
    pygame.mixer.load("assets/cardPlace1.ogg")
    pygame.mixer.music.play()

