import random
import math
import time

#-----
def draw_card(deck, hand, ascii_hand) -> None:
    global dealer_hand

    if len(deck) >= 1:
        c = random.choice(deck)
        hand.append(c)
        all_cards.remove(c)
        if hand == dealer_hand and first_draw == True:
            ascii_hand.append(create_card('hide', c))
        else:
            ascii_hand.append(create_card('show', c))
    else:
        print('Oopsie. We ran out of cards. Reshuffling...')
        reset_deck(all_cards, reshuffle=True, p=hand, d=dealer_hand)
        draw_card(deck, hand, ascii_hand)
#-----
def calculate_score(user_cards: list) -> int:
    score = 0
    value = None
    for card in user_cards:
        if card[0] == 'A':
            if (score + 11) > 21:
                value = 1
            else:
                value = 11
        elif card[0] in ['K', 'Q', 'J']:
            value = 10
        else:
            value = int(card[0])
        score += value
    return score

#-----
def create_card(card_type, card: list) -> list:
    suit_dict = {'C' : chr(9827),
                 'H': chr(9829),
                 'D': chr(9830),
                 'S': chr(9824)}
    line_list = []
    if card_type == 'show':
        line_list.append(' ___ ')
        if card[0] == "10":
            line_list.append('|10 |')
        else:
            line_list.append(f'|{card[0]}  |')
        line_list.append(f'| {suit_dict[card[1]]} |')
        if card[0] == "10":
            line_list.append('|_10|')
        else:
            line_list.append(f'|__{card[0]}|')
        return line_list
    line_list.append(' ___ ')
    line_list.append('|## |')
    line_list.append('|###|')
    line_list.append('|_##|')
    return line_list

#-----
def print_cards(cards, d_hand_showing = False):
    for line in range(4):
        cards_string = ""
        for card in cards:
            cards_string += card[line]
        print(cards_string)
    if cards == player_ascii_hand:
        print("_________",
            f'Your Hand - Score: {calculate_score(player_hand)}\n',
            sep='\n')
        print(f'Current Bet: {bet_size}')
        print(f'Remanining Balance: {user_credits}')
        print('------------------------------------------------------------')
    if cards == dealer_ascii_hand:
        if d_hand_showing == True:
            print("_________",
            f'Dealer Hand - Score: {calculate_score(dealer_hand)}\n',
            sep='\n')
        else:
            print("_________", 'Dealer Hand', '', sep='\n')

#------
def reveal_dealer_card(dealer_ascii_hand, dealer_hand):
    dealer_ascii_hand[0] = create_card('show', dealer_hand[0])

#------
def reset_deck(deck, reshuffle=False, p=None, d=None):
    suits = ['D', 'S', 'H', 'C']
    cards = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for x in suits:
        for y in cards:
            deck.append([y, x])
    if reshuffle == True:
        if len(p) > 0:
            for c in p:
                deck.remove(c)
        if len(d) > 0:
            for y in d:
                deck.remove(y)

#======================== MAIN PROGRAM =================================#

if __name__ == '__main__':
    all_cards = []
    reset_deck(all_cards)
    user_score = 0
    user_credits = 10000

    while user_credits >= 0:
        if user_credits == 0:
            print('You lost everything. Do you want to mortgage your house?')
            x = input('Y/n?\n>').lower()
            if x == 'y':
                user_credits = 10000
            elif x == 'n':
                print("I think I see the pit boss coming over...")
                break
            else:
                print("Huh?")
                continue

        player_hand = []
        player_ascii_hand = []
        dealer_hand = []
        dealer_ascii_hand = []
        first_draw = True

        #Deal first two cards and set game state
        print('------------------------------------------------------------')
        print(f"Your balance is {user_credits} credits.")
        try:
            bet_size = int(input("\nHow much would you like to bet?\n>"))
            if 0 < bet_size <= user_credits:
                user_credits -= bet_size
            else:
                print('\n...\n')
                time.sleep(2.5)
                print('You think you\'re pretty funny?\n')
                time.sleep(2)
                continue
        except ValueError:
            print('\nC\'mon. Be serious\n')
            continue


        draw_card(all_cards, player_hand, player_ascii_hand)
        draw_card(all_cards, dealer_hand, dealer_ascii_hand)
        first_draw = False
        draw_card(all_cards, player_hand, player_ascii_hand)
        draw_card(all_cards, dealer_hand, dealer_ascii_hand)

        print_cards(dealer_ascii_hand)
        print_cards(player_ascii_hand)

        p_score = calculate_score(player_hand)
        d_score = calculate_score(dealer_hand)
        
        #Check for blackjacks
        if not (d_score == 21 and p_score == 21):
            if d_score == 21:
                
                reveal_dealer_card(dealer_ascii_hand, dealer_hand)
                print_cards(dealer_ascii_hand, d_hand_showing=True)
                print_cards(player_ascii_hand)
                print('\nUnlucky! Dealer BlackJack :(\n')
                continue
            if p_score == 21:
                user_credits += (math.ceil(bet_size * 2.5))
                reveal_dealer_card(dealer_ascii_hand, dealer_hand)
                print_cards(dealer_ascii_hand, d_hand_showing=True)
                print_cards(player_ascii_hand)
                print('\nWinner! You got a BlackJack!\n')
                continue
        
        #If no blackjacks...
        while calculate_score(player_hand) < 21:
            p_move = input("\nWould you like to (H)it, (S)tand, or (D)ouble?\n>").lower()
            #Hit
            if p_move in ['h','hit']:
                draw_card(all_cards, player_hand, player_ascii_hand)
                print_cards(dealer_ascii_hand)
                print_cards(player_ascii_hand)
            #Stand
            elif p_move in ['s', 'stand', 'stay']:
                print('\nThe dealer shows their cards...')
                reveal_dealer_card(dealer_ascii_hand, dealer_hand)
                print_cards(dealer_ascii_hand, d_hand_showing=True)
                print_cards(player_ascii_hand)
                if calculate_score(dealer_hand) > calculate_score(player_hand):
                    break
                while calculate_score(dealer_hand) < 17:
                    draw_card(all_cards, dealer_hand, dealer_ascii_hand)
                    print_cards(dealer_ascii_hand, d_hand_showing=True)
                    print_cards(player_ascii_hand)
                break
            #Double Down
            elif p_move in ['d','double','double down','dd','double-down']:
                print('\nYou double your bet...\n')
                user_credits -= bet_size
                bet_size *= 2
                reveal_dealer_card(dealer_ascii_hand, dealer_hand)
                draw_card(all_cards, player_hand, player_ascii_hand)
                print_cards(dealer_ascii_hand, d_hand_showing=True)
                print_cards(player_ascii_hand)
                if calculate_score(player_hand) > 21:
                    break
                while calculate_score(dealer_hand) < 17:
                    draw_card(all_cards, dealer_hand, dealer_ascii_hand)
                    print_cards(dealer_ascii_hand, d_hand_showing=True)
                    print_cards(player_ascii_hand)
                break
            else:
                print('You wanna do what???')
        p_final = calculate_score(player_hand)
        d_final = calculate_score(dealer_hand)

        if p_final > 21:
            reveal_dealer_card(dealer_ascii_hand, dealer_hand)
            print_cards(dealer_ascii_hand, d_hand_showing=True)
            print_cards(player_ascii_hand)
            print('You busted!')

        if p_final > d_final and p_final <= 21:
            reveal_dealer_card(dealer_ascii_hand, dealer_hand)
            print_cards(dealer_ascii_hand, d_hand_showing=True)
            print_cards(player_ascii_hand)
            print('Congrats! You won!')
            user_credits += (bet_size * 2)

        if d_final > p_final and d_final <= 21:
            print('You lose... Again...')
        
        if d_final > 21:
            print('Dealer Busted! Lucky you ;)')
            user_credits += (bet_size * 2)

        if p_final == d_final:
            print_cards(dealer_ascii_hand, d_hand_showing=True)
            print_cards(player_ascii_hand)
            print("Pushed. You get your money back.")
            user_credits += bet_size

    print("You're outta money, ya bum! Get outta here!")   

#TODO:
#Correct the behavior for when blackjack is received 
#Test reshuffling more thoroughly 
#Refactor print_cards() function?
#Double option should only be available on first deal