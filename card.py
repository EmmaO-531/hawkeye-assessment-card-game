class Card:
    """ 
    Represents a single card with suit, rank, and a number value for comparisons
    """
    SUITS = ["♠", "♥", "♦", "♣"]
    RANKS = {
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
        "A": 14,
    }
   
    def __init__(self, suit, rank):
        if suit not in Card.SUITS:
            raise ValueError(f"Invalid suit: {suit}")
        if rank not in Card.RANKS:
            raise ValueError(f"Invalid rank: {rank}")
        
        self.suit = suit
        self.rank = rank   
        self.value = Card.RANKS[rank]
        
    def __str__(self):
        """
        card display for CLI e.g. "6♠" or " K♥"
        """
        return f"{self.rank}{self.suit}"
    
    def __repr__(self):
        """
        for list debugging
        """
        return self.__str__()
    
    def get_value(self):
        if self.rank.isdigit():  # 2–10
            return int(self.rank)

        if self.rank == "A":
            return 0
        
        if self.rank == "K":
            if self.suit in ["♥", "♦"]:
                return -3
            return 11

        # J or Q
        return 11