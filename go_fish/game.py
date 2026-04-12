import time 
from deck import Deck
from player import Player
from card import Card

class Game:
    def __init__(self):
        self.deck = Deck()
        self.player = Player("Player 1")
        self.computer = Player("Computer", is_computer=True)
        
    def setup(self):
        self.deck.shuffle()
        for _ in range(7):
            self.player.add_cards(self.deck.deal())
            self.computer.add_cards(self.deck.deal())
            
    # Display Helper 
    
    def print_separator(self):
        print("\n" + "-" * 45)
    
    def display_player_turn_info(self, current_player, oppenent):
        self.print_separator()
        print(f"\n{current_player.name}'s turn!")
        print(f"{current_player.name}'s score: {current_player.books}")
        
        if not current_player.is_computer:
            print("\nYour hand:")
            current_player.show_hand()
        else:
            print(f"\n{current_player.name}'s hand is hidden.")
            
        print(f"\nCards left in deck: {len(self.deck)}")
        
    # Turn Logic
    def player_turn(self):
        self.display_player_turn_info(self.player, self.computer)
        
        # Get a valid rank from player
        while True:
            rank = input("\nAsk for a rank: ").strip().upper()
            if rank in Card.RANKS:
                if self.player.has_rank(rank):
                    break
                else:
                    print(f"You don't have any {rank}s in your hand. Pick a rank you hold.")
            else:
                print(f"Invalid rank. Choose from: {','.join(Card.RANKS)}")
        print(f"\n{self.player.name} asks {self.computer.name} for {rank}s")
        
        if self.computer.has_rank(rank):
            taken = self.computer.remove_cards(rank)
            print(f"{self.computer.name} gives {len(taken)} {rank}(s) to {self.player.name}.")
            self.player.add_cards(taken)
        else:
            print(f"{self.computer.name} says 'Go Fish!'")
            drawn = self.deck.deal()
            if drawn:
                print(f"{self.player.name} draws a card.")
                self.player.add_cards(drawn)
            else:
                print("The deck is empty!")
    
    def computer_turn(self):
        self.display_player_turn_info(self.computer, self.player)
        
        print(f"\n{self.computer.name} is thinking...")
        time.sleep(1)
        
        rank = self.computer.choose_rank()
        if not rank:
            return

        print(f"{self.computer.name} asks {self.player.name} for {rank}s.")
        
        if self.player.has_rank(rank):
            taken = self.player.remove_cards(rank)
            print(f"{self.player.name} gives {len(taken)} {rank}(s) to {self.computer.name}.")
            self.computer.add_cards(taken)
        else:
            print(f"{self.player.name} says 'Go Fish!'")
            drawn = self.deck.deal()
            if drawn:
                print(f"{self.computer.name} draws a card.")
                self.computer.add_cards(drawn)
            else:
                print("The deck is empty!")
        input("\nPress Enter to continue...")
        
    # Game Over Check 
    def is_game_over(self):
        total_books = self.player.books + self.computer.books
        return total_books == 13 or (
            self.deck.is_empty() and len(self.player) == 0 and len(self.computer) == 0
        )
        
    def display_result(self):
        self.print_separator()
        print("\nGame Over!", end=" ")
        if self.player.books > self.computer.books:
            print(f"{self.player.name} wins with {self.player.books} books!")
        elif self.computer.books > self.player.books:
            print(f"{self.computer.name} wins with {self.computer.books} books!")
        else:
            print("It's a tie!")
        print(f"\n{self.player.name}: {self.player.books} books")
        print(f"{self.computer.name}: {self.computer.books} books")
        self.print_separator()
        
    # Main Loop
    
    def play(self):
        print("=" * 45)
        print("     Welcome to Go Fish!")
        print("=" * 45)
        self.setup()
        
        while not self.is_game_over():
            if len(self.player) > 0 or not self.deck.is_empty():
                if len(self.player) == 0:
                    drawn = self.deck.deal()
                    if drawn:
                        self.player.add_cards(drawn)
                self.player_turn()
            
            if self.is_game_over():
                break
            
            if len(self.computer) > 0 or not self.deck.is_empty():
                if len(self.computer) == 0:
                    drawn = self.deck.deal()
                    if drawn:
                        self.computer.add_cards(drawn)
                self.computer_turn()
        
        self.display_result()