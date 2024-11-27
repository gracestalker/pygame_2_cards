import pygame


def betting(screen, state, chip_values, width, height, table_color):

    # initializing variables
    pygame.font.init()
    font = pygame.font.Font(None, 36)
    chip_rects = []

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
        prompt = font.render(f"Your total: ${state}", True, (255,255,255))
        screen.blit(prompt, (width // 2 - prompt.get_width() // 2, height // 3))

        # draw chips
        for rect, value in chip_rects:
            text = font.render(f"{value}", True, (255,255,255))
            screen.blit(text, (rect.centerx - text.get_width() + 10 // 2, rect.centery - text.get_height() // 2 - 3))

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



