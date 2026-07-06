from discord import Client, app_commands, Intents, User, Reaction

from Controllers.ChallengeController import ChallengeController


class JetLagBot(Client):
    def __init__(self, intents: Intents = Intents.default()) -> None:
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def on_ready(self):
        print('Logged in as: {0} {1}'.format(self.user.name, self.user.id))

    async def on_reaction_add(self, reaction: Reaction, user: User):
        pass
        
    async def setup_hook(self) -> None:
        ChallengeController().register_commands(self.tree)
        
        await self.tree.sync()
        print("Completed command syncing.")