from deck import Deck

class CambioGame:
    def __init__(self, include_jokers=False):
        self.deck = Deck(include_jokers)
        self.deck.shuffle()
        self.player_cards = []
        self.computer_cards = []

    def deal_cards(self):
        self.player_cards = [self.deck.draw_card() for _ in range(4)]
        self.computer_cards = [self.deck.draw_card() for _ in range(4)]

    def calculate_total(self, cards):
        return sum(card.get_value() for card in cards)

    def show_hand(self, cards):
        return ", ".join(str(c) for c in cards)

    def swap_highest_card(self, cards):
        # Find highest-value card
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
        print("Welcome to Cambio :)")

        self.deal_cards()

        print("Your cards:")
        print(self.show_hand(self.player_cards))
        print(f"Total value: {self.calculate_total(self.player_cards)}\n")

        # Give swap option
        self.player_cards = self.swap_highest_card(self.player_cards)

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