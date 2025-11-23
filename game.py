from deck import Deck

"""
Game 1: Higher or Lower
-----------------------
Design Notes:
- Game logic is kept separate from card/deck modelling so the system is easier to extend.
  This allows multiple games (like Cambio) to reuse the same Deck and Card classes.
- The game loop is responsible only for user interaction and score tracking.
  This separation keeps the core logic simple, testable, and maintainable.
"""

class HigherLowerGame:
    def __init__(self, include_jokers=True):
        # Deck created independently so future games can use different rules or settings
        self.deck = Deck(include_jokers=include_jokers)
        self.deck.shuffle()
        self.score = 0
        self.current_card = None
    
    def start(self):
        print("Welcome to Higher or Lower :)")
        self.current_card = self.deck.draw_card()
        print(f"First card: {self.current_card}")

        while len(self.deck) > 0:
            # lower() keeps input consistent so comparison is reliable
            guess = input("Higher or Lower? (h/l or q to quit): ").lower()

            if guess == 'q':
                print("You quit the game :(")
                break
            
            if guess not in ('h', 'l'):
                print("Invalid input, try again.")
                # continue restarts the loop safely without running any comparison logic
                continue 
            
            next_card = self.deck.draw_card()
            print(f"Next card: {next_card}")

            # Compare card values to determine if the guess is correct
            if self.is_correct_guess(guess, self.current_card, next_card):
                print("Correct!!! :)")
                self.score += 1
            else:
                print("Wrong :(")

            self.current_card = next_card
            print(f"Score: {self.score}\n")

        print(f"Game over! Final score: {self.score}")

    def is_correct_guess(self, guess, current_card, next_card):
        """
        Check if the player's guess (higher/lower) matches the card comparison.
        Returns True if the guess is correct.
        """
        current_value = current_card.value
        next_value = next_card.value

        if guess == 'h':
            return next_value > current_value
        elif guess == 'l':
            return next_value < current_value
