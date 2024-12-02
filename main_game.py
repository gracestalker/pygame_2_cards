import pygame
import hands
import betting
import sounds

def main_game(screen, state, width, height, values, suits, table_color, card_values, card_images, card_back):

    # initializing betting values
    chip_values = [10, 50, 100, 500]
    bet = betting.betting(screen, state["total"], chip_values, width, height, table_color)
    total_bet = bet

    # initializing background
    background = hands.build_background(width, height, table_color)

    # set up game
    deck = hands.create_deck(values, suits)
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    split_hands = []
    current_hand_index = 0
    
    # check if the player has Blackjack
    
    if hands.calculate_hand(player_hand, card_values) == 21:
        end_screen = pygame.Surface((width, height))
        end_screen.fill(table_color)
        screen.blit(end_screen, (0,0))

        result = "Blackjack! You win!"
        state['total'] += int(total_bet * 1.5)  # Payout is usually 1.5 times the bet
        game_over = True
        player_turn = False
        hands.display_hand(screen, player_hand, 100, 400, card_images, card_back)
        hands.result_screen(result, screen, width, height, table_color, state)
        pygame.time.delay(2000)
        return

    
    # use different variables to tell which stages you are in in the game
    player_turn = True
    game_over = False
    result_processed = False
    split_mode = False
    bankrupt = False


    running = True
    while running:


        if not game_over and not bankrupt:
            # starting the background from the top of the screen
            screen.blit(background, (0, 0))

            hands.display_hand(screen, dealer_hand, 100, 100, card_images, card_back, hidden = player_turn and not game_over)

            if split_mode:
                num_hands = len(split_hands)
                hand_width = 300
                base_offset = -200
                spacing = (width - (num_hands * hand_width)) // (num_hands + 1)

                for idx, split_hand in enumerate(split_hands):
                    x_offset = base_offset + spacing + idx * (hand_width + spacing)
                    y_offset = 400
                    color = (0,255,0) if idx == current_hand_index else (255, 255, 255)

                    # draw a rectangle around the active hand
                    rect = pygame.Rect(x_offset - 15, y_offset - 20, hand_width, 140)
                    pygame.draw.rect(screen, color, rect, border_radius = 15, width = 3)
                    hands.display_hand(screen, split_hand, x_offset, y_offset, card_images, card_back)


            else:  
                # display normal hand              
                hands.display_hand(screen, player_hand, 100, 400, card_images, card_back)

        # displays a bankrupt screen when the player's total reaches 0
        elif bankrupt:
            # display a bankrupt screen
            end_screen = pygame.Surface((width, height))
            end_screen.fill((table_color))

            # load font
            info_f = "assets/fonts/game_text.ttf"
            font2 = pygame.font.Font(info_f, 80)
            font3 = pygame.font.Font(info_f, 36)

            # render text
            br = font2.render("The House always wins...", True, (255,255,255))
            instr = font3.render("Press [Q] to Quit", True, (255,255,255))

            # display the messages on the screen
            screen.blit(end_screen, (0,0))
            screen.blit(br, (width // 2 - br.get_width() // 2, height // 3))
            screen.blit(instr, (width // 2 - instr.get_width() // 2, height // 2 + 100))

            # event handling for quitting the bankrupt screen
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    pygame.quit()
                    exit()


        # after the game ends, show the results of the game
        else:
            if not result_processed:
                results = []

                if split_mode:
                    for idx, split_hand in enumerate(split_hands):
                        player_total = hands.calculate_hand(split_hand, card_values)
                        dealer_total = hands. calculate_hand(split_hand, card_values)

                        if player_total > 21:
                            results.append(f"Hand {idx+1}: Bust! Dealer wins.")
                            state['total'] -= total_bet
                        elif dealer_total > 21:
                            results.append(f"Hand {idx+1}: Dealer Bust! You win.")
                            state['total'] += total_bet
                        elif player_total > dealer_total:
                            results.append(f"Hand {idx+1}: You win!")
                            state['total'] += total_bet
                        elif player_total < dealer_total:
                            results.append(f"Hand {idx+1}: Dealer wins.")
                            state['total'] -= total_bet
                        elif player_total == dealer_total:
                            results.append("Hand {idx+1}: It's a Tie!")
                        else:
                            results.append(f"Hand {idx+1}: Dealer wins.")
                            state['total'] -= total_bet
                    
                else:
                    # display results
                    player_total = hands.calculate_hand(player_hand, card_values)
                    dealer_total = hands.calculate_hand(dealer_hand, card_values)
                    
                    if player_total > 21:
                        results.append("Bust! Dealer wins.")
                        state['total'] -= total_bet
                    elif dealer_total > 21:
                        results.append('Dealer busts! You win!')
                        state['total'] += total_bet
                    elif player_total > dealer_total:
                        results.append("Congratulations! You win!")
                        state['total'] += total_bet
                    elif player_total == dealer_total:
                        results.append("It's a tie!")
                    else:
                        results.append("You lost! Dealer wins.")
                        state['total'] -= total_bet


                if game_over and not result_processed:
                    end_screen = pygame.Surface((width, height))
                    end_screen.fill(table_color)
                    screen.blit(end_screen, (0,0))
                    
                    for idx, result in enumerate(results):
                        hands.result_screen(result, screen, width, height, table_color, state)
                        pygame.display.flip()

                    # results screen
                    result_processed = True
            
            
        # event handling and initializing keys for game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if player_turn and not game_over:
                if event.type == pygame.KEYDOWN:
                    # this is to hit and gain a card for your hand
                    if event.key == pygame.K_h: 
                        sounds.deal_sound()
                        if split_mode:
                            split_hands[current_hand_index].append(deck.pop())
                            if hands.calculate_hand(split_hands[current_hand_index], card_values) > 21:
                                current_hand_index += 1
                                if current_hand_index >= len(split_hands):
                                    player_turn = False
                        else:
                            player_hand.append(deck.pop())
                            if hands.calculate_hand(player_hand, card_values) > 21:
                                player_turn = False
                                game_over = True

                    # this is to stop drawing cards and keep your hand.
                    elif event.key == pygame.K_s:
                        if split_mode:
                            # Check if the current hand is done
                            if hands.calculate_hand(split_hands[current_hand_index], card_values) > 21:
                                current_hand_index += 1  # Move to the next hand
                            if current_hand_index >= len(split_hands):  # All hands have been played
                                player_turn = False

                        else:
                            player_turn = False
                    
                    # this is to split the deck
                    elif event.key == pygame.K_f:
                        if len(player_hand) == 2 and player_hand[0][0] == player_hand[1][0]:
                            hand1, hand2 = hands.split(player_hand, deck)
                            if hand1 and hand2:
                                split_hands = [hand1, hand2]
                                split_mode = True

            if game_over and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    running = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    exit()
        
        if not player_turn and not game_over:
            hands.dealer_turn(screen, dealer_hand, deck, card_images, card_back, table_color, card_values)
            game_over = True

        pygame.display.flip()
