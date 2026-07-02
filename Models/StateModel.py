import json

from Classes.State import State
from Constants import data_path


class StateModel:
    def __init__(self):
        self.states: dict[int, State] = {}
        self._load()
    
    def _load(self):
        with open(data_path.joinpath("States.json"), "r") as f:
            d: dict = json.load(f)
            self.states = {int(k): State.from_dict(v) for k, v in d.items()}
        print(self.states)
    
    def get_state(self, state_id: int) -> State:
        return self.states[state_id]
            
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
        