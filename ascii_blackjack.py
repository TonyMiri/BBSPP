import random

def draw_card(deck, hand, ascii_hand) -> None:
    c = random.choice(deck)
    hand.append(c)
    all_cards.remove(c)
    if hand == dealer_hand and first_draw == True:
        ascii_hand.append(create_card('hide', c))
    else:
        ascii_hand.append(create_card('show', c))

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

def print_cards(cards, who, d_hand_showing = False):
    for line in range(4):
        cards_string = ""
        for card in cards:
            cards_string += card[line]
        print(cards_string)
    if who == 'player':
        print("_________",
            f'Your Hand - Current Score: {calculate_score(player_hand)}\n',
            sep='\n')
        print(f'Current Bet: {bet_size}')
        print(f'Remanining Balance: {user_credits}')
    if who == 'dealer':
        if d_hand_showing == True:
            print("_________",
            f'Dealer Hand - Dealer Score: {calculate_score(dealer_hand)}\n',
            sep='\n')
        else:
            print("_________", 'Dealer Hand', '', sep='\n')

def reveal_dealer_card(dealer_ascii_hand, dealer_hand):
    dealer_ascii_hand[0] = create_card('show', dealer_hand[0])

if __name__ == '__main__':
    suits = ['D', 'S', 'H', 'C']
    cards = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    all_cards = []

    for x in suits:
        for y in cards:
            all_cards.append([y, x])
    
    user_score = 0
    user_credits = 10000

    while user_credits > 0:
        player_hand = []
        player_ascii_hand = []
        dealer_hand = []
        dealer_ascii_hand = []
        first_draw = True
        d_hand_showing = False

        print(f"Your balance is {user_credits} credits.")
        bet_size = input("How much would you like to bet?\n>")
        user_credits -= int(bet_size)

        draw_card(all_cards, player_hand, player_ascii_hand)
        draw_card(all_cards, dealer_hand, dealer_ascii_hand)
        first_draw = False
        draw_card(all_cards, player_hand, player_ascii_hand)
        draw_card(all_cards, dealer_hand, dealer_ascii_hand)

        print_cards(dealer_ascii_hand, 'dealer')
        print_cards(player_ascii_hand, 'player')
        p_move = input("\nWould you like to (H)it, (S)tand, or (D)ouble?\n>")
        reveal_dealer_card(dealer_ascii_hand, dealer_hand)
        print_cards(dealer_ascii_hand, 'dealer', d_hand_showing=True)