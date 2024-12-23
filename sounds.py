import pygame

# initialize the mixer so we can use sound
pygame.mixer.init()

# variables
# using mixer.Sound to make it a sound effect instead of replacing the background noise
deal = pygame.mixer.Sound("assets/sounds/cardPlace1.ogg")
lose = pygame.mixer.Sound("assets/sounds/lose.mp3")
win = pygame.mixer.Sound("assets/sounds/win.wav")
crickets = pygame.mixer.Sound("assets/sounds/cricket.wav")
go = pygame.mixer.Sound("assets/sounds/game_over.mp3")

# background music, find a casino sounds
def background_music():
    # make this music.load so it is a background noise
    pygame.mixer.music.load("assets/sounds/background_noise.mp3")
    pygame.mixer.music.play(-1, 0.0)
    pygame.mixer.music.set_volume(0.3)


# using .play() to make it a sound effect
# money noise after round ends and when you place your bet
def deal_sound():
    deal.play()

# when player loses a hand
def lose_sound():
    lose.play()  

# when player wins a hand
def win_sound():
    win.play()

# when player ties a hand
def crickets_sound():
    crickets.play()

# when player goes bankrupt
def game_over():
    go.play()