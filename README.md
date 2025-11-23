# hawkeye-assessment-card-game
Higher or Lower & Cambio — Card Games

## Overview
This project contains two simple CLI card games built in Python using object-oriented design. Both games share the same Card and Deck classes but apply different rules and scoring systems.

### Game 1 — Higher/Lower Card Game
- The game uses a full deck of cards  
  - Kings have the highest value, and Aces have the lowest  
  - Users can optionally add Jokers to the deck  
- **Step 1:** The computer randomly selects a card from the deck  
- **Step 2:** The user guesses whether the next card will be higher or lower  
- **Step 3:** The computer randomly selects another card. If the user's guess is correct, they earn a point and move on to the next round  
- **Step 4:** The user can continue playing until all cards have been shown, at which point the game ends and a final score is revealed  
  - The user may also quit at any time and receive their final score  
- Jokers can be added to the deck, but they currently do not serve a purpose  

### Extension: Game 2 — Cambio
- Similar to the first game, this game also uses a full deck of cards  
- Card values differ in this game:  
  - Red Kings (♥ & ♦) have the lowest value at **–3 points**  
  - All other face cards are worth **11 points**  
  - Aces are worth **0**  
  - Numbered cards match their numerical value  
- **Step 1:** The computer randomly deals four cards to the user and four to itself  
- **Step 2:** The user sees their cards, and the computer identifies the user's highest-value card  
- **Step 3:** The computer asks the user whether they want to randomly swap out their highest-value card, and performs the swap if requested  
- **Step 4:** The computer reveals the total value of the user’s cards and its own, then announces the winner  

### Design Decisions
#### Object-Oriented Structure
- I used an object-oriented approach to keep the project modular and easy to extend.
- The Card and Deck classes provide a shared foundation for both games, allowing each game to apply its own rules without duplicating card logic.
- This structure also makes it easier to add new games or variations in the future, since they can all reuse the same deck and card management code.

#### Card Representation
- Cards are represented using their suit and rank, with each Card object storing this information along with a numerical value.
- Using __str__ and __repr__ ensures that cards display cleanly in the CLI, which improves usability during gameplay and debugging.

#### Deck Behaviour
- The Deck class handles deck construction, optional jokers, shuffling, and drawing cards.
- Keeping these functions inside the deck makes the game logic simpler, since each game only needs to request cards rather than worrying about how they are stored or randomised.

#### Game Logic Separation
- Higher/Lower and Cambio each live in their own game classes so their rules stay separated.
- This avoids mixing scoring rules or gameplay flow between the two games, while still sharing the same underlying card and deck structure.

#### CLI-Based Interaction
- I chose a CLI interface to keep the focus on game logic, card modelling, and program structure rather than UI design.
- This also keeps the project simple and accessible, while still leaving room for optional extensions like a GUI.

#### Extensibility
- Jokers are included as an optional deck feature to show how extra card types can be introduced and handled by new game variations.

### How to Run
**1.** Ensure you have Python 3 installed
**2.** Close the repository
**3.** Run the desired game from the command line:
**4.** Follow the on-screen prompts to play

### Future Improvements
- **Assign a Purpose to Jokers:** Currently, jokers are optional and do not affect gameplay. Future versions could give them special roles or abilities to add strategic depth.
- **GUI Enhancements:** Introduce a graphical interface for both games, with buttons, animations, colours, and sound effects, making the games more interactive and visually engaging.
- **Expanded Cambio Rules:** Implement additional rules for Cambio, such as multiple rounds, special card effects, and more strategic gameplay, reflecting the actual card game.
- **Testing Framework:** Add automated tests for the Card, Deck, and game classes to ensure correctness and make future modifications easier.