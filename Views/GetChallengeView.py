from discord import Interaction
from discord.ui import View

from Classes.State import State
from Models.StateModel import StateModel
from Views.StateSelect import StateSelect


class GetChallengeView(View):
    def __init__(self, options: list[State]):
        super().__init__(timeout=60*10)
        
        self.state_select = StateSelect(self, options)
        self.state_select.callback = self.__callback

    async def __callback(self, interaction: Interaction):
        state_id = int(self.state_select.get_option())
        state = StateModel().get_state(state_id)
        await interaction.response.send_message(state.challenge.markup_format(), ephemeral=True)
        