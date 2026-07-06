from datetime import datetime
from typing import Union
from json import dumps, loads

from discord import Thread
from discord.abc import GuildChannel

from Classes.Deck import Deck

HOURS_PER_PRIVATE_CARD = 3

class Game:
    def __init__(self, start_time: datetime = None, channel: Union[GuildChannel, Thread] = None, deck: Deck = None, captains: dict[str, str] = None):
        if start_time is None:
            self.start_time: datetime = datetime.now()
        else:
            self.start_time: datetime = start_time
        self.channel: Union[GuildChannel, Thread] = channel
        self.deck: Deck = deck
        self.captains: dict[str, str] = captains
    
    def get_hours_since_start(self) -> int:
        return int((datetime.now() - self.start_time).total_seconds() / 3600)
    
    def get_private_cards(self, team: str) -> list[int]:
       cards = self.get_hours_since_start() // HOURS_PER_PRIVATE_CARD
       return self.deck.get_hand(team, cards)
    
    def to_json(self):
        d = {
            'start_time': self.start_time.isoformat(),
            'channel': self.channel.id,
            'deck': self.deck.to_json(),
            'captains': self.captains,
        }
        
        return dumps(d)
        
    @staticmethod
    def from_json(json_str: str):
        d = loads(json_str)
        d['start_time'] = datetime.fromisoformat(d['start_time'])
        d['deck'] = Deck(**d['deck'])
        return Game(**d)
    