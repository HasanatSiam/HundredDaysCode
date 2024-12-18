import random

def deal_card():
    # Returns a random card from the deck
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    # Take a list of cards and return the score calculated from the card
    # if 11 in cards and if 10 in cards and len(cards)==2:
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


user_cards = []
com_cards = []
user_score = -1
comp_score = -1
is_game_over = False

for _ in range(2):
    # Deal the card for both the user and the computer
    new_card = deal_card()
    user_cards.append(new_card)
    com_cards.append(deal_card())

while not is_game_over:
    user_score = calculate_score(user_cards)
    comp_score = calculate_score(com_cards)
    print(f"Youre cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {com_cards[0]}")

    if user_score == 0 or comp_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user_should_deal = input("type 'y' to get another card, type 'n' to pass: ")
        if user_should_deal == 'y':
            user_cards.append(deal_card())
        else:
            is_game_over = True

while comp_score != 0 and comp_score < 17:
    com_cards.append(deal_card)
    comp_score = calculate_score(com_cards)