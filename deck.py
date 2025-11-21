import random
from card import Card

class Deck:
    """a standard deck of 52 playing cards and optional jokers"""

    def __init__(self, include_jokers=False):
        self.cards =[]      #holds 'Card' objects
        self.build_deck(include_jokers)

    def build_deck(self, include_jokers):
        suits = ["♠", "♥", "♦", "♣"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
        
        if include_jokers:
            self.cards.append(Card("Joker", "Black"))
            self.cards.append(Card("Joker", "Red"))

    def shuffle(self):      #shuffle the deck in place
            random.shuffle(self.cards)

    def draw_card(self):
            if len(self.cards) ==0:
                return None     # or raise an exception
            return self.cards.pop(0)        #remove and return the top card
        
    def __str__(self):
            return ', '.join(str(card) for card in self.cards)
            
    def __len__(self):
            return len(self.cards)
            