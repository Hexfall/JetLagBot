import json
from json import dumps


class Challenge:
    def __init__(self, title: str, description: str):
        self.title = title
        self.description = description
        
    def to_json(self):
         return dumps(
             self,
             default=lambda o: o.__dict__,
             sort_keys=True,
             indent=4
         )

    @staticmethod
    def from_json(json_str: str):
        return Challenge.from_dict(json.loads(json_str))

    @staticmethod
    def from_dict(d: dict):
        return Challenge(**d)
    
    def __repr__(self):
        return str(self)
    
    def __str__(self):
        return self.title
    
    def markup_format(self):
        return f"# {self.title}\n{self.description}"