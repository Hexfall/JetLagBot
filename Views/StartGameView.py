from typing import Union

from discord import ButtonStyle, User, Thread
from discord.abc import GuildChannel
from discord.ui import View, UserSelect, Button

from Constants import IGNORE_RESPONSE
from Models.GameModel import GameModel
from Models.StateModel import StateModel


class StartGameView(View):
    def __init__(self):
        super().__init__(timeout=60*10)
        
        self.red_captain = UserSelect(placeholder="Choose red captain...", min_values=1, max_values=1)
        self.blue_captain = UserSelect(placeholder="Choose blue captain...", min_values=1, max_values=1)
        self.submit_button = Button(label="Start game", style=ButtonStyle.success)

        self.red_captain.callback = IGNORE_RESPONSE
        self.blue_captain.callback = IGNORE_RESPONSE
        self.submit_button.callback = self.on_submit
        
        self.add_item(self.red_captain)
        self.add_item(self.blue_captain)
        self.add_item(self.submit_button)
    
    async def on_submit(self, interaction):
        print(f"Starting new game with captains {self.get_red_captain().display_name} and {self.get_blue_captain().display_name}")
        with GameModel() as gm:
            gm.start_new_game(
                interaction.channel_id,
                self.get_red_captain().mention,
                self.get_blue_captain().mention,
            )
        await interaction.response.send_message(f"New game started with red team captain {self.get_red_captain().mention} and blue team captain {self.get_blue_captain().mention}")
        with GameModel() as gm:
            with StateModel() as sm:
                states = [
                    sm.get_state(id).name for id in gm.get_tableau()
                ]
        await interaction.followup.send("\n- ".join(["# Tableau"] + states))
        await self.callback(
            {
                'red': self.get_red_captain(),
                'blue': self.get_blue_captain(),
            },
            interaction.channel
        )
    
    def get_red_captain(self) -> User:
        return self.red_captain.values[0]
    
    def get_blue_captain(self) -> User:
        return self.blue_captain.values[0]
    
    async def callback(self, users: dict[str, User], channel: Union[GuildChannel, Thread]):
        pass