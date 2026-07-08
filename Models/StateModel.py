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
    
    def get_state(self, state_id: int) -> State:
        return self.states[state_id]
    
    def get_states(self, state_ids: list[int]) -> list[State]:
        return [self.get_state(id) for id in state_ids]
    
    def get_state_name(self, state_id: int) -> str:
        return str(self.get_state(state_id))
    
    def get_state_names(self, state_ids: list[int]) -> list[str]:
        return [self.get_state_name(id) for id in state_ids]
            
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    
    def get_state_ids(self) -> list[int]:
        return list(self.states.keys())
    
    def get_states_in_markup(self, state_ids: list[int]) -> str:
        return "- " + "\n- ".join(self.get_state_names(state_ids))
        