import random


class Card:
    def __init__(self, suit, cardval):
        self.suit = suit
        self.cardval = cardval

    def show(self):
        return self.cardval + "" + self.suit

    def score(self):
        return self.cardval


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        suits = ('\u2666', '\u2660', '\u2663', '\u2665')
        vals = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

        for s in suits:
            for v in vals:
                self.cards.append(Card(s, v))

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()

    def show(self):
        for c in self.cards:
            c.show()


class Hand:
    def __init__(self):
        self.hand_cards = []
        self.hand_variable = []
        self.hand_score = 0
        self.score = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                      '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}

    def add_handcard(self, deck, num_of_cards):
        for n in range(num_of_cards):
            self.hand_cards.append(deck.draw_card())
        self.hand_variable = []
        for card in self.hand_cards:
            self.hand_variable.append(card.show())

    def count_hand(self):
        self.hand_score = 0
        for card in self.hand_cards:
            self.hand_score += self.score.get(card.score())
        if self.hand_score > 21:
            for card in self.hand_cards:
                if self.score.get(card.score()) == 11 and self.hand_score > 21:
                    self.hand_score -= 10


class CompHand:
    def __init__(self):
        self.hand_cards = []
        self.hand_variable = []
        self.hand_shown_variable = []
        self.hand_score = 0
        self.visible_score = 0
        self.score = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                      '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}

    def add_handcard(self, deck, num_of_cards):
        for n in range(num_of_cards):
            self.hand_cards.append(deck.draw_card())
        self.hand_variable = []
        for card in self.hand_cards:
            self.hand_variable.append(card.show())
        self.hand_shown_variable = []
        for card in self.hand_cards[1:]:
            self.hand_shown_variable.append(card.show())

    def count_hand(self):
        self.hand_score = 0
        for card in self.hand_cards:
            self.hand_score += self.score.get(card.score())
        if self.hand_score > 21:
            for card in self.hand_cards:
                if self.score.get(card.score()) == 11 and self.hand_score > 21:
                    self.hand_score -= 10

    def count_visible_hand(self):
        self.visible_score = 0
        for card in self.hand_cards[1:]:
            self.visible_score += self.score.get(card.score())
        if self.visible_score > 21:
            for card in self.hand_cards:
                if self.score.get(card.score()) == 11 and self.visible_score > 21:
                    self.visible_score -= 10
