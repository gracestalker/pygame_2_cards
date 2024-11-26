import pygame


def betting(screen, state, chip_values, width, height, table_color):

    pygame.font.init()
    font = pygame.font.Font(None, 36)
    chip_rects = []

    # create chip buttons
    # center them
    chip_y = height // 2
    chip_x = width // 2 - (len(chip_values) * 50) // 2
    
    for i, value in enumerate(chip_values):
        rect = pygame.Rect(chip_x + i * 100, chip_y, 80, 80)
        chip_rects.append((rect, value))

    betting = True
    while betting:
        # background for betting screen
        screen.fill((table_color))

        # display betting process
        prompt = font.render(f"Your total: ${state}", True, (255,255,255))
        screen.blit(prompt, (width // 2 - prompt.get_width() // 2, height // 3))

        # draw chips
        for rect, value in chip_rects:
            pygame.draw.ellipse(screen, (255,255,0), rect)
            text = font.render(f"${value}", True, (0,0,0))
            screen.blit(text, (rect.centerx - text.get_width() // 2, rect.centery - text.get_height() // 2))

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



