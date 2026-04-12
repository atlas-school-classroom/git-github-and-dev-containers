import random
from card import Card

class Player:
    def __init__(self, name, is_computer=False):
        self.name = name
        self.hand = []
        self.books = 0
        self.is_computer = is_computer
    
    # Hand Management
    def add_cards(self, cards):     # Add a list to hand then re-sort 
        if isinstance(cards, Card):
            cards = [cards]
        self.hand.extend(cards)
        self.sort_hand()
        self.check_books()
        
    def remove_cards(self, rank):    # Remove & Return all cards of the given rank
        matching = [c for c in self.hand if c.rank == rank]
        self.hand = [c for c in self.hand if c.rank != rank]
        return matching
    
    #Sorting
    def sort_hand(self):            # Sort hand by rank index using insertion sort 
        for i in range(1, len(self.hand)):
            key = self.hand[i]
            j = i - 1
            while j >= 0 and self.hand[j].rank_index() > key.rank_index():
                self.hand[j + 1] = self.hand[j]
                j -= 1
            self.hand[j + 1] = key
    
    # Binary search 
    def has_rank(self, rank):       # Binary search on sorted hand for given rank. Returns T or F
        target = Card.RANKS.index(rank)
        lo, hi = 0, len(self.hand) -1
        while lo <= hi:
            mid = (lo + hi) // 2
            mid_index = self.hand[mid].rank_index()
            if mid_index == target:
                return True
            elif mid_index < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return False
    
    # Books
    def check_books(self):          # Form books & remove them from hand.
        rank_counts = {}
        for card in self.hand:
            rank_counts[card.rank] = rank_counts.get(card.rank, 0) + 1
            
        for rank, count in rank_counts.items():
            if count == 4:
                self.hand = [c for c in self.hand if c.rank != rank]
                self.books += 1
                print(f"\n {self.name} formed a book of {rank}s! (Total books: {self.books})")
    
    # AI Logic Computer picks a random rank from its hand.
    def choose_rank(self):
        return random.choice(self.hand).rank if self.hand else None
    
    # Display
    def show_hand(self):
        if not self.hand:
            print(" (empty hand)")
        for card in self.hand:
            print(f"    {card}")
    
    def __len__(self):
        return len(self.hand)
        
    