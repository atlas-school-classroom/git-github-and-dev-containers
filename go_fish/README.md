# Go Fish
a Command line implementation of the classis card game Go Fish 

# How to Run 
main.py

# Structure 
main.py Entry point 
card.py Card class with rank & suit
deck.py Deck class with Fisher Yates Shuffle
player.py Player class Human & Computer 
game.py Game Loop and Rules 

# Algorithm Used 
Fisher-Yates Shuffle - Deck.shuffle in deck.py
Insertion Sort - Player.sort_hand in player.py
Binary Search - Olayer.has_rank in player.py

# Rules
Each player starts with 7 cards
on your turn, ask for a rank you hold in your hand 
if the oppenent has it, they give you all the matching cards 
Collect all 4 cards of arank to form a book
Most books at the end wins 