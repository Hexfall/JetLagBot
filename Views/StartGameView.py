from discord import ButtonStyle, User
from discord.ui import View, UserSelect, Button

from Constants import IGNORE_RESPONSE
from Models.GameModel import GameModel


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
        await interaction.response.send_message("New game started!")
    
    def get_red_captain(self) -> User:
        return self.red_captain.values[0]
    
    def get_blue_captain(self) -> User:
        return self.blue_captain.values[0]