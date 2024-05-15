import sys
from class_player import Player
import random


def get_score(cards):
    """
    Calculate the blackjack score of a hand of cards.

    Parameters:
    - cards (list of str): The list of card names in the player's hand.

    Returns:
    - int: The total score of the hand accounting for the special rules of Aces.
    """
    score = 0
    ace_count = 0
    for i in cards:
        if i == 'Jack' or i == 'Queen' or i == 'King':
            score += 10
        elif i == 'Ace':
            ace_count += 1
            score += 11
        else:
            score += int(i)
    while score > 21 and ace_count > 0:
        score -= 10
        ace_count -= 1
    return score


def pick_cards(cards):
    """
    Select a random card from a list of cards.

    Parameters:
    - cards (list of str): The full deck from which to pick a card.

    Returns:
    - str: A randomly chosen card.
    """
    random_card = cards[random.randint(0, 12)]
    return random_card


def menu(player_cards, dealer_cards, player):
    """
    Display the game menu with the current game state.

    Parameters:
    - player_cards (list of str): List of the player's cards.
    - dealer_cards (list of str): List of the dealer's cards.
    - player (Player object): The player's instance with their current state.
    """
    print('------------------')
    print(f'(N)ew card, (C)heck score, (E)xit')
    shown_dealer_cards = dealer_cards.copy()
    shown_dealer_cards[0] = '*'
    print(f'Dealers cards: {shown_dealer_cards}')
    print(f'Your cards: {player_cards}')
    player.print()
    print('------------------')


def main():
    """
    The main game loop that handles user input and game progression.
    """
    player = Player()
    while True:
        print(f'(S)tart, (E)xit')
        cards = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        bet = ''
        action = input(' > ?').upper()
        player_cards = []
        dealer_cards = []

        while action != 'E':
            if get_score(dealer_cards) < 17:
                dealer_cards.append(pick_cards(cards))
                if get_score(player_cards) > 21:
                    print('You busted! Player Wins!')
                    break
            if action == 'S':
                for i in range(2):
                    player_cards.append(pick_cards(cards))
                for i in range(2):
                    dealer_cards.append(pick_cards(cards))
                menu(player_cards, dealer_cards, player)
                bet = int(input('bet ?'))
                player.bet(bet)
                action = input(' > ?').upper()
            if action == 'N':
                player_cards.append(pick_cards(cards))
                menu(player_cards, dealer_cards, player)
                if get_score(player_cards) > 21:
                    print('You busted! Dealer Wins!')
                    break
            elif action == 'C':
                player_score = get_score(player_cards)
                dealer_score = get_score(dealer_cards)
                print(f'{player_score}, {dealer_score}')
                if player_score > dealer_score:
                    player.change_balance(bet * 2)
                    player.print()
                    print('Player Wins!')
                    break
                else:
                    if dealer_score > 21:
                        print('Player Wins!')
                        player.change_balance(bet * 2)
                        break
                    else:
                        print('Dealer Wins!')
                        break
            if action == 'E':
                break
            action = input(' > ?').upper()
        player.check_balance()
        restart = input('Checkout (Y/N)?').upper()
        if restart == 'N':
            break


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nInterrupted')
        sys.exit(0)
