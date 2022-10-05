import random

suits = ['D', 'S', 'H', 'C']
cards = ['1','2','3','4','5','6','7','8','9','10','J','Q','K','A']
all_cards = []
for x in suits:
    for y in cards:
        all_cards.append([y, x])

def draw_card() -> list:
    global all_cards

    card = random.choice(all_cards)
    all_cards = all_cards.remove(card)
    return card

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

def print_cards(cards, multi=False):
    if multi == False:
        for x in cards:
            print(x)
        return

    for line in range(4):
        cards_string = ""
        for card in cards:
            cards_string += card[line]
        print(cards_string)


# def get_player_move():
#     move = input()

if __name__ == '__main__':

    while True:
        user_score = 0
        user_credits = 10000

        bet_size = input("How much would you like to bet?\n>")

        player_ascii_hand = []
        player_hand = draw_card()
        player_hand = player_hand.append(draw_card())


        dealer_ascii_hand = []
        dealer_hand = draw_card()
        dealer_hand = dealer_hand.append(draw_card())
        first_draw = True

        for x in player_hand:
            player_ascii_hand.append(create_card('show', x))

        for x in dealer_hand:
            if first_draw:
                dealer_ascii_hand.append(create_card('hide', x))
                dealer_ascii_hand.append(create_card('show', x))

        print_cards(dealer_ascii_hand, multi=True)
        print("_________", 'Dealer Hand', '', sep='\n')
        print_cards(player_ascii_hand, multi=True)
        print("_________", 'Your Hand', '', sep='\n')