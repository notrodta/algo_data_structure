# Deck of Cards: Design the data structures for a generic deck of cards. Explain how you would subclass the data structures to implement blackjack.


class Deck:
    card_nums = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    suits_types = [1,2,3,4]

    cards = [] # list of all cards in deck

    def initialize_deck(self):
        pass

    #suffles deck
    def shuffle(self):
        pass




class Card(Deck):
    def __init__(self, card_num, suit):
        self.card_num = card_num
        self.suit = suit


class Hand():
    def __init__(self):
        self.cards = []

    @property
    def total_points(self):
        return 0

    @property
    def is_busted(self):
        if self.total_points > 21:
            return True
        return False

    @property
    def is_blackjack(self):
        if self.total_points == 21:
            return True
        return False

    def get_card_value(self, card):
        if self.total_points < 21 and card.card_num == 1:
            return 10
        elif self.total_points > 21 and card.card_num == 1:
            return 1

        if card.card_num >= 10 and card.card_num <= 13:
            return 10

    def add_card(self, card):
        self.cards.append(card)



class BlackJack:
    used_cards = []
    players = [] # list of distinct Hand objects

    winner = None

    is_game_over = False













