from discord import User, ButtonStyle, Interaction
from discord.ui import View, Button

from Constants import IGNORE_RESPONSE
from Models.GameModel import GameModel
from Models.StateModel import StateModel
from Views.DiscardStateView import DiscardStateView
from Views.StateSelect import StateSelect


class ClaimStateView(View):
    def __init__(self, owner: User):
        super().__init__(timeout=60*10)
        
        with GameModel() as gm:
            self.team = gm.get_team_by_captain(owner.mention)
            options = gm.get_active_cards(self.team)
        
        with StateModel() as sm:
            options = [sm.get_state(id) for id in options]
        
        self.state_select = StateSelect(self, options)
        self.state_select.callback = IGNORE_RESPONSE
        
        self.submit_button = Button(label="Claim state", style=ButtonStyle.success)
        self.submit_button.callback = self.__callback
        self.add_item(self.submit_button)
    
    async def __callback(self, interaction: Interaction):
        state_id = int(self.state_select.get_option())
        with GameModel() as gm:
            new_state_id = gm.claim(self.team, state_id)
            tableau_ids = gm.get_tableau()
            scores = gm.game.uf.get_scores()
        with StateModel() as sm:
            claimed_state = sm.get_state(state_id)
            if new_state_id is None:
                new_state = None
            else:
                new_state = sm.get_state(new_state_id)
            tableau = sm.get_states_in_markup(tableau_ids)
        
        if new_state is None:
            new_state_text = "The claimed state was a private state, so no new state has been added to the tableau."
        else:
            new_state_text = f"The tableau has been refilled with {new_state.name}."
        
        score_text = f"The scores are now: Red team {scores['red'][0]} ({scores['red'][1]}) and Blue team {scores['blue'][0]} ({scores['blue'][1]})."

        await interaction.response.send_message(
            f"{self.team.capitalize()} team has claimed {claimed_state}. {new_state_text}\n\n# Tableau\n{tableau}\n\n{score_text}"
        )
        await interaction.followup.send(f"Pick a state to discard (remember to check for veto)", view=DiscardStateView(), ephemeral=True)