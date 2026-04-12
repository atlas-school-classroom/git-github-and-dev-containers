import random
from card import Card

class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for suit in Card.SUITS for rank in Card.RANKS]
    
    def shuffle(self):          # Fisher Yates Shuffle algorithm
        n = len(self.cards)
        for i in range(n - 1, 0, -1):
            j = random.randint(0, i)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]
            
    def deal(self):             # Remove & return the top card. Returns None if deck is mt
        return self.cards.pop() if self.cards else None
    
    def is_empty(self):
        return len(self.cards) == 0
    
    def __len__(self):
        return len(self.cards)
        
 