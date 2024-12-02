import pygame
import buttons


# function to show instructions before gameplay
def instructions(screen, width, height):
    
    # rgb colors
    white = (255,255,255)
    table_color = (53, 101, 77)

    # fonts for title screen
    play_f = "assets/fonts/play_again.ttf"
    info_f = "assets/fonts/game_text.ttf"
    font1 = pygame.font.Font(play_f, 150)
    font2 = pygame.font.Font(info_f, 50)
    font3 = pygame.font.Font(info_f, 75)

    # instructions/welcome text
    welcome = font3.render("WELCOME TO...", True, white)
    blj = font1.render("BLACKJACK", True, white)
    b_inst = font2.render("Click the Chips to Bet!", True, white)
    h_inst = font2.render("Press [H] to Hit", True, white)
    s_inst = font2.render("Press [S] to Stand", True, white)
    f_inst = font2.render("Press [F] to Split", True, white)
    d_inst = font2.render("Press [D] to Double Down", True, white)
    inst = font3.render("INSTRUCTIONS:", True, white)
    und = font3.render("___________________________________________________________________________", True, white)

    # create surface to blit onto
    inst_surface = pygame.Surface((width, height))
    inst_surface.fill(table_color)

    # welcome screen
    inst_surface.blit(welcome, (width // 2 - 175, 75))

    screen.blit(inst_surface, (0,0))
    pygame.display.flip()
    pygame.time.delay(2000) 

    # blackjack screen
    inst_surface.blit(blj, (width // 2 - 470, 225))

    screen.blit(inst_surface, (0,0))
    pygame.display.flip()
    pygame.time.delay(2000)

    inst_surface.fill(table_color)

    # instructions screen
    inst_surface.blit(inst, (width // 2 - 200, 50))
    inst_surface.blit(und, (0, 100))
    inst_surface.blit(b_inst, (width // 2 - 250, 200))
    inst_surface.blit(h_inst, (width // 2 - 180, 275))   
    inst_surface.blit(s_inst, (width // 2 - 200, 350))
    inst_surface.blit(f_inst, (width // 2 - 195, 425))
    inst_surface.blit(d_inst, (width // 2 - 270, 500))

    screen.blit(inst_surface, (0,0))
    pygame.display.flip()
    pygame.time.delay(6000)
   

# function for my title screen to start the game
def title_screen(screen, result, state, width, height):

    instructions(screen, width, height)

    # initialize images used on title screen
    start_image = pygame.image.load('assets/kenney_boardgame-pack/PNG/background/start_btn.png')
    quit_image = pygame.image.load('assets/kenney_boardgame-pack/PNG/background/quit_btn.png')
    blackjack_logo = pygame.image.load('assets/kenney_boardgame-pack/PNG/background/blackjack.png')

    # changing the image sizes
    new_width = 200
    new_heightS = 200
    new_heightQ = 100
    start_image = pygame.transform.scale(start_image, (new_width, new_heightS))
    quit_image = pygame.transform.scale(quit_image, (new_heightQ, new_heightQ))


    # create button instances
    start_button = buttons.Button(400, 350, start_image)
    quit_button = buttons.Button(900, 0, quit_image)
    blackjack_logo = buttons.Button(315, 50, blackjack_logo)


    run = True
    while run:

        screen.fill((53, 101, 77))

        if start_button.draw(screen):
            print('START')
            return True

        if quit_button.draw(screen):
            print('QUIT')
            pygame.quit()
            return False
        
        # draw game logo
        blackjack_logo.draw(screen)

        # event handler
        for event in pygame.event.get():
            # quit game
            if event.type == pygame.QUIT:
                pygame.quit()
                return False

        pygame.display.flip()