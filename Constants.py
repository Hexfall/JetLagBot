from pathlib import Path

data_path = Path(__file__).parent.joinpath("Data").absolute()

async def IGNORE_RESPONSE(interaction):
    await interaction.response.defer()

TABLEAU_SIZE = 6
HOURS_PER_PRIVATE_CARD = 3
PRIVATE_HAND_SIZE = 3