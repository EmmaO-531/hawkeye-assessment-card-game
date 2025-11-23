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

### Design Decision
