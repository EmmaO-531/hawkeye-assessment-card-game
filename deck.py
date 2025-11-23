import random
from card import Card

"""
Represents a deck of playing cards and provides basic operations for card games.

Design Notes:
- Deck() creates a standard deck of 52 cards, or 54 if including jokers.
- The 'include_jokers' parameter allows optional addition of 2 jokers:
    * Default is False since most games do not use jokers.
    * Makes the class flexible for future games.
- shuffle() randomizes the order of cards in the deck.
- draw_card() removes and returns the top card, preventing it from being drawn again,
  mimicking a real-life deck.
- __str__() provides a user-friendly string representation of the full deck.
- __len__() allows len(deck) to show the remaining number of cards.
"""

class Deck:
    def __init__(self, include_jokers=False):
        self.cards = []  # Holds Card objects
        self.build_deck(include_jokers)

    def build_deck(self, include_jokers):
        suits = ["♠", "♥", "♦", "♣"]
        ranks = ["A","2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

        # Create all combinations of suits and ranks
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]

        # Optionally add jokers
        if include_jokers:
            self.cards.append(Card("Joker", "Black"))
            self.cards.append(Card("Joker", "Red"))

    def shuffle(self):
        """Randomly shuffles the deck in-place."""
        random.shuffle(self.cards)

    def draw_card(self):
        """
        Removes and returns the top card of the deck.
        Returns None if the deck is empty.
        """
        if len(self.cards) == 0:
            return None
        return self.cards.pop(0)

    def __str__(self):
        """Returns a user-friendly string representation of all cards in the deck."""
        return ', '.join(str(card) for card in self.cards)

    def __len__(self):
        """Returns the number of remaining cards in the deck."""
        return len(self.cards)