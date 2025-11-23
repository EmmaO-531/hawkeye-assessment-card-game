from game import HigherLowerGame
from game2 import CambioGame
"""
    Welcome to the Card Games Hub!
    Choose between two exciting card games: 
    1. Higher or Lower - Guess if the next card is higher or lower than the current one.
    2. Cambio - Aim to have the lowest total card value in your hand.
        - with red Kings counting as -3 points!
    You can also choose to include jokers in the deck for added fun!
    
"""
def main():
    print("Choose a game:")
    print("1. Higher or Lower")
    print("2. Cambio (lowest total wins)")

    option = input("Enter 1 or 2: ")

    include_jokers = input("Include jokers? (yes/no): ").lower() in ["yes", "y"]

    if option == "1":
        print("Starting the Higher or Lower Game...")
        game = HigherLowerGame(include_jokers)
        game.start()
    else:
        print("Starting the Cambio Game...")
        game = CambioGame(include_jokers)
        game.start()

if __name__ == "__main__":
    main()