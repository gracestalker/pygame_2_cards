import pygame
import betting
import br
import hands
import sh
import sounds

# main game loop to minimize code on screen
def main_game(screen, state, width, height, table_color, values, suits, card_values, card_images, card_back):

    # initializing betting values
    chip_values = [10, 50, 100, 500]
    bet = betting.betting(screen, state["total"], chip_values, width, height, table_color)
    total_bet = bet

    # initializing background
    background = hands.build_background(width, height, table_color)

    # set up game, recreates a deck after every hand so you cannot count cards or run out of cards
    deck = hands.create_deck(values, suits)
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    split_hands = []
    current_hand_index = 0
    
    # check if the player has Blackjack
    if hands.calculate_hand(player_hand, card_values) == 21:
        results = ["Blackjack! You Win!"]
        state['total'] += int(total_bet * 1.5)  # payout is usually 1.5 times the bet
        game_over = True
        player_turn = False

        # display end screen
        end_screen = pygame.Surface((width, height))
        end_screen.fill(table_color)
        screen.blit(end_screen, (0,0))

        hands.display_hand(screen, player_hand, 100, 400, card_images, card_back)

        for idx, result in enumerate(results):
            pygame.time.delay(1500)
            hands.result_screen(results, result, screen, width, height, table_color, state)

        pygame.display.flip()
        # the delay allows the player to see that they got a Blackjack instead of just adding to their total
        pygame.time.delay(2000)
        return

    
    # use different variables to tell which stages you are in in the game
    player_turn = True
    game_over = False
    result_processed = False
    split_mode = False
    bankrupt = False

    # main while loop for game
    running = True
    while running:

        # allows the player to go bankrupt and not get stuck on the betting screen
        if state['total'] <= 0:
            bankrupt = True
            game_over = True

        # blits background to start the game
        if not game_over and not bankrupt:
            # starting the background from the top of the screen
            screen.blit(background, (0, 0))


            # deal hands to player and dealer in their spots
            hands.display_hand(screen, dealer_hand, 100, 100, card_images, card_back, hidden=player_turn and not game_over)

            # if the player has two of the same cards, they can split it
            if split_mode:

                # variables for split loops
                num_hands = len(split_hands)
                hand_width = 350
                base_offset = -200
                spacing = (width - (num_hands * hand_width)) // (num_hands + 1)

                # loop to make the two hands split and center so there is room to gain more cards
                for idx, split_hand in enumerate(split_hands):
                    x_offset = base_offset + spacing + idx * (hand_width + spacing)
                    y_offset = 400
                    # allows for the rectangle with the card to change colors based on what hand you are on
                    color = (0,255,0) if idx == current_hand_index else (255, 255, 255)

                    # draw a rectangle around the active hand
                    rect = pygame.Rect(x_offset + 250, y_offset - 20, hand_width, 140)
                    pygame.draw.rect(screen, color, rect, border_radius = 15, width = 3)
                    hands.display_hand(screen, split_hand, x_offset, y_offset, card_images, card_back)


            else:  
                # display player hand that isn't split             
                hands.display_hand(screen, player_hand, 100, 400, card_images, card_back)

        # displays a bankrupt screen when the player's total reaches 0
        elif bankrupt:
            # display a bankrupt screen
            sounds.game_over()
            br.bankrupt_screen(width, height, table_color, screen)


        # after the game ends, show the results of the game
        else:
            if not result_processed:
                results = []

                if split_mode:
                    for idx, split_hand in enumerate(split_hands):
                        player_total = hands.calculate_hand(split_hand, card_values)
                        dealer_total = hands. calculate_hand(dealer_hand, card_values)

                        if player_total > 21:
                            results.append(f"Hand {idx+1}: Bust! Dealer wins.")
                            state['total'] -= total_bet
                            sounds.lose_sound()
                        elif dealer_total > 21:
                            results.append(f"Hand {idx+1}: Dealer Bust! You win.")
                            state['total'] += total_bet
                            sounds.win_sound()
                        elif player_total > dealer_total:
                            results.append(f"Hand {idx+1}: You win!")
                            state['total'] += total_bet
                            sounds.win_sound()
                        elif player_total < dealer_total:
                            results.append(f"Hand {idx+1}: Dealer wins.")
                            state['total'] -= total_bet
                            sounds.lose_sound()
                        elif player_total == dealer_total:
                            results.append(f"Hand {idx+1}: It's a Tie!")
                            sounds.crickets_sound()
                        else:
                            results.append(f"Hand {idx+1}: Dealer wins.")
                            state['total'] -= total_bet
                            sounds.lose_sound()
                    
                else:
                    # display results
                    player_total = hands.calculate_hand(player_hand, card_values)
                    dealer_total = hands.calculate_hand(dealer_hand, card_values)
                    
                    if player_total > 21:
                        results.append("Bust! Dealer wins.")
                        state['total'] -= total_bet
                        sounds.lose_sound()
                    elif dealer_total > 21:
                        results.append('Dealer busts! You win!')
                        state['total'] += total_bet
                        sounds.win_sound()
                    elif player_total > dealer_total:
                        results.append("Congratulations! You win!")
                        state['total'] += total_bet
                        sounds.win_sound()
                    elif player_total == dealer_total:
                        results.append("It's a tie!")
                        sounds.crickets_sound()
                    else:
                        results.append("You lost! Dealer wins.")
                        state['total'] -= total_bet
                        sounds.lose_sound()


                if game_over and not result_processed:
                    end_screen = pygame.Surface((width, height))
                    end_screen.fill(table_color)
                    screen.blit(end_screen, (0,0))
                    
                    for idx, result in enumerate(results):
                        pygame.time.delay(1500)
                        hands.result_screen(results, result, screen, width, height, table_color, state)
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
                                screen.fill(table_color)

                                # shows the card you busted on
                                hands.display_hand(screen, player_hand, 100, 400, card_images, card_back)
                                hands.display_hand(screen, dealer_hand, 100, 100, card_images, card_back, hidden=True)  # Show dealer's face-down card
                                pygame.display.flip()
                                pygame.time.delay(1000)

                    # this is to stop drawing cards and keep your hand.
                    elif event.key == pygame.K_s:
                        if split_mode:
                            current_hand_index += 1
                            # Check if the current hand is done
                            if current_hand_index >= len(split_hands):  # All hands have been played
                                player_turn = False
                                hands.display_hand(screen, dealer_hand, 100, 100, card_images, card_back, hidden=player_turn)
                        else:
                            player_turn = False
                            hands.display_hand(screen, dealer_hand, 100, 100, card_images, card_back, hidden=player_turn)

                    
                    # this is to split the deck
                    elif event.key == pygame.K_f:
                        if len(player_hand) == 2 and player_hand[0][0] == player_hand[1][0]:
                            hand1, hand2 = hands.split(player_hand, deck)
                            if hand1 and hand2:
                                split_hands = [hand1, hand2]
                                split_mode = True

                    elif event.key == pygame.K_d:
                        if len(player_hand) ==2 and not split_mode:
                            if state['total'] >= total_bet:
                                total_bet *= 2

                                player_hand.append(deck.pop())

                                player_turn = False
                                game_over = hands.calculate_hand(player_hand, card_values) > 21

                                # shows the card you busted on
                                hands.display_hand(screen, player_hand, 100, 400, card_images, card_back)
                                hands.display_hand(screen, dealer_hand, 100, 100, card_images, card_back, hidden=True)  # Show dealer's face-down card
                                pygame.display.flip()
                                pygame.time.delay(1000)
                            
                            else:
                                print("Not enough chips to double down.")

            if game_over and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    running = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    exit()
        
        if not player_turn and not game_over:
            hands.dealer_turn(screen, dealer_hand, player_hand, deck, card_images, card_back, table_color, card_values, split_hands, width)
            
            game_over = True

        pygame.display.flip()