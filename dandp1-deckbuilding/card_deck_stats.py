from pprint import pprint

suits = ['S', 'H', 'C', 'D']
values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'K', 'Q', 'J']
cards = []
deck = {}

for suit in suits:
    for value in values:
        card = suit+value
        cards.append(card)

for card in cards:
    if card[1] == 'A':
        deck[card] = 1
    elif card[1] in ['K', 'Q', 'J']:
        deck[card] = 10
    else:
        deck[card] = int(card[1])

pprint(deck)


