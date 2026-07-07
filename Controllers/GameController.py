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
    with GameModel() as gm:
        with StateModel() as sm:
            states = [
                sm.get_state(id).name for id in gm.get_tableau()
            ]
    await interaction.response.send_message("\n- ".join(["# Tableau"] + states))

@app_commands.command(name="get_private_hand", description="Privately print your private hand.")
async def get_private_hand(interaction: Interaction):
    with GameModel() as gm:
        team = gm.get_team_by_captain(interaction.user.mention)
        ids = gm.get_private_hand(team)
    with StateModel() as sm:
        states = [
            sm.get_state(id).name for id in ids
        ]
    await interaction.response.send_message("\n- ".join([f'# {team.capitalize()} Team Private Hand'] + states), ephemeral=True)
    
@app_commands.command(name="get_options", description="Prints tableau and private hand options.")
async def get_options(interaction: Interaction):
    with GameModel() as gm:
        team = gm.get_team_by_captain(interaction.user.mention)
        tableau_ids = gm.get_tableau()
        private_hand_ids = gm.get_private_hand(team)
    with StateModel() as sm:
        tableau = [
            sm.get_state(id).name for id in tableau_ids
        ]
        private_hand = [
            sm.get_state(id).name for id in private_hand_ids
        ]
    
    await interaction.response.send_message(
        f"{'\n- '.join(['# Tableau'] + tableau)}\n{'\n- '.join([f'# {team.capitalize()} Team Private Hand'] + private_hand)}",
        ephemeral=True,
    )

@app_commands.command(name="get_status", description="Get's the current board state.")
async def get_status(interaction: Interaction):
    with GameModel() as gm:
        red_claimed_ids = gm.get_claimed('red')
        red_captain = gm.get_captain('red')
        blue_claimed_ids = gm.get_claimed('blue')
        blue_captain = gm.get_captain('blue')
    
    with StateModel() as sm:
        red_claimed = [
            sm.get_state(id).name for id in red_claimed_ids
        ]
        blue_claimed = [
            sm.get_state(id).name for id in blue_claimed_ids
        ]
    
    blue_status = f"## Blue team ({blue_captain}) currently has {len(blue_claimed)} claimed states:\n- {'\n- '.join(blue_claimed)}"
    red_status = f"## Red team ({red_captain}) currently has {len(red_claimed)} claimed states:\n- {'\n- '.join(red_claimed)}"
    
    await interaction.response.send_message(f"{red_status}\n{blue_status}")

class GameController:
    def __init__(self):
        self.commands = [
            start_game,
            claim,
            discard,
            show_tableau,
            get_private_hand,
            get_options,
            get_status,
        ]
    
    def register_commands(self, tree: app_commands.CommandTree):
        for command in self.commands:
            tree.add_command(command)