import pygame
import hands


# split hands outcomes
def splitted(split_hands, dealer_hand, card_values, results, state, total_bet):

    for idx, split_hand in enumerate(split_hands):
        player_total = hands.calculate_hand(split_hand, card_values)
        dealer_total = hands.calculate_hand(dealer_hand, card_values)

    # all of the outcomes that could happen
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
        results.append(f"Hand {idx+1}: It's a Tie!")
    else:
        results.append(f"Hand {idx+1}: Dealer wins.")
        state['total'] -= total_bet