from deck import Deck

"""
Game 1: Cambio
-----------------------
Design Notes:
- Uses the shared Deck and Card classes from the other game.
    - Separates game logic from card modelling to allow future expansion with new games.
    - Player and computer each receive four cards; card values vary by rules:
        * Red Kings (♥ & ♦) are -3 points
        * All other face cards are 11 points
        * Aces are 0
        * Number cards match their numerical value
    - Player has an option to swap their highest-value card once, introducing a risk/reward element.
"""
class CambioGame:
    def __init__(self, include_jokers=False):
        self.deck = Deck(include_jokers)
        self.deck.shuffle()
        self.player_cards = []
        self.computer_cards = []

    def deal_cards(self):
        # Deals 4 cards each to player and computer
        self.player_cards = [self.deck.draw_card() for _ in range(4)]
        self.computer_cards = [self.deck.draw_card() for _ in range(4)]

    def calculate_total(self, cards):
        # Calculates and returns the total value of a hand
        return sum(card.get_value() for card in cards)

    def show_hand(self, cards):
        # Returns a string representation of a hand for display purposes
        return ", ".join(str(c) for c in cards)

    def swap_highest_card(self, cards):
        """
        Find highest-value card nd offers the player
        the option to swap it for a new random card from the deck.
        """
        highest = max(cards, key=lambda c: c.get_value())
        print(f"Your highest card is: {highest}")

        choice = input("Do you want to swap it? (yes/no): ").strip().lower()
        if choice not in ("yes", "y"):
            return cards  # No change

        new_card = self.deck.draw_card()
        print(f"You drew: {new_card}")

        # Replace the highest card
        index = cards.index(highest)
        cards[index] = new_card

        return cards

    def start(self):

        """
        Runs the game loop:
        - Deals initial cards
        - Displays player's hand and total
        - Offers swap option
        - Calculates totals and determines the winner
        """
        print("Welcome to Cambio :)")

        self.deal_cards()

        print("Your cards:")
        print(self.show_hand(self.player_cards))
        print(f"Total value: {self.calculate_total(self.player_cards)}\n")

        # Give swap option
        self.player_cards = self.swap_highest_card(self.player_cards)

        # Final totals
        print("Your final hand:")
        print(self.show_hand(self.player_cards))
        player_total = self.calculate_total(self.player_cards)
        print(f"Final total: {player_total}\n")

        # Computer total
        comp_total = self.calculate_total(self.computer_cards)
        print(f"Computer's total was: {comp_total}")

        # Decide winner
        if player_total < comp_total:
            print("You win!")
        elif player_total > comp_total:
            print("Computer wins!")
        else:
            print("It's a tie!")