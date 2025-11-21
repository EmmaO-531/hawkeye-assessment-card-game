<<<<<<< HEAD
from deck import Deck

class HigherLowerGame:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.score = 0
        self.current_card = None
    
    def start(self):
        print("Welcome to Higher or Lower :)")
        self.current_card = self.deck.draw_card()
        print(f"First card: {self.current_card}")

        while len(self.deck) > 0:
            guess = input("Higher or Lower? (h/l or q to quit): ").lower()

            if guess == 'q':
                print("You quit the game :(")
                break
            
            if guess not in ('h', 'l'):
                print("Invalid input, try again.")
                continue
            
            next_card = self.deck.draw_card()
            print(f"Next card: {next_card}")

            #Compare the rank values
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
        Return True if player guessed correctly. 
        """
        current_value = current_card.value
        next_value = next_card.value

        if guess == 'h':
            return next_value > current_value
        elif guess == 'l':
=======
from deck import Deck

class HigherLowerGame:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.score = 0
        self.current_card = None
    
    def start(self):
        print("Welcome to Higer or Lower :)")
        self.current_card = self.deck.draw_card()
        print(f"First card: {self.current_card}")

        while len(self.deck) > 0:
            guess = input("Higher or Lower? (h/1 or q to quit): ").lower()

            if guess == 'q':
                print("You quit the game :(")
                break
            
            if guess not in ('h', 'l'):
                print("Invalid input, try again.")
                continue
            
            next_card = self.deck.draw_card()
            print(f"Next card: {next_card}")

            #Compare the rank values
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
        Return True if player guessed correctly. 
        """
        current_value = current_card.value
        next_value = next_card.value

        if guess == 'h':
            return next_value > current_value
        elif guess == 'l':
>>>>>>> 703d7c5078ccd9996ea0f0b2587632953050e75a
            return next_value < current_value