from game import HigherLowerGame
from game2 import CambioGame

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