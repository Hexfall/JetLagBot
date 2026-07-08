import json
from random import choice
from typing import Optional


TABLEAU_SIZE = 6
HAND_SIZE = 3

class Deck:
    def __init__(
            self, 
            deck: list[int], 
            tableau: list[int] = None,
            hands: dict[str, list[int]] = None,
            claimed: dict[str, list[int]] = None,
    ):
        self.deck: list[int] = deck
        
        if tableau is None:
            tableau = []
        self.tableau: list[int] = tableau
        
        if hands is None:
            self.hands = {
                'red': [],
                'blue': [],
            }
            self.fill_hands()
        else:
            self.hands: dict[str, list[int]] = hands
        
        if claimed is None:
            claimed = {
                'red': [],
                'blue': [],
            }
        self.claimed: dict[str, list[int]] = claimed
        
        self.refill_tableau()
    
    def refill_tableau(self) -> Optional[int]:
        refilled: bool = len(self.tableau) < TABLEAU_SIZE and len(self.deck) > 0
        while len(self.tableau) < TABLEAU_SIZE and len(self.deck) > 0:
            self.tableau.append(self.draw())
        
        if refilled:
            return self.tableau[-1]
        return None
    
    def fill_hands(self):
        for hand in self.hands.values():
            while len(hand) < HAND_SIZE and len(self.deck) > 0:
                hand.append(self.draw())

    # Remove and return a random card from the deck
    def draw(self) -> int:
        card = choice(self.deck)
        self.deck.remove(card)
        return card
    
    def claim(self, card: int, team: str) -> Optional[int]:
        if card in self.tableau:
            self.tableau.remove(card)
        elif card in self.hands[team]:
            pass
        else:
            raise ValueError(f"Card {card} is not in the deck or {team}'s hand.")

            
        self.claimed[team].append(card)
        
        return self.refill_tableau()
    
    def get_hand(self, team: str, amount: int) -> list[int]:
        if amount > len(self.hands[team]):
            return self.hands[team]
        return self.hands[team][:amount]
    
    def discard(self, card: int) -> int:
        self.tableau.remove(card)
        
        refill = self.refill_tableau()
        
        self.deck.append(card)
        
        if refill is None:
            # Tableau couldn't be filled because of the empty deck.
            refill = self.refill_tableau()
        return refill
    
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)
    
    def to_dict(self):
        return self.__dict__