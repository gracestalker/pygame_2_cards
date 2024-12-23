import pygame  

# displays a bankrupt screen if the player's total reaches 0
def bankrupt_screen(width, height, table_color, screen):
    
    # initialize variables
    white = (255,255,255)
    end_screen = pygame.Surface((width, height))
    end_screen.fill((table_color))

    # load font
    info_f = "assets/fonts/game_text.ttf"
    font2 = pygame.font.Font(info_f, 80)
    font3 = pygame.font.Font(info_f, 36)

    # render text
    br = font2.render("The House always wins...", True, white)
    instr = font3.render("Press [Q] to Quit", True, white)

    # display the messages on the screen
    screen.blit(end_screen, (0,0))
    screen.blit(br, (width // 2 - br.get_width() // 2, height // 3))
    screen.blit(instr, (width // 2 - instr.get_width() // 2, height // 2 + 100))

    # event handling for quitting the bankrupt screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # you can only quit the game, there is no restart. Allows for you to go through the whole game again with new money.
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            pygame.quit()
            exit()