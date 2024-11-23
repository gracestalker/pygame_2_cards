import pygame
import buttons

# function for my title screen to start the game
def title_screen(screen):


    start_image = pygame.image.load('assets/kenney_boardgame-pack/PNG/background/start_btn.png')
    quit_image = pygame.image.load('assets/kenney_boardgame-pack/PNG/background/quit_btn.png')
    blackjack_logo = pygame.image.load('assets/kenney_boardgame-pack/PNG/background/blackjack.png')

    # changing the image sizes
    new_width = 200
    new_heightS = 200
    new_heightQ = 100

    start_image = pygame.transform.scale(start_image, (new_width, new_heightS))
    quit_image = pygame.transform.scale(quit_image, (new_heightQ, new_heightQ))


    # create button instance
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
        
        #draw game logo
        blackjack_logo.draw(screen)

        # event handler
        for event in pygame.event.get():
            # quit game
            if event.type == pygame.QUIT:
                pygame.quit()
                return False

        pygame.display.flip()