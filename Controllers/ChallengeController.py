from discord import app_commands, Interaction

from Models.StateModel import StateModel
from Views.GetChallengeView import GetChallengeView


@app_commands.command(name="get_challenge_any", description="Get the challenge for any state in the game.")
async def get_challenge_any(interaction: Interaction) -> None:
    with StateModel() as sm:
        options = list(sm.states.values())
    await interaction.response.send_message(
        "lol, this doesn't work yet.",
        view=GetChallengeView(options),
        ephemeral=True,
    )
    
@app_commands.command(name="get_challenge", description="View the challenge for a state in the tableau.")
async def get_challenge(interaction: Interaction) -> None:
    with StateModel() as sm:
        options = list(sm.states.values())
    await interaction.response.send_message(
        "lol, this doesn't work yet.",
        view=GetChallengeView(options),
        ephemeral=True,
    )
    
class ChallengeController:
    def __init__(self):
        self.commands = [
            get_challenge_any,
            get_challenge,
        ]
    
    def register_commands(self, tree: app_commands.CommandTree):
        for command in self.commands:
            tree.add_command(command)