from discord import Interaction, User, ButtonStyle
from discord.ui import View, Button

from Classes.State import State
from Constants import IGNORE_RESPONSE
from Models.GameModel import GameModel
from Models.StateModel import StateModel
from Views.StateSelect import StateSelect


class GetChallengeView(View):
    def __init__(self, show_all: bool = False, owner: User = None):
        super().__init__(timeout=60*10)
        
        with StateModel() as sm:
            with GameModel() as gm:
                if show_all:
                    options = list(sm.states.values())
                else:
                    options = [
                        sm.get_state(id) for id in gm.get_active_cards(
                            gm.get_team_by_captain(owner.mention)
                        )
                    ]
                    
        self.state_select = StateSelect(self, options)
        self.state_select.callback = IGNORE_RESPONSE
        
        self.submit_button = Button(label="Get challenge", style=ButtonStyle.success)
        self.submit_button.callback = self.__callback
        self.add_item(self.submit_button)
        

    async def __callback(self, interaction: Interaction):
        state_id = int(self.state_select.get_option())
        state = StateModel().get_state(state_id)
        await interaction.response.send_message(f"# {state.name} Challenge:\n{state.challenge.markup_format()}", ephemeral=True)
        