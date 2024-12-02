import pygame
import sounds

def betting(screen, state, chip_values, width, height, table_color):

    # initializing variables
    pygame.font.init()
    chip_rects = []
    info_f = "assets/fonts/game_text.ttf"
    font2 = pygame.font.Font(info_f, 36)

    # create chip buttons
    # center them
    red_chip = pygame.image.load('assets/kenney_boardgame-pack/PNG/Chips/chipRedWhite.png')
    blue_chip = pygame.image.load('assets/kenney_boardgame-pack/PNG/Chips/chipBlueWhite.png')
    green_chip = pygame.image.load('assets/kenney_boardgame-pack/PNG/Chips/chipGreenWhite.png')
    black_chip = pygame.image.load('assets/kenney_boardgame-pack/PNG/Chips/chipBlackWhite.png')

    chip_y = height // 2
    chip_x = width // 2 - (len(chip_values) * 50) // 2

    
    # create placement for chips
    for i, value in enumerate(chip_values):
        rect = pygame.Rect(chip_x + i * 100 - 75, chip_y - 5, 80, 80)
        chip_rects.append((rect, value))

    betting = True
    while betting:
        # background for betting screen
        screen.fill((table_color))

        # blit chips onto screen
        screen.blit(red_chip, (chip_x - 75, chip_y))
        screen.blit(green_chip, (chip_x + 25, chip_y))
        screen.blit(blue_chip, (chip_x + 125, chip_y))
        screen.blit(black_chip, (chip_x + 220, chip_y))

        # display betting process
        prompt = font2.render(f"Your total: ${state}", True, (255,255,255))
        screen.blit(prompt, (width // 2 - prompt.get_width() // 2, height // 3))

        # draw chips
        for rect, value in chip_rects:
            text = font2.render(f"{value}", True, (255,255,255))
            screen.blit(text, (rect.centerx - text.get_width() + 10 // 2, rect.centery - text.get_height() // 2 - 3))

        # instructional text
        bet_inst = font2.render("Click Your Bet!", True, (255,255,255))
        screen.blit(bet_inst, (390,425))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                pygame.font.quit
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for rect, value in chip_rects:
                    if rect.collidepoint(mouse_pos):
                        if value > state:
                            print("You cannot bet more than your total.")
                        else:
                            return value