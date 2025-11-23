"""
Represents a single playing card, with a suit, rank, and numeric value.

Design Notes:
- SUITS and RANKS are class-level attributes:
    * They allow easy validation of inputs.
    * They belong to the class, not each instance, so memory is saved.
    * Centralising this information makes the code easier to maintain.
"""
class Card:
    
    SUITS = ["♠", "♥", "♦", "♣"]
    RANKS = {
        "A": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
    }
   
    def __init__(self, suit, rank):
        # Input validation prevents illegal cards entering the deck
        if suit not in Card.SUITS:
            raise ValueError(f"Invalid suit: {suit}")
        if rank not in Card.RANKS:
            raise ValueError(f"Invalid rank: {rank}")
        
        self.suit = suit
        self.rank = rank 
        # Stored for fast numeric comparisons in Game 1 (Higher/Lower)
        self.value = Card.RANKS[rank]
        
    def __str__(self):
        """
        User-friendly CLI display (e.g., "6♠", "Q♥").
        """
        return f"{self.rank}{self.suit}"
    
    def __repr__(self):
        """
        Developer-friendly representation used when cards appear in lists.
        """
        return self.__str__()
    
    def get_value(self):
        """
        Value rules for the Cambio game.
        These differ from the default 'value' used in Higher/Lower.
        """
        # Number cards keep their number
        if self.rank.isdigit():  
            return int(self.rank)

        # Aces are worth 0
        if self.rank == "A":
            return 0
        
        # Kings: red kings are -3, black kings are 11
        if self.rank == "K":
            if self.suit in ["♥", "♦"]:
                return -3
            return 11

        # Jacks, Queens
        return 11
