from typing import Optional

from Classes.Game import Game
from Constants import data_path
from Models.StateModel import StateModel

file_path = data_path.joinpath("games.json")

class GameModel:
    def __init__(self):
        self.game: Game = None
        self.changes = False
        self.__load()

    def __load(self):
        if not file_path.exists():
            return
        with open(file_path, "r") as f:
            self.game = Game.from_json(f.read())
    
    def __save(self):
        with open(file_path, "w") as f:
            f.write(self.game.to_json())
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.changes:
            self.__save()
    
    def start_new_game(self, channel_id: int, red_captain: str, blue_captain: str):
        with StateModel() as sm:
            self.game = Game.new_game(
                channel_id,
                captains={
                    'red': red_captain,
                    'blue': blue_captain,
                },
                deck=sm.get_state_ids(),
            )
        self.changes = True
    
    def active_game(self) -> bool:
        return self.game is not None
    
    def get_team_by_captain(self, captain: str) -> str:
        for team, c in self.game.captains.items():
            if c == captain:
                return team
        return None
    
    def get_active_cards(self, team: Optional[str]) -> list[int]:
        return self.game.get_active_cards(team)
    
    def get_tableau(self) -> list[int]:
        return self.game.get_tableau()