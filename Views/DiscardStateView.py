from discord import ButtonStyle, Interaction
from discord.ui import View, Button

from Constants import IGNORE_RESPONSE
from Models.GameModel import GameModel
from Models.StateModel import StateModel
from Views.StateSelect import StateSelect


class DiscardStateView(View):
    def __init__(self):
        super().__init__(timeout=60*10)
        
        with GameModel() as gm:
            options = gm.get_tableau()
        with StateModel() as sm:
            options = [sm.get_state(id) for id in options]
        
        self.state_select = StateSelect(self, options)
        self.state_select.callback = IGNORE_RESPONSE

        self.submit_button = Button(label="Discard state", style=ButtonStyle.danger)
        self.submit_button.callback = self.__callback
        self.add_item(self.submit_button)
    
    async def __callback(self, interaction: Interaction):
        state_id = int(self.state_select.get_option())
        with GameModel() as gm:
            new_state_id = gm.discard(state_id)
        with StateModel() as sm:
            discarded_state = sm.get_state(state_id)
            new_state = sm.get_state(new_state_id)
        
        discarded_text = f"{discarded_state} has been discarded from the tableau."
        new_state_text = f"The tableau has been refilled with {new_state.name}."
        
        await interaction.response.send_message(f"{discarded_text} {new_state_text}")