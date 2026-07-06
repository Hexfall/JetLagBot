from discord import app_commands, Interaction

from CreateStates import states
from Models.GameModel import GameModel
from Models.StateModel import StateModel
from Views.StartGameView import StartGameView

@app_commands.command(name="start_game", description="Start a new game.")
async def start_game(interaction: Interaction):
    await interaction.response.send_message(view=StartGameView(), ephemeral=True)

@app_commands.command(name="claim", description="Claim a state for your team.")
async def claim(interaction: Interaction):
    pass

@app_commands.command(name="discard", description="Discard a state from the tableau.")
async def discard(interaction: Interaction):
    pass

@app_commands.command(name="show_tableau", description="Print the public tableau.")
async def show_tableau(interaction: Interaction):
    with GameModel as gm:
        with StateModel as sm:
            states = [
                sm.get_state(id).name for id in gm.get_tableau()
            ]
    await interaction.response.send_message("- ".join(["# Tableau"] + states))

class GameController:
    def __init__(self):
        self.commands = [
            start_game,
        ]
    
    def register_commands(self, tree: app_commands.CommandTree):
        for command in self.commands:
            tree.add_command(command)