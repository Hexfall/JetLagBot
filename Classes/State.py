import json
from json import dumps
from Classes.Challenge import Challenge


class State:
    def __init__(self, id: int, name: str, neighbors: list[int] = None, challenge: Challenge = None):
        self.id: int = id
        self.name: str = name
        if neighbors is None:
            neighbors = []
        self.neighbors: list[int] = neighbors
        self.challenge: Challenge = challenge

    def to_json(self):
        return dumps(
            self,
            default=lambda o: o.__dict__,
            sort_keys=True,
            indent=4
        )
    
    @staticmethod
    def from_json(json_str: str):
        return State.from_dict(json.loads(json_str))

    @staticmethod
    def from_dict(d: dict):
        challenge = Challenge.from_dict(d.pop("challenge"))
        return State(**d, challenge=challenge)
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return str(self)