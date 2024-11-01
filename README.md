Snake-Water-Gun Game in Python
This is a simple text-based Python game implementing the classic "Snake-Water-Gun" game (similar to "Rock-Paper-Scissors") using a command-line interface. The player chooses one of three options: Snake, Water, or Gun. The computer randomly selects an option as well, and the game rules determine the winner:

Snake drinks Water → Snake wins.
Water douses Gun → Water wins.
Gun shoots Snake → Gun wins.
The program uses a dictionary for converting user input to a numeric format, allowing for easy comparison with the computer’s choice. Outcomes like "Win," "Lose," or "Draw" are printed based on the selections.

Features
Random Selection: The computer's choice is randomized for each round.
Input Handling: The game takes user input for selection (case-insensitive).
Result Display: The game displays both the player and computer choices, along with the outcome.
