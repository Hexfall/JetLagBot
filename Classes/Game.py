from datetime import datetime
from typing import Optional
from json import dumps, loads

from Classes.Deck import Deck
from Classes.UnionFind import UnionFind
from Constants import HOURS_PER_PRIVATE_CARD


class Game:
    def __init__(self, start_time: datetime = None, channel_id: int = None, deck: Deck = None, captains: dict[str, str] = None, uf: UnionFind = None):
        if start_time is None:
            self.start_time: datetime = datetime.now()
        else:
            self.start_time: datetime = start_time
        self.channel_id: int = channel_id
        self.deck: Deck = deck
        self.captains: dict[str, str] = captains
        if uf is None:
            self.uf: UnionFind = UnionFind.new_uf([])
        else:
            self.uf: UnionFind = uf
    
    def get_hours_since_start(self) -> int:
        return int((datetime.now() - self.start_time).total_seconds() / 3600)
    
    def get_private_cards(self, team: Optional[str]) -> list[int]:
        if team is None:
            return []
        cards = self.get_hours_since_start() // HOURS_PER_PRIVATE_CARD + 1
        return self.deck.get_hand(team, cards)
    
    def get_active_cards(self, team: Optional[str]) -> list[int]:
        return self.deck.tableau + self.get_private_cards(team)
    
    def get_tableau(self) -> list[int]:
        return self.deck.tableau
    
    def to_json(self):
        d = {
            'start_time': self.start_time.isoformat(),
            'channel_id': self.channel_id,
            'deck': self.deck.to_dict(),
            'captains': self.captains,
            'uf': self.uf.to_dict(),
        }
        
        return dumps(
            d,
            indent=4,
        )
        
    @staticmethod
    def from_json(json_str: str):
        d = loads(json_str)
        d['start_time'] = datetime.fromisoformat(d['start_time'])
        d['deck'] = Deck(**d['deck'])
        d['uf'] = UnionFind(**d['uf'])
        return Game(**d)
    
    @staticmethod
    def new_game(channel_id: int, captains: dict[str, str], deck: list[int]):
        return Game(
            channel_id=channel_id,
            captains=captains,
            deck=Deck(deck),
            uf=UnionFind.new_uf(deck),
        )
    